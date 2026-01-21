# Day 13 Pre-Reading Materials

## Databricks Platform Administration Training
### Standards, Certification & Wrap-Up

---

## Overview

Day 13 is the final day covering administration best practices, certification exam preparation, and the capstone project. This day consolidates all learning from the course.

**Estimated Reading Time**: 25-30 minutes

---

## Required Reading

### 1. Administration Best Practices

**Source**: Databricks Documentation

**Key Concepts to Understand**:
- Workspace organization
- Security baselines
- Operational standards

**Read**: [Best practices for account and workspace setup](https://docs.databricks.com/en/admin/workspace/best-practices.html)

**Focus Areas**:
- Naming conventions
- Environment separation
- Governance policies

### 2. Certification Exam Guide

**Source**: Databricks Certification

**Key Concepts to Understand**:
- Exam format and structure
- Domain coverage
- Study strategies

**Read**: [Databricks Certified Associate Platform Administrator](https://www.databricks.com/learn/certification/platform-administrator-associate)

**Focus Areas**:
- Exam objectives
- Practice questions
- Registration process

### 3. Unity Catalog Best Practices

**Source**: Databricks Documentation

**Key Concepts to Understand**:
- Catalog organization patterns
- Permission strategies
- Migration considerations

**Read**: [Unity Catalog best practices](https://docs.databricks.com/en/data-governance/unity-catalog/best-practices.html)

**Focus Areas**:
- Three-level namespace design
- Group-based permissions
- Data sharing patterns

---

## Key Terminology

| Term | Definition |
|------|------------|
| **LTS Runtime** | Long-Term Support Databricks Runtime |
| **Naming Convention** | Standard patterns for resource names |
| **Security Baseline** | Minimum security configuration requirements |
| **Runbook** | Documented operational procedures |
| **Capstone Project** | Comprehensive hands-on assessment |
| **Practice Exam** | Sample questions for certification prep |

---

## Certification Exam Overview

| Aspect | Details |
|--------|---------|
| **Name** | Databricks Certified Associate Platform Administrator |
| **Duration** | 90 minutes |
| **Questions** | 45 multiple choice |
| **Passing Score** | 70% |
| **Format** | Proctored, online |
| **Validity** | 2 years |

---

## Exam Domain Weights

```
Domain Coverage:

Databricks Platform        ~20%  ████████
Identity & Access          ~20%  ████████
Unity Catalog              ~25%  ██████████
Compute Management         ~20%  ████████
Operations                 ~15%  ██████
```

---

## High-Yield Exam Topics

1. **Unity Catalog**
   - Three-level namespace (Catalog → Schema → Table)
   - USAGE privilege requirement
   - Managed vs External tables

2. **Identity Management**
   - Account admin vs Workspace admin
   - SCIM provisioning flow
   - Service principals for automation

3. **Compute**
   - Job cluster vs All-purpose cluster
   - Cluster policies attributes
   - SQL warehouse types

4. **Operations**
   - System tables for monitoring
   - Job orchestration concepts
   - Troubleshooting basics

---

## Naming Convention Examples

| Resource | Pattern | Example |
|----------|---------|---------|
| Workspace | {env}-{region}-{purpose} | prod-us-east-analytics |
| Catalog | {env}_{domain} | prod_sales |
| Schema | {layer}_{source} | bronze_crm |
| Cluster | {team}-{purpose}-{size} | de-etl-medium |
| Job | {domain}_{pipeline}_{schedule} | sales_daily_etl |

---

## Security Checklist

```
Identity & Access:
□ SSO enabled
□ SCIM provisioning configured
□ Group-based permissions
□ Service principals for automation
□ Personal access tokens restricted

Network & Data:
□ IP access lists configured
□ Private Link (if required)
□ Customer-managed keys (if required)
□ Audit logging enabled
□ Data encryption verified
```

---

## Self-Assessment Questions

1. What are the five domains covered in the certification exam?
2. What is the minimum passing score for the exam?
3. Why should service principals be used instead of user accounts for CI/CD?
4. What is the recommended naming convention for catalogs?

---

## Course Review Summary

| Day | Topic | Key Takeaway |
|-----|-------|--------------|
| 1 | Platform Overview | Lakehouse = Data Lake + Warehouse |
| 2 | Account Console | Account vs Workspace administration |
| 3 | Identity Management | Groups for scalable permissions |
| 4 | Spark Administration | Jobs, Stages, Tasks hierarchy |
| 5 | Delta Lake | ACID transactions, time travel |
| 6 | Unity Catalog Setup | Metastore → Catalog → Schema → Table |
| 7 | UC Governance | USAGE required at every level |
| 8 | IAM & SCIM | Automated identity provisioning |
| 9 | Compute | Cluster policies for governance |
| 10 | Jobs & CI/CD | Databricks Asset Bundles |
| 11 | Monitoring | System tables for observability |
| 12 | Compliance & Cost | Network security, cost optimization |
| 13 | Standards | Best practices and certification |

---

## Recommended Additional Reading

- [Exam preparation guide](https://www.databricks.com/learn/training/certification-faq)
- [Databricks documentation](https://docs.databricks.com/)
- [Community forums](https://community.databricks.com/)
- [Databricks Academy](https://www.databricks.com/learn/training)

---

*Pre-reading materials for Databricks Platform Administration Training - Day 13*
