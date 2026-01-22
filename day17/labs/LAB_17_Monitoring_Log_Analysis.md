# Lab 17: Monitoring & Log Analysis
## Databricks Platform Administration Training

**Duration:** 45 minutes
**Difficulty:** Intermediate-Advanced
**Prerequisites:** Days 14-16 completed

---

## Lab Overview

In this lab, you will query system tables for observability, analyze job and cluster logs, and build monitoring queries. You'll learn to troubleshoot common issues using Databricks diagnostic tools.

---

## Learning Objectives

By completing this lab, you will be able to:
- Query system tables for billing and usage data
- Analyze audit logs for security events
- Troubleshoot job failures using logs
- Build monitoring dashboards with SQL

---

## Part 1: System Tables Overview (10 minutes)

### Task 1.1: Verify System Tables Access

1. Navigate to **SQL Editor**
2. Run the following query to check available system tables:

```sql
-- List available system schemas
SHOW SCHEMAS IN system;
```

3. Explore the schemas:

```sql
-- List tables in billing schema
SHOW TABLES IN system.billing;

-- List tables in access schema
SHOW TABLES IN system.access;

-- List tables in compute schema
SHOW TABLES IN system.compute;
```

**Note:** If you don't have access to system tables, contact your workspace admin or use sample data provided.

---

## Part 2: Billing Analysis Queries (15 minutes)

### Task 2.1: Daily DBU Consumption

Run the following queries to analyze billing data:

```sql
-- Daily DBU usage (last 30 days)
SELECT
    DATE(usage_date) as day,
    sku_name,
    SUM(usage_quantity) as total_dbus
FROM system.billing.usage
WHERE usage_date >= current_date() - 30
GROUP BY DATE(usage_date), sku_name
ORDER BY day DESC, total_dbus DESC;
```

### Task 2.2: Usage by Tags

```sql
-- DBU usage by team tag (if tags are used)
SELECT
    custom_tags['Team'] as team,
    DATE_TRUNC('week', usage_date) as week,
    sku_name,
    SUM(usage_quantity) as total_dbus
FROM system.billing.usage
WHERE usage_date >= current_date() - 30
  AND custom_tags['Team'] IS NOT NULL
GROUP BY custom_tags['Team'], DATE_TRUNC('week', usage_date), sku_name
ORDER BY week DESC, total_dbus DESC;
```

### Task 2.3: Identify Top Cost Drivers

```sql
-- Top 10 most expensive clusters
SELECT
    cluster_name,
    sku_name,
    SUM(usage_quantity) as total_dbus,
    ROUND(SUM(usage_quantity) * 0.55, 2) as estimated_cost_usd
FROM system.billing.usage
WHERE usage_date >= current_date() - 7
GROUP BY cluster_name, sku_name
ORDER BY total_dbus DESC
LIMIT 10;
```

---

## Part 3: Audit Log Analysis (10 minutes)

### Task 3.1: Recent User Activity

```sql
-- Recent login activity
SELECT
    event_time,
    user_identity.email as user_email,
    action_name,
    source_ip_address,
    response.status_code
FROM system.access.audit
WHERE action_name LIKE '%Login%'
  AND event_time >= current_date() - 7
ORDER BY event_time DESC
LIMIT 50;
```

### Task 3.2: Permission Changes

```sql
-- Recent permission changes (security audit)
SELECT
    event_time,
    user_identity.email as changed_by,
    action_name,
    request_params.workspace_id,
    request_params.principal as affected_principal,
    response.status_code
FROM system.access.audit
WHERE action_name LIKE '%Permission%'
  OR action_name LIKE '%Grant%'
  OR action_name LIKE '%Revoke%'
ORDER BY event_time DESC
LIMIT 100;
```

### Task 3.3: Failed Actions

```sql
-- Failed API calls (potential security issues)
SELECT
    event_time,
    user_identity.email,
    action_name,
    source_ip_address,
    response.status_code,
    response.error_message
FROM system.access.audit
WHERE response.status_code >= 400
  AND event_time >= current_date() - 7
ORDER BY event_time DESC
LIMIT 50;
```

---

## Part 4: Job Failure Analysis (10 minutes)

### Task 4.1: Find Failed Jobs

Navigate to **Workflows** and review recent job runs. For any failed job:

1. Click on the failed run
2. Review the **Timeline** to see which task failed
3. Click on the failed task
4. Review:
   - Error message
   - Stack trace
   - Driver logs

### Task 4.2: Common Failure Patterns

Look for these common issues in logs:

| Error Pattern | Likely Cause | Resolution |
|---------------|--------------|------------|
| `OutOfMemoryError` | Data too large | Increase driver memory |
| `Connection refused` | Network issue | Check firewall, peering |
| `AccessDenied` | Permission issue | Verify IAM/ACLs |
| `Table not found` | Wrong catalog/schema | Check Unity Catalog path |
| `Timeout exceeded` | Long-running query | Optimize query or increase timeout |

### Task 4.3: Analyze Spark UI

If a job has performance issues:

1. Click on the job run
2. Navigate to **Spark UI**
3. Check the **Stages** tab:
   - Look for data skew (some tasks much slower)
   - Check shuffle read/write sizes
   - Identify spill to disk

---

## Part 5: Build Monitoring Query (Optional)

### Task 5.1: Create a Monitoring View

```sql
-- Create a monitoring summary view
CREATE OR REPLACE VIEW admin_monitoring.daily_summary AS
SELECT
    DATE(usage_date) as report_date,
    COUNT(DISTINCT workspace_id) as active_workspaces,
    COUNT(DISTINCT cluster_id) as clusters_used,
    SUM(CASE WHEN sku_name LIKE '%ALL_PURPOSE%' THEN usage_quantity ELSE 0 END) as all_purpose_dbus,
    SUM(CASE WHEN sku_name LIKE '%JOBS%' THEN usage_quantity ELSE 0 END) as jobs_dbus,
    SUM(CASE WHEN sku_name LIKE '%SQL%' THEN usage_quantity ELSE 0 END) as sql_dbus,
    SUM(usage_quantity) as total_dbus
FROM system.billing.usage
WHERE usage_date >= current_date() - 30
GROUP BY DATE(usage_date)
ORDER BY report_date DESC;
```

---

## Cleanup

No cleanup required for this lab (queries only).

---

## Lab Validation Checklist

- [ ] Queried system.billing.usage for DBU consumption
- [ ] Analyzed billing data by tags
- [ ] Queried audit logs for user activity
- [ ] Identified permission changes in audit logs
- [ ] Analyzed a job failure (if available)
- [ ] Understood common error patterns

---

## Discussion Questions

1. How often should you review audit logs for security purposes?
2. What alerts would you set up based on billing data?
3. How can you detect unusual user activity from audit logs?
4. What's the most important metric to track for cost governance?

---

## Assignment (Optional - Intermediate)

**Monitoring Dashboard Design**

Design a monitoring dashboard for a Databricks administrator with the following requirements:

**Executive View:**
- Total monthly spend
- Month-over-month trend
- Top 5 cost centers

**Operations View:**
- Daily DBU consumption by SKU
- Failed jobs in last 24 hours
- Long-running clusters (>8 hours)

**Security View:**
- Failed login attempts
- Permission changes
- Unusual access patterns

Create SQL queries for each metric and sketch the dashboard layout.

---

*Lab Version: 2.0 | Day 17 - Monitoring & Log Analysis*
