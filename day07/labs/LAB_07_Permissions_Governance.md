# Lab 07: Permissions & Governance

## Databricks Platform Administration Training
### Duration: 60 Minutes | Difficulty: Intermediate

---

## Lab Overview

Configure Unity Catalog permissions, implement security patterns, explore data lineage, and understand audit logging for governance compliance.

### Learning Objectives

- Grant and revoke permissions using SQL
- Understand permission inheritance and USAGE requirements
- Create secure views with column and row filtering
- Explore data lineage visualization
- Query audit logs for compliance reporting

---

## Part 1: Setup Test Environment (10 minutes)

### Task 1.1: Create Lab Catalog and Schemas

```sql
-- Create catalog for lab exercises
CREATE CATALOG IF NOT EXISTS security_lab
COMMENT 'Security and governance lab exercises';

-- Create schemas
CREATE SCHEMA IF NOT EXISTS security_lab.raw_data
COMMENT 'Raw data with restricted access';

CREATE SCHEMA IF NOT EXISTS security_lab.reporting
COMMENT 'Reporting data for analysts';

-- Verify structure
SHOW SCHEMAS IN security_lab;
```

### Task 1.2: Create Sample Tables

```sql
-- Create employees table with sensitive data
CREATE TABLE security_lab.raw_data.employees (
    emp_id INT,
    name STRING,
    email STRING,
    ssn STRING,
    salary DECIMAL(10,2),
    department STRING,
    hire_date DATE
);

INSERT INTO security_lab.raw_data.employees VALUES
    (1, 'Alice Johnson', 'alice@company.com', '123-45-6789', 95000.00, 'Engineering', '2022-01-15'),
    (2, 'Bob Smith', 'bob@company.com', '234-56-7890', 85000.00, 'Marketing', '2022-03-20'),
    (3, 'Carol Williams', 'carol@company.com', '345-67-8901', 105000.00, 'Engineering', '2021-06-10'),
    (4, 'David Brown', 'david@company.com', '456-78-9012', 75000.00, 'Sales', '2023-02-01'),
    (5, 'Eve Davis', 'eve@company.com', '567-89-0123', 92000.00, 'Marketing', '2022-09-15');

-- Create sales table
CREATE TABLE security_lab.raw_data.sales (
    sale_id INT,
    sale_date DATE,
    amount DECIMAL(10,2),
    region STRING,
    sales_rep_id INT
);

INSERT INTO security_lab.raw_data.sales VALUES
    (1, '2024-01-15', 5000.00, 'North', 4),
    (2, '2024-01-16', 7500.00, 'South', 4),
    (3, '2024-01-17', 3200.00, 'East', 4),
    (4, '2024-01-18', 8900.00, 'West', 4),
    (5, '2024-01-19', 4100.00, 'North', 4);
```

---

## Part 2: Grant and Revoke Permissions (15 minutes)

### Task 2.1: Understand Current Permissions

```sql
-- Check current grants on the catalog
SHOW GRANTS ON CATALOG security_lab;

-- Check grants on schema
SHOW GRANTS ON SCHEMA security_lab.raw_data;

-- Check grants on table
SHOW GRANTS ON TABLE security_lab.raw_data.employees;
```

**Document current state:**
| Object | Grantee | Privileges |
|--------|---------|------------|
| security_lab (catalog) | | |
| raw_data (schema) | | |
| employees (table) | | |

### Task 2.2: Grant Read Access to Analysts

```sql
-- Grant catalog-level USAGE (required to see anything in catalog)
GRANT USAGE ON CATALOG security_lab TO `analysts`;

-- Grant schema-level USAGE and SELECT
GRANT USAGE ON SCHEMA security_lab.reporting TO `analysts`;
GRANT SELECT ON SCHEMA security_lab.reporting TO `analysts`;

-- Verify grants
SHOW GRANTS TO `analysts`;
```

### Task 2.3: Grant Full Access to Data Engineers

```sql
-- Grant comprehensive access to engineers
GRANT USAGE ON CATALOG security_lab TO `data_engineers`;
GRANT ALL PRIVILEGES ON SCHEMA security_lab.raw_data TO `data_engineers`;
GRANT ALL PRIVILEGES ON SCHEMA security_lab.reporting TO `data_engineers`;

-- Verify
SHOW GRANTS TO `data_engineers`;
```

### Task 2.4: Test the USAGE Requirement

```sql
-- Without USAGE on catalog, this would fail even with SELECT on table
-- Demonstrate by granting only SELECT (simulate for understanding)

-- This pattern shows why USAGE is critical:
-- User needs: USAGE on catalog + USAGE on schema + SELECT on table

-- Grant minimal access for specific table
GRANT USAGE ON CATALOG security_lab TO `temp_user`;
GRANT USAGE ON SCHEMA security_lab.raw_data TO `temp_user`;
GRANT SELECT ON TABLE security_lab.raw_data.sales TO `temp_user`;
-- temp_user can now SELECT from sales, but NOT from employees
```

### Task 2.5: Revoke Permissions

```sql
-- Revoke access from temp user
REVOKE SELECT ON TABLE security_lab.raw_data.sales FROM `temp_user`;
REVOKE USAGE ON SCHEMA security_lab.raw_data FROM `temp_user`;
REVOKE USAGE ON CATALOG security_lab FROM `temp_user`;

-- Verify revocation
SHOW GRANTS TO `temp_user`;
```

---

## Part 3: Secure Views (15 minutes)

### Task 3.1: Create Column-Masked View

```sql
-- Create view that masks sensitive columns
CREATE OR REPLACE VIEW security_lab.reporting.employees_safe AS
SELECT
    emp_id,
    name,
    -- Mask email domain
    CONCAT(SUBSTRING(email, 1, 3), '***@company.com') AS email_masked,
    -- Completely hide SSN
    '***-**-****' AS ssn_masked,
    -- Hide exact salary, show range
    CASE
        WHEN salary < 80000 THEN 'Under 80K'
        WHEN salary < 100000 THEN '80K-100K'
        ELSE 'Over 100K'
    END AS salary_range,
    department,
    hire_date
FROM security_lab.raw_data.employees;

-- Query the safe view
SELECT * FROM security_lab.reporting.employees_safe;
```

### Task 3.2: Create Dynamic Column Mask

```sql
-- Create view with conditional masking based on group membership
CREATE OR REPLACE VIEW security_lab.reporting.employees_dynamic AS
SELECT
    emp_id,
    name,
    email,
    -- Only show SSN to HR group
    CASE
        WHEN is_member_of('hr_team') THEN ssn
        ELSE '***-**-****'
    END AS ssn,
    -- Only show exact salary to managers
    CASE
        WHEN is_member_of('managers') OR is_member_of('hr_team') THEN salary
        ELSE NULL
    END AS salary,
    department,
    hire_date
FROM security_lab.raw_data.employees;

-- Test the view
SELECT * FROM security_lab.reporting.employees_dynamic;
```

### Task 3.3: Create Row-Filtered View

```sql
-- Create view that filters rows based on user's department access
CREATE OR REPLACE VIEW security_lab.reporting.sales_by_permission AS
SELECT
    s.sale_id,
    s.sale_date,
    s.amount,
    s.region
FROM security_lab.raw_data.sales s
WHERE
    -- Show all data to admins
    is_member_of('admins')
    OR
    -- Show only specific regions based on group
    (is_member_of('north_team') AND s.region = 'North')
    OR
    (is_member_of('south_team') AND s.region = 'South')
    OR
    (is_member_of('all_regions') AND TRUE);

-- Test the view
SELECT * FROM security_lab.reporting.sales_by_permission;
```

### Task 3.4: Grant Access to Secure Views

```sql
-- Grant analysts access to the safe views only
GRANT SELECT ON VIEW security_lab.reporting.employees_safe TO `analysts`;
GRANT SELECT ON VIEW security_lab.reporting.employees_dynamic TO `analysts`;
GRANT SELECT ON VIEW security_lab.reporting.sales_by_permission TO `analysts`;

-- Analysts cannot access raw tables, only these views
-- Verify what analysts can see
SHOW GRANTS TO `analysts`;
```

---

## Part 4: Data Lineage (10 minutes)

### Task 4.1: Create Derived Tables for Lineage

```sql
-- Create aggregated table from raw data
CREATE TABLE security_lab.reporting.department_summary AS
SELECT
    department,
    COUNT(*) as employee_count,
    AVG(salary) as avg_salary,
    MIN(hire_date) as earliest_hire,
    MAX(hire_date) as latest_hire
FROM security_lab.raw_data.employees
GROUP BY department;

-- Create another derived table
CREATE TABLE security_lab.reporting.sales_summary AS
SELECT
    region,
    COUNT(*) as num_sales,
    SUM(amount) as total_amount,
    AVG(amount) as avg_amount
FROM security_lab.raw_data.sales
GROUP BY region;

-- Create a join table showing lineage from multiple sources
CREATE TABLE security_lab.reporting.sales_with_department AS
SELECT
    s.sale_id,
    s.sale_date,
    s.amount,
    s.region,
    e.name as sales_rep_name,
    e.department
FROM security_lab.raw_data.sales s
JOIN security_lab.raw_data.employees e ON s.sales_rep_id = e.emp_id;
```

### Task 4.2: View Lineage in Data Explorer

1. Navigate to **Catalog** in the left sidebar
2. Expand `security_lab` → `reporting`
3. Click on `sales_with_department`
4. Click the **Lineage** tab
5. Observe the upstream tables: `sales` and `employees`

**Document observed lineage:**
| Target Table | Upstream Sources |
|--------------|------------------|
| department_summary | |
| sales_summary | |
| sales_with_department | |

### Task 4.3: Query Lineage Programmatically

```sql
-- Query table lineage from system tables
SELECT
    source_table_full_name,
    target_table_full_name,
    event_time
FROM system.access.table_lineage
WHERE target_table_full_name LIKE 'security_lab.reporting.%'
ORDER BY event_time DESC
LIMIT 20;
```

---

## Part 5: Audit Logging (10 minutes)

### Task 5.1: Query Recent Access Events

```sql
-- Query audit logs for recent activity on our lab catalog
SELECT
    event_time,
    action_name,
    user_identity.email as user_email,
    request_params.full_name_arg as object_name,
    response.status_code
FROM system.access.audit
WHERE
    event_date >= current_date() - 1
    AND request_params.full_name_arg LIKE 'security_lab%'
ORDER BY event_time DESC
LIMIT 50;
```

### Task 5.2: Track Permission Changes

```sql
-- Find all permission-related events
SELECT
    event_time,
    action_name,
    user_identity.email as admin_user,
    request_params
FROM system.access.audit
WHERE
    event_date >= current_date() - 7
    AND action_name IN ('updatePermissions', 'getPermissions')
ORDER BY event_time DESC
LIMIT 20;
```

### Task 5.3: Monitor Table Access

```sql
-- Track who accessed specific tables
SELECT
    event_time,
    user_identity.email as user_email,
    action_name,
    request_params.full_name_arg as table_name,
    source_ip_address
FROM system.access.audit
WHERE
    event_date >= current_date() - 1
    AND action_name IN ('getTable', 'generateTemporaryTableCredential')
    AND request_params.full_name_arg LIKE 'security_lab%'
ORDER BY event_time DESC;
```

### Task 5.4: Create Audit Summary Report

```sql
-- Create a summary of access patterns
SELECT
    user_identity.email as user_email,
    action_name,
    COUNT(*) as event_count,
    MIN(event_time) as first_access,
    MAX(event_time) as last_access
FROM system.access.audit
WHERE
    event_date >= current_date() - 7
    AND request_params.full_name_arg LIKE 'security_lab%'
GROUP BY user_identity.email, action_name
ORDER BY event_count DESC;
```

---

## Part 6: Cleanup

### Task 6.1: Clean Up Lab Resources

```sql
-- Drop views
DROP VIEW IF EXISTS security_lab.reporting.employees_safe;
DROP VIEW IF EXISTS security_lab.reporting.employees_dynamic;
DROP VIEW IF EXISTS security_lab.reporting.sales_by_permission;

-- Drop derived tables
DROP TABLE IF EXISTS security_lab.reporting.department_summary;
DROP TABLE IF EXISTS security_lab.reporting.sales_summary;
DROP TABLE IF EXISTS security_lab.reporting.sales_with_department;

-- Drop source tables
DROP TABLE IF EXISTS security_lab.raw_data.employees;
DROP TABLE IF EXISTS security_lab.raw_data.sales;

-- Drop schemas
DROP SCHEMA IF EXISTS security_lab.reporting;
DROP SCHEMA IF EXISTS security_lab.raw_data;

-- Drop catalog (if permitted)
-- DROP CATALOG IF EXISTS security_lab;
```

---

## Lab Validation Checklist

- [ ] Created catalog and schemas with proper structure
- [ ] Granted permissions using GRANT statements
- [ ] Understood USAGE requirement for parent containers
- [ ] Revoked permissions using REVOKE statements
- [ ] Created column-masked secure view
- [ ] Created row-filtered secure view
- [ ] Created derived tables showing lineage
- [ ] Viewed lineage in Data Explorer
- [ ] Queried audit logs for access events
- [ ] Cleaned up lab resources

---

## Challenge Exercise

Create a comprehensive access control solution:

1. Design a three-tier access model:
   - **Bronze**: Raw data access (data engineers only)
   - **Silver**: Cleansed data (analysts with some masking)
   - **Gold**: Aggregated reporting (all business users)

2. Implement views for each tier with appropriate security

3. Create an audit dashboard showing:
   - Most accessed tables
   - Users with most data access
   - Failed access attempts

---

## Lab Summary

You learned:
1. GRANT and REVOKE SQL syntax for permissions
2. Importance of USAGE privilege on containers
3. Creating secure views with column masking
4. Implementing row-level security with dynamic filters
5. Exploring data lineage in Data Explorer
6. Querying audit logs for compliance

---

*Lab Version: 2.0 | Databricks Platform Administration Training - Day 7*
