# Day 14 Pre-Reading Materials

## Databricks Platform Administration Training
### Cluster Architecture & Types

---

## Overview

Day 14 dives deep into cluster architecture, understanding the different cluster types, autoscaling mechanisms, and how to choose the right configuration for different workloads. This foundational knowledge is critical for effective compute governance.

**Estimated Reading Time**: 25-30 minutes

---

## Required Reading

### 1. Cluster Architecture Fundamentals

**Source**: Databricks Documentation

**Key Concepts to Understand**:
- Driver node vs worker node roles
- Spark executors and task distribution
- Data partitioning across nodes

**Read**: [Compute configuration overview](https://docs.databricks.com/en/compute/configure.html)

**Focus Areas**:
- How Spark distributes work across nodes
- Memory and CPU allocation patterns
- Driver sizing considerations

### 2. Cluster Types

**Source**: Databricks Documentation

**Key Concepts to Understand**:
- All-purpose clusters (interactive development)
- Job clusters (automated workloads)
- Instance pools (startup acceleration)

**Read**: [Create clusters](https://docs.databricks.com/en/compute/clusters-manage.html)

**Focus Areas**:
- When to use each cluster type
- Cost implications of each type
- Access modes and Unity Catalog compatibility

### 3. Autoscaling Configuration

**Source**: Databricks Documentation

**Key Concepts to Understand**:
- Min/max worker settings
- Scale-up and scale-down behavior
- Optimized autoscaling

**Read**: [Cluster autoscaling](https://docs.databricks.com/en/compute/configure.html#autoscaling)

**Focus Areas**:
- How autoscaling responds to load
- Configuring aggressive vs conservative scaling
- Cost vs performance trade-offs

---

## Key Terminology

| Term | Definition |
|------|------------|
| **Driver Node** | Coordinates tasks, maintains SparkContext, collects results |
| **Worker Node** | Executes tasks, stores partitioned data |
| **Executor** | JVM process on worker that runs tasks |
| **All-Purpose Cluster** | Long-running cluster for interactive development |
| **Job Cluster** | Ephemeral cluster created/terminated per job |
| **Instance Pool** | Pre-warmed instances for faster cluster startup |
| **Spot Instance** | Spare cloud capacity at discounted pricing |
| **Photon** | Databricks native query engine for SQL/DataFrame |

---

## Cluster Type Selection Matrix

| Workload | Recommended Type | Reason |
|----------|------------------|--------|
| Notebook development | All-Purpose | Interactive, persistent |
| Scheduled ETL | Job Cluster | Cost-efficient, isolated |
| Ad-hoc SQL queries | SQL Warehouse | Optimized, serverless option |
| ML training | All-Purpose or Job | Depends on interactivity needs |
| Streaming | Job Cluster (long-running) | Dedicated resources |

---

## Architecture Diagram

```
┌─────────────────────────────────────────────────────┐
│                   DRIVER NODE                       │
│  ┌───────────────────────────────────────────────┐  │
│  │  SparkContext  │  DAG Scheduler  │  Results   │  │
│  └───────────────────────────────────────────────┘  │
└─────────────────────┬───────────────────────────────┘
                      │ Task Distribution
    ┌─────────────────┼─────────────────┐
    ▼                 ▼                 ▼
┌──────────┐    ┌──────────┐    ┌──────────┐
│ WORKER 1 │    │ WORKER 2 │    │ WORKER N │
│┌────────┐│    │┌────────┐│    │┌────────┐│
││Executor││    ││Executor││    ││Executor││
│└────────┘│    │└────────┘│    │└────────┘│
│ [Data]   │    │ [Data]   │    │ [Data]   │
└──────────┘    └──────────┘    └──────────┘
```

---

## Self-Assessment Questions

1. What is the role of the driver node vs worker nodes?
2. When should you use job clusters instead of all-purpose clusters?
3. How does autoscaling decide when to add or remove workers?
4. What are the benefits of using instance pools?
5. Why should the driver node be on-demand rather than Spot?

---

## Recommended Additional Reading

- [Databricks Runtime versions](https://docs.databricks.com/en/release-notes/runtime/index.html)
- [Cluster access modes](https://docs.databricks.com/en/compute/configure.html#access-modes)
- [Photon acceleration](https://docs.databricks.com/en/compute/photon.html)
- [Spot instances best practices](https://docs.databricks.com/en/compute/configure.html#spot-instances)

---

*Pre-reading materials for Databricks Platform Administration Training - Day 14*
