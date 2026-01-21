# Day 13 Final Assessment: Comprehensive Review

## Databricks Platform Administration Training
### Duration: 20 Minutes | 20 Questions | 70% to Pass

---

### Question 1
What is the top-level container in the Unity Catalog hierarchy?

- [ ] A) Catalog
- [ ] B) Schema
- [ ] C) Metastore
- [ ] D) Table

---

### Question 2
Which privilege is required to access any child objects within a catalog or schema?

- [ ] A) SELECT
- [ ] B) USAGE
- [ ] C) READ
- [ ] D) ACCESS

---

### Question 3
What does SCIM stand for?

- [ ] A) Secure Cloud Identity Manager
- [ ] B) System for Cross-domain Identity Management
- [ ] C) Single Cloud Identity Module
- [ ] D) Standard Credential Interface Method

---

### Question 4
Which cluster access mode is required for Unity Catalog support?

- [ ] A) No Isolation Shared
- [ ] B) High Concurrency
- [ ] C) Single User or Shared
- [ ] D) Custom only

---

### Question 5
What happens when you DROP a managed table in Unity Catalog?

- [ ] A) Only metadata is removed
- [ ] B) Both metadata and data are deleted
- [ ] C) Data is moved to a recycle bin
- [ ] D) Nothing, managed tables cannot be dropped

---

### Question 6
What is the default retention period for Delta Lake time travel?

- [ ] A) 1 day
- [ ] B) 7 days
- [ ] C) 30 days
- [ ] D) Forever

---

### Question 7
Which SQL command shows the transaction history of a Delta table?

- [ ] A) SHOW HISTORY table_name
- [ ] B) DESCRIBE HISTORY table_name
- [ ] C) SELECT * FROM table_history
- [ ] D) VIEW TRANSACTIONS table_name

---

### Question 8
What is the recommended identity type for CI/CD pipelines?

- [ ] A) Regular user account
- [ ] B) Admin user account
- [ ] C) Service principal
- [ ] D) Guest account

---

### Question 9
What is the primary benefit of cluster pools?

- [ ] A) Unlimited compute capacity
- [ ] B) Reduced cluster startup time
- [ ] C) Free compute resources
- [ ] D) Better query performance

---

### Question 10
Which job trigger type starts a job when new files arrive in cloud storage?

- [ ] A) Scheduled
- [ ] B) Manual
- [ ] C) File Arrival
- [ ] D) Continuous

---

### Question 11
What are Databricks Asset Bundles (DABs)?

- [ ] A) Compressed notebook files
- [ ] B) Infrastructure as Code for Databricks resources
- [ ] C) Python packages
- [ ] D) Data storage containers

---

### Question 12
Where are Databricks system tables located?

- [ ] A) In the default catalog
- [ ] B) In the system catalog
- [ ] C) In the hive_metastore catalog
- [ ] D) In each workspace catalog

---

### Question 13
What is data skew in Spark?

- [ ] A) Data corruption in parquet files
- [ ] B) Uneven distribution of data across partitions
- [ ] C) Missing data in columns
- [ ] D) Duplicate records in tables

---

### Question 14
What does Private Link provide in Databricks?

- [ ] A) Faster query performance
- [ ] B) Private connectivity without using public internet
- [ ] C) Lower storage costs
- [ ] D) Automatic data encryption

---

### Question 15
What is the primary unit for measuring Databricks compute costs?

- [ ] A) CPU hours
- [ ] B) DBU (Databricks Unit)
- [ ] C) Memory GB
- [ ] D) Storage TB

---

### Question 16
Which feature allows you to enforce tagging requirements on clusters?

- [ ] A) Unity Catalog
- [ ] B) Cluster Policies
- [ ] C) SQL Warehouses
- [ ] D) Delta Lake

---

### Question 17
What component coordinates Spark job execution?

- [ ] A) Worker node
- [ ] B) Executor
- [ ] C) Driver node
- [ ] D) Task

---

### Question 18
What SQL syntax grants permissions in Unity Catalog?

- [ ] A) PERMIT SELECT TO user
- [ ] B) GRANT SELECT ON table TO user
- [ ] C) ALLOW user ACCESS table
- [ ] D) SET PERMISSION SELECT FOR user

---

### Question 19
Which system table contains billing usage data?

- [ ] A) system.access.audit
- [ ] B) system.billing.usage
- [ ] C) system.compute.clusters
- [ ] D) system.workflow.jobs

---

### Question 20
What is the three-level namespace in Unity Catalog?

- [ ] A) Database → Schema → Table
- [ ] B) Metastore → Database → Table
- [ ] C) Catalog → Schema → Table
- [ ] D) Workspace → Catalog → Table

---

## Answer Key

| Q | Answer | Topic | Explanation |
|---|--------|-------|-------------|
| 1 | C | Unity Catalog | Metastore is the top-level container |
| 2 | B | Unity Catalog | USAGE is required on containers to access children |
| 3 | B | Identity | System for Cross-domain Identity Management |
| 4 | C | Compute | Unity Catalog requires Single User or Shared modes |
| 5 | B | Unity Catalog | Dropping managed table deletes both metadata and data |
| 6 | B | Delta Lake | Default retention is 7 days (168 hours) |
| 7 | B | Delta Lake | DESCRIBE HISTORY shows transaction history |
| 8 | C | Identity | Service principals are for automation |
| 9 | B | Compute | Pools reduce cluster startup time |
| 10 | C | Jobs | File Arrival trigger monitors storage |
| 11 | B | CI/CD | DABs are IaC for Databricks |
| 12 | B | Monitoring | System tables are in system catalog |
| 13 | B | Spark | Skew is uneven partition distribution |
| 14 | B | Network | Private Link avoids public internet |
| 15 | B | Cost | DBU is the billing unit |
| 16 | B | Governance | Cluster Policies enforce configurations |
| 17 | C | Spark | Driver coordinates execution |
| 18 | B | Unity Catalog | Standard SQL GRANT syntax |
| 19 | B | Monitoring | system.billing.usage has cost data |
| 20 | C | Unity Catalog | Catalog → Schema → Table |

---

## Scoring Guide

| Score | Result |
|-------|--------|
| 18-20 | Excellent - Ready for certification |
| 14-17 | Good - Review weak areas |
| 10-13 | Fair - Additional study recommended |
| < 10 | Needs Improvement - Review course materials |

---

*Final Assessment Version: 2.0 | Databricks Platform Administration Training - Day 13*
