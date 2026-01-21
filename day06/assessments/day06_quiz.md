# Day 6 Quiz: Unity Catalog Architecture & Setup

## Databricks Platform Administration Training
### Duration: 10 Minutes | 10 Questions | 70% to Pass

---

### Question 1
What is the top-level container in Unity Catalog?

- [ ] A) Catalog
- [ ] B) Schema
- [ ] C) Metastore
- [ ] D) Table

---

### Question 2
What is the correct three-level namespace hierarchy in Unity Catalog?

- [ ] A) Database → Schema → Table
- [ ] B) Metastore → Database → Table
- [ ] C) Catalog → Schema → Table
- [ ] D) Workspace → Catalog → Table

---

### Question 3
What happens when you DROP a managed table in Unity Catalog?

- [ ] A) Only metadata is removed
- [ ] B) Both metadata and data are deleted
- [ ] C) Data is moved to a recycle bin
- [ ] D) Nothing, managed tables cannot be dropped

---

### Question 4
What is a Storage Credential in Unity Catalog?

- [ ] A) A username and password
- [ ] B) A reference to cloud IAM credentials
- [ ] C) A personal access token
- [ ] D) An encryption key

---

### Question 5
How many metastores can be assigned to a single workspace?

- [ ] A) Unlimited
- [ ] B) One per workspace
- [ ] C) One per catalog
- [ ] D) None, metastores are optional

---

### Question 6
What is the purpose of an External Location?

- [ ] A) To store user credentials
- [ ] B) To define a path in cloud storage for external tables
- [ ] C) To cache query results
- [ ] D) To log audit events

---

### Question 7
Which SQL syntax is used to grant permissions in Unity Catalog?

- [ ] A) PERMIT SELECT TO user
- [ ] B) GRANT SELECT ON table TO user
- [ ] C) ALLOW user ACCESS table
- [ ] D) SET PERMISSION SELECT FOR user

---

### Question 8
What does Unity Catalog automatically track?

- [ ] A) Only table creation
- [ ] B) Data lineage across transformations
- [ ] C) User login times only
- [ ] D) File sizes only

---

### Question 9
Where is Unity Catalog metadata stored?

- [ ] A) In the customer's cloud storage only
- [ ] B) In the Databricks Control Plane
- [ ] C) In each workspace locally
- [ ] D) In Apache Hive Metastore

---

### Question 10
What is the primary benefit of Unity Catalog's centralized governance?

- [ ] A) Faster query performance
- [ ] B) Unified access control across all workspaces
- [ ] C) Reduced storage costs
- [ ] D) Automatic data backup

---

## Answer Key

| Q | Answer | Explanation |
|---|--------|-------------|
| 1 | C | Metastore is the top-level container for all Unity Catalog objects |
| 2 | C | Catalog → Schema → Table (within a metastore) |
| 3 | B | Dropping a managed table deletes both metadata and data |
| 4 | B | Storage Credential references cloud IAM for accessing storage |
| 5 | B | One metastore per workspace (in the same region) |
| 6 | B | External Location defines a path in cloud storage for external data |
| 7 | B | Standard SQL GRANT syntax is used |
| 8 | B | Unity Catalog automatically tracks data lineage |
| 9 | B | Metadata is stored in the Databricks Control Plane |
| 10 | B | Centralized governance enables unified access control across workspaces |

---

*Quiz Version: 2.0 | Databricks Platform Administration Training - Day 6*
