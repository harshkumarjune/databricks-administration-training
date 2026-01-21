# Day 6 Pre-Reading Materials

## Databricks Platform Administration Training
### Unity Catalog: Architecture & Setup

---

## Overview

Day 6 introduces Unity Catalog, Databricks' unified governance solution. Understanding Unity Catalog architecture is essential for implementing data governance at scale.

**Estimated Reading Time**: 30-35 minutes

---

## Required Reading

### 1. Unity Catalog Overview

**Source**: Databricks Documentation

**Key Concepts to Understand**:
- What problems does Unity Catalog solve?
- How does it differ from the legacy Hive metastore?
- What assets can be governed?

**Read**: [What is Unity Catalog?](https://docs.databricks.com/en/data-governance/unity-catalog/index.html)

**Focus Areas**:
- Unified governance for data and AI
- Cross-workspace data sharing
- Automatic lineage tracking

### 2. Three-Level Namespace

**Source**: Databricks Documentation

**Key Concepts to Understand**:
- Catalog → Schema → Table hierarchy
- How namespacing affects access
- Fully qualified names

**Read**: [Unity Catalog object model](https://docs.databricks.com/en/data-governance/unity-catalog/index.html#the-unity-catalog-object-model)

**Focus Areas**:
- Metastore as top-level container
- Catalog organization patterns
- Schema naming conventions

### 3. Metastore Configuration

**Source**: Databricks Documentation

**Key Concepts to Understand**:
- One metastore per region
- Metastore to workspace binding
- Storage configuration

**Read**: [Create a Unity Catalog metastore](https://docs.databricks.com/en/data-governance/unity-catalog/create-metastore.html)

**Focus Areas**:
- Metastore admin role
- Root storage location
- Workspace assignment

---

## Key Terminology

| Term | Definition |
|------|------------|
| **Unity Catalog** | Centralized governance solution for data and AI |
| **Metastore** | Top-level container for all Unity Catalog objects (regional) |
| **Catalog** | Container for schemas, first level of namespace |
| **Schema** | Container for tables/views, second level of namespace |
| **Managed Table** | Table where Unity Catalog manages the data lifecycle |
| **External Table** | Table pointing to data in external storage |
| **Storage Credential** | Object referencing cloud IAM for storage access |
| **External Location** | Mapping of storage path to storage credential |

---

## Architecture Diagram

```
Account
  └── Metastore (us-east-1)
        ├── Catalog: dev_sales
        │     ├── Schema: bronze
        │     ├── Schema: silver
        │     └── Schema: gold
        └── Catalog: prod_sales
              ├── Schema: bronze
              ├── Schema: silver
              └── Schema: gold

Workspaces attached to metastore:
  - workspace-dev (us-east-1)
  - workspace-prod (us-east-1)
```

---

## Self-Assessment Questions

1. What is the relationship between a metastore and workspaces?
2. Why can a metastore only attach to workspaces in the same region?
3. What's the difference between a managed table and an external table?
4. What happens to data when you DROP a managed table vs external table?

---

## Recommended Additional Reading

- [Unity Catalog best practices](https://docs.databricks.com/en/data-governance/unity-catalog/best-practices.html)
- [Managed vs external tables](https://docs.databricks.com/en/data-governance/unity-catalog/create-tables.html)
- [Storage credentials and external locations](https://docs.databricks.com/en/data-governance/unity-catalog/manage-external-locations-and-credentials.html)

---

*Pre-reading materials for Databricks Platform Administration Training - Day 6*
