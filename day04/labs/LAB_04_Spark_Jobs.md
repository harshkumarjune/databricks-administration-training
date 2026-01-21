# Lab 04: Run Spark Jobs & Review Execution

## Databricks Platform Administration Training
### Duration: 60 Minutes | Difficulty: Intermediate

---

## Lab Overview

In this lab, you will run Spark jobs and explore the execution metrics from an administrator's perspective. You'll learn to interpret the Spark UI and cluster metrics to understand job performance.

### Learning Objectives

- Run Spark jobs on a Databricks cluster
- Navigate the Spark UI
- Interpret job, stage, and task metrics
- Identify potential performance issues
- Review cluster resource utilization

---

## Part 1: Cluster Setup (10 minutes)

### Task 1.1: Create or Attach to Cluster

1. Navigate to **Compute** in the sidebar

2. Either:
   - Use an existing running cluster, OR
   - Create a new cluster with these settings:

| Setting | Value |
|---------|-------|
| Name | `lab04-spark-exploration` |
| Runtime | Latest LTS (e.g., 14.3 LTS) |
| Node Type | Standard_DS3_v2 or similar |
| Workers | 2 (fixed) |
| Auto-termination | 30 minutes |

3. Wait for cluster to start

### Task 1.2: Create Lab Notebook

1. Navigate to **Workspace** → Your folder

2. Create a new notebook:
   - Name: `Lab04-Spark-Jobs`
   - Language: Python

3. Attach to your cluster

---

## Part 2: Run Basic Spark Jobs (15 minutes)

### Task 2.1: Simple Transformation and Action

Add and run these cells:

**Cell 1: Create Sample Data**
```python
# Create a simple DataFrame
data = [(i, f"Name_{i}", i * 10) for i in range(1, 10001)]
df = spark.createDataFrame(data, ["id", "name", "value"])

# Show first 5 rows (ACTION - triggers execution)
df.show(5)
```

**Cell 2: Transformations (Lazy)**
```python
# These are transformations - no execution yet
filtered_df = df.filter(df.value > 500)
grouped_df = filtered_df.groupBy("name").sum("value")

# Check the execution plan (no data movement yet)
grouped_df.explain()
```

**Cell 3: Trigger Execution**
```python
# Action triggers execution
result = grouped_df.count()
print(f"Result count: {result}")
```

### Task 2.2: Document Observations

After running, note:

| Observation | Value |
|-------------|-------|
| Time for Cell 1 | |
| Time for Cell 3 | |
| Did Cell 2 take time? | |

---

## Part 3: Explore Spark UI (20 minutes)

### Task 3.1: Access Spark UI

1. While cluster is running, click on the cluster name

2. Go to **Apps** tab → **Spark UI**

3. You should see the Spark History Server

### Task 3.2: Jobs Tab

1. Click on **Jobs** tab

2. Find the jobs from your notebook runs

3. Document:

| Job ID | Description | Duration | Stages |
|--------|-------------|----------|--------|
| | | | |
| | | | |

### Task 3.3: Stages Tab

1. Click on **Stages** tab

2. Find a completed stage and click on it

3. Document:

| Metric | Value |
|--------|-------|
| Stage ID | |
| Duration | |
| Tasks (Total/Succeeded/Failed) | |
| Shuffle Read | |
| Shuffle Write | |

### Task 3.4: Task Details

1. In the stage details, scroll to the task table

2. Examine task distribution:

| Metric | Min | Max | Median |
|--------|-----|-----|--------|
| Duration | | | |
| GC Time | | | |
| Shuffle Read | | | |

**Question**: Is there significant variance between min and max? (This could indicate data skew)

---

## Part 4: Run a Job with Shuffle (15 minutes)

### Task 4.1: Create Shuffle-Heavy Job

```python
# Create two DataFrames for join
df1 = spark.range(100000).withColumn("key", (col("id") % 100).cast("int"))
df2 = spark.range(1000).withColumnRenamed("id", "key2").withColumn("key", col("key2") % 100)

# Join operation (causes shuffle)
joined = df1.join(df2, "key")

# Trigger execution
joined.count()
```

### Task 4.2: Analyze the Join

1. Return to Spark UI → Jobs

2. Find the join job

3. How many stages does it have?

| Stage | Operation | Shuffle Read | Shuffle Write |
|-------|-----------|--------------|---------------|
| 1 | | | |
| 2 | | | |
| 3 | | | |

### Task 4.3: SQL Tab Analysis

1. Go to **SQL** tab in Spark UI

2. Find the query for your join

3. Click to see the query plan visualization

4. Screenshot or note the plan structure

---

## Part 5: Executor Metrics (10 minutes)

### Task 5.1: Review Executors Tab

1. Go to **Executors** tab

2. Document executor status:

| Executor | Address | Status | RDD Blocks | Memory Used | Disk Used |
|----------|---------|--------|------------|-------------|-----------|
| driver | | | | | |
| 0 | | | | | |
| 1 | | | | | |

### Task 5.2: Cluster Metrics

1. Return to the cluster page

2. Click on **Metrics** tab

3. Review the charts:

| Metric | Observation |
|--------|-------------|
| CPU Utilization | |
| Memory Usage | |
| Network I/O | |

---

## Lab Validation Checklist

- [ ] Created and ran basic Spark jobs
- [ ] Accessed Spark UI
- [ ] Reviewed Jobs tab
- [ ] Analyzed Stages and Tasks
- [ ] Ran shuffle-heavy job (join)
- [ ] Reviewed executor metrics
- [ ] Checked cluster metrics

---

## Challenge Exercise (Optional)

### Identify Performance Issues

Run this intentionally problematic code and diagnose the issues:

```python
# Problematic code - can you identify why?
df = spark.range(10000000)
result = df.repartition(1).collect()  # Don't actually run collect() on large data!
```

**Questions:**
1. What's wrong with `repartition(1)`?
2. Why is `collect()` dangerous on large datasets?
3. How would you fix this code?

---

## Lab Summary

In this lab, you:

1. Ran Spark jobs and observed lazy evaluation
2. Navigated the Spark UI to analyze execution
3. Understood jobs, stages, and tasks
4. Identified shuffle operations
5. Reviewed resource utilization

### Key Admin Insights

- Use Spark UI to diagnose slow jobs
- Look for task skew (uneven distribution)
- Monitor shuffle sizes for joins
- Check executor memory and GC time

---

*Lab Version: 2.0 | Databricks Platform Administration Training - Day 4*
