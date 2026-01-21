# Capstone Project: Enterprise Databricks Environment Design

## Databricks Platform Administration Training
### Duration: 2-3 Hours | Comprehensive Integration Exercise

---

## Project Overview

Design and document a complete Databricks environment for **TechFlow Industries**, a mid-sized technology company migrating to a data lakehouse architecture. This capstone integrates all concepts from the 13-day training program.

---

## Company Profile: TechFlow Industries

| Attribute | Details |
|-----------|---------|
| **Industry** | Technology / SaaS |
| **Employees** | 500 total, 75 Databricks users |
| **Teams** | Data Engineering, Data Science, Analytics, Finance |
| **Data Volume** | 50 TB, growing 5 TB/month |
| **Environments** | Development, Staging, Production |
| **Compliance** | SOC 2 Type II, GDPR |
| **Cloud** | AWS (primary), considering multi-cloud |

### Business Requirements

1. **Data Engineering** needs to build ETL pipelines processing 10M+ records daily
2. **Data Science** requires ML workloads with GPU access
3. **Analytics** needs self-service SQL access to curated datasets
4. **Finance** requires strict access controls for financial data
5. **All teams** need cost visibility and chargeback

---

## Part 1: Unity Catalog Architecture (30 minutes)

### Task 1.1: Design Catalog Structure

Create a catalog hierarchy that supports:
- Environment separation (dev/staging/prod)
- Domain-based organization (sales, customers, products, finance)
- Medallion architecture (bronze, silver, gold)
- Team sandboxes for experimentation

**Deliverable**: Complete the catalog structure diagram

```
Metastore: techflow_metastore
│
├── Catalog: _______________
│   ├── Schema: _______________
│   ├── Schema: _______________
│   └── Schema: _______________
│
├── Catalog: _______________
│   ├── Schema: _______________
│   └── Schema: _______________
│
└── Catalog: _______________
    ├── Schema: _______________
    ├── Schema: _______________
    └── Schema: _______________
```

### Task 1.2: Define Storage Locations

Specify external storage locations for:

| Location Name | Cloud Path | Purpose |
|---------------|------------|---------|
| | s3://techflow-.../ | |
| | s3://techflow-.../ | |
| | s3://techflow-.../ | |

### Task 1.3: Managed vs External Tables

Document your table strategy:

| Data Type | Table Type | Reason |
|-----------|------------|--------|
| Raw ingestion data | | |
| Transformed data | | |
| ML feature stores | | |
| Regulatory data | | |

---

## Part 2: Identity & Access Management (30 minutes)

### Task 2.1: Group Structure

Design groups that support role-based access:

| Group Name | Members | Purpose |
|------------|---------|---------|
| | Data Engineers | |
| | Data Scientists | |
| | Business Analysts | |
| | Finance Team | |
| | Platform Team | |

### Task 2.2: Permission Matrix

Complete the permission matrix:

| Group | dev_techflow | staging_techflow | prod_techflow |
|-------|--------------|------------------|---------------|
| Data Engineers | | | |
| Data Scientists | | | |
| Analysts | | | |
| Finance | | | |

### Task 2.3: Service Principals

Design service principals for automation:

| Service Principal | Purpose | Permissions |
|-------------------|---------|-------------|
| | CI/CD Pipeline | |
| | ETL Scheduler | |
| | ML Training | |
| | Reporting | |

### Task 2.4: Write Permission SQL

```sql
-- Grant statements for Data Engineers


-- Grant statements for Data Scientists


-- Grant statements for Analysts


-- Grant statements for Finance (restricted)

```

---

## Part 3: Compute Governance (30 minutes)

### Task 3.1: Cluster Policy - Development

Design a cost-controlled development policy:

```json
{
  "name": "techflow-dev-policy",
  "definition": {
    "spark_version": {
      "type": "___",
      "pattern": "___",
      "defaultValue": "___"
    },
    "node_type_id": {
      "type": "___",
      "values": [___],
      "defaultValue": "___"
    },
    "num_workers": {
      "type": "___",
      "minValue": ___,
      "maxValue": ___
    },
    "autotermination_minutes": {
      "type": "___",
      "minValue": ___,
      "maxValue": ___,
      "defaultValue": ___
    },
    "custom_tags.Team": {
      "type": "___"
    },
    "custom_tags.Environment": {
      "type": "___",
      "value": "___"
    }
  }
}
```

### Task 3.2: Cluster Policy - Production

Design a stable production policy:

```json
{
  "name": "techflow-prod-policy",
  "definition": {
    // Complete the policy
  }
}
```

### Task 3.3: Cluster Policy - Data Science

Design an ML-enabled policy with optional GPU:

```json
{
  "name": "techflow-ml-policy",
  "definition": {
    // Complete the policy
  }
}
```

### Task 3.4: SQL Warehouse Configuration

| Warehouse | Size | Scaling | Auto-Stop | Purpose |
|-----------|------|---------|-----------|---------|
| | | | | Ad-hoc queries |
| | | | | BI dashboards |
| | | | | ETL SQL |

---

## Part 4: Job Orchestration (20 minutes)

### Task 4.1: ETL Workflow Design

Design a multi-task workflow for daily data processing:

```
Workflow: daily_etl_pipeline
│
├── Task: _______________
│   Type: _______________
│   Cluster: _______________
│   Dependencies: None
│
├── Task: _______________
│   Type: _______________
│   Cluster: _______________
│   Dependencies: [___]
│
└── Task: _______________
    Type: _______________
    Cluster: _______________
    Dependencies: [___]
```

### Task 4.2: Job Configuration

| Setting | Value | Reason |
|---------|-------|--------|
| Trigger | | |
| Max Concurrent Runs | | |
| Retry Policy | | |
| Alert Recipients | | |
| Timeout | | |

### Task 4.3: CI/CD Strategy

Document deployment approach:

| Environment | Branch | Trigger | Approvals |
|-------------|--------|---------|-----------|
| Development | | | |
| Staging | | | |
| Production | | | |

---

## Part 5: Monitoring & Cost Governance (20 minutes)

### Task 5.1: Cost Monitoring Queries

Write SQL queries for cost analysis:

```sql
-- Query 1: Daily DBU by team


-- Query 2: Cost by environment


-- Query 3: Tag compliance percentage

```

### Task 5.2: Dashboard Design

Sketch a cost governance dashboard:

| Widget | Chart Type | Query |
|--------|------------|-------|
| | | |
| | | |
| | | |
| | | |

### Task 5.3: Alert Configuration

| Alert | Threshold | Recipients | Frequency |
|-------|-----------|------------|-----------|
| Daily DBU exceeds budget | | | |
| Tag compliance below target | | | |
| Job failure rate | | | |

---

## Part 6: Security Configuration (20 minutes)

### Task 6.1: Network Security

| Feature | Configuration | Justification |
|---------|---------------|---------------|
| Private Link | | |
| Secure Cluster Connectivity | | |
| IP Access Lists | | |
| VPC/VNet Peering | | |

### Task 6.2: Data Security

| Feature | Configuration | Scope |
|---------|---------------|-------|
| Encryption at Rest | | |
| Encryption in Transit | | |
| Customer-Managed Keys | | |
| Column-Level Security | | |
| Row-Level Security | | |

### Task 6.3: Compliance Controls

| Requirement | Implementation |
|-------------|----------------|
| SOC 2 audit logging | |
| GDPR data access | |
| Data retention | |
| Access reviews | |

---

## Part 7: Documentation (10 minutes)

### Task 7.1: Architecture Summary

Write a one-page executive summary of your design.

### Task 7.2: Runbook Outline

Create an outline for an administrator runbook:

1. **Daily Tasks**
   -
   -
   -

2. **Weekly Tasks**
   -
   -
   -

3. **Monthly Tasks**
   -
   -
   -

4. **Incident Response**
   -
   -
   -

---

## Submission Requirements

### Deliverables Checklist

- [ ] Unity Catalog structure diagram and SQL
- [ ] Group structure and permission matrix
- [ ] Service principal design
- [ ] Three cluster policies (dev, prod, ML)
- [ ] SQL warehouse configuration
- [ ] ETL workflow design
- [ ] CI/CD deployment strategy
- [ ] Cost monitoring queries
- [ ] Dashboard design
- [ ] Alert configuration
- [ ] Security configuration
- [ ] Architecture summary
- [ ] Runbook outline

### Evaluation Criteria

| Criteria | Points | Description |
|----------|--------|-------------|
| Catalog Design | 15 | Logical structure, naming conventions |
| Access Control | 15 | Least privilege, group-based |
| Compute Governance | 15 | Cost control, appropriate constraints |
| Job Design | 10 | Proper dependencies, error handling |
| Cost Monitoring | 10 | Useful queries, actionable alerts |
| Security | 15 | Defense in depth, compliance |
| Documentation | 10 | Clear, complete, actionable |
| Best Practices | 10 | Industry standards, Databricks recommendations |
| **Total** | **100** | |

### Grading Scale

| Score | Grade | Certification Readiness |
|-------|-------|-------------------------|
| 90-100 | A | Certification Ready |
| 80-89 | B | Strong Foundation |
| 70-79 | C | Additional Review Needed |
| < 70 | NC | Requires Re-submission |

---

## Reference Solution

A reference solution is available in `CAPSTONE_SOLUTION.md` (trainer access only). Participants should attempt the capstone independently before reviewing the reference.

---

*Capstone Project Version: 2.0 | Databricks Platform Administration Training*
