# Day 11 Quiz: Monitoring & Troubleshooting

## Databricks Platform Administration Training
### Duration: 10 Minutes | 10 Questions | 70% to Pass

---

### Question 1
Where are Databricks system tables located?

- [ ] A) In the default catalog
- [ ] B) In the system catalog
- [ ] C) In the hive_metastore catalog
- [ ] D) In each workspace catalog

---

### Question 2
Which system table contains audit logs for security monitoring?

- [ ] A) system.billing.usage
- [ ] B) system.access.audit
- [ ] C) system.compute.clusters
- [ ] D) system.workflow.jobs

---

### Question 3
What is data skew in Spark?

- [ ] A) Data corruption in parquet files
- [ ] B) Uneven distribution of data across partitions
- [ ] C) Missing data in columns
- [ ] D) Duplicate records in tables

---

### Question 4
Where can you view detailed Spark job execution information?

- [ ] A) Admin Console
- [ ] B) Unity Catalog
- [ ] C) Spark UI
- [ ] D) SQL Warehouse settings

---

### Question 5
Which Spark configuration helps handle data skew automatically?

- [ ] A) spark.sql.shuffle.partitions
- [ ] B) spark.sql.adaptive.skewJoin.enabled
- [ ] C) spark.executor.memory
- [ ] D) spark.driver.memory

---

### Question 6
What does the system.billing.usage table track?

- [ ] A) User login history
- [ ] B) DBU consumption and usage details
- [ ] C) Query execution plans
- [ ] D) Cluster configurations

---

### Question 7
What is the recommended way to persist cluster logs after termination?

- [ ] A) Copy logs manually
- [ ] B) Configure cluster log delivery to cloud storage
- [ ] C) Increase cluster memory
- [ ] D) Enable auto-scaling

---

### Question 8
Which metric indicates a job performance problem in Spark UI?

- [ ] A) All tasks completing at similar times
- [ ] B) Some tasks taking 10x longer than others
- [ ] C) Even data distribution
- [ ] D) Low shuffle read

---

### Question 9
What can cause an OutOfMemoryError in Spark?

- [ ] A) Too many partitions
- [ ] B) Large shuffle or collect on large dataset
- [ ] C) Fast network
- [ ] D) Small data files

---

### Question 10
What feature in Databricks SQL allows automated notifications based on query results?

- [ ] A) Dashboards
- [ ] B) Alerts
- [ ] C) Queries
- [ ] D) Warehouses

---

## Answer Key

| Q | Answer | Explanation |
|---|--------|-------------|
| 1 | B | System tables are located in the `system` catalog |
| 2 | B | system.access.audit contains audit logs for all actions |
| 3 | B | Data skew is uneven distribution causing some tasks to be slower |
| 4 | C | Spark UI provides detailed job, stage, and task information |
| 5 | B | Adaptive Query Execution with skewJoin handles skew automatically |
| 6 | B | system.billing.usage tracks DBU consumption for cost analysis |
| 7 | B | Configure cluster log delivery path to persist logs |
| 8 | B | Large variance in task duration (stragglers) indicates problems |
| 9 | B | Large shuffles or collecting large datasets can cause OOM |
| 10 | B | SQL Alerts trigger notifications based on query result conditions |

---

*Quiz Version: 2.0 | Databricks Platform Administration Training - Day 11*
