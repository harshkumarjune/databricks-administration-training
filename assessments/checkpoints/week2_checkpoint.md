# Week 2 Checkpoint Assessment
## Databricks Platform Administration Training
### Data Governance & Identity (Days 6-10)

**Duration:** 20 Minutes | 15 Questions | 70% to Pass (11/15)

---

## Instructions

This checkpoint assessment covers material from Week 2 (Days 6-10):
- Day 6: Apache Spark for Administrators
- Day 7: Delta Lake Fundamentals
- Day 8: Unity Catalog Architecture
- Day 9: Unity Catalog Permissions & Governance
- Day 10: IAM & Identity Federation

Complete all questions before checking the answer key.

---

### Question 1
In a Spark cluster, which component is responsible for coordinating job execution?

- [ ] A) Executor
- [ ] B) Worker node
- [ ] C) Driver
- [ ] D) Cluster manager

---

### Question 2
What are the main components in Spark's execution hierarchy (from highest to lowest level)?

- [ ] A) Tasks → Stages → Jobs
- [ ] B) Jobs → Stages → Tasks
- [ ] C) Stages → Jobs → Tasks
- [ ] D) Jobs → Tasks → Stages

---

### Question 3
What does Delta Lake add to standard Parquet files?

- [ ] A) Compression algorithms
- [ ] B) Transaction log for ACID compliance
- [ ] C) Faster read speeds only
- [ ] D) Cloud storage optimization

---

### Question 4
Which SQL command shows the history of changes to a Delta table?

- [ ] A) SHOW HISTORY table_name
- [ ] B) DESCRIBE HISTORY table_name
- [ ] C) SELECT * FROM table_name.history
- [ ] D) LIST VERSIONS table_name

---

### Question 5
What is the default retention period for Delta Lake time travel?

- [ ] A) 24 hours
- [ ] B) 7 days
- [ ] C) 30 days
- [ ] D) 90 days

---

### Question 6
In Unity Catalog, what is the correct three-level namespace hierarchy?

- [ ] A) Database.Schema.Table
- [ ] B) Catalog.Schema.Table
- [ ] C) Metastore.Catalog.Table
- [ ] D) Schema.Catalog.Table

---

### Question 7
What happens when you DROP a managed table in Unity Catalog?

- [ ] A) Only metadata is removed; data remains
- [ ] B) Both metadata and underlying data are deleted
- [ ] C) Data is moved to a recycle bin
- [ ] D) The table becomes read-only

---

### Question 8
Which privilege must be granted for a user to access objects within a catalog?

- [ ] A) SELECT
- [ ] B) READ
- [ ] C) USAGE
- [ ] D) ACCESS

---

### Question 9
What is the purpose of a storage credential in Unity Catalog?

- [ ] A) To authenticate users logging into Databricks
- [ ] B) To provide access to underlying cloud storage
- [ ] C) To encrypt data at rest
- [ ] D) To configure network security

---

### Question 10
Which statement correctly grants SELECT access on a table?

- [ ] A) `GRANT SELECT ON TABLE catalog.schema.table FOR user_name`
- [ ] B) `GRANT SELECT ON TABLE catalog.schema.table TO user_name`
- [ ] C) `ALLOW SELECT ON catalog.schema.table TO user_name`
- [ ] D) `PERMIT SELECT TABLE catalog.schema.table user_name`

---

### Question 11
What is a service principal in the context of Databricks?

- [ ] A) A human user with admin privileges
- [ ] B) A machine identity for automated processes
- [ ] C) A group of users
- [ ] D) A type of cluster configuration

---

### Question 12
For GDPR compliance, which Unity Catalog feature helps implement data minimization?

- [ ] A) Time travel
- [ ] B) Column masking
- [ ] C) Cluster policies
- [ ] D) Job scheduling

---

### Question 13
What is the difference between managed and external tables in Unity Catalog?

- [ ] A) Managed tables are faster
- [ ] B) External tables can only be read
- [ ] C) Managed table data is deleted on DROP; external table data is retained
- [ ] D) External tables don't support transactions

---

### Question 14
Which cloud IAM integration allows Databricks to assume a role for accessing cloud resources?

- [ ] A) Service principal
- [ ] B) Instance profile (AWS) / Managed identity (Azure)
- [ ] C) Personal access token
- [ ] D) SAML federation

---

### Question 15
What does lineage tracking in Unity Catalog automatically capture?

- [ ] A) User login history
- [ ] B) Data dependencies and transformations between tables
- [ ] C) Cluster resource usage
- [ ] D) Cost allocation

---

## Answer Key

| Q | Answer | Explanation |
|---|--------|-------------|
| 1 | C | The driver coordinates execution, distributing work to executors |
| 2 | B | Jobs → Stages → Tasks is the correct hierarchy (high to low) |
| 3 | B | Delta Lake adds a transaction log enabling ACID transactions |
| 4 | B | DESCRIBE HISTORY shows the change history of a Delta table |
| 5 | B | Default retention is 7 days; configurable with delta.logRetentionDuration |
| 6 | B | Catalog.Schema.Table is the Unity Catalog three-level namespace |
| 7 | B | Managed tables delete both metadata AND underlying data on DROP |
| 8 | C | USAGE is required to access objects within a catalog or schema |
| 9 | B | Storage credentials provide access to cloud storage locations |
| 10 | B | GRANT privilege ON object TO principal is the correct syntax |
| 11 | B | Service principals are machine identities for automation |
| 12 | B | Column masking hides sensitive data to implement data minimization |
| 13 | C | Key difference: managed table DROP deletes data; external DROP only removes metadata |
| 14 | B | Instance profiles (AWS) and managed identities (Azure) enable cloud resource access |
| 15 | B | Lineage automatically tracks data dependencies and transformations |

---

## Score Interpretation

| Score | Interpretation | Recommendation |
|-------|----------------|----------------|
| 13-15 (87-100%) | Excellent | Ready for Week 3 material |
| 11-12 (70-80%) | Good | Review weak areas before continuing |
| 8-10 (53-67%) | Needs Improvement | Review Days 6-10 materials |
| <8 (<53%) | Requires Remediation | Revisit Week 2 content before continuing |

---

## Topics to Review if Struggling

### If Questions 1-2 Were Difficult:
Review Day 6 - Spark Architecture:
- Driver vs Executor roles
- Job execution hierarchy

### If Questions 3-5 Were Difficult:
Review Day 7 - Delta Lake:
- Transaction log purpose
- Time travel commands
- VACUUM operation

### If Questions 6-9 Were Difficult:
Review Day 8 - Unity Catalog Architecture:
- Three-level namespace
- Managed vs External tables
- Storage credentials and external locations

### If Questions 10-12 Were Difficult:
Review Day 9 - Unity Catalog Permissions:
- GRANT syntax
- USAGE privilege
- Permission inheritance

### If Questions 13-15 Were Difficult:
Review Day 10 - IAM & Identity:
- Service principals
- Cloud IAM integration
- Lineage tracking

---

*Checkpoint Version: 3.0 | Databricks Platform Administration Training - Week 2*
