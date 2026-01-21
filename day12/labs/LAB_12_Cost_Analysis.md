# Lab 12: Cost Analysis & Governance

## Databricks Platform Administration Training
### Duration: 45 Minutes | Difficulty: Intermediate

---

## Lab Overview

Analyze Databricks costs using system tables, create cost allocation reports, and implement governance controls.

### Learning Objectives

- Query billing usage data
- Analyze costs by team and project
- Create cost allocation dashboards
- Set up budget alerts
- Implement tagging governance

---

## Part 1: Explore Billing Data (10 minutes)

### Task 1.1: View Usage Table Schema

```sql
-- Examine billing usage table structure
DESCRIBE system.billing.usage;

-- View sample data
SELECT *
FROM system.billing.usage
WHERE usage_date >= current_date() - 7
LIMIT 100;
```

### Task 1.2: Understand Key Columns

Document the important columns:

| Column | Description |
|--------|-------------|
| usage_date | |
| workspace_id | |
| sku_name | |
| usage_type | |
| usage_quantity | |
| usage_metadata | |

### Task 1.3: View List Prices

```sql
-- Check available SKU pricing
SELECT *
FROM system.billing.list_prices
ORDER BY sku_name;
```

---

## Part 2: Cost Analysis Queries (15 minutes)

### Task 2.1: Total DBU Usage by Day

```sql
-- Daily DBU consumption trend
SELECT
    usage_date,
    SUM(usage_quantity) AS total_dbus,
    COUNT(DISTINCT workspace_id) AS active_workspaces
FROM system.billing.usage
WHERE usage_date >= current_date() - 30
GROUP BY usage_date
ORDER BY usage_date DESC;
```

### Task 2.2: Cost by SKU

```sql
-- Usage breakdown by SKU type
SELECT
    sku_name,
    SUM(usage_quantity) AS total_dbus,
    COUNT(DISTINCT usage_date) AS active_days,
    ROUND(SUM(usage_quantity) / COUNT(DISTINCT usage_date), 2) AS avg_daily_dbus
FROM system.billing.usage
WHERE usage_date >= current_date() - 30
GROUP BY sku_name
ORDER BY total_dbus DESC;
```

### Task 2.3: Cost by Workspace

```sql
-- Usage by workspace
SELECT
    workspace_id,
    sku_name,
    SUM(usage_quantity) AS total_dbus
FROM system.billing.usage
WHERE usage_date >= current_date() - 30
GROUP BY workspace_id, sku_name
ORDER BY total_dbus DESC
LIMIT 20;
```

### Task 2.4: Cost by Tags (Team/Project)

```sql
-- Cost allocation by team (if tags are used)
SELECT
    usage_metadata.custom_tags['Team'] AS team,
    usage_metadata.custom_tags['Project'] AS project,
    sku_name,
    SUM(usage_quantity) AS total_dbus
FROM system.billing.usage
WHERE usage_date >= current_date() - 30
    AND usage_metadata.custom_tags['Team'] IS NOT NULL
GROUP BY 1, 2, 3
ORDER BY total_dbus DESC;
```

### Task 2.5: Week-over-Week Comparison

```sql
-- Compare this week to last week
WITH weekly_usage AS (
    SELECT
        CASE
            WHEN usage_date >= current_date() - 7 THEN 'This Week'
            ELSE 'Last Week'
        END AS period,
        sku_name,
        SUM(usage_quantity) AS total_dbus
    FROM system.billing.usage
    WHERE usage_date >= current_date() - 14
    GROUP BY 1, 2
)
SELECT
    sku_name,
    MAX(CASE WHEN period = 'Last Week' THEN total_dbus END) AS last_week,
    MAX(CASE WHEN period = 'This Week' THEN total_dbus END) AS this_week,
    ROUND(
        (MAX(CASE WHEN period = 'This Week' THEN total_dbus END) -
         MAX(CASE WHEN period = 'Last Week' THEN total_dbus END)) * 100.0 /
        NULLIF(MAX(CASE WHEN period = 'Last Week' THEN total_dbus END), 0),
        2
    ) AS change_pct
FROM weekly_usage
GROUP BY sku_name
ORDER BY this_week DESC;
```

---

## Part 3: Cost Optimization Analysis (10 minutes)

### Task 3.1: Identify High-Cost Clusters

```sql
-- Most expensive clusters (by DBU usage)
SELECT
    usage_metadata.cluster_id AS cluster_id,
    usage_metadata.cluster_name AS cluster_name,
    SUM(usage_quantity) AS total_dbus,
    COUNT(DISTINCT usage_date) AS active_days
FROM system.billing.usage
WHERE usage_date >= current_date() - 30
    AND usage_metadata.cluster_id IS NOT NULL
GROUP BY 1, 2
ORDER BY total_dbus DESC
LIMIT 20;
```

### Task 3.2: Identify Potentially Idle Clusters

```sql
-- Clusters with low utilization (high runtime, low output)
SELECT
    usage_metadata.cluster_id,
    usage_metadata.cluster_name,
    SUM(usage_quantity) AS total_dbus,
    COUNT(DISTINCT usage_date) AS active_days,
    ROUND(SUM(usage_quantity) / COUNT(DISTINCT usage_date), 2) AS avg_daily_dbus
FROM system.billing.usage
WHERE usage_date >= current_date() - 7
    AND sku_name LIKE '%ALL_PURPOSE%'
    AND usage_metadata.cluster_id IS NOT NULL
GROUP BY 1, 2
HAVING avg_daily_dbus < 1 -- Low average usage might indicate idle time
ORDER BY total_dbus DESC;
```

### Task 3.3: Job vs Interactive Usage

```sql
-- Compare job compute vs all-purpose compute
SELECT
    CASE
        WHEN sku_name LIKE '%JOBS%' THEN 'Jobs Compute'
        WHEN sku_name LIKE '%ALL_PURPOSE%' THEN 'Interactive Compute'
        WHEN sku_name LIKE '%SQL%' THEN 'SQL Compute'
        ELSE 'Other'
    END AS compute_category,
    SUM(usage_quantity) AS total_dbus,
    ROUND(SUM(usage_quantity) * 100.0 / SUM(SUM(usage_quantity)) OVER (), 2) AS pct_of_total
FROM system.billing.usage
WHERE usage_date >= current_date() - 30
GROUP BY 1
ORDER BY total_dbus DESC;
```

---

## Part 4: Build Cost Dashboard (10 minutes)

### Task 4.1: Create Dashboard

1. Go to **SQL** → **Dashboards**
2. Click **Create Dashboard**
3. Name: `Cost Governance Dashboard`

### Task 4.2: Add Widgets

**Widget 1: Daily DBU Trend (Line Chart)**
```sql
SELECT
    usage_date,
    SUM(usage_quantity) AS total_dbus
FROM system.billing.usage
WHERE usage_date >= current_date() - 30
GROUP BY usage_date
ORDER BY usage_date;
```

**Widget 2: Usage by SKU (Pie Chart)**
```sql
SELECT
    sku_name,
    SUM(usage_quantity) AS total_dbus
FROM system.billing.usage
WHERE usage_date >= current_date() - 30
GROUP BY sku_name
ORDER BY total_dbus DESC;
```

**Widget 3: Top Teams by Cost (Bar Chart)**
```sql
SELECT
    COALESCE(usage_metadata.custom_tags['Team'], 'Untagged') AS team,
    SUM(usage_quantity) AS total_dbus
FROM system.billing.usage
WHERE usage_date >= current_date() - 30
GROUP BY 1
ORDER BY total_dbus DESC
LIMIT 10;
```

**Widget 4: Month-to-Date Total (Counter)**
```sql
SELECT ROUND(SUM(usage_quantity), 0) AS mtd_dbus
FROM system.billing.usage
WHERE usage_date >= date_trunc('month', current_date());
```

### Task 4.3: Schedule Dashboard Refresh

1. Click **Schedule** on dashboard
2. Set refresh: Every 4 hours
3. Save schedule

---

## Part 5: Create Budget Alert

### Task 5.1: Create Alert Query

```sql
-- Alert: Daily usage exceeds threshold
SELECT
    usage_date,
    SUM(usage_quantity) AS daily_dbus
FROM system.billing.usage
WHERE usage_date = current_date()
GROUP BY usage_date
HAVING daily_dbus > 500; -- Adjust threshold as needed
```

### Task 5.2: Set Up Alert

1. Save query as `Daily DBU Threshold Check`
2. Click **Create Alert**
3. Configure:
   - Name: `High Daily DBU Usage`
   - Trigger: When query returns results
   - Destination: Your email
   - Schedule: Every 1 hour

---

## Part 6: Tagging Governance

### Task 6.1: Identify Untagged Resources

```sql
-- Find untagged usage
SELECT
    workspace_id,
    sku_name,
    usage_metadata.cluster_id,
    SUM(usage_quantity) AS total_dbus
FROM system.billing.usage
WHERE usage_date >= current_date() - 7
    AND (
        usage_metadata.custom_tags['Team'] IS NULL
        OR usage_metadata.custom_tags['Team'] = ''
    )
GROUP BY 1, 2, 3
ORDER BY total_dbus DESC
LIMIT 20;
```

### Task 6.2: Tag Compliance Report

```sql
-- Tag compliance percentage
SELECT
    ROUND(
        SUM(CASE WHEN usage_metadata.custom_tags['Team'] IS NOT NULL THEN usage_quantity ELSE 0 END) * 100.0 /
        SUM(usage_quantity),
        2
    ) AS tagged_pct,
    ROUND(
        SUM(CASE WHEN usage_metadata.custom_tags['Team'] IS NULL THEN usage_quantity ELSE 0 END) * 100.0 /
        SUM(usage_quantity),
        2
    ) AS untagged_pct
FROM system.billing.usage
WHERE usage_date >= current_date() - 30;
```

---

## Lab Validation Checklist

- [ ] Explored billing usage table structure
- [ ] Analyzed daily DBU consumption
- [ ] Calculated cost by SKU and workspace
- [ ] Identified high-cost clusters
- [ ] Compared job vs interactive compute
- [ ] Created cost governance dashboard
- [ ] Set up budget alert
- [ ] Analyzed tag compliance

---

## Challenge Exercise

Build a comprehensive cost governance solution:

1. **Executive Cost Report**:
   - Monthly cost summary
   - Trend analysis (3-month comparison)
   - Top 5 cost drivers
   - Cost forecast

2. **Team Chargeback Report**:
   - Cost by team/project
   - Breakdown by SKU
   - Month-over-month change
   - Export to CSV

3. **Optimization Recommendations**:
   - Identify idle all-purpose clusters
   - Find jobs that could use spot instances
   - Recommend cluster right-sizing
   - Calculate potential savings

---

## Lab Summary

You learned:
1. Querying billing usage system tables
2. Analyzing costs by various dimensions
3. Identifying cost optimization opportunities
4. Building cost governance dashboards
5. Setting up budget alerts
6. Implementing tagging compliance

---

*Lab Version: 2.0 | Databricks Platform Administration Training - Day 12*
