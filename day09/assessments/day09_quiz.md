# Day 9 Quiz: Cluster & SQL Warehouse Administration

## Databricks Platform Administration Training
### Duration: 10 Minutes | 10 Questions | 70% to Pass

---

### Question 1
What is the main difference between an all-purpose cluster and a job cluster?

- [ ] A) All-purpose clusters are faster
- [ ] B) Job clusters are created and terminated automatically per job run
- [ ] C) All-purpose clusters cannot run Spark
- [ ] D) Job clusters support more users

---

### Question 2
What does auto-termination do for a cluster?

- [ ] A) Deletes the cluster configuration
- [ ] B) Stops the cluster after a period of inactivity
- [ ] C) Restarts the cluster automatically
- [ ] D) Scales down to zero workers

---

### Question 3
Which cluster access mode is required for Unity Catalog support?

- [ ] A) No Isolation Shared
- [ ] B) High Concurrency
- [ ] C) Single User or Shared
- [ ] D) Custom only

---

### Question 4
What is the purpose of a cluster policy?

- [ ] A) To speed up cluster performance
- [ ] B) To enforce constraints on cluster configurations
- [ ] C) To monitor cluster usage
- [ ] D) To backup cluster data

---

### Question 5
What benefit do instance pools provide?

- [ ] A) Unlimited compute capacity
- [ ] B) Reduced cluster startup time
- [ ] C) Free compute resources
- [ ] D) Better query performance

---

### Question 6
Which SQL Warehouse type is managed entirely by Databricks?

- [ ] A) Classic
- [ ] B) Pro
- [ ] C) Serverless
- [ ] D) Custom

---

### Question 7
How do you increase concurrent query capacity for a SQL Warehouse?

- [ ] A) Increase auto-termination time
- [ ] B) Add more clusters (horizontal scaling)
- [ ] C) Reduce warehouse size
- [ ] D) Disable caching

---

### Question 8
What is the recommended instance configuration for the driver node when using Spot instances?

- [ ] A) Use Spot for both driver and workers
- [ ] B) Keep driver on-demand, use Spot for workers
- [ ] C) Use on-demand for workers, Spot for driver
- [ ] D) Spot instances cannot be used with clusters

---

### Question 9
What does "LTS" mean in the context of Databricks Runtime versions?

- [ ] A) Large Table Support
- [ ] B) Long Term Support
- [ ] C) Latest Technology Stack
- [ ] D) Low Throughput System

---

### Question 10
What is the primary cost control mechanism for development clusters?

- [ ] A) Using the largest instance types
- [ ] B) Disabling autoscaling
- [ ] C) Setting auto-termination and using Spot instances
- [ ] D) Running clusters 24/7

---

## Answer Key

| Q | Answer | Explanation |
|---|--------|-------------|
| 1 | B | Job clusters are created when a job starts and terminated when it ends |
| 2 | B | Auto-termination stops idle clusters to save costs |
| 3 | C | Unity Catalog requires Single User or Shared access modes |
| 4 | B | Cluster policies enforce rules and constraints on configurations |
| 5 | B | Pools maintain idle instances for faster cluster startup |
| 6 | C | Serverless warehouses are fully managed by Databricks |
| 7 | B | Adding more clusters (horizontal scaling) increases query concurrency |
| 8 | B | Driver should be on-demand for stability, workers can use Spot |
| 9 | B | LTS = Long Term Support, indicating stable, supported versions |
| 10 | C | Auto-termination and Spot instances are key cost control measures |

---

*Quiz Version: 2.0 | Databricks Platform Administration Training - Day 9*
