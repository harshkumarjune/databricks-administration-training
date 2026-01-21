# Post-Training Assessment: Databricks Platform Administration

## Databricks Platform Administration Training
### Duration: 20 Minutes | 20 Questions | Knowledge Validation

---

## Instructions

This assessment validates your learning from the Databricks Platform Administration Training. A score of 80% or higher indicates successful completion of learning objectives. Compare your score to the pre-assessment to measure improvement.

---

### Question 1
In the Databricks architecture, which component is responsible for managing user sessions, notebooks, and API requests?

- [ ] A) Data Plane
- [ ] B) Control Plane
- [ ] C) Compute Cluster
- [ ] D) Unity Catalog

---

### Question 2
When configuring Unity Catalog, what is the relationship between a metastore and workspaces?

- [ ] A) One workspace can have multiple metastores
- [ ] B) One metastore per workspace, always
- [ ] C) One metastore can be attached to multiple workspaces in the same region
- [ ] D) Metastores are not related to workspaces

---

### Question 3
A user has SELECT permission on a table `catalog.schema.table`. What additional permissions do they need to successfully query this table?

- [ ] A) No additional permissions needed
- [ ] B) USAGE on the catalog and schema
- [ ] C) READ on the catalog
- [ ] D) MODIFY on the table

---

### Question 4
Which cluster policy attribute type would you use to allow only specific values like "development", "staging", "production"?

- [ ] A) fixed
- [ ] B) range
- [ ] C) allowlist
- [ ] D) regex

---

### Question 5
What is the main difference between a job cluster and an all-purpose cluster?

- [ ] A) Job clusters cost more
- [ ] B) Job clusters are created and terminated with each job run
- [ ] C) All-purpose clusters cannot run notebooks
- [ ] D) Job clusters support more languages

---

### Question 6
Which system table schema contains billing and DBU usage information?

- [ ] A) system.access
- [ ] B) system.billing
- [ ] C) system.compute
- [ ] D) system.workflow

---

### Question 7
What protocol does SCIM use to automatically provision users from an identity provider to Databricks?

- [ ] A) SAML
- [ ] B) OAuth
- [ ] C) REST API
- [ ] D) LDAP

---

### Question 8
In Delta Lake, which command is used to permanently delete data that is older than the retention period?

- [ ] A) OPTIMIZE
- [ ] B) ZORDER
- [ ] C) VACUUM
- [ ] D) COMPACT

---

### Question 9
What is the purpose of Secure Cluster Connectivity (SCC)?

- [ ] A) Encrypt data at rest
- [ ] B) Ensure cluster nodes have no public IP addresses
- [ ] C) Manage user passwords
- [ ] D) Speed up network connections

---

### Question 10
Which identity type should be used for automated pipelines and CI/CD processes instead of personal user accounts?

- [ ] A) Admin account
- [ ] B) Service principal
- [ ] C) Guest user
- [ ] D) Group account

---

### Question 11
In a Databricks workflow with multiple tasks, what determines the execution order?

- [ ] A) Task creation order
- [ ] B) Task names alphabetically
- [ ] C) Task dependencies (DAG)
- [ ] D) Random selection

---

### Question 12
What is the main advantage of using spot/preemptible instances for Databricks worker nodes?

- [ ] A) Better performance
- [ ] B) Significant cost savings (60-90%)
- [ ] C) More reliable uptime
- [ ] D) Faster startup time

---

### Question 13
Which SQL command would you use to view all permissions on a specific table?

- [ ] A) LIST PERMISSIONS ON TABLE
- [ ] B) DESCRIBE GRANTS ON TABLE
- [ ] C) SHOW GRANTS ON TABLE
- [ ] D) VIEW PERMISSIONS ON TABLE

---

### Question 14
What is a key difference between managed tables and external tables in Unity Catalog?

- [ ] A) Managed tables can only store CSV data
- [ ] B) External tables are always faster
- [ ] C) Dropping a managed table deletes the underlying data; external tables retain data
- [ ] D) External tables don't support ACID transactions

---

### Question 15
Which account-level role can create and manage Unity Catalog metastores?

- [ ] A) Workspace Admin
- [ ] B) Metastore Admin
- [ ] C) Account Admin
- [ ] D) Data Owner

---

### Question 16
What Spark UI tab would you examine to identify data skew issues?

- [ ] A) Environment
- [ ] B) Stages (task duration variance)
- [ ] C) Storage
- [ ] D) SQL

---

### Question 17
What is the purpose of custom tags on Databricks clusters?

- [ ] A) Speed up computations
- [ ] B) Enable encryption
- [ ] C) Cost allocation and resource tracking
- [ ] D) Improve query performance

---

### Question 18
Which Databricks Asset Bundles command deploys resources to a target environment?

- [ ] A) databricks bundle run
- [ ] B) databricks bundle deploy
- [ ] C) databricks bundle push
- [ ] D) databricks bundle apply

---

### Question 19
Row filters and column masks in Unity Catalog are examples of what type of access control?

- [ ] A) Role-based access control
- [ ] B) Attribute-based access control
- [ ] C) Fine-grained access control
- [ ] D) Network access control

---

### Question 20
What is the purpose of IP access lists in Databricks?

- [ ] A) Speed up network connections
- [ ] B) Restrict workspace access to specific IP ranges
- [ ] C) Configure cluster networking
- [ ] D) Manage DNS resolution

---

## Answer Key

| Q | Answer | Explanation | Topic |
|---|--------|-------------|-------|
| 1 | B | The Control Plane manages sessions, notebooks, APIs, and job scheduling | Architecture |
| 2 | C | A regional metastore can attach to multiple workspaces in the same region | Unity Catalog |
| 3 | B | USAGE is required on parent containers (catalog and schema) to access child objects | Permissions |
| 4 | C | Allowlist restricts values to a specific set of options | Cluster Policies |
| 5 | B | Job clusters are ephemeral - created when job starts, terminated when complete | Compute |
| 6 | B | system.billing.usage contains DBU consumption data | System Tables |
| 7 | C | SCIM uses REST API calls to synchronize identity data | Identity |
| 8 | C | VACUUM removes data files beyond the retention period | Delta Lake |
| 9 | B | SCC ensures cluster nodes have no public IPs for enhanced security | Network Security |
| 10 | B | Service principals are designed for automation and non-interactive access | Identity |
| 11 | C | Task dependencies form a DAG (Directed Acyclic Graph) for execution order | Workflows |
| 12 | B | Spot instances provide 60-90% cost savings over on-demand | Cost Management |
| 13 | C | SHOW GRANTS ON TABLE displays all grants on the specified table | Permissions |
| 14 | C | Managed tables' data is deleted on DROP; external tables keep underlying data | Unity Catalog |
| 15 | C | Account Admins manage account-level resources including metastores | Administration |
| 16 | B | The Stages tab shows task duration variance which reveals data skew | Troubleshooting |
| 17 | C | Tags enable cost allocation, chargeback, and resource tracking | Cost Governance |
| 18 | B | `databricks bundle deploy` pushes bundle resources to the target | CI/CD |
| 19 | C | Row filters and column masks provide fine-grained (row/column level) access control | Data Security |
| 20 | B | IP access lists allow/block access based on source IP addresses | Network Security |

---

## Scoring

| Score | Percentage | Result |
|-------|------------|--------|
| 18-20 | 90-100% | Excellent - Ready for certification |
| 16-17 | 80-89% | Passed - Strong understanding |
| 14-15 | 70-79% | Good - Review weak areas |
| 12-13 | 60-69% | Fair - Additional study recommended |
| Below 12 | <60% | Needs review - Revisit course materials |

---

## Learning Improvement Calculation

Compare with Pre-Assessment score:

| Pre-Assessment | Post-Assessment | Improvement |
|----------------|-----------------|-------------|
| ___/15 | ___/20 | ___% growth |

**Formula**: ((Post % - Pre %) / Pre %) × 100 = % Improvement

---

*Post-Assessment Version: 2.0 | Databricks Platform Administration Training*
