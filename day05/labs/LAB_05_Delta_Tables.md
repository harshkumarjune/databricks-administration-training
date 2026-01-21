# Lab 05: Inspect Delta Tables & Review Versions

## Databricks Platform Administration Training
### Duration: 60 Minutes | Difficulty: Intermediate

---

## Lab Overview

In this lab, you will explore Delta Lake tables, understand the transaction log, practice time travel queries, and learn administrative operations like VACUUM and OPTIMIZE.

### Learning Objectives

- Create and examine Delta table structure
- View transaction history
- Query historical versions with time travel
- Manage table versions with VACUUM
- Optimize tables for performance

---

## Part 1: Create Delta Tables (15 minutes)

### Task 1.1: Create Lab Notebook

1. Create notebook: `Lab05-Delta-Tables`
2. Attach to a cluster

### Task 1.2: Create a Delta Table

```python
# Create sample data
data = [
    (1, "Alice", "Engineering", 75000),
    (2, "Bob", "Marketing", 65000),
    (3, "Carol", "Engineering", 80000),
    (4, "David", "Sales", 70000),
    (5, "Eve", "Marketing", 72000)
]

df = spark.createDataFrame(data, ["id", "name", "department", "salary"])

# Save as Delta table
df.write.format("delta").mode("overwrite").saveAsTable("training_employees")
```

### Task 1.3: Examine Table Structure

```sql
-- View table details
DESCRIBE EXTENDED training_employees;
```

```python
# Find the table location
table_location = spark.sql("DESCRIBE EXTENDED training_employees").filter("col_name = 'Location'").collect()[0][1]
print(f"Table location: {table_location}")
```

```python
# List files in the Delta table directory
dbutils.fs.ls(table_location)
```

**Document:**
| File/Folder | Purpose |
|-------------|---------|
| _delta_log/ | |
| part-*.parquet | |

---

## Part 2: Transaction History (15 minutes)

### Task 2.1: Make Changes to Create History

```sql
-- Update: Give Engineering a raise
UPDATE training_employees SET salary = salary * 1.10 WHERE department = 'Engineering';
```

```sql
-- Insert new employee
INSERT INTO training_employees VALUES (6, 'Frank', 'Sales', 68000);
```

```sql
-- Delete an employee
DELETE FROM training_employees WHERE id = 4;
```

### Task 2.2: View Transaction History

```sql
DESCRIBE HISTORY training_employees;
```

**Document the history:**
| Version | Operation | Timestamp | User |
|---------|-----------|-----------|------|
| 0 | | | |
| 1 | | | |
| 2 | | | |
| 3 | | | |

### Task 2.3: Examine Log Files

```python
# List transaction log files
dbutils.fs.ls(f"{table_location}/_delta_log/")
```

---

## Part 3: Time Travel (15 minutes)

### Task 3.1: Query by Version

```sql
-- Current data
SELECT * FROM training_employees;

-- Original data (version 0)
SELECT * FROM training_employees VERSION AS OF 0;

-- After update (version 1)
SELECT * FROM training_employees VERSION AS OF 1;
```

**Compare results:**
| Version | Row Count | David Present? | Engineering Salaries |
|---------|-----------|----------------|---------------------|
| 0 | | | |
| 1 | | | |
| Current | | | |

### Task 3.2: Query by Timestamp

```sql
-- Find a timestamp from history
DESCRIBE HISTORY training_employees;

-- Query at that timestamp
SELECT * FROM training_employees TIMESTAMP AS OF '2024-01-20 10:00:00';
```

### Task 3.3: Restore Table

```sql
-- Restore to version 0 (original data)
RESTORE TABLE training_employees TO VERSION AS OF 0;

-- Verify restoration
SELECT * FROM training_employees;

-- Check history - restore creates new version
DESCRIBE HISTORY training_employees;
```

---

## Part 4: VACUUM and Retention (10 minutes)

### Task 4.1: Check Current Files

```python
# Count data files
files = dbutils.fs.ls(table_location)
data_files = [f for f in files if f.name.endswith('.parquet')]
print(f"Data files: {len(data_files)}")
```

### Task 4.2: Run VACUUM (Dry Run)

```sql
-- Dry run to see what would be deleted
VACUUM training_employees DRY RUN;
```

### Task 4.3: Understand Retention

```sql
-- View current retention setting
SHOW TBLPROPERTIES training_employees;
```

```sql
-- Set custom retention (example)
ALTER TABLE training_employees SET TBLPROPERTIES ('delta.deletedFileRetentionDuration' = '168 hours');
```

**Note:** VACUUM with retention < 7 days requires setting `spark.databricks.delta.retentionDurationCheck.enabled = false`

---

## Part 5: Optimization (5 minutes)

### Task 5.1: Run OPTIMIZE

```sql
-- Compact small files
OPTIMIZE training_employees;
```

### Task 5.2: View Optimization Results

```sql
DESCRIBE HISTORY training_employees;
```

Look for the OPTIMIZE operation in history.

---

## Lab Validation Checklist

- [ ] Created Delta table
- [ ] Examined table structure and files
- [ ] Made changes and viewed history
- [ ] Queried historical versions
- [ ] Practiced RESTORE
- [ ] Ran VACUUM dry run
- [ ] Executed OPTIMIZE

---

## Challenge Exercise

Create a table with data skew and demonstrate how Z-ORDER improves query performance:

```sql
-- Create table with date column
CREATE TABLE sales_data AS
SELECT
    id,
    date_add('2024-01-01', cast(rand() * 365 as int)) as sale_date,
    cast(rand() * 1000 as decimal(10,2)) as amount
FROM range(100000);

-- Optimize with Z-ORDER
OPTIMIZE sales_data ZORDER BY (sale_date);
```

---

## Lab Summary

You learned:
1. Delta table structure (data files + transaction log)
2. Transaction history with DESCRIBE HISTORY
3. Time travel with VERSION AS OF and TIMESTAMP AS OF
4. Table restoration with RESTORE
5. Storage management with VACUUM
6. Performance optimization with OPTIMIZE

---

*Lab Version: 2.0 | Databricks Platform Administration Training - Day 5*
