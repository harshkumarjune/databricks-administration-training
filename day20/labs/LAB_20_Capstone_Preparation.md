# Lab 20: Capstone Project Preparation & Execution
## Databricks Platform Administration Training

**Duration:** 60 minutes (within 2-hour session)
**Difficulty:** All Levels (Track-dependent)
**Prerequisites:** Days 1-19 completed

---

## Lab Overview

This lab provides guidance for completing your capstone project. You'll apply all concepts learned throughout the 20-day program to design and document a complete enterprise Databricks environment for TechFlow Industries.

---

## Capstone Track Selection

| Track | Duration | Focus Areas | Recommended For |
|-------|----------|-------------|-----------------|
| **Beginner** | 30 min | Unity Catalog structure, basic permissions | New to Databricks admin |
| **Intermediate** | 45 min | + Cluster policies, job workflows | Some experience |
| **Advanced** | 60 min | + Security, compliance, cost governance | Production experience |

**Select your track based on:**
- Your comfort level with the material
- Time available
- Certification goals

---

## TechFlow Industries Scenario

### Company Profile

| Attribute | Details |
|-----------|---------|
| **Industry** | Technology / SaaS |
| **Databricks Users** | 75 across 4 teams |
| **Teams** | Data Engineering, Data Science, Analytics, Finance |
| **Environments** | Development, Staging, Production |
| **Data Volume** | 50 TB, growing 5 TB/month |
| **Compliance** | SOC 2 Type II, GDPR |
| **Cloud** | Azure (primary) |

### Data Domain Summary

| Domain | Description | Sensitivity |
|--------|-------------|-------------|
| `raw_data` | Ingestion zone | Medium |
| `processed` | Cleansed data | Medium |
| `analytics` | Business metrics | Low |
| `finance` | Financial reports | High |
| `ml_features` | ML feature store | Medium |
| `pii` | Personal data | High (GDPR) |

---

## Part 1: Environment Setup (5 minutes)

### Task 1.1: Prepare Your Workspace

1. Open a new notebook or SQL editor
2. Create a scratch area for your design work:

```sql
-- Create your capstone workspace (optional)
CREATE SCHEMA IF NOT EXISTS training_catalog.capstone_workspace;
USE training_catalog.capstone_workspace;
```

### Task 1.2: Review Requirements Checklist

**All Tracks:**
- [ ] Catalog hierarchy diagram
- [ ] Permission matrix (groups × objects)
- [ ] Development cluster policy (JSON)

**Intermediate Track (+):**
- [ ] Production cluster policy
- [ ] Staging environment design
- [ ] Job workflow diagram

**Advanced Track (+):**
- [ ] ML-optimized cluster policy
- [ ] Security configuration document
- [ ] Compliance controls mapping (SOC 2/GDPR)
- [ ] Cost monitoring queries
- [ ] Administrator runbook outline

---

## Part 2: Unity Catalog Design (15 minutes)

### Task 2.1: Design Catalog Structure

Create your three-level namespace design:

```
metastore: techflow_metastore
├── catalog: techflow_dev
│   ├── schema: raw_data
│   ├── schema: processed
│   ├── schema: analytics
│   └── schema: ml_features
├── catalog: techflow_staging
│   └── [mirror of dev structure]
├── catalog: techflow_prod
│   └── [mirror of dev structure]
└── catalog: techflow_shared
    ├── schema: finance (high security)
    └── schema: reference_data
```

### Task 2.2: Write Catalog Creation SQL

```sql
-- Beginner: Create basic catalog structure
CREATE CATALOG IF NOT EXISTS techflow_dev;
CREATE SCHEMA IF NOT EXISTS techflow_dev.raw_data;
CREATE SCHEMA IF NOT EXISTS techflow_dev.processed;
CREATE SCHEMA IF NOT EXISTS techflow_dev.analytics;
CREATE SCHEMA IF NOT EXISTS techflow_dev.ml_features;

-- Document your design decisions:
-- Why separate catalogs per environment?
-- What naming conventions are you using?
```

### Task 2.3: Design Permission Matrix

| Group | techflow_dev | techflow_staging | techflow_prod | finance |
|-------|--------------|------------------|---------------|---------|
| data_engineers | ALL PRIVILEGES | SELECT, MODIFY | SELECT | NONE |
| data_scientists | SELECT, CREATE | SELECT | SELECT | NONE |
| analysts | SELECT | SELECT | SELECT | SELECT (masked) |
| finance_team | NONE | NONE | NONE | ALL PRIVILEGES |
| platform_admins | ALL PRIVILEGES | ALL PRIVILEGES | ALL PRIVILEGES | ALL PRIVILEGES |

### Task 2.4: Write Permission GRANT Statements

```sql
-- Create groups (conceptual)
-- CREATE GROUP data_engineers;
-- CREATE GROUP data_scientists;
-- CREATE GROUP analysts;
-- CREATE GROUP finance_team;

-- Grant permissions
GRANT USAGE ON CATALOG techflow_dev TO data_engineers;
GRANT ALL PRIVILEGES ON SCHEMA techflow_dev.raw_data TO data_engineers;
GRANT ALL PRIVILEGES ON SCHEMA techflow_dev.processed TO data_engineers;

GRANT USAGE ON CATALOG techflow_dev TO data_scientists;
GRANT SELECT, CREATE TABLE ON SCHEMA techflow_dev.ml_features TO data_scientists;

-- Continue for all groups and catalogs...
```

---

## Part 3: Cluster Policy Design (15 minutes)

### Task 3.1: Development Cluster Policy

Create a cost-controlled development cluster policy:

```json
{
  "spark_version": {
    "type": "regex",
    "pattern": "14\\.[0-9]+\\.x-scala2\\.12",
    "defaultValue": "14.3.x-scala2.12"
  },
  "node_type_id": {
    "type": "allowlist",
    "values": [
      "Standard_DS3_v2",
      "Standard_DS4_v2",
      "Standard_E4ds_v4"
    ],
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
  },
  "spark_conf.spark.databricks.cluster.profile": {
    "type": "fixed",
    "value": "singleNode",
    "hidden": true
  }
}
```

### Task 3.2: Production Cluster Policy (Intermediate+)

```json
{
  "spark_version": {
    "type": "fixed",
    "value": "14.3.x-scala2.12"
  },
  "node_type_id": {
    "type": "allowlist",
    "values": [
      "Standard_E8ds_v4",
      "Standard_E16ds_v4"
    ]
  },
  "driver_node_type_id": {
    "type": "fixed",
    "value": "Standard_E8ds_v4"
  },
  "num_workers": {
    "type": "range",
    "minValue": 2,
    "maxValue": 16
  },
  "autoscale.min_workers": {
    "type": "range",
    "minValue": 2,
    "maxValue": 4
  },
  "autoscale.max_workers": {
    "type": "range",
    "minValue": 4,
    "maxValue": 16
  },
  "azure_attributes.availability": {
    "type": "fixed",
    "value": "SPOT_WITH_FALLBACK_AZURE"
  },
  "custom_tags.Team": {
    "type": "unlimited",
    "isOptional": false
  },
  "custom_tags.Environment": {
    "type": "fixed",
    "value": "production"
  },
  "custom_tags.CostCenter": {
    "type": "unlimited",
    "isOptional": false
  }
}
```

### Task 3.3: ML Cluster Policy (Advanced)

```json
{
  "spark_version": {
    "type": "regex",
    "pattern": "14\\.[0-9]+\\.x-gpu-ml-scala2\\.12"
  },
  "node_type_id": {
    "type": "allowlist",
    "values": [
      "Standard_NC6s_v3",
      "Standard_NC12s_v3"
    ]
  },
  "num_workers": {
    "type": "range",
    "minValue": 1,
    "maxValue": 4
  },
  "autotermination_minutes": {
    "type": "range",
    "minValue": 60,
    "maxValue": 240,
    "defaultValue": 120
  },
  "custom_tags.Team": {
    "type": "fixed",
    "value": "data_science"
  },
  "custom_tags.Workload": {
    "type": "fixed",
    "value": "ml_training"
  },
  "init_scripts.0.workspace.destination": {
    "type": "fixed",
    "value": "/Shared/ml-init-scripts/gpu-setup.sh",
    "hidden": true
  }
}
```

---

## Part 4: Job Workflow Design (Intermediate+, 10 minutes)

### Task 4.1: Design ETL Pipeline Workflow

```
Daily ETL Pipeline (CRON: 0 2 * * *)
├── Task 1: ingest_raw_data (notebook)
│   └── Cluster: job-cluster-etl
├── Task 2: validate_data (notebook)
│   └── Depends on: Task 1 (ALL_SUCCESS)
├── Task 3: transform_to_silver (notebook)
│   └── Depends on: Task 2 (ALL_SUCCESS)
├── Task 4: aggregate_to_gold (notebook)
│   └── Depends on: Task 3 (ALL_SUCCESS)
└── Task 5: notify_completion (notification task)
    └── Depends on: Task 4 (ALL_DONE)
```

### Task 4.2: Document Workflow Configuration

| Task | Type | Cluster | Timeout | Retries |
|------|------|---------|---------|---------|
| ingest_raw_data | Notebook | Job cluster | 60 min | 2 |
| validate_data | Notebook | Same cluster | 30 min | 1 |
| transform_to_silver | Notebook | Same cluster | 90 min | 2 |
| aggregate_to_gold | Notebook | Same cluster | 45 min | 1 |
| notify_completion | Notification | N/A | 5 min | 0 |

---

## Part 5: Security & Compliance (Advanced, 10 minutes)

### Task 5.1: Security Configuration Checklist

| Security Control | Configuration | Status |
|------------------|---------------|--------|
| SSO/SAML | Azure AD integration | [ ] |
| SCIM provisioning | Auto-sync groups | [ ] |
| IP access lists | Corporate IPs only | [ ] |
| Private Link | Backend connectivity | [ ] |
| CMK encryption | Azure Key Vault | [ ] |
| Audit logging | system.access.audit | [ ] |

### Task 5.2: GDPR Compliance Mapping

```sql
-- Query for GDPR data access audit
SELECT
    DATE(event_time) as access_date,
    user_identity.email,
    action_name,
    request_params.table_full_name
FROM system.access.audit
WHERE request_params.table_full_name LIKE '%pii%'
  AND event_time >= current_date() - 30
ORDER BY event_time DESC;
```

---

## Part 6: Cost Monitoring (Advanced, 5 minutes)

### Task 6.1: Team Cost Analysis Query

```sql
-- Monthly cost by team
SELECT
    DATE_TRUNC('month', usage_date) as month,
    custom_tags['Team'] as team,
    SUM(usage_quantity) as total_dbus,
    ROUND(SUM(usage_quantity) * 0.55, 2) as estimated_cost
FROM system.billing.usage
WHERE usage_date >= current_date() - 90
GROUP BY DATE_TRUNC('month', usage_date), custom_tags['Team']
ORDER BY month DESC, estimated_cost DESC;
```

### Task 6.2: Tag Compliance Check

```sql
-- Verify tagging compliance
SELECT
    ROUND(
        100.0 * SUM(CASE WHEN custom_tags['Team'] IS NOT NULL THEN usage_quantity ELSE 0 END)
        / SUM(usage_quantity), 2
    ) as team_tag_compliance_pct,
    ROUND(
        100.0 * SUM(CASE WHEN custom_tags['CostCenter'] IS NOT NULL THEN usage_quantity ELSE 0 END)
        / SUM(usage_quantity), 2
    ) as costcenter_tag_compliance_pct
FROM system.billing.usage
WHERE usage_date >= current_date() - 30;
```

---

## Submission

### Deliverables Checklist

**Beginner Track:**
- [ ] Catalog hierarchy document (visual + SQL)
- [ ] Permission matrix
- [ ] Development cluster policy JSON
- [ ] Brief design rationale (1-2 paragraphs)

**Intermediate Track (+ above):**
- [ ] Production cluster policy JSON
- [ ] Job workflow design document
- [ ] Environment separation strategy

**Advanced Track (+ above):**
- [ ] ML cluster policy JSON
- [ ] Security controls checklist
- [ ] Compliance mapping document
- [ ] Cost monitoring queries
- [ ] Administrator runbook outline

### Validation

Use the capstone validation script:

```bash
python run_validation.py --track [beginner|intermediate|advanced] --submission your_submission.json
```

---

## Lab Validation Checklist

- [ ] Selected appropriate track
- [ ] Completed catalog hierarchy design
- [ ] Created permission matrix
- [ ] Wrote development cluster policy
- [ ] (Intermediate+) Created production cluster policy
- [ ] (Intermediate+) Designed job workflow
- [ ] (Advanced) Completed security checklist
- [ ] (Advanced) Wrote cost monitoring queries
- [ ] Prepared submission for validation

---

*Lab Version: 3.0 | Day 20 - Capstone Project*
