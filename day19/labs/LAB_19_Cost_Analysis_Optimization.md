# Lab 19: Cost Analysis & Optimization
## Databricks Platform Administration Training

**Duration:** 45 minutes
**Difficulty:** Intermediate-Advanced
**Prerequisites:** Days 14-18 completed

---

## Lab Overview

In this lab, you will analyze cost data using system tables, identify optimization opportunities, and create cost governance reports. You'll develop practical skills for managing Databricks costs in an enterprise environment.

---

## Learning Objectives

By completing this lab, you will be able to:
- Query billing data for cost analysis
- Identify cost optimization opportunities
- Create chargeback reports by team/project
- Build cost alert queries

---

## Part 1: Cost Analysis Queries (15 minutes)

### Task 1.1: Monthly Cost Summary

```sql
-- Monthly cost summary by SKU
SELECT
    DATE_TRUNC('month', usage_date) as month,
    sku_name,
    SUM(usage_quantity) as total_dbus,
    ROUND(SUM(usage_quantity) * 0.55, 2) as estimated_cost_usd
FROM system.billing.usage
WHERE usage_date >= DATE_TRUNC('month', current_date()) - INTERVAL 3 MONTH
GROUP BY DATE_TRUNC('month', usage_date), sku_name
ORDER BY month DESC, estimated_cost_usd DESC;
```

### Task 1.2: Cost by Environment

```sql
-- Cost breakdown by environment tag
SELECT
    COALESCE(custom_tags['Environment'], 'untagged') as environment,
    sku_name,
    SUM(usage_quantity) as total_dbus,
    ROUND(SUM(usage_quantity) * 0.55, 2) as estimated_cost_usd,
    ROUND(100.0 * SUM(usage_quantity) / SUM(SUM(usage_quantity)) OVER(), 2) as pct_of_total
FROM system.billing.usage
WHERE usage_date >= current_date() - 30
GROUP BY custom_tags['Environment'], sku_name
ORDER BY estimated_cost_usd DESC;
```

### Task 1.3: All-Purpose vs Jobs Comparison

```sql
-- Compare All-Purpose (interactive) vs Jobs (automated) costs
SELECT
    CASE
        WHEN sku_name LIKE '%ALL_PURPOSE%' THEN 'All-Purpose (Interactive)'
        WHEN sku_name LIKE '%JOBS%' THEN 'Jobs (Automated)'
        WHEN sku_name LIKE '%SQL%' THEN 'SQL Warehouse'
        WHEN sku_name LIKE '%DLT%' THEN 'Delta Live Tables'
        ELSE 'Other'
    END as compute_type,
    SUM(usage_quantity) as total_dbus,
    ROUND(SUM(usage_quantity) * 0.55, 2) as estimated_cost_usd,
    ROUND(100.0 * SUM(usage_quantity) / SUM(SUM(usage_quantity)) OVER(), 2) as pct_of_total
FROM system.billing.usage
WHERE usage_date >= current_date() - 30
GROUP BY 1
ORDER BY estimated_cost_usd DESC;
```

---

## Part 2: Identify Optimization Opportunities (15 minutes)

### Task 2.1: Long-Running All-Purpose Clusters

```sql
-- Clusters that may benefit from being Job clusters
SELECT
    cluster_name,
    custom_tags['Team'] as team,
    COUNT(DISTINCT DATE(usage_date)) as days_used,
    SUM(usage_quantity) as total_dbus,
    ROUND(SUM(usage_quantity) * 0.55, 2) as estimated_cost_usd
FROM system.billing.usage
WHERE usage_date >= current_date() - 30
  AND sku_name LIKE '%ALL_PURPOSE%'
GROUP BY cluster_name, custom_tags['Team']
HAVING SUM(usage_quantity) > 100  -- More than 100 DBUs
ORDER BY estimated_cost_usd DESC
LIMIT 20;
```

### Task 2.2: Untagged Resources

```sql
-- Find resources without proper tagging (compliance issue)
SELECT
    cluster_name,
    sku_name,
    SUM(usage_quantity) as total_dbus,
    ROUND(SUM(usage_quantity) * 0.55, 2) as unattributed_cost
FROM system.billing.usage
WHERE usage_date >= current_date() - 30
  AND (custom_tags['Team'] IS NULL OR custom_tags['Team'] = '')
GROUP BY cluster_name, sku_name
ORDER BY unattributed_cost DESC
LIMIT 20;
```

### Task 2.3: Tagging Compliance Report

```sql
-- Tagging compliance percentage
SELECT
    'Tagged' as status,
    SUM(CASE WHEN custom_tags['Team'] IS NOT NULL THEN usage_quantity ELSE 0 END) as dbus,
    ROUND(100.0 * SUM(CASE WHEN custom_tags['Team'] IS NOT NULL THEN usage_quantity ELSE 0 END)
          / SUM(usage_quantity), 2) as percentage
FROM system.billing.usage
WHERE usage_date >= current_date() - 30

UNION ALL

SELECT
    'Untagged' as status,
    SUM(CASE WHEN custom_tags['Team'] IS NULL THEN usage_quantity ELSE 0 END) as dbus,
    ROUND(100.0 * SUM(CASE WHEN custom_tags['Team'] IS NULL THEN usage_quantity ELSE 0 END)
          / SUM(usage_quantity), 2) as percentage
FROM system.billing.usage
WHERE usage_date >= current_date() - 30;
```

---

## Part 3: Chargeback Reports (10 minutes)

### Task 3.1: Team-Based Chargeback

```sql
-- Monthly chargeback report by team
SELECT
    DATE_TRUNC('month', usage_date) as billing_month,
    COALESCE(custom_tags['Team'], 'Shared/Unallocated') as team,
    SUM(CASE WHEN sku_name LIKE '%ALL_PURPOSE%' THEN usage_quantity ELSE 0 END) as interactive_dbus,
    SUM(CASE WHEN sku_name LIKE '%JOBS%' THEN usage_quantity ELSE 0 END) as jobs_dbus,
    SUM(CASE WHEN sku_name LIKE '%SQL%' THEN usage_quantity ELSE 0 END) as sql_dbus,
    SUM(usage_quantity) as total_dbus,
    ROUND(SUM(usage_quantity) * 0.55, 2) as total_cost_usd
FROM system.billing.usage
WHERE usage_date >= DATE_TRUNC('month', current_date()) - INTERVAL 1 MONTH
  AND usage_date < DATE_TRUNC('month', current_date())
GROUP BY DATE_TRUNC('month', usage_date), custom_tags['Team']
ORDER BY total_cost_usd DESC;
```

### Task 3.2: Cost Center Allocation

```sql
-- Cost center allocation with project breakdown
SELECT
    COALESCE(custom_tags['CostCenter'], 'UNALLOCATED') as cost_center,
    COALESCE(custom_tags['Project'], 'No Project') as project,
    SUM(usage_quantity) as total_dbus,
    ROUND(SUM(usage_quantity) * 0.55, 2) as estimated_cost_usd
FROM system.billing.usage
WHERE usage_date >= current_date() - 30
GROUP BY custom_tags['CostCenter'], custom_tags['Project']
ORDER BY cost_center, estimated_cost_usd DESC;
```

---

## Part 4: Cost Alerts (5 minutes)

### Task 4.1: Daily Spend Alert Query

```sql
-- Alert: Daily spend exceeds threshold
WITH daily_spend AS (
    SELECT
        DATE(usage_date) as day,
        SUM(usage_quantity) * 0.55 as daily_cost
    FROM system.billing.usage
    WHERE usage_date = current_date() - 1
    GROUP BY DATE(usage_date)
)
SELECT
    day,
    daily_cost,
    CASE
        WHEN daily_cost > 500 THEN 'CRITICAL: Over $500/day'
        WHEN daily_cost > 300 THEN 'WARNING: Over $300/day'
        ELSE 'OK'
    END as alert_status
FROM daily_spend;
```

### Task 4.2: Weekly Trend Alert

```sql
-- Alert: Week-over-week cost increase
WITH weekly_costs AS (
    SELECT
        DATE_TRUNC('week', usage_date) as week,
        SUM(usage_quantity) * 0.55 as weekly_cost
    FROM system.billing.usage
    WHERE usage_date >= current_date() - 14
    GROUP BY DATE_TRUNC('week', usage_date)
)
SELECT
    week,
    weekly_cost,
    LAG(weekly_cost) OVER (ORDER BY week) as prev_week_cost,
    ROUND(100.0 * (weekly_cost - LAG(weekly_cost) OVER (ORDER BY week))
          / LAG(weekly_cost) OVER (ORDER BY week), 2) as pct_change
FROM weekly_costs
ORDER BY week DESC;
```

---

## Cleanup

No cleanup required for this lab (queries only).

---

## Lab Validation Checklist

- [ ] Analyzed monthly cost by SKU
- [ ] Identified cost by environment tags
- [ ] Compared All-Purpose vs Jobs costs
- [ ] Found long-running interactive clusters
- [ ] Identified untagged resources
- [ ] Created team-based chargeback report
- [ ] Built cost alert queries

---

## Optimization Recommendations Template

Based on your analysis, fill in recommendations:

| Finding | Current Cost Impact | Recommended Action | Expected Savings |
|---------|---------------------|-------------------|------------------|
| Long-running all-purpose clusters | $__/month | Convert to job clusters | ~50% |
| Untagged resources | $__/month | Enforce tagging policy | Better attribution |
| High interactive usage | $__/month | Review necessity | 10-30% |

---

## Assignment (Optional - Advanced)

**Cost Optimization Plan**

Create a comprehensive cost optimization plan including:

1. **Current State Analysis**
   - Total monthly spend
   - Breakdown by SKU, team, environment
   - Tagging compliance percentage

2. **Optimization Opportunities**
   - Top 5 cost reduction opportunities
   - Estimated savings for each

3. **Implementation Plan**
   - Quick wins (can implement immediately)
   - Medium-term changes (need planning)
   - Long-term governance improvements

4. **Monitoring Dashboard**
   - Key metrics to track
   - Alert thresholds
   - Reporting cadence

Submit as a markdown document with supporting SQL queries.

---

*Lab Version: 2.0 | Day 19 - Cost Analysis & Optimization*
