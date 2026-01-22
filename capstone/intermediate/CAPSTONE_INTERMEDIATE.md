# Capstone Project: Intermediate Track
## Enterprise Databricks Environment Design - TechFlow Industries

**Duration:** 45 minutes
**Difficulty:** Intermediate
**Focus:** Unity Catalog + Compute Governance + Job Workflows

---

## Scenario Overview

You are a Databricks administrator at **TechFlow Industries**. Building on foundational governance, you need to design compute policies and job orchestration.

### Company Profile

| Attribute | Details |
|-----------|---------|
| **Teams** | Data Engineering (10), Data Science (5), Analytics (15), Finance (5) |
| **Data Domains** | Sales, Customers, Products, Finance |
| **Environments** | Development, Staging, Production |
| **Workloads** | ETL pipelines, ML training, BI dashboards |

---

## Part 1: Complete Unity Catalog Design (10 minutes)

### Task 1.1: Full Catalog Hierarchy

```
Metastore: techflow_metastore
│
├── Catalog: dev_techflow
│   ├── Schema: sales
│   ├── Schema: customers
│   ├── Schema: products
│   ├── Schema: sandbox_<username>  (per-user sandboxes)
│   └── Schema: ml_experiments
│
├── Catalog: staging_techflow
│   ├── Schema: sales
│   ├── Schema: customers
│   └── Schema: products
│
├── Catalog: prod_techflow
│   ├── Schema: bronze (raw data)
│   ├── Schema: silver (cleansed)
│   ├── Schema: gold (curated)
│   └── Schema: finance (restricted)
│
└── Catalog: sandbox
    └── Schema: <team_sandboxes>
```

### Task 1.2: Create SQL for Structure

```sql
-- Production Catalog with Medallion Architecture
CREATE CATALOG IF NOT EXISTS prod_techflow;
USE CATALOG prod_techflow;

CREATE SCHEMA IF NOT EXISTS bronze COMMENT 'Raw ingested data';
CREATE SCHEMA IF NOT EXISTS silver COMMENT 'Cleansed and validated data';
CREATE SCHEMA IF NOT EXISTS gold COMMENT 'Business-ready curated data';
CREATE SCHEMA IF NOT EXISTS finance COMMENT 'Restricted financial data';

-- Staging Catalog
CREATE CATALOG IF NOT EXISTS staging_techflow;
USE CATALOG staging_techflow;

CREATE SCHEMA IF NOT EXISTS sales;
CREATE SCHEMA IF NOT EXISTS customers;
CREATE SCHEMA IF NOT EXISTS products;
```

---

## Part 2: Permission Matrix (10 minutes)

### Task 2.1: Complete Permission Matrix

| Group | dev_techflow | staging_techflow | prod_techflow.bronze | prod_techflow.silver | prod_techflow.gold | prod_techflow.finance |
|-------|--------------|------------------|----------------------|----------------------|--------------------|-----------------------|
| data_engineers | ALL | ALL | ALL | ALL | SELECT | - |
| data_scientists | SELECT | SELECT | - | SELECT | SELECT | - |
| data_analysts | - | - | - | - | SELECT | - |
| finance_team | - | - | - | - | SELECT | ALL |
| platform_admins | ALL | ALL | ALL | ALL | ALL | ALL |

### Task 2.2: Grant Statements

```sql
-- Data Engineers
GRANT ALL PRIVILEGES ON CATALOG dev_techflow TO data_engineers;
GRANT ALL PRIVILEGES ON CATALOG staging_techflow TO data_engineers;
GRANT ALL PRIVILEGES ON SCHEMA prod_techflow.bronze TO data_engineers;
GRANT ALL PRIVILEGES ON SCHEMA prod_techflow.silver TO data_engineers;
GRANT SELECT ON SCHEMA prod_techflow.gold TO data_engineers;

-- Data Scientists
GRANT USE CATALOG, SELECT ON CATALOG dev_techflow TO data_scientists;
GRANT USE CATALOG, SELECT ON CATALOG staging_techflow TO data_scientists;
GRANT USE CATALOG ON CATALOG prod_techflow TO data_scientists;
GRANT SELECT ON SCHEMA prod_techflow.silver TO data_scientists;
GRANT SELECT ON SCHEMA prod_techflow.gold TO data_scientists;

-- Data Analysts
GRANT USE CATALOG ON CATALOG prod_techflow TO data_analysts;
GRANT SELECT ON SCHEMA prod_techflow.gold TO data_analysts;

-- Finance Team
GRANT USE CATALOG ON CATALOG prod_techflow TO finance_team;
GRANT SELECT ON SCHEMA prod_techflow.gold TO finance_team;
GRANT ALL PRIVILEGES ON SCHEMA prod_techflow.finance TO finance_team;
```

---

## Part 3: Cluster Policies (10 minutes)

### Task 3.1: Development Policy

```json
{
  "name": "techflow-dev-policy",
  "definition": {
    "spark_version": {
      "type": "regex",
      "pattern": "^14\\.[0-9]+\\.x-scala2\\.12$",
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

### Task 3.2: Production Policy

```json
{
  "name": "techflow-prod-policy",
  "definition": {
    "spark_version": {
      "type": "fixed",
      "value": "14.3.x-scala2.12",
      "hidden": true
    },
    "node_type_id": {
      "type": "fixed",
      "value": "Standard_E8ds_v4"
    },
    "driver_node_type_id": {
      "type": "fixed",
      "value": "Standard_E4ds_v4"
    },
    "autoscale.min_workers": {
      "type": "range",
      "minValue": 2,
      "maxValue": 20
    },
    "autoscale.max_workers": {
      "type": "range",
      "minValue": 2,
      "maxValue": 20
    },
    "custom_tags.Environment": {
      "type": "fixed",
      "value": "production"
    },
    "custom_tags.CostCenter": {
      "type": "regex",
      "pattern": "^CC-[0-9]{4}$",
      "isOptional": false
    }
  }
}
```

---

## Part 4: Job Workflow Design (10 minutes)

### Task 4.1: ETL Workflow Diagram

```
┌─────────────────────────────────────────────────────────────┐
│              Daily ETL Pipeline Workflow                    │
│                                                             │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐             │
│  │ Extract  │───►│ Extract  │───►│ Extract  │             │
│  │ Sales    │    │ Customers│    │ Products │             │
│  └────┬─────┘    └────┬─────┘    └────┬─────┘             │
│       │               │               │                    │
│       └───────────────┼───────────────┘                    │
│                       ▼                                    │
│              ┌─────────────┐                               │
│              │  Transform  │                               │
│              │   (Join)    │                               │
│              └──────┬──────┘                               │
│                     │                                      │
│        ┌────────────┼────────────┐                        │
│        ▼            ▼            ▼                        │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐                  │
│  │ Load     │ │ Load     │ │ Load     │                  │
│  │ Bronze   │ │ Silver   │ │ Gold     │                  │
│  └──────────┘ └──────────┘ └──────────┘                  │
└─────────────────────────────────────────────────────────────┘
```

### Task 4.2: Job Configuration

| Setting | Value | Reason |
|---------|-------|--------|
| **Trigger** | CRON: `0 2 * * *` | Run daily at 2 AM |
| **Timezone** | UTC | Consistent scheduling |
| **Max Concurrent Runs** | 1 | Prevent duplicate processing |
| **Retry Policy** | 2 retries, 5 min interval | Handle transient failures |
| **Timeout** | 2 hours | Prevent runaway jobs |
| **Cluster** | Job cluster (prod policy) | Cost-efficient |

---

## Part 5: SQL Warehouse Configuration (5 minutes)

### Task 5.1: Warehouse Design

| Warehouse | Size | Auto Stop | Max Clusters | Purpose |
|-----------|------|-----------|--------------|---------|
| analytics-wh | Medium | 15 min | 4 | Ad-hoc analyst queries |
| bi-dashboards-wh | Large | 30 min | 8 | BI tool connections |
| etl-wh | Small | 10 min | 2 | ETL SQL tasks |

---

## Deliverables Checklist

- [ ] Complete catalog hierarchy (4 catalogs)
- [ ] Full permission matrix (5 groups × 6 permission areas)
- [ ] SQL GRANT statements for all permissions
- [ ] Development cluster policy (JSON)
- [ ] Production cluster policy (JSON)
- [ ] ETL workflow diagram
- [ ] Job configuration table
- [ ] SQL warehouse configuration

---

## Evaluation Criteria (Intermediate)

| Criteria | Points | Your Score |
|----------|--------|------------|
| Catalog structure (medallion architecture) | 15 | |
| Permission matrix (complete, least privilege) | 20 | |
| Cluster policy - Development | 15 | |
| Cluster policy - Production | 15 | |
| Job workflow design | 15 | |
| SQL warehouse configuration | 10 | |
| Documentation clarity | 10 | |
| **Total** | **100** | |

**Passing Score:** 70 points

---

## What's Next?

After completing the Intermediate track, consider the **Advanced track** which adds:
- Full security configuration (network, encryption)
- Compliance controls (SOC 2, GDPR)
- Cost monitoring dashboard
- Administrator runbooks

---

*Capstone Intermediate Track | Version 3.0*
