# Capstone Project: Beginner Track
## Enterprise Databricks Environment Design - TechFlow Industries

**Duration:** 30 minutes
**Difficulty:** Beginner
**Focus:** Unity Catalog Structure & Basic Permissions

---

## Scenario Overview

You are a new Databricks administrator at **TechFlow Industries**. Your task is to design the foundational data governance structure using Unity Catalog.

### Company Profile (Simplified)

| Attribute | Details |
|-----------|---------|
| **Teams** | Data Engineering (10), Analytics (15) |
| **Data Domains** | Sales, Customers |
| **Environments** | Development, Production |

---

## Part 1: Unity Catalog Structure (15 minutes)

### Task 1.1: Design the Catalog Hierarchy

Complete the following catalog structure:

```
Metastore: techflow_metastore
│
├── Catalog: dev_techflow
│   ├── Schema: sales
│   │   ├── Table: raw_orders
│   │   └── Table: raw_products
│   └── Schema: customers
│       └── Table: raw_customers
│
└── Catalog: prod_techflow
    ├── Schema: sales
    │   ├── Table: orders (curated)
    │   └── Table: products (curated)
    └── Schema: customers
        └── Table: customers (curated)
```

### Task 1.2: Create the Structure (SQL)

Write SQL statements to create this structure:

```sql
-- Create Development Catalog
CREATE CATALOG IF NOT EXISTS dev_techflow;

-- Create Production Catalog
CREATE CATALOG IF NOT EXISTS prod_techflow;

-- Create Schemas in Dev
USE CATALOG dev_techflow;
CREATE SCHEMA IF NOT EXISTS sales;
CREATE SCHEMA IF NOT EXISTS customers;

-- Create Schemas in Prod
USE CATALOG prod_techflow;
CREATE SCHEMA IF NOT EXISTS sales;
CREATE SCHEMA IF NOT EXISTS customers;
```

---

## Part 2: Group Structure (10 minutes)

### Task 2.1: Design Groups

| Group Name | Members | Purpose |
|------------|---------|---------|
| data_engineers | 10 engineers | ETL development and data pipelines |
| data_analysts | 15 analysts | SQL queries and reporting |
| platform_admins | 2 admins | Platform management |

### Task 2.2: Create Groups

```sql
-- Note: Groups are typically created via Admin Console or SCIM
-- This represents the conceptual design

-- Group: data_engineers
-- Members: engineering team
-- Purpose: Full access to dev, read access to prod

-- Group: data_analysts
-- Members: analytics team
-- Purpose: Read access to prod curated data

-- Group: platform_admins
-- Members: admin team
-- Purpose: Full control over both catalogs
```

---

## Part 3: Basic Permissions (5 minutes)

### Task 3.1: Grant Permissions

Write SQL GRANT statements:

```sql
-- Platform Admins: Full access to everything
GRANT ALL PRIVILEGES ON CATALOG dev_techflow TO platform_admins;
GRANT ALL PRIVILEGES ON CATALOG prod_techflow TO platform_admins;

-- Data Engineers: Full access to dev, read on prod
GRANT ALL PRIVILEGES ON CATALOG dev_techflow TO data_engineers;
GRANT USE CATALOG ON CATALOG prod_techflow TO data_engineers;
GRANT SELECT ON CATALOG prod_techflow TO data_engineers;

-- Data Analysts: Read access to prod only
GRANT USE CATALOG ON CATALOG prod_techflow TO data_analysts;
GRANT SELECT ON CATALOG prod_techflow TO data_analysts;
```

---

## Deliverables Checklist

- [ ] Catalog hierarchy diagram with 2 catalogs
- [ ] Schema structure with sales and customers
- [ ] 3 groups defined with members and purpose
- [ ] SQL statements to create catalogs and schemas
- [ ] SQL GRANT statements for permissions

---

## Evaluation Criteria (Beginner)

| Criteria | Points | Your Score |
|----------|--------|------------|
| Catalog structure (correct hierarchy) | 20 | |
| Schema design (appropriate separation) | 15 | |
| Group design (clear purpose) | 15 | |
| Permission grants (least privilege) | 20 | |
| SQL syntax correctness | 15 | |
| Documentation clarity | 15 | |
| **Total** | **100** | |

**Passing Score:** 70 points

---

## Sample Solution Format

### Catalog Diagram

```
┌─────────────────────────────────────────┐
│         techflow_metastore              │
│                                         │
│  ┌─────────────┐   ┌─────────────┐     │
│  │ dev_techflow│   │prod_techflow│     │
│  ├─────────────┤   ├─────────────┤     │
│  │ sales       │   │ sales       │     │
│  │ customers   │   │ customers   │     │
│  └─────────────┘   └─────────────┘     │
└─────────────────────────────────────────┘
```

### Permission Matrix

| Group | dev_techflow | prod_techflow |
|-------|--------------|---------------|
| platform_admins | ALL | ALL |
| data_engineers | ALL | SELECT |
| data_analysts | - | SELECT |

---

## What's Next?

After completing the Beginner track, consider attempting the **Intermediate track** which adds:
- Permission matrices
- Cluster policies
- Job workflow design
- SQL warehouse configuration

---

*Capstone Beginner Track | Version 3.0*
