# Lab 06: Unity Catalog Setup & Configuration

## Databricks Platform Administration Training
### Duration: 60 Minutes | Difficulty: Intermediate

---

## Lab Overview

Configure Unity Catalog components including catalogs, schemas, tables, and views. Explore the metastore configuration, understand storage concepts, and navigate the Data Explorer interface.

### Learning Objectives

By the end of this lab, you will be able to:
- Explore and document metastore configuration
- Create catalogs with proper naming conventions
- Create schemas following medallion architecture
- Create managed and external tables
- Create views for data abstraction
- Navigate Data Explorer and view lineage
- Understand storage credentials and external locations (conceptual)

### Prerequisites

- Databricks workspace with Unity Catalog enabled
- User account with catalog creation privileges (or instructor-provided catalog)
- SQL Editor access

---

## Part 1: Explore Metastore Configuration (10 minutes)

### Task 1.1: Access the Data Explorer

1. Log in to your Databricks workspace
2. Click **Catalog** in the left sidebar
3. You should see the Data Explorer interface with available catalogs

**Checkpoint**: Record what catalogs you see:
- [ ] `main` (default catalog)
- [ ] `hive_metastore` (legacy)
- [ ] Other catalogs: ________________

### Task 1.2: Examine Metastore Details

In the Data Explorer, click the gear icon or navigate to workspace settings to find metastore information:

| Property | Your Value |
|----------|------------|
| Metastore Name | |
| Cloud Region | |
| Default Catalog | |
| Metastore Admin | |

### Task 1.3: Understand the Three-Level Namespace

Run the following queries to explore the current structure:

```sql
-- List all catalogs you have access to
SHOW CATALOGS;

-- List schemas in the main catalog
SHOW SCHEMAS IN main;

-- List tables in the default schema
SHOW TABLES IN main.default;
```

**Document your findings:**
| Level | Example from Your Environment |
|-------|-------------------------------|
| Catalog | |
| Schema | |
| Table | |

---

## Part 2: Create Catalog Structure (15 minutes)

### Task 2.1: Create a Training Catalog

```sql
-- Create a new catalog for this lab
-- Note: You may need CREATE CATALOG privilege
CREATE CATALOG IF NOT EXISTS training_lab
COMMENT 'Training lab catalog for Unity Catalog exercises';

-- Set as current catalog
USE CATALOG training_lab;

-- Verify creation
SHOW CATALOGS LIKE 'training*';
```

**If you cannot create catalogs**, use an instructor-provided catalog or work within an existing sandbox catalog.

### Task 2.2: Create Medallion Architecture Schemas

Create schemas following the bronze/silver/gold pattern:

```sql
-- Bronze layer: Raw ingested data
CREATE SCHEMA IF NOT EXISTS training_lab.bronze
COMMENT 'Raw data as ingested from source systems';

-- Silver layer: Cleansed and conformed data
CREATE SCHEMA IF NOT EXISTS training_lab.silver
COMMENT 'Cleansed, validated, and transformed data';

-- Gold layer: Business-ready aggregates
CREATE SCHEMA IF NOT EXISTS training_lab.gold
COMMENT 'Business-level aggregates and reporting tables';

-- Sandbox for experimentation
CREATE SCHEMA IF NOT EXISTS training_lab.sandbox
COMMENT 'Sandbox for ad-hoc analysis and testing';

-- Verify all schemas
SHOW SCHEMAS IN training_lab;
```

**Checkpoint**: List your created schemas:
- [ ] bronze
- [ ] silver
- [ ] gold
- [ ] sandbox

### Task 2.3: Document Schema Properties

```sql
-- Examine schema details
DESCRIBE SCHEMA EXTENDED training_lab.bronze;
```

| Property | Value |
|----------|-------|
| Schema Location | |
| Owner | |
| Comment | |

---

## Part 3: Create Tables (20 minutes)

### Task 3.1: Create a Managed Table in Bronze

```sql
-- Set context
USE CATALOG training_lab;
USE SCHEMA bronze;

-- Create managed table for raw customer data
CREATE TABLE IF NOT EXISTS customers_raw (
    customer_id INT COMMENT 'Unique customer identifier',
    first_name STRING COMMENT 'Customer first name',
    last_name STRING COMMENT 'Customer last name',
    email STRING COMMENT 'Customer email address',
    phone STRING COMMENT 'Customer phone number',
    created_at TIMESTAMP COMMENT 'Record creation timestamp',
    source_system STRING COMMENT 'Source system identifier'
)
COMMENT 'Raw customer data from CRM system'
TBLPROPERTIES (
    'quality' = 'bronze',
    'source' = 'crm_export'
);

-- Insert sample data
INSERT INTO customers_raw VALUES
    (1001, 'Alice', 'Johnson', 'alice.johnson@email.com', '555-0101', current_timestamp(), 'CRM'),
    (1002, 'Bob', 'Smith', 'bob.smith@email.com', '555-0102', current_timestamp(), 'CRM'),
    (1003, 'Carol', 'Williams', 'carol.williams@email.com', '555-0103', current_timestamp(), 'CRM'),
    (1004, 'David', 'Brown', 'david.brown@email.com', '555-0104', current_timestamp(), 'CRM'),
    (1005, 'Eve', 'Davis', 'eve.davis@email.com', '555-0105', current_timestamp(), 'CRM');

-- Query to verify
SELECT * FROM customers_raw;
```

### Task 3.2: Examine Managed Table Properties

```sql
-- Get detailed table information
DESCRIBE EXTENDED training_lab.bronze.customers_raw;
```

**Document the table properties:**
| Property | Value |
|----------|-------|
| Table Type | |
| Location | |
| Provider | |
| Owner | |

**Key Question**: What would happen if you DROP this managed table?

### Task 3.3: Create a Silver Layer Table

```sql
USE SCHEMA silver;

-- Create cleansed customer table
CREATE TABLE IF NOT EXISTS customers_cleansed AS
SELECT
    customer_id,
    INITCAP(first_name) AS first_name,
    INITCAP(last_name) AS last_name,
    LOWER(email) AS email,
    REGEXP_REPLACE(phone, '[^0-9]', '') AS phone_normalized,
    created_at,
    current_timestamp() AS processed_at
FROM training_lab.bronze.customers_raw
WHERE email IS NOT NULL;

-- Verify
SELECT * FROM customers_cleansed;
```

### Task 3.4: Create a Gold Layer Aggregate

```sql
USE SCHEMA gold;

-- Create business aggregate
CREATE TABLE IF NOT EXISTS customer_metrics AS
SELECT
    COUNT(*) AS total_customers,
    COUNT(DISTINCT email) AS unique_emails,
    MIN(created_at) AS first_customer_date,
    MAX(created_at) AS latest_customer_date,
    current_timestamp() AS report_generated
FROM training_lab.silver.customers_cleansed;

-- Query the metrics
SELECT * FROM customer_metrics;
```

### Task 3.5: Create a View

```sql
USE SCHEMA gold;

-- Create a view that masks sensitive data
CREATE OR REPLACE VIEW customer_directory AS
SELECT
    customer_id,
    first_name,
    last_name,
    CONCAT(SUBSTRING(email, 1, 3), '***@***') AS masked_email,
    CONCAT('***-***-', RIGHT(phone_normalized, 4)) AS masked_phone
FROM training_lab.silver.customers_cleansed;

-- Query the view
SELECT * FROM customer_directory;
```

---

## Part 4: Data Explorer Navigation (10 minutes)

### Task 4.1: Browse Your Catalog

1. In the Data Explorer, expand `training_lab`
2. Navigate through each schema (bronze, silver, gold)
3. Click on `customers_raw` table

**Explore each tab:**
- [ ] **Overview**: Table description and properties
- [ ] **Columns**: Column names, types, and comments
- [ ] **Sample Data**: Preview first rows (if permitted)
- [ ] **Details**: Full table properties
- [ ] **History**: Table version history
- [ ] **Lineage**: Data flow dependencies
- [ ] **Permissions**: Access control settings

### Task 4.2: View Data Lineage

1. Navigate to `training_lab.gold.customer_metrics` in Data Explorer
2. Click the **Lineage** tab
3. Observe the data flow from bronze → silver → gold

**Document the lineage:**
```
Source: ________________
  ↓
Transform: ________________
  ↓
Target: ________________
```

### Task 4.3: Search Functionality

1. Use the search bar at the top of Data Explorer
2. Search for "customer"
3. Note how it finds tables, columns, and comments

**Search results found:**
- Tables: _____
- Columns: _____

---

## Part 5: Understanding External Tables (Conceptual)

### Task 5.1: Understand the Difference

| Aspect | Managed Table | External Table |
|--------|---------------|----------------|
| Data location | Metastore-managed storage | Your specified cloud path |
| DROP behavior | Deletes data AND metadata | Deletes metadata only |
| Use case | New data, full lifecycle | Existing data, shared access |
| Creation | `CREATE TABLE` | `CREATE TABLE ... LOCATION` |

### Task 5.2: External Table Syntax (Reference Only)

```sql
-- NOTE: This requires storage credential and external location
-- DO NOT RUN unless you have proper access configured

-- Example external table creation
-- CREATE TABLE training_lab.bronze.external_orders (
--     order_id INT,
--     customer_id INT,
--     amount DECIMAL(10,2),
--     order_date DATE
-- )
-- LOCATION 's3://your-bucket/path/to/data/';
```

**Key Takeaway**: External tables require:
1. Storage Credential (IAM role/service principal)
2. External Location (path mapping with credential)
3. CREATE EXTERNAL TABLE privilege on that location

---

## Part 6: Cleanup (5 minutes)

### Task 6.1: Remove Test Objects

```sql
-- Drop tables in reverse dependency order
DROP TABLE IF EXISTS training_lab.gold.customer_metrics;
DROP VIEW IF EXISTS training_lab.gold.customer_directory;
DROP TABLE IF EXISTS training_lab.silver.customers_cleansed;
DROP TABLE IF EXISTS training_lab.bronze.customers_raw;

-- Drop schemas
DROP SCHEMA IF EXISTS training_lab.sandbox;
DROP SCHEMA IF EXISTS training_lab.gold;
DROP SCHEMA IF EXISTS training_lab.silver;
DROP SCHEMA IF EXISTS training_lab.bronze;

-- Drop catalog (optional - check with instructor)
-- DROP CATALOG IF EXISTS training_lab;
```

### Task 6.2: Verify Cleanup

```sql
-- Confirm schemas are removed
SHOW SCHEMAS IN training_lab;

-- Should show only 'default' or error if catalog was dropped
```

---

## Lab Validation Checklist

- [ ] Explored metastore configuration and documented properties
- [ ] Created catalog with proper naming and comments
- [ ] Created medallion architecture schemas (bronze, silver, gold)
- [ ] Created managed table with sample data
- [ ] Examined table properties (type, location, owner)
- [ ] Created CTAS table in silver layer
- [ ] Created aggregate table in gold layer
- [ ] Created a view with data masking
- [ ] Navigated Data Explorer and explored all tabs
- [ ] Viewed and documented data lineage
- [ ] Used search functionality
- [ ] Cleaned up test resources

---

## Challenge Exercises (Optional)

### Challenge 1: Add Table Constraints
```sql
-- Add NOT NULL constraint to a column
-- ALTER TABLE training_lab.bronze.customers_raw
-- ALTER COLUMN customer_id SET NOT NULL;
```

### Challenge 2: Table Properties
```sql
-- Add custom tags for data classification
-- ALTER TABLE training_lab.bronze.customers_raw
-- SET TBLPROPERTIES ('pii' = 'true', 'retention_days' = '365');
```

### Challenge 3: Dynamic View
Create a view that filters data based on the current user's group membership (advanced - requires row-level security setup).

---

## Lab Summary

In this lab, you learned:

1. **Metastore Exploration** - How to examine Unity Catalog configuration
2. **Catalog Creation** - Creating and organizing catalogs
3. **Schema Design** - Implementing medallion architecture (bronze/silver/gold)
4. **Managed Tables** - Creating tables with governance
5. **Views** - Creating abstraction layers with data masking
6. **Data Explorer** - Navigating the UI and viewing lineage
7. **External Tables** - Understanding the concept (for future labs)

---

## Key Takeaways

| Concept | Remember |
|---------|----------|
| Three-level namespace | catalog.schema.table |
| Managed tables | DROP deletes data |
| External tables | DROP keeps data |
| USAGE privilege | Required on catalog AND schema |
| Lineage | Automatic when using SQL |

---

*Lab Version: 2.0 | Databricks Platform Administration Training - Day 6*
