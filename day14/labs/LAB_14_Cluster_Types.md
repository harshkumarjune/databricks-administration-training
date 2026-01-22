# Lab 14: Cluster Architecture & Types
## Databricks Platform Administration Training

**Duration:** 45 minutes
**Difficulty:** Intermediate
**Prerequisites:** Days 1-13 completed

---

## Lab Overview

In this lab, you will explore different cluster types, configure auto-scaling, and understand runtime version selection. By the end, you'll be able to select the right cluster configuration for various workloads.

---

## Learning Objectives

By completing this lab, you will be able to:
- Create and compare All-Purpose vs Job clusters
- Configure auto-scaling with appropriate limits
- Select appropriate Databricks Runtime versions
- Understand cluster access modes and their implications

---

## Part 1: Exploring Cluster Types (15 minutes)

### Task 1.1: Create an All-Purpose Cluster

1. Navigate to **Compute** in the left sidebar
2. Click **Create Cluster**
3. Configure the cluster:
   - **Name:** `lab14-all-purpose-<your-initials>`
   - **Policy:** (leave as Unrestricted for now)
   - **Access Mode:** Shared
   - **Databricks Runtime:** 14.3 LTS
   - **Node Type:** Standard_DS3_v2 (or equivalent)
   - **Workers:** Min: 1, Max: 4 (enable auto-scaling)
   - **Auto-termination:** 30 minutes

4. Click **Create Cluster** and wait for it to start

### Task 1.2: Review Cluster Configuration

While waiting, examine:
- What driver node type was automatically selected?
- What Spark configuration options are available?
- What tags are applied by default?

**Question:** Why might you choose Shared access mode over Single User?

---

## Part 2: Auto-scaling Configuration (10 minutes)

### Task 2.1: Understand Auto-scaling Behavior

1. Once your cluster is running, open the **Spark UI**
2. Navigate to the **Executors** tab
3. Note the current number of executors

### Task 2.2: Trigger Scale-up

1. Create a new notebook attached to your cluster
2. Run the following code to generate load:

```python
# Generate workload to trigger auto-scaling
from pyspark.sql.functions import rand, col

# Create a large dataset
df = spark.range(0, 100000000).withColumn("value", rand())

# Perform aggregation (will trigger tasks on workers)
result = df.groupBy((col("id") % 1000).alias("group")).count()
result.count()
```

3. While running, monitor the **Executors** tab
4. Observe how workers are added based on pending tasks

**Question:** How long did it take for additional workers to be added?

---

## Part 3: Runtime Version Comparison (10 minutes)

### Task 3.1: Compare Runtime Features

Review the following runtime options in the cluster creation UI:

| Runtime | Key Features | Use Case |
|---------|--------------|----------|
| Standard | Core Spark libraries | General ETL |
| ML | TensorFlow, PyTorch, scikit-learn | Machine Learning |
| Photon | Vectorized query engine | SQL workloads |
| GPU | CUDA support | Deep Learning |

### Task 3.2: Identify LTS Versions

1. In the cluster creation UI, look for versions marked **LTS**
2. Note the current LTS versions available

**Best Practice:** For production workloads, always use LTS versions for stability and longer support windows.

---

## Part 4: Access Modes Deep Dive (10 minutes)

### Task 4.1: Compare Access Modes

Create a table comparing access modes:

| Access Mode | Unity Catalog | User Isolation | Libraries | Use Case |
|-------------|---------------|----------------|-----------|----------|
| Single User | ✓ | Full | All | ML, custom libs |
| Shared | ✓ | Process-level | Cluster-installed | Team dev |
| No Isolation | ✗ | None | All | Legacy only |

### Task 4.2: Test Access Mode Behavior

If you have admin access:

1. Create a cluster with **Single User** access mode assigned to yourself
2. Notice that only you can attach notebooks to this cluster
3. Terminate the cluster when done

---

## Cleanup

1. **Terminate** your `lab14-all-purpose-<your-initials>` cluster
2. Do NOT delete the cluster (you may use it for reference)

---

## Lab Validation Checklist

- [ ] Created an All-Purpose cluster with auto-scaling
- [ ] Observed auto-scaling behavior under load
- [ ] Identified current LTS runtime versions
- [ ] Understand the difference between access modes
- [ ] Terminated clusters to avoid unnecessary costs

---

## Discussion Questions

1. When would you use a Job cluster instead of an All-Purpose cluster?
2. What are the cost implications of auto-scaling vs fixed-size clusters?
3. Why is Single User access mode required for certain ML workloads?
4. How does Photon runtime improve query performance?

---

## Assignment (Optional - Intermediate)

**Cluster Configuration Analysis**

Analyze the following scenario and recommend cluster configurations:

**Scenario:** Your company has three teams:
1. **Data Engineering** - Runs daily ETL jobs processing 100GB
2. **Data Science** - Develops ML models with custom Python libraries
3. **Business Analysts** - Runs ad-hoc SQL queries for reports

For each team, specify:
- Recommended cluster type (All-Purpose vs Job)
- Access mode
- Runtime version
- Auto-scaling configuration
- Auto-termination setting

Submit your recommendations as a markdown document.

---

*Lab Version: 2.0 | Day 14 - Cluster Architecture & Types*
