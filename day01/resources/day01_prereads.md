# Day 1 Pre-Reading Materials

## Databricks Platform Administration Training
### Lakehouse & Workspace Foundations

---

## Overview

Day 1 introduces the foundational concepts of the Databricks Lakehouse Platform. These pre-reading materials will help you maximize your learning during the training session.

**Estimated Reading Time**: 20-30 minutes

---

## Required Reading

### 1. Lakehouse Architecture

**Source**: Databricks Documentation & Blog

**Key Concepts to Understand**:
- What problems does the Lakehouse architecture solve?
- How does Lakehouse compare to traditional data lakes and warehouses?
- What makes Delta Lake essential to the Lakehouse?

**Read**: [What is a Data Lakehouse?](https://docs.databricks.com/en/lakehouse/index.html)

**Focus Areas**:
- The evolution from data warehouses to data lakes to Lakehouse
- Key capabilities: ACID transactions, schema enforcement, governance
- Support for diverse workloads (BI, ML, streaming)

### 2. Databricks Architecture

**Source**: Databricks Documentation

**Key Concepts to Understand**:
- Control Plane vs Data Plane separation
- Where does compute run? Where is data stored?
- How does Databricks interact with your cloud account?

**Read**: [Databricks architecture overview](https://docs.databricks.com/en/getting-started/overview.html)

**Focus Areas**:
- Security implications of the two-plane architecture
- Cloud-specific deployment patterns
- Network connectivity between planes

### 3. Workspace Concepts

**Source**: Databricks Documentation

**Key Concepts to Understand**:
- What objects exist in a workspace?
- How is the workspace UI organized?
- What's the difference between workspace objects and data objects?

**Read**: [Databricks workspace](https://docs.databricks.com/en/workspace/index.html)

**Focus Areas**:
- Folders, notebooks, libraries, and repos
- Compute resources (clusters, SQL warehouses)
- Admin vs user capabilities

---

## Recommended Additional Reading

### Platform Overview
- [Get started with Databricks](https://docs.databricks.com/en/getting-started/index.html)
- [Databricks concepts](https://docs.databricks.com/en/getting-started/concepts.html)

### Administrator Introduction
- [Administration overview](https://docs.databricks.com/en/admin/index.html)
- [Account and workspace administration](https://docs.databricks.com/en/admin/account-settings-e2/index.html)

---

## Key Terminology

Review these terms before Day 1:

| Term | Definition |
|------|------------|
| **Lakehouse** | Architecture combining data lake flexibility with warehouse reliability |
| **Delta Lake** | Open-source storage layer providing ACID transactions on data lakes |
| **Control Plane** | Databricks-managed services (UI, scheduler, metadata) |
| **Data Plane** | Customer-managed compute and storage in their cloud account |
| **Workspace** | A Databricks deployment environment for teams |
| **Cluster** | A set of compute resources for running notebooks and jobs |
| **SQL Warehouse** | Compute endpoint optimized for SQL queries |
| **Unity Catalog** | Centralized governance solution for data and AI |

---

## Self-Assessment Questions

Before Day 1, see if you can answer:

1. What problem does the Lakehouse architecture solve that data lakes alone cannot?
2. Why is it important that customer data stays in the customer's cloud account?
3. What's the difference between an all-purpose cluster and a job cluster?
4. Who would typically have Account Admin vs Workspace Admin privileges?

---

## Lab Environment Check

Before Day 1, ensure you have:

- [ ] Valid credentials for your training workspace
- [ ] Modern web browser (Chrome or Firefox)
- [ ] Stable internet connection
- [ ] Workspace URL provided by your trainer

---

*Pre-reading materials for Databricks Platform Administration Training - Day 1*
