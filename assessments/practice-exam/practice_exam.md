# Practice Certification Exam: Databricks Platform Administrator

## Databricks Platform Administration Training
### Duration: 90 Minutes | 45 Questions | 70% to Pass (32/45)

---

## Instructions

This practice exam simulates the Databricks Certified Associate Platform Administrator certification exam. Complete all questions within 90 minutes. Select the single best answer for each question.

---

## Section 1: Databricks Lakehouse Platform (8 Questions)

### Question 1
What is the top-level container in the Unity Catalog hierarchy?

- [ ] A) Catalog
- [ ] B) Schema
- [ ] C) Metastore
- [ ] D) Table

---

### Question 2
Which component of the Databricks architecture runs in the customer's cloud subscription?

- [ ] A) Control Plane
- [ ] B) Web Application
- [ ] C) Data Plane
- [ ] D) Unity Catalog Service

---

### Question 3
What storage format does Delta Lake use under the hood?

- [ ] A) ORC
- [ ] B) Avro
- [ ] C) Parquet
- [ ] D) JSON

---

### Question 4
What is the default retention period for Delta Lake time travel?

- [ ] A) 1 day
- [ ] B) 7 days
- [ ] C) 30 days
- [ ] D) Forever

---

### Question 5
Which SQL command shows the transaction history of a Delta table?

- [ ] A) SHOW HISTORY table_name
- [ ] B) DESCRIBE HISTORY table_name
- [ ] C) SELECT * FROM table_history
- [ ] D) VIEW TRANSACTIONS table_name

---

### Question 6
What happens when you DROP a managed table in Unity Catalog?

- [ ] A) Only metadata is removed
- [ ] B) Both metadata and data are deleted
- [ ] C) Data is moved to a recycle bin
- [ ] D) Nothing, managed tables cannot be dropped

---

### Question 7
What is the purpose of the Delta Lake transaction log?

- [ ] A) Store query results
- [ ] B) Record all changes for ACID compliance
- [ ] C) Cache frequently accessed data
- [ ] D) Compress data files

---

### Question 8
Which Databricks runtime version nomenclature indicates Long Term Support?

- [ ] A) DBR 14.0-beta
- [ ] B) DBR 13.3 LTS
- [ ] C) DBR 14.x-preview
- [ ] D) DBR-stable

---

## Section 2: Workspace Administration (7 Questions)

### Question 9
At which level are Unity Catalog metastores managed?

- [ ] A) Workspace level
- [ ] B) Account level
- [ ] C) Cluster level
- [ ] D) Job level

---

### Question 10
What is required to assign a metastore to a workspace?

- [ ] A) Workspace admin privileges
- [ ] B) Account admin privileges
- [ ] C) Metastore admin privileges
- [ ] D) Both B and C

---

### Question 11
Which setting controls whether users can download query results in a workspace?

- [ ] A) Cluster policies
- [ ] B) Workspace settings
- [ ] C) Unity Catalog permissions
- [ ] D) SQL warehouse configuration

---

### Question 12
What is the relationship between Account Console and Workspace Admin Console?

- [ ] A) They are the same interface
- [ ] B) Account Console manages resources across workspaces
- [ ] C) Workspace Admin Console manages multiple accounts
- [ ] D) They cannot be used together

---

### Question 13
Which workspace feature enables serverless compute?

- [ ] A) Unity Catalog
- [ ] B) SQL Warehouses (Serverless)
- [ ] C) Job Clusters
- [ ] D) Cluster Pools

---

### Question 14
What is the purpose of workspace folders?

- [ ] A) Store cluster configurations
- [ ] B) Organize notebooks, queries, and files
- [ ] C) Define user permissions
- [ ] D) Configure network settings

---

### Question 15
Which users can create new workspaces?

- [ ] A) Any workspace user
- [ ] B) Workspace admins only
- [ ] C) Account admins only
- [ ] D) Unity Catalog admins only

---

## Section 3: Identity and Access Management (8 Questions)

### Question 16
What does SCIM stand for?

- [ ] A) Secure Cloud Identity Manager
- [ ] B) System for Cross-domain Identity Management
- [ ] C) Single Cloud Identity Module
- [ ] D) Standard Credential Interface Method

---

### Question 17
Which privilege is required to access any child objects within a catalog or schema?

- [ ] A) SELECT
- [ ] B) USAGE
- [ ] C) READ
- [ ] D) ACCESS

---

### Question 18
What is the recommended identity type for CI/CD pipelines?

- [ ] A) Regular user account
- [ ] B) Admin user account
- [ ] C) Service principal
- [ ] D) Guest account

---

### Question 19
What SQL syntax grants permissions in Unity Catalog?

- [ ] A) PERMIT SELECT TO user
- [ ] B) GRANT SELECT ON table TO user
- [ ] C) ALLOW user ACCESS table
- [ ] D) SET PERMISSION SELECT FOR user

---

### Question 20
How does permission inheritance work in Unity Catalog?

- [ ] A) Child objects inherit all parent permissions by default
- [ ] B) Permissions must be set explicitly on each object
- [ ] C) Only USAGE is inherited, data permissions are not
- [ ] D) Inheritance only works for admin users

---

### Question 21
What is the benefit of using groups for permission management?

- [ ] A) Faster query performance
- [ ] B) Simplified administration and consistent access control
- [ ] C) Lower compute costs
- [ ] D) Automatic data encryption

---

### Question 22
Which authentication protocol is used for SCIM provisioning?

- [ ] A) OAuth 2.0
- [ ] B) SAML 2.0
- [ ] C) Kerberos
- [ ] D) LDAP

---

### Question 23
What is the purpose of row-level security in Unity Catalog?

- [ ] A) Encrypt specific rows
- [ ] B) Filter data based on user attributes
- [ ] C) Speed up row access
- [ ] D) Compress row data

---

## Section 4: Compute Management (8 Questions)

### Question 24
Which cluster access mode is required for Unity Catalog support?

- [ ] A) No Isolation Shared
- [ ] B) High Concurrency
- [ ] C) Single User or Shared
- [ ] D) Custom only

---

### Question 25
What is the primary benefit of cluster pools?

- [ ] A) Unlimited compute capacity
- [ ] B) Reduced cluster startup time
- [ ] C) Free compute resources
- [ ] D) Better query performance

---

### Question 26
Which feature allows you to enforce tagging requirements on clusters?

- [ ] A) Unity Catalog
- [ ] B) Cluster Policies
- [ ] C) SQL Warehouses
- [ ] D) Delta Lake

---

### Question 27
What is the primary unit for measuring Databricks compute costs?

- [ ] A) CPU hours
- [ ] B) DBU (Databricks Unit)
- [ ] C) Memory GB
- [ ] D) Storage TB

---

### Question 28
What component coordinates Spark job execution?

- [ ] A) Worker node
- [ ] B) Executor
- [ ] C) Driver node
- [ ] D) Task

---

### Question 29
Which instance type strategy provides the highest cost savings for fault-tolerant batch workloads?

- [ ] A) On-demand instances
- [ ] B) Reserved instances
- [ ] C) Spot/Preemptible instances
- [ ] D) Dedicated hosts

---

### Question 30
What is the recommended approach for the driver node when using Spot instances?

- [ ] A) Use Spot for driver to maximize savings
- [ ] B) Keep driver on-demand for stability
- [ ] C) Don't use any driver node
- [ ] D) Use GPU instances for driver

---

### Question 31
What is a SQL Warehouse in Databricks?

- [ ] A) A data storage location
- [ ] B) Managed compute for SQL analytics
- [ ] C) A type of cluster policy
- [ ] D) A network security feature

---

## Section 5: Jobs and Workflows (6 Questions)

### Question 32
Which job trigger type starts a job when new files arrive in cloud storage?

- [ ] A) Scheduled
- [ ] B) Manual
- [ ] C) File Arrival
- [ ] D) Continuous

---

### Question 33
What are Databricks Asset Bundles (DABs)?

- [ ] A) Compressed notebook files
- [ ] B) Infrastructure as Code for Databricks resources
- [ ] C) Python packages
- [ ] D) Data storage containers

---

### Question 34
What is the purpose of job task dependencies?

- [ ] A) Control task execution order
- [ ] B) Share data between clusters
- [ ] C) Reduce compute costs
- [ ] D) Encrypt task outputs

---

### Question 35
Which repair strategy re-runs only failed tasks in a job?

- [ ] A) Full repair
- [ ] B) Partial repair
- [ ] C) Task repair
- [ ] D) Selective repair

---

### Question 36
What is the maximum concurrent runs setting for a job?

- [ ] A) Controls how many instances of the job can run simultaneously
- [ ] B) Limits the number of tasks in a job
- [ ] C) Sets the maximum duration for a job run
- [ ] D) Defines retry behavior

---

### Question 37
Which job cluster type is recommended for production workloads?

- [ ] A) All-purpose clusters
- [ ] B) Job clusters
- [ ] C) Interactive clusters
- [ ] D) SQL warehouses

---

## Section 6: Security and Networking (4 Questions)

### Question 38
What does Private Link provide in Databricks?

- [ ] A) Faster query performance
- [ ] B) Private connectivity without using public internet
- [ ] C) Lower storage costs
- [ ] D) Automatic data encryption

---

### Question 39
What is Secure Cluster Connectivity (SCC)?

- [ ] A) Encryption of data at rest
- [ ] B) Clusters without public IP addresses
- [ ] C) SSO configuration
- [ ] D) SCIM provisioning

---

### Question 40
What does Customer-Managed Keys (CMK) provide?

- [ ] A) Faster data access
- [ ] B) Control over encryption keys used for data protection
- [ ] C) Automatic backup
- [ ] D) Network routing

---

### Question 41
Which IP Access List mode allows only specified IP ranges to access the workspace?

- [ ] A) Block mode
- [ ] B) Allow mode
- [ ] C) Mixed mode
- [ ] D) Audit mode

---

## Section 7: Monitoring and Optimization (4 Questions)

### Question 42
Where are Databricks system tables located?

- [ ] A) In the default catalog
- [ ] B) In the system catalog
- [ ] C) In the hive_metastore catalog
- [ ] D) In each workspace catalog

---

### Question 43
Which system table contains billing usage data?

- [ ] A) system.access.audit
- [ ] B) system.billing.usage
- [ ] C) system.compute.clusters
- [ ] D) system.workflow.jobs

---

### Question 44
What is data skew in Spark?

- [ ] A) Data corruption in parquet files
- [ ] B) Uneven distribution of data across partitions
- [ ] C) Missing data in columns
- [ ] D) Duplicate records in tables

---

### Question 45
Which Spark UI tab shows executor memory usage?

- [ ] A) Jobs tab
- [ ] B) Stages tab
- [ ] C) Executors tab
- [ ] D) SQL tab

---

## Answer Key

| Q | Answer | Domain | Explanation |
|---|--------|--------|-------------|
| 1 | C | Lakehouse | Metastore is the top-level container |
| 2 | C | Lakehouse | Data Plane runs in customer's cloud |
| 3 | C | Lakehouse | Delta Lake uses Parquet format |
| 4 | B | Lakehouse | Default retention is 7 days (168 hours) |
| 5 | B | Lakehouse | DESCRIBE HISTORY shows transaction history |
| 6 | B | Lakehouse | Dropping managed table deletes data and metadata |
| 7 | B | Lakehouse | Transaction log enables ACID compliance |
| 8 | B | Lakehouse | LTS suffix indicates Long Term Support |
| 9 | B | Workspace | Metastores are managed at account level |
| 10 | D | Workspace | Both account admin and metastore admin needed |
| 11 | B | Workspace | Workspace settings control download behavior |
| 12 | B | Workspace | Account Console manages across workspaces |
| 13 | B | Workspace | Serverless SQL Warehouses are serverless |
| 14 | B | Workspace | Folders organize notebooks and files |
| 15 | C | Workspace | Only account admins create workspaces |
| 16 | B | IAM | System for Cross-domain Identity Management |
| 17 | B | IAM | USAGE is required on containers |
| 18 | C | IAM | Service principals for automation |
| 19 | B | IAM | Standard SQL GRANT syntax |
| 20 | A | IAM | Child objects inherit parent permissions |
| 21 | B | IAM | Groups simplify administration |
| 22 | A | IAM | SCIM uses OAuth 2.0 for authentication |
| 23 | B | IAM | Row-level security filters by user |
| 24 | C | Compute | Unity Catalog requires Single User or Shared |
| 25 | B | Compute | Pools reduce cluster startup time |
| 26 | B | Compute | Cluster Policies enforce configurations |
| 27 | B | Compute | DBU is the billing unit |
| 28 | C | Compute | Driver coordinates execution |
| 29 | C | Compute | Spot instances for cost savings |
| 30 | B | Compute | Driver should be on-demand |
| 31 | B | Compute | SQL Warehouse is managed SQL compute |
| 32 | C | Jobs | File Arrival trigger monitors storage |
| 33 | B | Jobs | DABs are IaC for Databricks |
| 34 | A | Jobs | Dependencies control execution order |
| 35 | C | Jobs | Task repair re-runs only failed tasks |
| 36 | A | Jobs | Controls simultaneous job instances |
| 37 | B | Jobs | Job clusters for production |
| 38 | B | Security | Private Link avoids public internet |
| 39 | B | Security | SCC means no public IPs on clusters |
| 40 | B | Security | CMK provides encryption key control |
| 41 | B | Security | Allow mode permits only specified IPs |
| 42 | B | Monitoring | System tables in system catalog |
| 43 | B | Monitoring | system.billing.usage for billing data |
| 44 | B | Monitoring | Skew is uneven partition distribution |
| 45 | C | Monitoring | Executors tab shows memory usage |

---

## Scoring Guide

| Score | Percentage | Result |
|-------|------------|--------|
| 40-45 | 89-100% | Excellent - Certification Ready |
| 35-39 | 78-87% | Good - Minor Review Needed |
| 32-34 | 71-76% | Pass - Review Weak Areas |
| 27-31 | 60-69% | Borderline - Focused Study Required |
| < 27 | < 60% | More Preparation Needed |

---

## Domain Breakdown

| Domain | Questions | Weight |
|--------|-----------|--------|
| Lakehouse Platform | 8 | 18% |
| Workspace Administration | 7 | 16% |
| Identity & Access Management | 8 | 18% |
| Compute Management | 8 | 18% |
| Jobs & Workflows | 6 | 13% |
| Security & Networking | 4 | 9% |
| Monitoring & Optimization | 4 | 9% |

---

*Practice Exam Version: 2.0 | Databricks Platform Administration Training*
*Aligned with Databricks Certified Associate Platform Administrator Exam*
