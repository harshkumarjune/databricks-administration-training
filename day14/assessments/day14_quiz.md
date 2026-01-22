# Day 14 Quiz: Cluster Architecture & Types

## Databricks Platform Administration Training
### Duration: 10 Minutes | 10 Questions | 70% to Pass

---

### Question 1
What is the fundamental difference between all-purpose clusters and job clusters?

- [ ] A) All-purpose clusters can only run SQL
- [ ] B) Job clusters are automatically created and terminated with each job run
- [ ] C) All-purpose clusters are limited to single users
- [ ] D) Job clusters are always larger than all-purpose clusters

---

### Question 2
Which cluster access mode provides the highest level of isolation for sensitive workloads?

- [ ] A) No Isolation Shared
- [ ] B) Shared mode
- [ ] C) Single User mode
- [ ] D) Custom mode

---

### Question 3
What is the minimum recommended configuration for a production driver node?

- [ ] A) Same size as worker nodes
- [ ] B) Smallest available instance
- [ ] C) 2-4x more memory than workers
- [ ] D) No driver is needed in production

---

### Question 4
How does autoscaling determine when to add workers?

- [ ] A) Based on calendar schedule only
- [ ] B) Based on pending task queue and resource utilization
- [ ] C) Randomly to ensure availability
- [ ] D) Only when manually triggered

---

### Question 5
What is the benefit of using Databricks Runtime ML over standard runtime?

- [ ] A) Lower cost
- [ ] B) Pre-installed machine learning libraries
- [ ] C) Faster SQL queries
- [ ] D) Better network isolation

---

### Question 6
When should you use Photon-enabled clusters?

- [ ] A) For streaming workloads only
- [ ] B) For SQL and DataFrame-heavy workloads
- [ ] C) For Python-only workloads
- [ ] D) For clusters with less than 2 workers

---

### Question 7
What happens when a cluster node fails during a job execution?

- [ ] A) The entire job fails immediately
- [ ] B) Spark automatically re-executes lost tasks on remaining nodes
- [ ] C) The job pauses until manual intervention
- [ ] D) All data is lost permanently

---

### Question 8
What is the recommended approach for using Spot instances?

- [ ] A) Use Spot for both driver and worker nodes
- [ ] B) Use On-Demand for driver, Spot for workers with fallback
- [ ] C) Never use Spot instances in production
- [ ] D) Use Spot only for the driver node

---

### Question 9
Which autoscaling setting determines the maximum time to wait before scaling down?

- [ ] A) Min workers
- [ ] B) Max workers
- [ ] C) Scale down threshold
- [ ] D) Auto-termination

---

### Question 10
What is the purpose of Databricks Runtime versioning (e.g., 14.3 LTS)?

- [ ] A) Marketing purposes only
- [ ] B) To track costs per version
- [ ] C) To ensure compatibility and indicate support lifecycle
- [ ] D) To limit cluster sizes

---

## Answer Key

| Q | Answer | Explanation |
|---|--------|-------------|
| 1 | B | Job clusters are ephemeral - created at job start and terminated at completion |
| 2 | C | Single User mode provides complete isolation for one user's workload |
| 3 | C | Driver needs more memory for coordinating tasks and handling results |
| 4 | B | Autoscaler monitors pending tasks and cluster utilization metrics |
| 5 | B | Runtime ML includes pre-installed TensorFlow, PyTorch, scikit-learn, etc. |
| 6 | B | Photon is optimized for SQL/Spark SQL and DataFrame operations |
| 7 | B | Spark's fault tolerance re-executes lost partitions on available nodes |
| 8 | B | Driver on-demand ensures stability; workers on Spot with fallback saves cost |
| 9 | C | Scale down threshold controls how quickly idle workers are removed |
| 10 | C | Versioning tracks features, compatibility, and LTS indicates extended support |

---

*Quiz Version: 3.0 | Databricks Platform Administration Training - Day 14*
