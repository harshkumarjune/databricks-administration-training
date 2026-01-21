# Foundational Pre-Reading Materials

## Databricks Platform Administration Training
### Complete Before Day 1

---

## Overview

This document provides essential foundational reading to prepare you for the Databricks Platform Administration Training. Completing this material will ensure you have the baseline knowledge needed for success.

**Total Estimated Reading Time**: 2-3 hours

---

## Required Foundational Reading

### 1. Introduction to Databricks

**Source**: Databricks Documentation

**Key Concepts**:
- What is Databricks?
- The Lakehouse architecture
- How Databricks differs from traditional data platforms

**Read**: [Introduction to Databricks](https://docs.databricks.com/en/introduction/index.html)

**Time**: 30 minutes

---

### 2. Lakehouse Architecture

**Source**: Databricks Glossary

**Key Concepts**:
- Data Lake vs Data Warehouse vs Lakehouse
- Benefits of the Lakehouse approach
- ACID transactions on data lakes

**Read**: [What is a Data Lakehouse?](https://www.databricks.com/glossary/data-lakehouse)

**Time**: 20 minutes

---

### 3. Delta Lake Fundamentals

**Source**: Delta Lake Documentation

**Key Concepts**:
- What is Delta Lake?
- ACID transactions
- Time travel capabilities

**Read**: [Delta Lake Introduction](https://docs.databricks.com/en/delta/index.html)

**Time**: 30 minutes

---

### 4. Unity Catalog Overview

**Source**: Databricks Documentation

**Key Concepts**:
- Unified governance for data and AI
- The three-level namespace
- Why centralized governance matters

**Read**: [What is Unity Catalog?](https://docs.databricks.com/en/data-governance/unity-catalog/index.html)

**Time**: 30 minutes

---

### 5. Databricks Administration Basics

**Source**: Databricks Documentation

**Key Concepts**:
- Account vs Workspace administration
- Admin roles and responsibilities
- Key administrative tasks

**Read**: [Administration overview](https://docs.databricks.com/en/admin/index.html)

**Time**: 30 minutes

---

## Foundational Concepts Reference

### The Lakehouse Architecture

```
Traditional Approach:
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│  Data Lake  │ → │     ETL     │ → │  Data       │
│  (Storage)  │    │  Pipelines  │    │  Warehouse  │
└─────────────┘    └─────────────┘    └─────────────┘
      │                                      │
      ▼                                      ▼
   ML/Data Science                    BI/Analytics

Lakehouse Approach:
┌───────────────────────────────────────────────┐
│              Data Lakehouse                   │
│  ┌─────────────────────────────────────────┐  │
│  │           Delta Lake (Storage)          │  │
│  └─────────────────────────────────────────┘  │
│         │              │              │       │
│         ▼              ▼              ▼       │
│   ML/Data Science  BI/Analytics  Streaming   │
└───────────────────────────────────────────────┘
```

---

### Databricks Architecture Overview

```
┌─────────────────────────────────────────────────────┐
│                    Control Plane                     │
│              (Managed by Databricks)                 │
│  ┌─────────┐  ┌─────────┐  ┌─────────────────────┐  │
│  │ Web UI  │  │  APIs   │  │ Cluster Management  │  │
│  └─────────┘  └─────────┘  └─────────────────────┘  │
└─────────────────────────────────────────────────────┘
                         │
                         │ Secure Connection
                         ▼
┌─────────────────────────────────────────────────────┐
│                     Data Plane                       │
│           (Your Cloud Account - AWS/Azure/GCP)       │
│  ┌─────────────────┐  ┌─────────────────────────┐   │
│  │ Compute Clusters │  │   Data Storage          │   │
│  │  (VMs/Nodes)     │  │   (S3/ADLS/GCS)         │   │
│  └─────────────────┘  └─────────────────────────┘   │
└─────────────────────────────────────────────────────┘
```

---

### Unity Catalog Hierarchy

```
Account
  └── Metastore (Regional)
        ├── Catalog: sales
        │     ├── Schema: bronze
        │     │     ├── Table: raw_orders
        │     │     └── Table: raw_customers
        │     ├── Schema: silver
        │     │     └── Table: cleaned_orders
        │     └── Schema: gold
        │           └── Table: order_summary
        │
        └── Catalog: marketing
              └── Schema: analytics
                    └── Table: campaign_metrics
```

---

## Key Terminology Glossary

| Term | Definition |
|------|------------|
| **Lakehouse** | Architecture combining data lake and warehouse capabilities |
| **Delta Lake** | Open-source storage layer providing ACID transactions |
| **Unity Catalog** | Databricks' unified governance solution |
| **Metastore** | Top-level container for Unity Catalog objects |
| **Catalog** | First level of the three-level namespace |
| **Schema** | Second level (also called database) |
| **Control Plane** | Databricks-managed infrastructure |
| **Data Plane** | Customer's cloud infrastructure |
| **DBU** | Databricks Unit - compute consumption measure |
| **Workspace** | Collaborative environment for Databricks users |

---

## Pre-Training Self-Check

Before starting the training, ensure you can answer:

1. What is the difference between a data lake and a data warehouse?
2. What makes Delta Lake different from regular Parquet files?
3. What is the purpose of Unity Catalog?
4. What is the difference between Control Plane and Data Plane?
5. What is a DBU?

---

## Additional Resources

### Video Resources
- [Databricks Lakehouse Platform Overview](https://www.databricks.com/product/data-lakehouse)
- [Unity Catalog Deep Dive](https://www.databricks.com/product/unity-catalog)

### Interactive Learning
- [Databricks Academy Free Courses](https://www.databricks.com/learn/training)
- [Community Edition for Practice](https://community.cloud.databricks.com/)

---

*Foundational Pre-Reading for Databricks Platform Administration Training*
