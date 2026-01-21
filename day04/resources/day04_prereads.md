# Day 4 Pre-Reading Materials

## Databricks Platform Administration Training
### Spark Fundamentals for Administrators

---

## Overview

Day 4 introduces Apache Spark from an administrator's perspective. You don't need to write Spark code, but understanding how Spark works helps you monitor, troubleshoot, and optimize workloads.

**Estimated Reading Time**: 25-30 minutes

---

## Required Reading

### 1. Spark Architecture Overview

**Source**: Databricks Documentation & Apache Spark

**Key Concepts to Understand**:
- Driver and executor model
- Jobs, stages, and tasks
- How work is distributed across a cluster

**Read**: [Spark concepts](https://docs.databricks.com/en/getting-started/spark/index.html)

**Focus Areas**:
- Driver node responsibilities
- Executor lifecycle
- Parallelism and partitioning

### 2. Clusters in Databricks

**Source**: Databricks Documentation

**Key Concepts to Understand**:
- All-purpose vs job clusters
- Autoscaling behavior
- Cluster configuration options

**Read**: [Compute](https://docs.databricks.com/en/compute/index.html)

**Focus Areas**:
- When to use each cluster type
- Cost implications of cluster sizing
- Photon acceleration

### 3. Spark UI Basics

**Source**: Databricks Documentation

**Key Concepts to Understand**:
- Navigating the Spark UI
- Understanding job/stage/task breakdown
- Identifying performance bottlenecks

**Read**: [View Apache Spark job details](https://docs.databricks.com/en/compute/clusters-manage.html#view-spark-job-details)

**Focus Areas**:
- Jobs tab interpretation
- Stage details and task metrics
- Storage and executor tabs

---

## Key Terminology

| Term | Definition |
|------|------------|
| **Driver** | Process that coordinates Spark job execution |
| **Executor** | Process that runs tasks and stores data |
| **Job** | Complete computation triggered by an action |
| **Stage** | Set of tasks that can run in parallel |
| **Task** | Unit of work sent to an executor |
| **Partition** | Logical chunk of distributed data |
| **Shuffle** | Data redistribution between stages |
| **Spill** | Writing to disk when memory is insufficient |

---

## Visual Concept: Spark Execution Hierarchy

```
Driver
  └── Job (triggered by action like collect(), save())
        └── Stage 1 (separated by shuffle boundaries)
        │     └── Task 1.1 (one per partition)
        │     └── Task 1.2
        │     └── Task 1.3
        └── Stage 2
              └── Task 2.1
              └── Task 2.2
```

---

## Self-Assessment Questions

1. What's the difference between a job and a stage in Spark?
2. Why might one task in a stage take much longer than others?
3. What causes a shuffle, and why is it expensive?
4. What's the difference between an all-purpose cluster and a job cluster?

---

## Recommended Additional Reading

- [Apache Spark on Databricks](https://docs.databricks.com/en/spark/index.html)
- [Cluster configuration best practices](https://docs.databricks.com/en/compute/cluster-config-best-practices.html)
- [Debugging notebook](https://docs.databricks.com/en/notebooks/notebook-debug.html)

---

*Pre-reading materials for Databricks Platform Administration Training - Day 4*
