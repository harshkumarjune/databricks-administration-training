# Day 15 Pre-Reading Materials

## Databricks Platform Administration Training
### Cluster Policies & SQL Warehouses

---

## Overview

Day 15 covers cluster policies for compute governance and SQL Warehouse configuration for analytics workloads. You'll learn how to enforce organizational standards while enabling user productivity.

**Estimated Reading Time**: 30-35 minutes

---

## Required Reading

### 1. Cluster Policy Fundamentals

**Source**: Databricks Documentation

**Key Concepts to Understand**:
- Purpose of cluster policies
- Policy JSON structure
- Attribute types (fixed, range, allowlist, regex)

**Read**: [Manage cluster policies](https://docs.databricks.com/en/admin/clusters/policies.html)

**Focus Areas**:
- How policies constrain configuration
- Default values vs enforced values
- Policy permissions (CAN_USE)

### 2. Policy Attribute Types

**Source**: Databricks Documentation

**Key Concepts to Understand**:
- `fixed` - Enforced, unchangeable values
- `range` - Numeric min/max constraints
- `allowlist` - Predefined valid options
- `regex` - Pattern matching

**Read**: [Cluster policy attribute reference](https://docs.databricks.com/en/admin/clusters/policy-definition.html)

**Focus Areas**:
- `isOptional` for mandatory fields
- `hidden` for invisible constraints
- Combining attributes for comprehensive policies

### 3. SQL Warehouses

**Source**: Databricks Documentation

**Key Concepts to Understand**:
- Serverless vs Pro vs Classic
- Warehouse sizing (T-shirt sizes)
- Auto-stop and scaling

**Read**: [SQL warehouses](https://docs.databricks.com/en/compute/sql-warehouse/index.html)

**Focus Areas**:
- When to use SQL warehouse vs cluster
- Multi-cluster scaling
- Query queuing behavior

---

## Key Terminology

| Term | Definition |
|------|------------|
| **Cluster Policy** | JSON rules constraining cluster configurations |
| **Fixed Attribute** | Value that cannot be changed by users |
| **Allowlist** | Predefined list of valid values |
| **Range** | Numeric constraint with min/max |
| **SQL Warehouse** | Compute optimized for SQL queries |
| **Serverless** | Fully managed by Databricks, instant startup |
| **Pro Warehouse** | User-managed with advanced features |
| **Cluster Count** | Number of compute clusters backing a warehouse |

---

## Policy Attribute Type Reference

| Type | Description | Example |
|------|-------------|---------|
| `fixed` | Exact value enforced | `"type": "fixed", "value": "14.3.x-scala2.12"` |
| `range` | Numeric range | `"type": "range", "minValue": 1, "maxValue": 4` |
| `allowlist` | Select from list | `"type": "allowlist", "values": ["Small", "Medium"]` |
| `regex` | Pattern match | `"type": "regex", "pattern": "^CC-[0-9]{4}$"` |
| `unlimited` | Any value allowed | `"type": "unlimited"` |
| `forbidden` | Attribute cannot be set | `"type": "forbidden"` |

---

## SQL Warehouse Comparison

| Feature | Serverless | Pro | Classic |
|---------|------------|-----|---------|
| Startup time | Instant | 5-10 min | 5-10 min |
| Management | Fully managed | User managed | User managed |
| Cost model | DBU only | DBU + infra | DBU + infra |
| Scaling | Automatic | Configurable | Configurable |
| Best for | Most SQL workloads | Specific needs | Legacy |

---

## Sample Development Policy

```json
{
  "name": "dev-cluster-policy",
  "definition": {
    "spark_version": {
      "type": "regex",
      "pattern": "^14\\.[0-9]+\\.x-scala.*$",
      "defaultValue": "14.3.x-scala2.12"
    },
    "node_type_id": {
      "type": "allowlist",
      "values": ["Standard_DS3_v2", "Standard_DS4_v2"],
      "defaultValue": "Standard_DS3_v2"
    },
    "num_workers": {
      "type": "range",
      "minValue": 1,
      "maxValue": 4,
      "defaultValue": 2
    },
    "autotermination_minutes": {
      "type": "range",
      "minValue": 15,
      "maxValue": 60,
      "defaultValue": 30
    },
    "custom_tags.Team": {
      "type": "unlimited",
      "isOptional": false
    },
    "custom_tags.Environment": {
      "type": "fixed",
      "value": "development"
    }
  }
}
```

---

## Self-Assessment Questions

1. What's the difference between `fixed` and `allowlist` attribute types?
2. How does `isOptional: false` enforce mandatory tagging?
3. When would you use a serverless SQL warehouse vs Pro?
4. How do you grant users permission to use a cluster policy?
5. What happens if a user tries to create a cluster that violates policy?

---

## Recommended Additional Reading

- [Create and manage cluster policies](https://docs.databricks.com/en/admin/clusters/policies.html)
- [SQL warehouse access control](https://docs.databricks.com/en/compute/sql-warehouse/access-control.html)
- [Warehouse monitoring](https://docs.databricks.com/en/compute/sql-warehouse/monitor.html)
- [Query history](https://docs.databricks.com/en/sql/admin/query-history.html)

---

*Pre-reading materials for Databricks Platform Administration Training - Day 15*
