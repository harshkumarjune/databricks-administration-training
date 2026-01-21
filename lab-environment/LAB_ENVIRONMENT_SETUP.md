# Databricks Platform Administration Training
## Lab Environment Setup Guide

---

## Overview

This document provides comprehensive setup instructions for both **trainers** and **participants** to configure the lab environment for hands-on exercises.

---

# Part 1: Trainer Setup Guide

## A. Pre-Training Environment Preparation (1-2 Weeks Before)

### 1. Databricks Account Setup

#### Option 1: Databricks Partner/Training Account
```
1. Request training workspace from Databricks Partner Portal
2. Specify: Region, Cloud Provider, Number of Participants
3. Timeline: 5-7 business days
```

#### Option 2: Customer's Existing Databricks Account
```
1. Create dedicated training workspace
2. Ensure Unity Catalog is enabled
3. Configure appropriate quotas and limits
4. Create training admin account
```

#### Option 3: Databricks Community Edition (Limited)
```
⚠️ Not recommended for full training
- Limited to single-user scenarios
- No Unity Catalog features
- Use only for demos/overview
```

### 2. Workspace Configuration Checklist

| Task | Status | Notes |
|------|--------|-------|
| Create training workspace | [ ] | Name: `training-admin-[date]` |
| Enable Unity Catalog | [ ] | Create metastore |
| Configure storage | [ ] | S3/ADLS/GCS bucket |
| Set up identity provider | [ ] | SCIM or manual |
| Create participant accounts | [ ] | [count] users |
| Set resource quotas | [ ] | DBU limits |
| Configure cluster policies | [ ] | Training policies |
| Create sample data | [ ] | Load training datasets |

### 3. Participant Account Provisioning

#### Bulk User Creation Script (Databricks CLI)
```bash
# Create users from CSV file
# users.csv format: email,display_name

while IFS=',' read -r email name; do
  databricks users create --user-name "$email" --display-name "$name"
done < users.csv
```

#### Account Naming Convention
```
Pattern: participant-[number]@training-domain.com
Example: participant-01@databricks-training.com
         participant-02@databricks-training.com
```

### 4. Training Data Setup

#### Required Datasets

| Dataset | Purpose | Size | Lab Used |
|---------|---------|------|----------|
| `sales_data` | General queries | 100MB | Labs 5, 6, 10 |
| `customer_pii` | Security demo | 50MB | Lab 6 (masking) |
| `streaming_events` | DLT pipeline | 200MB | Lab 12 |
| `audit_logs_sample` | Monitoring | 100MB | Lab 15 |

#### Data Loading Script
```python
# Run in Databricks notebook
# Creates training catalog and loads sample data

# Create training catalog
spark.sql("CREATE CATALOG IF NOT EXISTS training_data")
spark.sql("USE CATALOG training_data")

# Create schemas
spark.sql("CREATE SCHEMA IF NOT EXISTS raw")
spark.sql("CREATE SCHEMA IF NOT EXISTS processed")
spark.sql("CREATE SCHEMA IF NOT EXISTS analytics")

# Load sample data
# [Sample data loading code]
```

### 5. Cluster Policies for Training

#### Restrictive Training Policy (JSON)
```json
{
  "name": "Training-Standard-Policy",
  "definition": {
    "spark_version": {
      "type": "regex",
      "pattern": "13\\.[0-9]+\\.x-scala.*"
    },
    "node_type_id": {
      "type": "allowlist",
      "values": ["Standard_DS3_v2", "i3.xlarge", "n1-standard-4"]
    },
    "num_workers": {
      "type": "range",
      "maxValue": 4,
      "defaultValue": 2
    },
    "autotermination_minutes": {
      "type": "fixed",
      "value": 30
    },
    "custom_tags.training": {
      "type": "fixed",
      "value": "databricks-admin-course"
    }
  }
}
```

### 6. Cost Controls

| Control | Setting | Purpose |
|---------|---------|---------|
| DBU Budget | 100 DBU/day/participant | Prevent runaway costs |
| Auto-termination | 30 minutes | Idle cluster shutdown |
| Max Workers | 4 nodes | Limit compute |
| Spot Instances | 80% spot | Cost optimization |
| Daily Spending Limit | $50/participant | Hard stop |

---

# Part 2: Participant Setup Guide

## A. Pre-Training Checklist

### Step 1: Verify Access Credentials

You should have received:
- [ ] Workspace URL: `https://[workspace].cloud.databricks.com`
- [ ] Username (email): `participant-XX@...`
- [ ] Temporary password: `[provided separately]`

### Step 2: First-Time Login

1. **Navigate to Workspace URL**
   ```
   Open browser → Enter workspace URL → Click "Sign In"
   ```

2. **Enter Credentials**
   ```
   Username: [your assigned email]
   Password: [temporary password]
   ```

3. **Change Password (if prompted)**
   ```
   - Minimum 8 characters
   - Include uppercase, lowercase, number
   - Store securely
   ```

4. **Verify Access**
   - [ ] Can see Workspace home page
   - [ ] Can access Data Explorer
   - [ ] Can view Compute tab
   - [ ] Can access Admin Console (if admin)

### Step 3: Explore the Interface

#### Key Navigation Areas

| Area | Path | Purpose |
|------|------|---------|
| Workspace | Left sidebar → Workspace | Notebooks, files |
| Data | Left sidebar → Data | Catalogs, tables |
| Compute | Left sidebar → Compute | Clusters, pools |
| Workflows | Left sidebar → Workflows | Jobs, pipelines |
| SQL | Left sidebar → SQL | SQL Editor, warehouses |

### Step 4: Create Your First Cluster (Verification)

1. **Navigate to Compute**
   ```
   Compute → Create Cluster
   ```

2. **Configure Cluster**
   ```
   Name: [your-name]-verification
   Policy: Training-Standard-Policy
   Cluster Mode: Single Node
   Node Type: [As allowed by policy]
   Databricks Runtime: Latest LTS
   ```

3. **Start and Verify**
   ```
   Click "Create Cluster" → Wait for "Running" status
   Expected time: 3-5 minutes
   ```

4. **Run Verification Command**
   ```python
   # Create new notebook, attach to cluster, run:
   print(f"Spark Version: {spark.version}")
   print(f"Cluster Working!")
   spark.sql("SELECT 'Hello Databricks!' as message").show()
   ```

### Step 5: Access Training Materials

1. **Import Training Notebooks**
   ```
   Workspace → Users → [your username]
   Right-click → Import
   Select training materials ZIP file
   ```

2. **Verify Lab Access**
   - [ ] Day 1 Labs folder visible
   - [ ] Can open Lab 1.1 notebook
   - [ ] Sample data accessible

---

## B. Lab Environment Architecture

### Environment Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                    DATABRICKS ACCOUNT                       │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────────────────────────────────────────────┐   │
│  │              TRAINING WORKSPACE                      │   │
│  ├─────────────────────────────────────────────────────┤   │
│  │                                                      │   │
│  │  ┌───────────────┐    ┌───────────────┐            │   │
│  │  │  Participant  │    │  Participant  │  ...       │   │
│  │  │  Cluster 1    │    │  Cluster 2    │            │   │
│  │  └───────┬───────┘    └───────┬───────┘            │   │
│  │          │                    │                     │   │
│  │  ┌───────┴────────────────────┴───────┐            │   │
│  │  │         SHARED CLUSTER POOL         │            │   │
│  │  │         (Pre-warmed nodes)          │            │   │
│  │  └───────────────────────────────────────┘            │   │
│  │                                                      │   │
│  │  ┌─────────────────────────────────────────────┐   │   │
│  │  │            UNITY CATALOG                     │   │   │
│  │  │  ┌──────────┐  ┌──────────┐  ┌──────────┐  │   │   │
│  │  │  │ training │  │ sandbox  │  │ samples  │  │   │   │
│  │  │  │ _data    │  │ _[user]  │  │          │  │   │   │
│  │  │  └──────────┘  └──────────┘  └──────────┘  │   │   │
│  │  └─────────────────────────────────────────────┘   │   │
│  │                                                      │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │              CLOUD STORAGE                           │   │
│  │   S3 / ADLS / GCS Bucket for training data          │   │
│  └─────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

---

## C. Common Issues and Solutions

### Issue 1: Cannot Create Cluster

**Symptoms:** "Permission denied" or "Policy violation" error

**Solutions:**
1. Ensure you're using the assigned cluster policy
2. Check node type matches policy allowlist
3. Verify workspace permissions with trainer
4. Check if DBU quota is exceeded

### Issue 2: Cannot Access Data

**Symptoms:** "Table not found" or "Access denied"

**Solutions:**
1. Verify catalog is selected: `USE CATALOG training_data;`
2. Check schema permissions with trainer
3. Ensure cluster has proper IAM role attached
4. Refresh Data Explorer

### Issue 3: Cluster Startup Slow

**Symptoms:** Cluster taking > 10 minutes to start

**Solutions:**
1. Use cluster pool if available
2. Check spot instance availability
3. Use smaller node type
4. Contact trainer - may be cloud capacity issue

### Issue 4: Notebook Not Saving

**Symptoms:** Changes not persisting, "Save failed" error

**Solutions:**
1. Check browser console for errors
2. Try different browser
3. Export notebook locally as backup
4. Clear browser cache and retry

---

## D. Lab Resource Limits

### Per-Participant Limits

| Resource | Limit | Notes |
|----------|-------|-------|
| Concurrent Clusters | 2 | Including job clusters |
| Max Workers per Cluster | 4 | Policy enforced |
| Cluster Runtime | 30 min idle | Auto-terminate |
| Storage (Personal) | 10 GB | In workspace |
| Daily DBU | 100 DBU | Contact trainer if exceeded |

### Shared Resources

| Resource | Availability | Notes |
|----------|--------------|-------|
| Cluster Pool | Shared 10 nodes | Faster startup |
| Sample Data Catalog | Read-only | training_data |
| SQL Warehouse | Shared Serverless | For SQL labs |

---

## E. End-of-Day Cleanup

### Participant Cleanup Checklist

At the end of each training day:

1. **Terminate Active Clusters**
   ```
   Compute → [Your Cluster] → Terminate
   ```

2. **Stop SQL Warehouses (if started)**
   ```
   SQL → SQL Warehouses → Stop
   ```

3. **Save Work**
   ```
   Export important notebooks locally
   ```

4. **Clear Temporary Data**
   ```python
   # Run in notebook if you created temp tables
   spark.sql("DROP TABLE IF EXISTS sandbox_[your_name].temp_table")
   ```

---

*Document Version: 1.0 | Last Updated: January 2026*
