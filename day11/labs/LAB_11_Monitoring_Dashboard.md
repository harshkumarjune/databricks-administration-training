# Lab 11: Monitoring & Troubleshooting Dashboard

## Databricks Platform Administration Training
### Duration: 45 Minutes | Difficulty: Intermediate

---

## Lab Overview

Build monitoring queries using system tables, analyze performance metrics, and create a dashboard for operational visibility.

### Learning Objectives

- Query system tables for operational insights
- Analyze job and cluster performance
- Track billing and usage patterns
- Build a monitoring dashboard
- Create alerts for operational issues

---

## Part 1: System Tables Exploration (10 minutes)

### Task 1.1: List Available System Tables

```sql
-- Show all system schemas
SHOW SCHEMAS IN system;

-- Show tables in access schema
SHOW TABLES IN system.access;

-- Show tables in billing schema
SHOW TABLES IN system.billing;

-- Show tables in compute schema
SHOW TABLES IN system.compute;

-- Show tables in workflow schema
SHOW TABLES IN system.workflow;
```

### Task 1.2: Examine Table Schemas

```sql
-- Audit log structure
DESCRIBE system.access.audit;

-- Billing usage structure
DESCRIBE system.billing.usage;

-- Cluster events structure
DESCRIBE system.compute.clusters;
```

Document the key columns you find:

| Table | Key Columns |
|-------|-------------|
| system.access.audit | |
| system.billing.usage | |
| system.compute.clusters | |

---

## Part 2: Security & Access Monitoring (10 minutes)

### Task 2.1: Recent User Activity

```sql
-- Most active users in the last 7 days
SELECT
    user_identity.email AS user_email,
    COUNT(*) AS action_count,
    COUNT(DISTINCT action_name) AS unique_actions
FROM system.access.audit
WHERE event_date >= current_date() - 7
GROUP BY user_identity.email
ORDER BY action_count DESC
LIMIT 20;
```

### Task 2.2: Security-Relevant Events

```sql
-- Permission changes in last 7 days
SELECT
    event_time,
    action_name,
    user_identity.email AS admin_user,
    request_params.securable_type,
    request_params.securable_full_name,
    request_params.changes
FROM system.access.audit
WHERE event_date >= current_date() - 7
    AND action_name IN ('updatePermissions', 'grantPermission', 'revokePermission')
ORDER BY event_time DESC
LIMIT 50;
```

### Task 2.3: Failed Access Attempts

```sql
-- Failed operations
SELECT
    event_date,
    action_name,
    user_identity.email AS user_email,
    response.status_code,
    response.error_message,
    COUNT(*) AS failure_count
FROM system.access.audit
WHERE event_date >= current_date() - 7
    AND response.status_code >= 400
GROUP BY 1, 2, 3, 4, 5
ORDER BY failure_count DESC
LIMIT 20;
```

---

## Part 3: Cost & Usage Analysis (10 minutes)

### Task 3.1: Daily DBU Usage

```sql
-- Daily DBU consumption
SELECT
    usage_date,
    sku_name,
    SUM(usage_quantity) AS total_dbus
FROM system.billing.usage
WHERE usage_date >= current_date() - 30
GROUP BY usage_date, sku_name
ORDER BY usage_date DESC, total_dbus DESC;
```

### Task 3.2: Usage by Workspace

```sql
-- Usage breakdown by workspace
SELECT
    workspace_id,
    sku_name,
    SUM(usage_quantity) AS total_dbus,
    COUNT(DISTINCT usage_date) AS active_days
FROM system.billing.usage
WHERE usage_date >= current_date() - 30
GROUP BY workspace_id, sku_name
ORDER BY total_dbus DESC;
```

### Task 3.3: Cost Trends

```sql
-- Weekly cost trend (if list_prices available)
SELECT
    DATE_TRUNC('week', usage_date) AS week_start,
    sku_name,
    SUM(usage_quantity) AS total_dbus
FROM system.billing.usage
WHERE usage_date >= current_date() - 90
GROUP BY 1, 2
ORDER BY 1 DESC, 3 DESC;
```

---

## Part 4: Job Performance Analysis (10 minutes)

### Task 4.1: Job Success Rate

```sql
-- Overall job success rate by day
SELECT
    DATE(end_time) AS run_date,
    COUNT(*) AS total_runs,
    SUM(CASE WHEN result_state = 'SUCCESS' THEN 1 ELSE 0 END) AS successful,
    SUM(CASE WHEN result_state = 'FAILED' THEN 1 ELSE 0 END) AS failed,
    SUM(CASE WHEN result_state = 'CANCELLED' THEN 1 ELSE 0 END) AS cancelled,
    ROUND(SUM(CASE WHEN result_state = 'SUCCESS' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS success_rate_pct
FROM system.workflow.job_runs
WHERE end_time >= current_date() - 30
GROUP BY 1
ORDER BY 1 DESC;
```

### Task 4.2: Longest Running Jobs

```sql
-- Jobs with longest average duration
SELECT
    job_id,
    COUNT(*) AS run_count,
    ROUND(AVG(TIMESTAMPDIFF(MINUTE, start_time, end_time)), 2) AS avg_duration_minutes,
    ROUND(MAX(TIMESTAMPDIFF(MINUTE, start_time, end_time)), 2) AS max_duration_minutes
FROM system.workflow.job_runs
WHERE end_time >= current_date() - 30
    AND result_state = 'SUCCESS'
GROUP BY job_id
HAVING run_count >= 5
ORDER BY avg_duration_minutes DESC
LIMIT 20;
```

### Task 4.3: Most Common Failure Reasons

```sql
-- Job failure analysis
SELECT
    job_id,
    result_state,
    COUNT(*) AS failure_count
FROM system.workflow.job_runs
WHERE end_time >= current_date() - 7
    AND result_state = 'FAILED'
GROUP BY job_id, result_state
ORDER BY failure_count DESC
LIMIT 20;
```

---

## Part 5: Query Performance (5 minutes)

### Task 5.1: Slowest Queries

```sql
-- Top 20 slowest queries in last 7 days
SELECT
    statement_id,
    executed_by,
    SUBSTRING(statement_text, 1, 100) AS query_preview,
    total_duration_ms / 1000 AS duration_seconds,
    rows_produced,
    warehouse_id
FROM system.query.history
WHERE start_time >= current_date() - 7
    AND status = 'FINISHED'
ORDER BY total_duration_ms DESC
LIMIT 20;
```

### Task 5.2: Query Volume by User

```sql
-- Query count and duration by user
SELECT
    executed_by,
    COUNT(*) AS query_count,
    ROUND(SUM(total_duration_ms) / 1000 / 60, 2) AS total_duration_minutes,
    ROUND(AVG(total_duration_ms) / 1000, 2) AS avg_duration_seconds
FROM system.query.history
WHERE start_time >= current_date() - 7
GROUP BY executed_by
ORDER BY query_count DESC
LIMIT 20;
```

---

## Part 6: Build Monitoring Dashboard

### Task 6.1: Create Dashboard

1. Go to **SQL** → **Dashboards**
2. Click **Create Dashboard**
3. Name it: `Platform Monitoring Dashboard`

### Task 6.2: Add Visualizations

Add the following queries as dashboard widgets:

**Widget 1: Daily Job Success Rate (Line Chart)**
```sql
SELECT
    DATE(end_time) AS run_date,
    ROUND(SUM(CASE WHEN result_state = 'SUCCESS' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS success_rate
FROM system.workflow.job_runs
WHERE end_time >= current_date() - 30
GROUP BY 1
ORDER BY 1;
```

**Widget 2: DBU Usage Trend (Area Chart)**
```sql
SELECT
    usage_date,
    SUM(usage_quantity) AS total_dbus
FROM system.billing.usage
WHERE usage_date >= current_date() - 30
GROUP BY usage_date
ORDER BY usage_date;
```

**Widget 3: Top Users by Activity (Bar Chart)**
```sql
SELECT
    user_identity.email AS user_email,
    COUNT(*) AS action_count
FROM system.access.audit
WHERE event_date >= current_date() - 7
GROUP BY 1
ORDER BY 2 DESC
LIMIT 10;
```

**Widget 4: Failed Jobs Today (Counter)**
```sql
SELECT COUNT(*) AS failed_jobs
FROM system.workflow.job_runs
WHERE DATE(end_time) = current_date()
    AND result_state = 'FAILED';
```

### Task 6.3: Configure Dashboard Refresh

1. Click **Schedule** on the dashboard
2. Set refresh interval: Every 1 hour
3. Enable auto-refresh

---

## Part 7: Create Alert

### Task 7.1: Create Failure Rate Alert

1. Create a new query:

```sql
-- Alert: Job failure rate > 10%
SELECT
    ROUND(
        SUM(CASE WHEN result_state = 'FAILED' THEN 1 ELSE 0 END) * 100.0 / NULLIF(COUNT(*), 0),
        2
    ) AS failure_rate_pct
FROM system.workflow.job_runs
WHERE end_time >= current_timestamp() - INTERVAL 24 HOURS;
```

2. Save the query as `Job Failure Rate Check`

3. Click **Create Alert**:
   - Name: `High Job Failure Rate`
   - Trigger when: Value > 10
   - Notification: Add your email
   - Schedule: Every 1 hour

---

## Lab Validation Checklist

- [ ] Explored system table schemas
- [ ] Queried audit logs for user activity
- [ ] Analyzed billing usage patterns
- [ ] Reviewed job success rates
- [ ] Identified slowest queries
- [ ] Created monitoring dashboard with visualizations
- [ ] Set up alert for job failures
- [ ] Configured dashboard refresh schedule

---

## Challenge Exercise

Build a comprehensive operations dashboard:

1. **Executive Summary Section**:
   - Total DBU cost MTD
   - Job success rate trend
   - Active users count
   - Critical alerts count

2. **Security Section**:
   - Permission changes
   - Failed access attempts
   - New user additions

3. **Performance Section**:
   - P95 query latency
   - Job duration trends
   - Cluster utilization

4. **Cost Optimization Section**:
   - Underutilized clusters
   - Long-running idle clusters
   - Cost by team/department

---

## Lab Summary

You learned:
1. Querying system tables for operational data
2. Analyzing security and audit events
3. Tracking cost and usage patterns
4. Monitoring job performance
5. Building SQL dashboards
6. Creating operational alerts

---

*Lab Version: 2.0 | Databricks Platform Administration Training - Day 11*
