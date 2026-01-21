# Day 9 Pre-Reading Materials

## Databricks Platform Administration Training
### Cluster & SQL Warehouse Administration

---

## Overview

Day 9 covers compute management, including clusters, cluster policies, pools, and SQL warehouses. Effective compute governance balances user productivity with cost control.

**Estimated Reading Time**: 30-35 minutes

---

## Required Reading

### 1. Cluster Types and Configuration

**Source**: Databricks Documentation

**Key Concepts to Understand**:
- All-purpose vs job clusters
- Autoscaling behavior
- Access modes (Single User, Shared)

**Read**: [Create a cluster](https://docs.databricks.com/en/compute/configure.html)

**Focus Areas**:
- Instance type selection
- Auto-termination settings
- Spark configuration options

### 2. Cluster Policies

**Source**: Databricks Documentation

**Key Concepts to Understand**:
- What policies control
- Policy JSON structure
- Enforcement vs defaults

**Read**: [Manage cluster policies](https://docs.databricks.com/en/admin/clusters/policies.html)

**Focus Areas**:
- Attribute types (fixed, range, allowlist)
- Mandatory tagging
- Cost control through policies

### 3. SQL Warehouses

**Source**: Databricks Documentation

**Key Concepts to Understand**:
- Serverless vs pro vs classic
- Warehouse sizing (T-shirt sizes)
- Auto-stop and scaling

**Read**: [SQL warehouses](https://docs.databricks.com/en/compute/sql-warehouse/index.html)

**Focus Areas**:
- When to use SQL warehouse vs cluster
- Scaling configuration
- Query queuing behavior

---

## Key Terminology

| Term | Definition |
|------|------------|
| **All-Purpose Cluster** | Interactive cluster for development and exploration |
| **Job Cluster** | Ephemeral cluster created for a specific job |
| **Cluster Policy** | Rules constraining cluster configuration |
| **Cluster Pool** | Set of idle instances for fast cluster startup |
| **SQL Warehouse** | Compute endpoint optimized for SQL queries |
| **Serverless** | Databricks-managed compute (no infrastructure management) |
| **Auto-termination** | Automatic cluster shutdown after idle period |
| **Autoscaling** | Dynamic adjustment of workers based on load |

---

## Cluster vs SQL Warehouse Comparison

| Aspect | Cluster | SQL Warehouse |
|--------|---------|---------------|
| Best for | Notebooks, ETL, ML | SQL queries, BI tools |
| Language support | Python, Scala, R, SQL | SQL only |
| Management | User configures | Simplified sizing |
| Unity Catalog | Requires Single User or Shared mode | Always supported |
| Serverless option | No | Yes (recommended) |
| Connection | Notebooks, APIs | JDBC/ODBC, SQL Editor |

---

## Cluster Policy Example

```json
{
  "spark_version": {
    "type": "regex",
    "pattern": "13\\.[0-9]+\\.x-scala.*",
    "defaultValue": "13.3.x-scala2.12"
  },
  "num_workers": {
    "type": "range",
    "minValue": 1,
    "maxValue": 4,
    "defaultValue": 2
  },
  "autotermination_minutes": {
    "type": "range",
    "minValue": 10,
    "maxValue": 60,
    "defaultValue": 30
  },
  "custom_tags.CostCenter": {
    "type": "regex",
    "pattern": "CC-[0-9]{5}"
  }
}
```

---

## Self-Assessment Questions

1. When should you use an all-purpose cluster vs a job cluster?
2. What's the benefit of cluster pools?
3. How do cluster policies help control costs?
4. What's the advantage of serverless SQL warehouses?

---

## Recommended Additional Reading

- [Cluster pools](https://docs.databricks.com/en/compute/pool-index.html)
- [Cluster access modes](https://docs.databricks.com/en/compute/configure.html#access-modes)
- [Photon](https://docs.databricks.com/en/compute/photon.html)
- [SQL warehouse sizing](https://docs.databricks.com/en/compute/sql-warehouse/warehouse-behavior.html)

---

*Pre-reading materials for Databricks Platform Administration Training - Day 9*
