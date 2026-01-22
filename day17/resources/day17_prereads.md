# Day 17 Pre-Reading Materials

## Databricks Platform Administration Training
### Monitoring & Troubleshooting

---

## Overview

Day 17 focuses on monitoring Databricks environments and troubleshooting common issues. You'll learn to use system tables, analyze logs, and apply systematic debugging approaches.

**Estimated Reading Time**: 30-35 minutes

---

## Required Reading

### 1. System Tables Overview

**Source**: Databricks Documentation

**Key Concepts to Understand**:
- Available system tables
- Data retention and freshness
- Query patterns for monitoring

**Read**: [Monitor usage with system tables](https://docs.databricks.com/en/administration-guide/system-tables/index.html)

**Focus Areas**:
- `system.billing.usage` for cost monitoring
- `system.compute.clusters` for compute tracking
- `system.access.audit` for security auditing

### 2. Cluster Monitoring

**Source**: Databricks Documentation

**Key Concepts to Understand**:
- Cluster events and logs
- Spark UI metrics
- Ganglia metrics (real-time)

**Read**: [View cluster logs](https://docs.databricks.com/en/compute/cluster-config.html#cluster-log-delivery)

**Focus Areas**:
- Driver and executor logs
- Event log analysis
- Resource utilization patterns

### 3. Troubleshooting Common Issues

**Source**: Databricks Documentation

**Key Concepts to Understand**:
- Out of memory errors
- Task failures and retries
- Cluster startup failures

**Read**: [Troubleshooting](https://docs.databricks.com/en/kb/clusters/index.html)

**Focus Areas**:
- Systematic debugging approach
- Log analysis techniques
- Performance bottleneck identification

---

## Key Terminology

| Term | Definition |
|------|------------|
| **System Tables** | Built-in tables tracking usage, billing, audit |
| **Audit Logs** | Records of user actions and data access |
| **Spark UI** | Web interface for monitoring Spark jobs |
| **Ganglia** | Real-time cluster resource monitoring |
| **Driver Logs** | Logs from the cluster driver node |
| **Executor Logs** | Logs from worker executors |
| **Event Log** | Spark event history for completed jobs |
| **OOM** | Out of Memory error |

---

## System Tables Reference

| Table | Purpose | Key Columns |
|-------|---------|-------------|
| `system.billing.usage` | Cost tracking | sku_name, usage_quantity, custom_tags |
| `system.compute.clusters` | Cluster history | cluster_name, creator, state |
| `system.access.audit` | Security audit | user_identity, action_name, request_params |
| `system.storage.predictive_optimization_operations_history` | Table optimization | table_name, operation_type |

---

## Four Golden Signals

| Signal | What to Monitor | Databricks Indicator |
|--------|-----------------|---------------------|
| **Latency** | Request duration | Query execution time, job duration |
| **Traffic** | Request volume | Active jobs, concurrent queries |
| **Errors** | Failure rate | Failed jobs, task failures |
| **Saturation** | Resource utilization | CPU/memory usage, queue depth |

---

## Common Issues and Solutions

| Issue | Symptoms | Investigation |
|-------|----------|---------------|
| OOM Error | Executor killed, task failures | Check partition sizes, memory settings |
| Slow Queries | High duration, timeouts | Examine Spark UI, check data skew |
| Cluster Won't Start | Pending state, errors | Check quota, permissions, network |
| Job Failures | Task errors, retries exhausted | Review driver logs, check data |

---

## Sample Monitoring Query

```sql
-- Daily cost by team from system tables
SELECT
    DATE(usage_date) as day,
    custom_tags['Team'] as team,
    sku_name,
    SUM(usage_quantity) as total_dbus,
    ROUND(SUM(usage_quantity) * 0.55, 2) as estimated_cost_usd
FROM system.billing.usage
WHERE usage_date >= current_date() - 30
GROUP BY DATE(usage_date), custom_tags['Team'], sku_name
ORDER BY day DESC, estimated_cost_usd DESC;
```

---

## Debugging Checklist

```
1. □ Identify the symptom (error message, behavior)
2. □ Check recent changes (code, config, data)
3. □ Review logs (driver, executor, event)
4. □ Analyze Spark UI (jobs, stages, tasks)
5. □ Check resource utilization (memory, CPU)
6. □ Isolate the issue (reproduce, simplify)
7. □ Apply fix and verify
8. □ Document for future reference
```

---

## Self-Assessment Questions

1. What are the Four Golden Signals and why are they important?
2. How do you query system tables for cost analysis?
3. Where do you find executor logs for a failed task?
4. What causes OutOfMemoryError and how do you resolve it?
5. How do audit logs support security investigations?

---

## Recommended Additional Reading

- [Query history](https://docs.databricks.com/en/sql/admin/query-history.html)
- [Spark UI guide](https://docs.databricks.com/en/compute/cluster-config.html#view-cluster-information)
- [Debugging notebooks](https://docs.databricks.com/en/notebooks/debugging.html)
- [Performance tuning](https://docs.databricks.com/en/optimizations/index.html)

---

*Pre-reading materials for Databricks Platform Administration Training - Day 17*
