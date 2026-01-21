# Day 11 Pre-Reading Materials

## Databricks Platform Administration Training
### Monitoring & Troubleshooting

---

## Overview

Day 11 covers observability, system tables, performance troubleshooting, and log analysis. Understanding monitoring is essential for maintaining healthy Databricks environments.

**Estimated Reading Time**: 30-35 minutes

---

## Required Reading

### 1. System Tables Overview

**Source**: Databricks Documentation

**Key Concepts to Understand**:
- System tables in Unity Catalog
- Available schemas (access, billing, compute, workflow, query)
- Query patterns for observability

**Read**: [Monitor usage with system tables](https://docs.databricks.com/en/admin/system-tables/index.html)

**Focus Areas**:
- Table retention periods
- Enabling system tables
- Common query patterns

### 2. Audit Logs

**Source**: Databricks Documentation

**Key Concepts to Understand**:
- What actions are logged
- Audit log schema
- Compliance use cases

**Read**: [Audit logging](https://docs.databricks.com/en/admin/account-settings/audit-logs.html)

**Focus Areas**:
- Event types and actions
- Query examples
- Security monitoring

### 3. Spark UI and Performance

**Source**: Databricks Documentation

**Key Concepts to Understand**:
- Spark UI tabs and metrics
- Identifying performance bottlenecks
- Reading execution plans

**Read**: [View Spark UI](https://docs.databricks.com/en/compute/spark-ui.html)

**Focus Areas**:
- Jobs, Stages, Tasks hierarchy
- Storage and executor metrics
- SQL query plans

---

## Key Terminology

| Term | Definition |
|------|------------|
| **System Tables** | Built-in tables for observability, billing, and governance |
| **Audit Log** | Record of all actions taken in Databricks |
| **Spark UI** | Web interface for monitoring Spark applications |
| **DBU** | Databricks Unit - unit of compute consumption |
| **Data Skew** | Uneven distribution of data across partitions |
| **Spill** | When data exceeds memory and writes to disk |
| **Straggler** | A task that takes much longer than others |
| **Driver Log** | Logs from the cluster driver node |

---

## System Tables Quick Reference

```
system
├── access
│   ├── audit                 -- All user/system actions
│   ├── table_lineage         -- Table-level lineage
│   └── column_lineage        -- Column-level lineage
├── billing
│   ├── usage                 -- DBU consumption
│   └── list_prices           -- Pricing information
├── compute
│   ├── clusters              -- Cluster history
│   └── warehouses            -- SQL warehouse history
├── workflow
│   ├── jobs                  -- Job definitions
│   ├── job_runs              -- Job execution history
│   └── job_tasks             -- Task-level details
└── query
    └── history               -- SQL query history
```

---

## Sample Monitoring Query

```sql
-- Daily cost summary by SKU
SELECT
  DATE(usage_date) AS date,
  sku_name,
  SUM(usage_quantity) AS total_dbus
FROM system.billing.usage
WHERE usage_date >= current_date() - 7
GROUP BY 1, 2
ORDER BY 1 DESC, 3 DESC;
```

---

## Self-Assessment Questions

1. What system schema contains audit log data?
2. How long is the default retention for audit logs?
3. What Spark UI tab shows task distribution across executors?
4. What causes data skew and how can you identify it?

---

## Common Performance Issues

| Issue | Symptom | Solution |
|-------|---------|----------|
| Data Skew | One task much slower than others | Repartition, salt keys, AQE |
| Memory Pressure | OOM errors, excessive GC | Increase memory, reduce partitions |
| Small Files | Many small tasks | OPTIMIZE, coalesce |
| Shuffle Spill | Disk write during shuffle | More memory, fewer partitions |

---

## Recommended Additional Reading

- [Databricks SQL alerts](https://docs.databricks.com/en/sql/user/alerts/index.html)
- [Query performance tuning](https://docs.databricks.com/en/optimizations/index.html)
- [Cluster event logs](https://docs.databricks.com/en/compute/cluster-event-log.html)
- [External monitoring integrations](https://docs.databricks.com/en/integrations/observability/index.html)

---

*Pre-reading materials for Databricks Platform Administration Training - Day 11*
