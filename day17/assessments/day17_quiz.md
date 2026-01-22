# Day 17 Quiz: Monitoring & Troubleshooting

## Databricks Platform Administration Training
### Duration: 10 Minutes | 10 Questions | 70% to Pass

---

### Question 1
Which system table provides cluster compute usage and cost data?

- [ ] A) system.access.audit
- [ ] B) system.compute.clusters
- [ ] C) system.billing.usage
- [ ] D) system.lakeflow.events

---

### Question 2
What are the Four Golden Signals in monitoring?

- [ ] A) CPU, Memory, Disk, Network
- [ ] B) Latency, Traffic, Errors, Saturation
- [ ] C) Cost, Performance, Security, Availability
- [ ] D) Input, Process, Output, Storage

---

### Question 3
Which log type captures user activities like login attempts and permission changes?

- [ ] A) Driver logs
- [ ] B) Executor logs
- [ ] C) Audit logs
- [ ] D) Spark event logs

---

### Question 4
What does a high shuffle write metric typically indicate?

- [ ] A) Excellent query performance
- [ ] B) Data redistribution between nodes, potential bottleneck
- [ ] C) Low memory usage
- [ ] D) Successful job completion

---

### Question 5
Where can you find detailed Spark executor logs for debugging failed tasks?

- [ ] A) Only in cloud storage
- [ ] B) Cluster UI → Spark UI → Executors tab
- [ ] C) Unity Catalog logs
- [ ] D) Executor logs are not available

---

### Question 6
What query would show all access to financial data in the last 30 days?

- [ ] A) SELECT * FROM system.compute.clusters
- [ ] B) SELECT * FROM system.access.audit WHERE action_name LIKE '%Table%' AND request_params LIKE '%finance%'
- [ ] C) SELECT * FROM system.billing.usage WHERE sku_name = 'finance'
- [ ] D) SELECT * FROM system.tables.information WHERE schema = 'finance'

---

### Question 7
What is the purpose of Ganglia metrics in Databricks clusters?

- [ ] A) User authentication tracking
- [ ] B) Real-time cluster resource monitoring (CPU, memory, network)
- [ ] C) Query result caching
- [ ] D) Data lineage tracking

---

### Question 8
What is a common cause of `OutOfMemoryError` on executors?

- [ ] A) Too many files in storage
- [ ] B) Data skew causing uneven partition sizes
- [ ] C) Network latency
- [ ] D) Insufficient cluster policies

---

### Question 9
Which metric helps identify expensive queries consuming excessive resources?

- [ ] A) Cluster uptime
- [ ] B) Query duration and bytes scanned
- [ ] C) User login count
- [ ] D) Storage capacity

---

### Question 10
What should you check first when a scheduled job suddenly starts failing?

- [ ] A) Delete and recreate the job
- [ ] B) Recent code changes, data changes, cluster/policy changes, and resource availability
- [ ] C) Increase cluster size immediately
- [ ] D) Wait for automatic recovery

---

## Answer Key

| Q | Answer | Explanation |
|---|--------|-------------|
| 1 | B | system.compute.clusters tracks cluster usage; system.billing.usage for costs |
| 2 | B | Google SRE's Four Golden Signals: Latency, Traffic, Errors, Saturation |
| 3 | C | Audit logs capture user actions, security events, and access patterns |
| 4 | B | High shuffle indicates data movement between nodes - often a bottleneck |
| 5 | B | Spark UI provides access to executor logs through the cluster interface |
| 6 | B | system.access.audit tracks all data access with query and object details |
| 7 | B | Ganglia provides real-time cluster resource utilization metrics |
| 8 | B | Data skew causes some partitions to be much larger, exhausting memory |
| 9 | B | Query duration and bytes scanned identify resource-intensive queries |
| 10 | B | Systematic debugging: check recent changes before making modifications |

---

*Quiz Version: 3.0 | Databricks Platform Administration Training - Day 17*
