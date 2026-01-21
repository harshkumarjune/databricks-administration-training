# Day 5 Pre-Reading Materials

## Databricks Platform Administration Training
### Delta Lake Fundamentals

---

## Overview

Day 5 covers Delta Lake, the storage layer that enables ACID transactions, time travel, and data versioning on data lakes. Understanding Delta Lake is essential for administrators managing data governance and troubleshooting.

**Estimated Reading Time**: 25-30 minutes

---

## Required Reading

### 1. Delta Lake Overview

**Source**: Databricks Documentation

**Key Concepts to Understand**:
- What makes Delta Lake different from plain Parquet?
- ACID transaction guarantees
- Schema enforcement and evolution

**Read**: [What is Delta Lake?](https://docs.databricks.com/en/delta/index.html)

**Focus Areas**:
- Transaction log (_delta_log)
- Optimistic concurrency control
- Unified batch and streaming

### 2. Time Travel

**Source**: Databricks Documentation

**Key Concepts to Understand**:
- Querying historical data versions
- Restoring tables to previous states
- Audit and compliance use cases

**Read**: [Work with Delta Lake table history](https://docs.databricks.com/en/delta/history.html)

**Focus Areas**:
- DESCRIBE HISTORY command
- VERSION AS OF and TIMESTAMP AS OF
- Retention settings

### 3. Table Maintenance

**Source**: Databricks Documentation

**Key Concepts to Understand**:
- Why maintenance operations matter
- OPTIMIZE and VACUUM commands
- Performance implications

**Read**: [Delta Lake table optimization](https://docs.databricks.com/en/delta/optimize.html)

**Focus Areas**:
- File compaction with OPTIMIZE
- Removing old files with VACUUM
- Z-ordering for query performance

---

## Key Terminology

| Term | Definition |
|------|------------|
| **Delta Lake** | Open-source storage layer with ACID transactions |
| **Transaction Log** | JSON files tracking all changes to a table |
| **ACID** | Atomicity, Consistency, Isolation, Durability |
| **Time Travel** | Ability to query historical versions of data |
| **OPTIMIZE** | Compacts small files into larger ones |
| **VACUUM** | Removes files no longer referenced by transaction log |
| **Z-Ordering** | Data layout optimization for query performance |
| **Schema Evolution** | Ability to add/modify columns over time |

---

## Key Commands Reference

```sql
-- View table history
DESCRIBE HISTORY table_name;

-- Query specific version
SELECT * FROM table_name VERSION AS OF 5;

-- Query by timestamp
SELECT * FROM table_name TIMESTAMP AS OF '2024-01-01';

-- Optimize table
OPTIMIZE table_name;

-- Vacuum old files (keep 7 days)
VACUUM table_name RETAIN 168 HOURS;

-- Restore to previous version
RESTORE TABLE table_name TO VERSION AS OF 5;
```

---

## Self-Assessment Questions

1. What's stored in the _delta_log directory?
2. What happens to old data files when you run VACUUM?
3. Why might time travel queries fail after running VACUUM?
4. What's the difference between OPTIMIZE and VACUUM?

---

## Recommended Additional Reading

- [Delta Lake quickstart](https://docs.databricks.com/en/delta/quick-start.html)
- [Configure data retention for time travel](https://docs.databricks.com/en/delta/history.html#configure-data-retention-for-time-travel)
- [Liquid clustering](https://docs.databricks.com/en/delta/clustering.html)

---

## Warning for Administrators

**VACUUM removes data permanently!**

Before running VACUUM, ensure:
- Retention period is appropriate for your use case
- No long-running queries depend on older versions
- Compliance requirements are considered

Default retention: 7 days (168 hours)
Minimum safe retention: Match your longest expected query or job runtime

---

*Pre-reading materials for Databricks Platform Administration Training - Day 5*
