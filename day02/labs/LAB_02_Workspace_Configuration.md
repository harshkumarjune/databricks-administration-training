# Lab 02: Workspace Configuration Walkthrough

## Databricks Platform Administration Training
### Duration: 30 Minutes | Difficulty: Beginner

---

## Lab Overview

In this lab, you will explore the workspace Admin Console and document the current configuration state. This exercise builds familiarity with administrative interfaces and establishes a baseline understanding of your workspace setup.

### Learning Objectives

By the end of this lab, you will be able to:
- Navigate the Workspace Admin Console
- Review and document user and group configurations
- Explore cluster policies and compute settings
- Identify key workspace settings and their purposes

### Prerequisites

- Workspace Admin access (or ability to view Admin Console)
- Completed Lab 01 (Workspace Navigation)

---

## Part 1: Accessing the Admin Console (5 minutes)

### Task 1.1: Navigate to Admin Console

1. Log into your Databricks workspace

2. Access the Admin Console:
   - Click your **username** in the top-right corner
   - Select **Admin Console** (or **Admin Settings**)

   OR

   - Click **Settings** (gear icon)
   - Select **Admin Console**

3. You should see the Admin Console dashboard

**Checkpoint**: Confirm you can see the Admin Console main page.

| Verification | Status |
|--------------|--------|
| Can access Admin Console | ☐ Yes / ☐ No |
| See Users section | ☐ Yes / ☐ No |
| See Groups section | ☐ Yes / ☐ No |

> **Note**: If you don't have admin access, partner with someone who does or observe the instructor's screen.

---

## Part 2: Reviewing User Configuration (10 minutes)

### Task 2.1: Document User List

1. Click on **Users** in the Admin Console

2. Review the user list and document:

| Metric | Count |
|--------|-------|
| Total Users | |
| Active Users (logged in recently) | |
| Admin Users | |
| Service Principals | |

3. Find yourself in the user list and document your entitlements:

| Entitlement | Enabled? |
|-------------|----------|
| Workspace access | |
| Databricks SQL access | |
| Allow cluster creation | |
| Allow instance pool creation | |

### Task 2.2: Explore User Details

1. Click on any user (or yourself) to view details

2. Document the available information:

| Information Available | Notes |
|-----------------------|-------|
| Email | |
| Display Name | |
| Groups | |
| Entitlements | |
| Last Login | |

### Task 2.3: Review Admin Privileges

1. Identify users with Admin privileges

2. Document:

| Question | Answer |
|----------|--------|
| How many workspace admins? | |
| Are admins managed via groups? | |

---

## Part 3: Reviewing Group Configuration (5 minutes)

### Task 3.1: List Groups

1. Click on **Groups** in the Admin Console

2. Document existing groups:

| Group Name | Members | Purpose |
|------------|---------|---------|
| admins | | Built-in admin group |
| users | | All workspace users |
| | | |
| | | |

### Task 3.2: Explore Group Details

1. Click on a group to view its members

2. Document:

| Question | Answer |
|----------|--------|
| Can you add members to groups? | |
| Can you create new groups? | |
| Are groups synced from IdP? | |

### Task 3.3: Best Practice Check

Evaluate against best practices:

| Best Practice | Current State | Notes |
|---------------|---------------|-------|
| Permissions assigned to groups | ☐ Yes / ☐ No | |
| Meaningful group names | ☐ Yes / ☐ No | |
| Groups documented | ☐ Yes / ☐ No | |

---

## Part 4: Reviewing Compute Configuration (5 minutes)

### Task 4.1: Explore Cluster Policies

1. Navigate to **Compute** → **Cluster Policies** (if available)

2. Document existing policies:

| Policy Name | Restrictions | Who Can Use |
|-------------|--------------|-------------|
| | | |
| | | |

> **Note**: If no cluster policies exist, document that finding.

### Task 4.2: Review Instance Pools

1. Navigate to **Compute** → **Instance Pools** (if available)

2. Document:

| Pool Name | Instance Type | Min/Max Instances |
|-----------|---------------|-------------------|
| | | |
| | | |

### Task 4.3: SQL Warehouses Overview

1. Navigate to **SQL Warehouses**

2. Document configured warehouses:

| Warehouse Name | Size | Type | State |
|----------------|------|------|-------|
| | | Classic/Serverless | |
| | | | |

---

## Part 5: Reviewing Workspace Settings (5 minutes)

### Task 5.1: General Settings

1. Navigate to **Workspace Settings** (or Settings → Workspace)

2. Document key settings:

| Setting | Current Value |
|---------|---------------|
| Workspace Name | |
| Region | |
| Cloud Provider | |

### Task 5.2: Security Settings

1. Review security-related settings:

| Setting | Current Value | Notes |
|---------|---------------|-------|
| Personal Access Tokens enabled | | |
| Maximum token lifetime | | |
| IP Access Lists configured | | |

### Task 5.3: Feature Settings

1. Review enabled features:

| Feature | Enabled? |
|---------|----------|
| Repos (Git integration) | |
| Serverless compute | |
| Unity Catalog | |

---

## Lab Summary Document

Complete this summary to document your workspace configuration:

### Workspace Overview

| Property | Value |
|----------|-------|
| Workspace Name | |
| Cloud Provider | |
| Region | |
| Total Users | |
| Total Groups | |

### Administrative Structure

| Question | Answer |
|----------|--------|
| How many workspace admins? | |
| Is SCIM configured? | |
| Are there custom groups? | |

### Compute Configuration

| Question | Answer |
|----------|--------|
| Cluster policies in use? | |
| Instance pools configured? | |
| SQL warehouses available? | |

### Security Posture

| Question | Answer |
|----------|--------|
| Token lifetime restricted? | |
| IP access lists enabled? | |
| Audit logging enabled? | |

### Recommendations

Based on your exploration, list any improvements you'd recommend:

1. _____________________________________
2. _____________________________________
3. _____________________________________

---

## Validation Checklist

- [ ] Accessed Admin Console successfully
- [ ] Documented user count and types
- [ ] Reviewed group configuration
- [ ] Explored compute policies/pools
- [ ] Reviewed workspace settings
- [ ] Completed summary document

---

## Discussion Questions

1. What surprised you about the current configuration?

2. Are permissions well-organized (groups vs individuals)?

3. What security improvements would you recommend?

4. How does this workspace compare to your expectations?

---

## Next Steps

- Review Day 2 slides for concepts covered
- Complete the Day 2 quiz
- Read pre-materials for Day 3: User, Group & Role Management

---

*Lab Version: 2.0 | Databricks Platform Administration Training - Day 2*
