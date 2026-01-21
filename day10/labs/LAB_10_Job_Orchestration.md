# Lab 10: Job Orchestration & CI/CD

## Databricks Platform Administration Training
### Duration: 45 Minutes | Difficulty: Intermediate

---

## Lab Overview

Create and manage Databricks jobs and workflows, configure scheduling and triggers, and explore CI/CD deployment patterns.

### Learning Objectives

- Create single and multi-task workflows
- Configure job triggers and schedules
- Set up notifications and alerts
- Work with Databricks Asset Bundles
- Deploy jobs using the CLI

---

## Part 1: Create Single-Task Job (10 minutes)

### Task 1.1: Create Notebook for Job

1. Go to **Workspace** → Create new notebook
2. Name it: `job_lab_etl`
3. Add the following code:

```python
# Cell 1: Get parameters
dbutils.widgets.text("env", "dev")
dbutils.widgets.text("date", "")

env = dbutils.widgets.get("env")
run_date = dbutils.widgets.get("date") or str(spark.sql("SELECT current_date()").collect()[0][0])

print(f"Environment: {env}")
print(f"Run Date: {run_date}")
```

```python
# Cell 2: Create sample data
data = [
    (1, "Product A", 100, run_date),
    (2, "Product B", 200, run_date),
    (3, "Product C", 150, run_date)
]

df = spark.createDataFrame(data, ["id", "product", "quantity", "date"])
df.show()
```

```python
# Cell 3: Write output
output_path = f"/tmp/job_lab/{env}/output_{run_date.replace('-', '')}"
df.write.mode("overwrite").parquet(output_path)
print(f"Data written to: {output_path}")
```

4. Save the notebook

### Task 1.2: Create Job

1. Navigate to **Workflows** in the left sidebar
2. Click **Create Job**
3. Configure:

| Setting | Value |
|---------|-------|
| Job Name | `lab-etl-job` |
| Task Name | `extract_transform` |
| Type | Notebook |
| Source | Workspace |
| Path | `/Users/{your-email}/job_lab_etl` |

4. Under **Cluster**:
   - Select **New job cluster** (or existing cluster for testing)
   - Choose smallest available instance type

5. Under **Parameters**:
   - Add: `env` = `dev`

6. Click **Create**

### Task 1.3: Run and Monitor Job

1. Click **Run now**
2. Observe the run in progress
3. After completion, review:
   - Run duration
   - Cluster used
   - Output logs
4. Check the output path for written data

---

## Part 2: Create Multi-Task Workflow (15 minutes)

### Task 2.1: Create Additional Notebooks

**Notebook 1: `job_lab_extract`**
```python
# Extract data
dbutils.widgets.text("source", "sales")
source = dbutils.widgets.get("source")

print(f"Extracting from source: {source}")

# Simulate extraction
data = [(i, f"record_{i}", i * 10) for i in range(1, 101)]
df = spark.createDataFrame(data, ["id", "name", "value"])

# Write to staging
df.write.mode("overwrite").parquet(f"/tmp/job_lab/staging/{source}")
print(f"Extracted {df.count()} records")

# Return value for downstream tasks
dbutils.notebook.exit(f"{df.count()}")
```

**Notebook 2: `job_lab_transform`**
```python
# Transform data
dbutils.widgets.text("source", "sales")
source = dbutils.widgets.get("source")

# Read from staging
df = spark.read.parquet(f"/tmp/job_lab/staging/{source}")

# Apply transformations
df_transformed = df.withColumn("value_doubled", df.value * 2)

# Write to processed
df_transformed.write.mode("overwrite").parquet(f"/tmp/job_lab/processed/{source}")
print(f"Transformed {df_transformed.count()} records")

dbutils.notebook.exit("success")
```

**Notebook 3: `job_lab_load`**
```python
# Load to final table
dbutils.widgets.text("source", "sales")
source = dbutils.widgets.get("source")

# Read processed data
df = spark.read.parquet(f"/tmp/job_lab/processed/{source}")

# Create or replace table
df.createOrReplaceTempView("final_data")
spark.sql(f"""
    CREATE TABLE IF NOT EXISTS default.lab_final_{source}
    USING DELTA
    AS SELECT * FROM final_data
""")

print(f"Loaded {df.count()} records to final table")
dbutils.notebook.exit("success")
```

### Task 2.2: Create Multi-Task Job

1. Go to **Workflows** → **Create Job**
2. Job Name: `lab-etl-workflow`

3. **Add Task 1: Extract**
   - Task name: `extract`
   - Type: Notebook
   - Path: `job_lab_extract`
   - Parameters: `source` = `sales`

4. **Add Task 2: Transform**
   - Click **Add task**
   - Task name: `transform`
   - Type: Notebook
   - Path: `job_lab_transform`
   - Parameters: `source` = `sales`
   - **Depends on**: `extract`

5. **Add Task 3: Load**
   - Click **Add task**
   - Task name: `load`
   - Type: Notebook
   - Path: `job_lab_load`
   - Parameters: `source` = `sales`
   - **Depends on**: `transform`

6. Click **Create**

### Task 2.3: Run Workflow

1. Click **Run now**
2. Observe the DAG visualization
3. Watch tasks execute sequentially
4. Review logs for each task

---

## Part 3: Configure Triggers & Notifications (10 minutes)

### Task 3.1: Add Schedule Trigger

1. Select your `lab-etl-workflow` job
2. Click **Triggers** → **Add trigger**
3. Configure schedule:
   - Trigger type: **Scheduled**
   - Schedule: Custom cron
   - Cron expression: `0 0 8 * * ?` (Daily at 8 AM)
   - Timezone: Your timezone

4. Save the trigger (you can disable it after testing)

### Task 3.2: Configure Notifications

1. In the job settings, go to **Email notifications**
2. Add notifications:
   - On start: (optional)
   - On success: your email
   - On failure: your email

3. Save settings

### Task 3.3: Configure Retry Policy

1. Click on a task in the job
2. Under **Task settings**:
   - Max retries: 2
   - Min retry interval: 60 seconds
   - Timeout: 3600 seconds (1 hour)

3. Save settings

---

## Part 4: Job Permissions (5 minutes)

### Task 4.1: View Job Permissions

1. Select your job
2. Click the **Permissions** button (top right)
3. Review current permissions:

| Principal | Permission |
|-----------|------------|
| Owner | IS_OWNER |
| (others) | |

### Task 4.2: Add Permissions

1. Click **Add**
2. Add a group with CAN_MANAGE_RUN permission
3. Save

### Task 4.3: Configure Run As

1. In job settings, find **Run as** option
2. Options:
   - Service principal (recommended for production)
   - Owner's identity
3. Note: Service principal must have access to notebooks and data

---

## Part 5: Databricks Asset Bundles (5 minutes)

### Task 5.1: Create Bundle Configuration

Create a file named `databricks.yml`:

```yaml
bundle:
  name: lab-etl-bundle

workspace:
  host: ${DATABRICKS_HOST}

resources:
  jobs:
    lab_etl_job:
      name: "Lab ETL Job (Bundle)"
      tasks:
        - task_key: extract
          notebook_task:
            notebook_path: ./notebooks/job_lab_extract
            base_parameters:
              source: sales
          new_cluster:
            spark_version: "13.3.x-scala2.12"
            node_type_id: "i3.xlarge"
            num_workers: 1

        - task_key: transform
          depends_on:
            - task_key: extract
          notebook_task:
            notebook_path: ./notebooks/job_lab_transform
            base_parameters:
              source: sales
          new_cluster:
            spark_version: "13.3.x-scala2.12"
            node_type_id: "i3.xlarge"
            num_workers: 1

targets:
  dev:
    workspace:
      host: ${DATABRICKS_HOST}
    default: true

  prod:
    workspace:
      host: ${DATABRICKS_HOST}
```

### Task 5.2: Deploy Bundle (CLI)

```bash
# Validate bundle
databricks bundle validate

# Deploy to dev target
databricks bundle deploy --target dev

# Run the deployed job
databricks bundle run lab_etl_job --target dev
```

---

## Part 6: Cleanup

### Task 6.1: Clean Up Resources

1. **Delete test jobs**:
   - Go to Workflows
   - Select and delete `lab-etl-job` and `lab-etl-workflow`

2. **Clean up data**:
```python
dbutils.fs.rm("/tmp/job_lab", recurse=True)
```

3. **Drop test table**:
```sql
DROP TABLE IF EXISTS default.lab_final_sales;
```

---

## Lab Validation Checklist

- [ ] Created single-task job with notebook
- [ ] Successfully ran job and verified output
- [ ] Created multi-task workflow with dependencies
- [ ] Observed DAG execution
- [ ] Configured schedule trigger
- [ ] Set up email notifications
- [ ] Configured retry policy
- [ ] Reviewed job permissions
- [ ] Created Asset Bundle configuration (optional)
- [ ] Cleaned up resources

---

## Challenge Exercise

Build a complete ETL pipeline:

1. **Create a parameterized workflow** that:
   - Accepts `date` parameter
   - Extracts data from multiple sources in parallel
   - Transforms and joins data
   - Loads to Delta table
   - Sends notification on completion

2. **Configure file arrival trigger**:
   - Monitor a cloud storage path
   - Trigger job when new files arrive

3. **Implement CI/CD**:
   - Store notebooks in Git
   - Create GitHub Actions workflow
   - Deploy to dev on PR, to prod on merge

---

## Lab Summary

You learned:
1. Creating single and multi-task jobs
2. Configuring task dependencies (DAG)
3. Setting up schedule and trigger options
4. Configuring notifications and retries
5. Managing job permissions
6. Working with Databricks Asset Bundles

---

*Lab Version: 2.0 | Databricks Platform Administration Training - Day 10*
