# Day 1 Quiz: Lakehouse & Workspace Foundations

## Databricks Platform Administration Training
### Duration: 10 Minutes | 10 Questions | 70% to Pass

---

## Instructions

- Select the **best** answer for each question
- Some questions may have multiple correct answers - select ALL that apply where indicated
- You need **70% (7/10)** to pass

---

### Question 1
What is a key advantage of the Lakehouse architecture over traditional two-tier (lake + warehouse) architectures?

- [ ] A) Lakehouse requires more data copies for different workloads
- [ ] B) Lakehouse provides a single copy of data for all workloads
- [ ] C) Lakehouse only supports structured data
- [ ] D) Lakehouse cannot support ACID transactions

---

### Question 2
Which component provides ACID transactions on data lake storage in the Databricks platform?

- [ ] A) Apache Spark
- [ ] B) Unity Catalog
- [ ] C) Delta Lake
- [ ] D) SQL Warehouse

---

### Question 3
In the Databricks architecture, where is customer data stored?

- [ ] A) In the Control Plane managed by Databricks
- [ ] B) In the Data Plane within the customer's cloud account
- [ ] C) In a shared multi-tenant database
- [ ] D) In Databricks' proprietary storage system

---

### Question 4
Which of the following are components of the Control Plane? (Select ALL that apply)

- [ ] A) Web application UI
- [ ] B) Compute clusters (VMs)
- [ ] C) Job scheduler
- [ ] D) Unity Catalog metadata service
- [ ] E) Customer's data storage

---

### Question 5
What is the purpose of a Databricks workspace?

- [ ] A) Only for storing data files
- [ ] B) A unified environment for data engineering, science, and analytics
- [ ] C) A backup system for cloud storage
- [ ] D) A monitoring dashboard only

---

### Question 6
Which type of cluster is optimized for automated, scheduled workloads?

- [ ] A) All-purpose cluster
- [ ] B) Job cluster
- [ ] C) SQL warehouse
- [ ] D) Interactive cluster

---

### Question 7
What is the scope of an Account Admin's responsibilities?

- [ ] A) A single workspace only
- [ ] B) A specific cluster only
- [ ] C) The entire Databricks account including all workspaces
- [ ] D) Only Unity Catalog objects

---

### Question 8
In Azure Databricks, which network option allows you to deploy Databricks into your own virtual network for enhanced isolation?

- [ ] A) Public subnet deployment
- [ ] B) VNet injection
- [ ] C) Service endpoint
- [ ] D) Load balancer integration

---

### Question 9
Which of the following are best practices for Databricks administrators? (Select ALL that apply)

- [ ] A) Assign permissions directly to individual users
- [ ] B) Use groups for permission management
- [ ] C) Apply the principle of least privilege
- [ ] D) Document all configuration decisions
- [ ] E) Give all users admin access for convenience

---

### Question 10
What does the Lakehouse architecture combine?

- [ ] A) Only streaming and batch processing
- [ ] B) Data lake flexibility with data warehouse reliability
- [ ] C) Multiple separate storage systems
- [ ] D) Only machine learning and AI workloads

---

## Answer Key

| Question | Correct Answer(s) | Explanation |
|----------|-------------------|-------------|
| 1 | B | Lakehouse eliminates data duplication by providing a single copy of data for BI, ML, and engineering workloads |
| 2 | C | Delta Lake provides ACID transactions, time travel, and schema enforcement on data lake storage |
| 3 | B | Customer data resides in the Data Plane within the customer's own cloud account (S3, ADLS, GCS) |
| 4 | A, C, D | The Control Plane includes the UI, scheduler, and Unity Catalog service. Compute (VMs) and data storage are in the Data Plane |
| 5 | B | A workspace is a unified environment for all data personas to collaborate |
| 6 | B | Job clusters are created per-job, optimized for automated workloads, and terminated after completion |
| 7 | C | Account Admins manage the entire account including all workspaces, identity, billing, and Unity Catalog |
| 8 | B | VNet injection deploys Databricks resources into a customer-managed virtual network |
| 9 | B, C, D | Best practices include using groups, least privilege, and documentation. Never assign permissions to individuals or give blanket admin access |
| 10 | B | Lakehouse combines the flexibility and low cost of data lakes with the reliability, governance, and performance of data warehouses |

---

## Scoring

| Score | Result |
|-------|--------|
| 9-10 | Excellent! Strong understanding of Lakehouse fundamentals |
| 7-8 | Passed. Review any missed topics |
| 5-6 | Needs improvement. Review slides before Day 2 |
| Below 5 | Recommended: Re-review Day 1 materials |

---

*Quiz Version: 2.0 | Databricks Platform Administration Training - Day 1*
