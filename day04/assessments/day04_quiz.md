# Day 4 Quiz: Spark Fundamentals for Administrators

## Databricks Platform Administration Training
### Duration: 10 Minutes | 10 Questions | 70% to Pass

---

### Question 1
In Spark architecture, what is the role of the Driver?

- [ ] A) Execute tasks on data partitions
- [ ] B) Store data across the cluster
- [ ] C) Orchestrate execution and schedule tasks
- [ ] D) Manage network communication only

---

### Question 2
What triggers actual execution in Spark?

- [ ] A) Transformations like filter() and select()
- [ ] B) Actions like count() and collect()
- [ ] C) Creating a DataFrame
- [ ] D) Importing libraries

---

### Question 3
What is a "shuffle" in Spark?

- [ ] A) Random sampling of data
- [ ] B) Redistribution of data across partitions
- [ ] C) Sorting data within a partition
- [ ] D) Caching data in memory

---

### Question 4
Which operations commonly cause shuffles? (Select ALL that apply)

- [ ] A) filter()
- [ ] B) groupBy()
- [ ] C) join()
- [ ] D) select()
- [ ] E) orderBy()

---

### Question 5
What does "data skew" indicate?

- [ ] A) Data is evenly distributed
- [ ] B) Some partitions have much more data than others
- [ ] C) Data is corrupted
- [ ] D) Cluster is under-provisioned

---

### Question 6
In the Spark UI, which tab shows information about data redistribution?

- [ ] A) Jobs tab
- [ ] B) Stages tab (shuffle read/write metrics)
- [ ] C) Storage tab
- [ ] D) Environment tab

---

### Question 7
What does high GC (Garbage Collection) time in task metrics indicate?

- [ ] A) Network issues
- [ ] B) Disk failures
- [ ] C) Memory pressure
- [ ] D) CPU overload

---

### Question 8
Which cluster type is optimized for scheduled, automated workloads?

- [ ] A) All-purpose cluster
- [ ] B) Job cluster
- [ ] C) SQL warehouse
- [ ] D) Interactive cluster

---

### Question 9
What is the correct hierarchy of Spark execution units (smallest to largest)?

- [ ] A) Job → Stage → Task
- [ ] B) Task → Stage → Job
- [ ] C) Stage → Task → Job
- [ ] D) Task → Job → Stage

---

### Question 10
What should an administrator look for to identify data skew issues?

- [ ] A) High total job duration
- [ ] B) Large variance in task durations within a stage
- [ ] C) Many successful jobs
- [ ] D) Low shuffle write

---

## Answer Key

| Question | Answer | Explanation |
|----------|--------|-------------|
| 1 | C | The Driver orchestrates execution, builds the DAG, and schedules tasks |
| 2 | B | Spark uses lazy evaluation; only Actions trigger execution |
| 3 | B | Shuffle redistributes data across partitions, often across the network |
| 4 | B, C, E | groupBy, join, and orderBy cause shuffles; filter and select are narrow transformations |
| 5 | B | Data skew means uneven partition sizes, causing some tasks to run much longer |
| 6 | B | Stages tab shows shuffle read/write metrics |
| 7 | C | High GC time indicates memory pressure, often from processing large data |
| 8 | B | Job clusters are created per-job and terminated after, ideal for automation |
| 9 | B | Task is smallest (one partition), Stage contains tasks, Job contains stages |
| 10 | B | Data skew shows as large variance in task durations within the same stage |

---

*Quiz Version: 2.0 | Databricks Platform Administration Training - Day 4*
