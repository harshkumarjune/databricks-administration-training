# Lab 15: Cluster Policies & SQL Warehouses
## Databricks Platform Administration Training

**Duration:** 45 minutes
**Difficulty:** Intermediate-Advanced
**Prerequisites:** Day 14 completed

---

## Lab Overview

In this lab, you will create cluster policies to enforce governance rules and configure SQL warehouses for analytics workloads. You'll implement real-world policies that control costs and standardize configurations.

---

## Learning Objectives

By completing this lab, you will be able to:
- Create cluster policies with various constraint types
- Enforce mandatory tags for cost allocation
- Configure SQL warehouses with appropriate sizing
- Set up warehouse auto-scaling and permissions

---

## Part 1: Creating Cluster Policies (20 minutes)

### Task 1.1: Create a Development Policy

1. Navigate to **Compute** → **Policies** tab
2. Click **Create Policy**
3. Name: `lab15-dev-policy-<your-initials>`
4. Add the following policy definition:

```json
{
  "spark_version": {
    "type": "regex",
    "pattern": "^14\\.[0-9]+\\.x-scala2\\.12$",
    "defaultValue": "14.3.x-scala2.12"
  },
  "node_type_id": {
    "type": "allowlist",
    "values": [
      "Standard_DS3_v2",
      "Standard_DS4_v2",
      "Standard_E4ds_v4"
    ],
    "defaultValue": "Standard_DS3_v2"
  },
  "driver_node_type_id": {
    "type": "fixed",
    "value": "Standard_DS3_v2",
    "hidden": true
  },
  "num_workers": {
    "type": "range",
    "minValue": 1,
    "maxValue": 4,
    "defaultValue": 2
  },
  "autotermination_minutes": {
    "type": "range",
    "minValue": 10,
    "maxValue": 60,
    "defaultValue": 30
  },
  "custom_tags.Team": {
    "type": "unlimited",
    "isOptional": false
  },
  "custom_tags.Environment": {
    "type": "fixed",
    "value": "development"
  }
}
```

5. Click **Create**

### Task 1.2: Test the Policy

1. Go to **Compute** → **Create Cluster**
2. Select your `lab15-dev-policy-<your-initials>` policy
3. Notice how the options are now constrained:
   - Runtime versions are limited
   - Worker count has max of 4
   - Team tag is required
4. Try to change the Environment tag - notice it's fixed

**Question:** What happens if you try to enter more than 4 workers?

---

## Part 2: Production Policy (10 minutes)

### Task 2.1: Create a Production Policy

Create a new policy for production workloads:

1. Name: `lab15-prod-policy-<your-initials>`
2. Definition:

```json
{
  "spark_version": {
    "type": "fixed",
    "value": "14.3.x-scala2.12",
    "hidden": true
  },
  "node_type_id": {
    "type": "fixed",
    "value": "Standard_E8ds_v4"
  },
  "driver_node_type_id": {
    "type": "fixed",
    "value": "Standard_E4ds_v4"
  },
  "num_workers": {
    "type": "range",
    "minValue": 4,
    "maxValue": 20
  },
  "autoscale.min_workers": {
    "type": "range",
    "minValue": 4,
    "maxValue": 20
  },
  "autoscale.max_workers": {
    "type": "range",
    "minValue": 4,
    "maxValue": 20
  },
  "autotermination_minutes": {
    "type": "fixed",
    "value": 0,
    "hidden": true
  },
  "custom_tags.Environment": {
    "type": "fixed",
    "value": "production"
  },
  "custom_tags.CostCenter": {
    "type": "regex",
    "pattern": "^CC-[0-9]{4}$",
    "isOptional": false
  }
}
```

### Task 2.2: Compare Policy Behaviors

| Aspect | Dev Policy | Prod Policy |
|--------|------------|-------------|
| Runtime | Regex pattern | Fixed |
| Max Workers | 4 | 20 |
| Auto-termination | 10-60 min | Disabled |
| Required Tags | Team | CostCenter |

---

## Part 3: SQL Warehouse Configuration (15 minutes)

### Task 3.1: Create a SQL Warehouse

1. Navigate to **SQL Warehouses**
2. Click **Create SQL Warehouse**
3. Configure:
   - **Name:** `lab15-analytics-wh-<your-initials>`
   - **Size:** Small
   - **Auto Stop:** 15 minutes
   - **Scaling:** Min 1, Max 2 clusters
   - **Type:** Pro (or Serverless if available)

4. Click **Create**

### Task 3.2: Test Warehouse Functionality

1. Wait for the warehouse to start
2. Go to **SQL Editor**
3. Select your warehouse
4. Run a simple query:

```sql
-- Test query
SELECT 1 as test_column;

-- Query sample data (if available)
SELECT * FROM samples.nyctaxi.trips LIMIT 10;
```

### Task 3.3: Review Query History

1. Navigate to **Query History**
2. Find your recent queries
3. Review:
   - Execution time
   - Rows returned
   - Query status

---

## Part 4: Warehouse Permissions (Optional)

### Task 4.1: Configure Warehouse Permissions

If you have admin access:

1. Click on your warehouse
2. Go to **Permissions** tab
3. Add a permission:
   - Principal: A group (e.g., `data_analysts`)
   - Permission: CAN USE
4. Review the permission hierarchy

---

## Cleanup

1. **Stop** your SQL warehouse
2. Keep cluster policies (they don't incur cost)

---

## Lab Validation Checklist

- [ ] Created development cluster policy with constraints
- [ ] Created production cluster policy with stricter controls
- [ ] Verified policy enforcement when creating clusters
- [ ] Created and tested a SQL warehouse
- [ ] Ran queries and reviewed query history
- [ ] Stopped warehouse to avoid costs

---

## Discussion Questions

1. How do cluster policies help with cost control?
2. What's the difference between `allowlist` and `regex` policy types?
3. When would you use a Pro warehouse vs Serverless?
4. How do warehouse scaling clusters affect concurrency?

---

## Assignment (Optional - Advanced)

**Compute Governance Strategy**

Design a complete compute governance strategy for a company with:
- 50 data engineers (need flexible development)
- 20 data scientists (need GPU and ML libraries)
- 100 analysts (need SQL access only)
- 5 platform admins

Create:
1. Three cluster policies (Dev, ML, Production)
2. Two SQL warehouse configurations (Ad-hoc, BI Dashboards)
3. Permission matrix showing who can use what

Submit as a markdown document with JSON policy definitions.

---

*Lab Version: 2.0 | Day 15 - Cluster Policies & SQL Warehouses*
