# Lab 09: Cluster & SQL Warehouse Setup

## Databricks Platform Administration Training
### Duration: 45 Minutes | Difficulty: Intermediate

---

## Lab Overview

Create and configure compute resources including all-purpose clusters, cluster policies, instance pools, and SQL warehouses.

### Learning Objectives

- Create and configure all-purpose clusters
- Define and apply cluster policies
- Set up instance pools
- Create and configure SQL warehouses
- Test compute resource configurations

---

## Part 1: Create All-Purpose Cluster (10 minutes)

### Task 1.1: Create Basic Cluster

1. Navigate to **Compute** in the left sidebar
2. Click **Create compute**
3. Configure the cluster:

| Setting | Value |
|---------|-------|
| Cluster Name | `lab-dev-cluster` |
| Policy | Unrestricted (or available policy) |
| Access Mode | Single User |
| Single User | (your email) |
| Databricks Runtime | Latest LTS (13.3 LTS or newer) |
| Node Type | (smallest available, e.g., i3.xlarge) |

4. Under **Advanced Options**:
   - Enable autoscaling: Min 1, Max 2 workers
   - Auto-termination: 30 minutes

5. Click **Create Compute**

### Task 1.2: Document Cluster Configuration

After cluster starts, document:

| Property | Value |
|----------|-------|
| Cluster ID | |
| Runtime Version | |
| Driver Type | |
| Worker Type | |
| Auto-termination | |

### Task 1.3: Explore Cluster UI

1. Click on your running cluster
2. Explore the tabs:
   - **Configuration** – View settings
   - **Metrics** – Monitor performance
   - **Driver Logs** – View driver output
   - **Spark UI** – Detailed Spark info
   - **Apps** – Installed libraries

---

## Part 2: Create Cluster Policy (10 minutes)

### Task 2.1: Navigate to Policies

1. Go to **Compute** → **Policies** tab
2. Click **Create policy**

### Task 2.2: Define Cost-Controlled Policy

Create a policy with these restrictions:

**Policy Name**: `cost-controlled-dev`

```json
{
  "spark_version": {
    "type": "regex",
    "pattern": "13\\.[0-9]+\\.x-scala.*|14\\.[0-9]+\\.x-scala.*",
    "defaultValue": "13.3.x-scala2.12"
  },
  "node_type_id": {
    "type": "allowlist",
    "values": [
      "i3.xlarge",
      "i3.2xlarge",
      "m5.large",
      "m5.xlarge"
    ],
    "defaultValue": "i3.xlarge"
  },
  "driver_node_type_id": {
    "type": "fixed",
    "value": "i3.xlarge"
  },
  "autotermination_minutes": {
    "type": "range",
    "minValue": 10,
    "maxValue": 60,
    "defaultValue": 30
  },
  "num_workers": {
    "type": "range",
    "minValue": 0,
    "maxValue": 4,
    "defaultValue": 1
  },
  "custom_tags.Environment": {
    "type": "fixed",
    "value": "development"
  }
}
```

3. Click **Create**

### Task 2.3: Assign Policy to Group

1. Select the `cost-controlled-dev` policy
2. Click **Permissions**
3. Add permission:
   - Group: `analysts` (or available group)
   - Permission: `CAN_USE`

### Task 2.4: Test Policy

1. Create a new cluster using the policy
2. Verify restrictions are enforced:
   - [ ] Limited instance types shown
   - [ ] Auto-termination range enforced
   - [ ] Worker count limited to max 4

---

## Part 3: Create Instance Pool (10 minutes)

### Task 3.1: Create Pool

1. Go to **Compute** → **Pools** tab
2. Click **Create pool**
3. Configure:

| Setting | Value |
|---------|-------|
| Pool Name | `lab-dev-pool` |
| Min Idle Instances | 1 |
| Max Capacity | 5 |
| Node Type | i3.xlarge (or available type) |
| Idle Instance Auto-termination | 30 minutes |

4. Under **Preloaded Spark Versions**, add:
   - Latest LTS runtime

5. Click **Create**

### Task 3.2: Create Cluster Using Pool

1. Create a new cluster
2. Under **Node Type**, select:
   - **Use pool**: `lab-dev-pool`
3. Note the faster start time when pool has idle instances

### Task 3.3: Monitor Pool Usage

1. Go back to the pool
2. View the **Usage** statistics:

| Metric | Value |
|--------|-------|
| Idle Instances | |
| Used Instances | |
| Pending Instances | |

---

## Part 4: Create SQL Warehouse (10 minutes)

### Task 4.1: Create Warehouse

1. Navigate to **SQL Warehouses** in the left sidebar
2. Click **Create SQL warehouse**
3. Configure:

| Setting | Value |
|---------|-------|
| Name | `lab-analytics-warehouse` |
| Cluster Size | 2X-Small (for testing) |
| Type | Serverless (if available) or Pro |
| Auto Stop | 15 minutes |

4. Under **Scaling**:
   - Min clusters: 1
   - Max clusters: 2

5. Click **Create**

### Task 4.2: View Connection Details

1. Click on your warehouse
2. Click **Connection details**
3. Document the connection information:

| Property | Value |
|----------|-------|
| Server Hostname | |
| Port | |
| HTTP Path | |

### Task 4.3: Test SQL Query

1. Click **Open query editor** (or go to SQL Editor)
2. Ensure your warehouse is selected
3. Run a test query:

```sql
-- Test query
SELECT current_timestamp() as current_time,
       current_user() as current_user,
       current_catalog() as catalog;

-- Sample data query
SELECT * FROM samples.nyctaxi.trips LIMIT 10;
```

### Task 4.4: Review Query History

1. Go to **Query History** in SQL Editor
2. Find your recent queries
3. Note the execution time and rows scanned

---

## Part 5: Warehouse Configuration (5 minutes)

### Task 5.1: Configure Query Routing (Optional)

If you have multiple warehouses, configure routing:

1. Go to **SQL Admin Console**
2. Configure default warehouse for users
3. Set up query routing rules

### Task 5.2: Configure Warehouse Permissions

1. Select your warehouse
2. Click **Permissions**
3. Add permission:
   - Group: `analysts`
   - Permission: `CAN_USE`

### Task 5.3: Generate Connection String

For BI tools, format the JDBC URL:

```
jdbc:databricks://{hostname}:443/default;transportMode=http;ssl=1;httpPath={http_path}
```

Example:
```
jdbc:databricks://adb-1234567890123456.cloud.databricks.com:443/default;transportMode=http;ssl=1;httpPath=/sql/1.0/warehouses/abc123def456
```

---

## Part 6: Cleanup

### Task 6.1: Terminate Test Resources

1. **Terminate cluster**:
   - Go to Compute → select `lab-dev-cluster` → Terminate

2. **Stop SQL warehouse**:
   - Go to SQL Warehouses → select `lab-analytics-warehouse` → Stop

3. **Optionally delete pool**:
   - Only if not needed for other tests

---

## Lab Validation Checklist

- [ ] Created all-purpose cluster with autoscaling
- [ ] Configured auto-termination for cost control
- [ ] Created cluster policy with restrictions
- [ ] Assigned policy to a group
- [ ] Tested policy enforcement
- [ ] Created instance pool
- [ ] Created cluster using the pool
- [ ] Created SQL warehouse
- [ ] Retrieved connection details
- [ ] Executed test SQL queries
- [ ] Configured warehouse permissions

---

## Challenge Exercise

### Create a Complete Compute Strategy

Design and implement compute resources for a team:

1. **Development Environment**:
   - Policy: Max 2 workers, 30 min auto-terminate
   - Pool: 2 min idle instances
   - Spot instances for workers

2. **Production ETL**:
   - Policy: LTS runtime only, Photon enabled
   - No auto-termination
   - On-demand instances

3. **Analytics**:
   - SQL Warehouse: Serverless, Medium
   - Auto-scale 1-4 clusters
   - 15 min auto-stop

Document your design:

| Environment | Compute Type | Policy | Cost Controls |
|-------------|--------------|--------|---------------|
| Development | | | |
| Production | | | |
| Analytics | | | |

---

## Lab Summary

You learned:
1. Creating and configuring all-purpose clusters
2. Defining cluster policies for governance
3. Setting up instance pools for fast starts
4. Creating SQL warehouses for analytics
5. Configuring compute permissions
6. Cost control strategies

---

*Lab Version: 2.0 | Databricks Platform Administration Training - Day 9*
