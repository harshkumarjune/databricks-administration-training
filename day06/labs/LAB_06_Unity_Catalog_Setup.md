# Lab 06: Unity Catalog Setup

## Databricks Platform Administration Training
### Duration: 60 Minutes | Difficulty: Intermediate

---

## Lab Overview

Configure Unity Catalog components including catalogs, schemas, and tables. Explore the metastore configuration and understand the governance model.

### Learning Objectives

- Explore metastore configuration
- Create catalogs and schemas
- Create managed and external tables
- Navigate Data Explorer
- Understand storage credentials and external locations

---

## Part 1: Explore Metastore (15 minutes)

### Task 1.1: Access Data Explorer

1. Navigate to **Catalog** in the left sidebar
2. Review the catalog hierarchy displayed

### Task 1.2: Document Metastore Configuration

Navigate to workspace settings or account console to find metastore details:

| Property | Value |
|----------|-------|
| Metastore Name | |
| Region | |
| Default Catalog | |
| Storage Root | |

---

## Part 2: Create Catalog Hierarchy (20 minutes)

### Task 2.1: Create a Catalog

```sql
-- Create training catalog
CREATE CATALOG IF NOT EXISTS lab_training
COMMENT 'Catalog for training exercises';

-- Verify
SHOW CATALOGS;
```

### Task 2.2: Create Schemas

```sql
-- Create schemas within the catalog
CREATE SCHEMA IF NOT EXISTS lab_training.raw_data
COMMENT 'Raw ingested data';

CREATE SCHEMA IF NOT EXISTS lab_training.processed
COMMENT 'Processed and cleaned data';

-- Verify
SHOW SCHEMAS IN lab_training;
```

### Task 2.3: Create Managed Table

```sql
-- Create managed table
CREATE TABLE lab_training.raw_data.customers (
    customer_id INT,
    name STRING,
    email STRING,
    created_date DATE
);

-- Insert sample data
INSERT INTO lab_training.raw_data.customers VALUES
    (1, 'Alice Johnson', 'alice@example.com', '2024-01-15'),
    (2, 'Bob Smith', 'bob@example.com', '2024-01-16'),
    (3, 'Carol Williams', 'carol@example.com', '2024-01-17');

-- Query the table
SELECT * FROM lab_training.raw_data.customers;
```

### Task 2.4: Examine Table Properties

```sql
DESCRIBE EXTENDED lab_training.raw_data.customers;
```

Document:
| Property | Value |
|----------|-------|
| Type | Managed/External |
| Location | |
| Owner | |

---

## Part 3: Data Explorer Navigation (15 minutes)

### Task 3.1: Browse Catalog

1. In Data Explorer, expand `lab_training`
2. Expand `raw_data` schema
3. Click on `customers` table
4. Explore tabs: Columns, Sample Data, Details, Permissions

### Task 3.2: Search Functionality

1. Use the search bar to find `customers`
2. Search for tables by column name

### Task 3.3: View Lineage

1. Create a derived table:

```sql
CREATE TABLE lab_training.processed.customer_summary AS
SELECT
    COUNT(*) as total_customers,
    MIN(created_date) as first_customer,
    MAX(created_date) as latest_customer
FROM lab_training.raw_data.customers;
```

2. Navigate to `customer_summary` in Data Explorer
3. Click **Lineage** tab to see data flow

---

## Part 4: Cleanup (10 minutes)

### Task 4.1: Clean Up Test Resources

```sql
-- Drop tables
DROP TABLE IF EXISTS lab_training.processed.customer_summary;
DROP TABLE IF EXISTS lab_training.raw_data.customers;

-- Drop schemas
DROP SCHEMA IF EXISTS lab_training.processed;
DROP SCHEMA IF EXISTS lab_training.raw_data;

-- Drop catalog (if permitted)
-- DROP CATALOG IF EXISTS lab_training;
```

---

## Lab Validation Checklist

- [ ] Explored metastore configuration
- [ ] Created catalog and schemas
- [ ] Created managed table with data
- [ ] Navigated Data Explorer
- [ ] Viewed table lineage
- [ ] Cleaned up test resources

---

## Lab Summary

You learned:
1. Unity Catalog three-level namespace
2. Creating catalogs and schemas
3. Managed table creation
4. Data Explorer navigation
5. Lineage visualization

---

*Lab Version: 2.0 | Databricks Platform Administration Training - Day 6*
