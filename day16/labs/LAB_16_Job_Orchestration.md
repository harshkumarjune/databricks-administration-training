# Lab 16: Job Orchestration & Workflows
## Databricks Platform Administration Training

**Duration:** 45 minutes
**Difficulty:** Intermediate
**Prerequisites:** Days 14-15 completed

---

## Lab Overview

In this lab, you will create multi-task workflows, configure job scheduling, and implement retry policies. You'll build a realistic ETL workflow with task dependencies and notifications.

---

## Learning Objectives

By completing this lab, you will be able to:
- Create multi-task jobs with dependencies
- Configure CRON-based scheduling
- Implement retry and timeout policies
- Set up job notifications and alerts

---

## Part 1: Create a Simple Job (10 minutes)

### Task 1.1: Create a Notebook for the Job

1. Navigate to **Workspace**
2. Create a new folder: `lab16_workflows`
3. Create a notebook: `01_extract_data`
4. Add the following code:

```python
# 01_extract_data
# Simulates data extraction

from datetime import datetime

# Log start
print(f"Extract started at: {datetime.now()}")

# Simulate extraction (create sample data)
data = [
    {"id": 1, "name": "Alice", "amount": 100},
    {"id": 2, "name": "Bob", "amount": 200},
    {"id": 3, "name": "Charlie", "amount": 150}
]

df = spark.createDataFrame(data)

# Save to Delta table
df.write.mode("overwrite").saveAsTable("lab16_extracted_data")

print(f"Extract completed: {df.count()} rows")
print(f"Extract finished at: {datetime.now()}")
```

### Task 1.2: Create a Basic Job

1. Navigate to **Workflows** → **Jobs**
2. Click **Create Job**
3. Configure:
   - **Task name:** `extract`
   - **Type:** Notebook
   - **Source:** Workspace
   - **Path:** Select your `01_extract_data` notebook
   - **Cluster:** Create new job cluster (2 workers, Standard runtime)
4. Name the job: `lab16-etl-pipeline-<your-initials>`
5. Click **Create**

---

## Part 2: Build Multi-Task Workflow (15 minutes)

### Task 2.1: Create Additional Notebooks

Create two more notebooks in `lab16_workflows`:

**02_transform_data:**
```python
# 02_transform_data
# Applies transformations

from datetime import datetime
from pyspark.sql.functions import col, upper

print(f"Transform started at: {datetime.now()}")

# Read extracted data
df = spark.table("lab16_extracted_data")

# Apply transformations
df_transformed = df.withColumn("name_upper", upper(col("name"))) \
                   .withColumn("amount_with_tax", col("amount") * 1.1)

# Save transformed data
df_transformed.write.mode("overwrite").saveAsTable("lab16_transformed_data")

print(f"Transform completed: {df_transformed.count()} rows")
print(f"Transform finished at: {datetime.now()}")
```

**03_load_data:**
```python
# 03_load_data
# Loads data to final destination

from datetime import datetime

print(f"Load started at: {datetime.now()}")

# Read transformed data
df = spark.table("lab16_transformed_data")

# Simulate load to final destination
df.write.mode("overwrite").saveAsTable("lab16_final_data")

# Validate
final_count = spark.table("lab16_final_data").count()
print(f"Load completed: {final_count} rows in final table")
print(f"Load finished at: {datetime.now()}")

# Set output for downstream tasks
dbutils.jobs.taskValues.set(key="row_count", value=final_count)
```

### Task 2.2: Add Tasks with Dependencies

1. Edit your job `lab16-etl-pipeline-<your-initials>`
2. Add a new task:
   - **Task name:** `transform`
   - **Type:** Notebook
   - **Path:** `02_transform_data`
   - **Depends on:** `extract`
   - **Cluster:** Use same job cluster as `extract`
3. Add another task:
   - **Task name:** `load`
   - **Type:** Notebook
   - **Path:** `03_load_data`
   - **Depends on:** `transform`
   - **Cluster:** Use same job cluster

Your workflow should look like:
```
extract → transform → load
```

---

## Part 3: Configure Scheduling (10 minutes)

### Task 3.1: Add CRON Schedule

1. In your job, click **Add Trigger**
2. Select **Scheduled**
3. Configure:
   - **Schedule:** `0 8 * * *` (Daily at 8 AM)
   - **Timezone:** Your timezone
4. **Note:** Don't enable the schedule yet (to avoid automatic runs)

### Task 3.2: Understand CRON Expressions

Review common CRON patterns:

| Expression | Meaning |
|------------|---------|
| `0 8 * * *` | Daily at 8 AM |
| `0 */6 * * *` | Every 6 hours |
| `0 8 * * 1-5` | Weekdays at 8 AM |
| `0 0 1 * *` | First day of month |

---

## Part 4: Configure Retry & Notifications (10 minutes)

### Task 4.1: Add Retry Policy

1. Click on the `transform` task
2. Expand **Advanced options**
3. Configure retry:
   - **Max retries:** 2
   - **Min retry interval:** 60 seconds

### Task 4.2: Add Job Timeout

1. In job settings, add:
   - **Job timeout:** 30 minutes

### Task 4.3: Configure Notifications (Optional)

1. Click **Edit notifications**
2. Add email notification:
   - **On failure:** Your email
   - **On success:** (leave blank)

---

## Part 5: Run and Monitor (Optional)

### Task 5.1: Run the Job

1. Click **Run now**
2. Monitor the execution in the **Runs** tab
3. Click on the run to see task-level details

### Task 5.2: Review Job Output

1. Click on each task to see:
   - Output logs
   - Duration
   - Cluster metrics

---

## Cleanup

1. **Cancel** any running jobs
2. **Delete** the schedule (or leave disabled)
3. Keep the job for reference

---

## Lab Validation Checklist

- [ ] Created three notebooks for ETL pipeline
- [ ] Built multi-task workflow with dependencies
- [ ] Configured CRON-based scheduling
- [ ] Added retry policies to tasks
- [ ] Set job-level timeout
- [ ] (Optional) Ran job and reviewed output

---

## Discussion Questions

1. When should you use "All Success" vs "At Least One Success" dependencies?
2. How do retry policies differ at task vs job level?
3. What are the cost implications of using job clusters vs existing clusters?
4. How would you handle a task that occasionally fails due to transient issues?

---

## Assignment (Optional - Intermediate)

**ETL Workflow Design**

Design an ETL workflow for the following scenario:

**Requirements:**
- Ingest data from 3 sources (API, S3, Database)
- All sources must complete before transformation starts
- Transformation has two parallel paths (fast and slow)
- Final load depends on both transformation paths
- Job should run daily at 2 AM
- Retry failed ingestion tasks up to 3 times
- Send Slack notification on failure

Create a workflow diagram and list all configuration settings.

---

*Lab Version: 2.0 | Day 16 - Job Orchestration & Workflows*
