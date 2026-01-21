# Lab 03: User & Group Administration

## Databricks Platform Administration Training
### Duration: 60 Minutes | Difficulty: Intermediate

---

## Lab Overview

In this lab, you will create and manage users, groups, and permissions in a Databricks workspace. You'll practice the access management best practices covered in Day 3.

### Learning Objectives

By the end of this lab, you will be able to:
- Create users in a workspace
- Create and configure custom groups
- Assign users to groups
- Configure entitlements
- Verify permission inheritance

### Prerequisites

- Workspace Admin access
- Completed Day 2 Lab

---

## Part 1: User Management (20 minutes)

### Task 1.1: Review Current Users

1. Navigate to **Admin Console** → **Users**

2. Document current state:

| Metric | Count |
|--------|-------|
| Total users | |
| Admin users | |
| Users created today | |

### Task 1.2: Create Test Users

> **Note**: If you don't have email addresses to invite, use placeholder emails for this exercise (they won't receive invites).

1. Click **Add User**

2. Create three test users (or document how you would):

| User Email | Display Name | Purpose |
|------------|--------------|---------|
| engineer1@training.local | Engineer One | Data engineering |
| scientist1@training.local | Scientist One | Data science |
| analyst1@training.local | Analyst One | Business analytics |

3. For each user, configure initial entitlements:

| User | Workspace Access | SQL Access | Cluster Creation |
|------|------------------|------------|------------------|
| engineer1 | ✓ | ✓ | ✓ |
| scientist1 | ✓ | ✓ | ✓ |
| analyst1 | ✓ | ✓ | ✗ |

### Task 1.3: Verify User Creation

1. Confirm users appear in the user list

2. Click on each user to verify:
   - Entitlements are set correctly
   - No groups assigned yet
   - Not admin

---

## Part 2: Group Management (20 minutes)

### Task 2.1: Create Custom Groups

1. Navigate to **Admin Console** → **Groups**

2. Create the following groups:

| Group Name | Description |
|------------|-------------|
| `training-engineers` | Data engineering team |
| `training-scientists` | Data science team |
| `training-analysts` | Business analytics team |
| `training-compute-users` | Users allowed to create clusters |

3. For each group, click **Create Group** and enter:
   - Group name
   - Optionally add description in notes

### Task 2.2: Configure Group Hierarchy

1. Add `training-engineers` and `training-scientists` to `training-compute-users`:
   - Open `training-compute-users`
   - Click **Add members**
   - Select groups: `training-engineers`, `training-scientists`

2. This creates a hierarchy:
   ```
   training-compute-users
   ├── training-engineers
   └── training-scientists
   ```

### Task 2.3: Assign Users to Groups

1. Add users to their respective groups:

| User | Group |
|------|-------|
| engineer1 | training-engineers |
| scientist1 | training-scientists |
| analyst1 | training-analysts |

2. Verify assignments:
   - Open each user → check Groups tab
   - Open each group → verify Members

### Task 2.4: Document Group Configuration

| Group | Direct Members | Inherited Members | Total |
|-------|----------------|-------------------|-------|
| training-engineers | | | |
| training-scientists | | | |
| training-analysts | | | |
| training-compute-users | | | |

---

## Part 3: Entitlement Configuration (10 minutes)

### Task 3.1: Configure Group Entitlements

1. For `training-compute-users` group:
   - Open the group
   - Go to **Entitlements** tab
   - Enable **Allow cluster creation**

2. For `training-analysts` group:
   - Ensure **Databricks SQL access** is enabled
   - **Allow cluster creation** should be disabled

### Task 3.2: Verify Entitlement Inheritance

1. Check user `engineer1`:
   - Direct entitlements
   - Inherited from `training-engineers`
   - Inherited from `training-compute-users`

2. Document the effective permissions:

| User | Can Create Clusters | SQL Access | Source |
|------|---------------------|------------|--------|
| engineer1 | | | |
| scientist1 | | | |
| analyst1 | | | |

### Task 3.3: Test Permission Denial

1. Verify that `analyst1` cannot create clusters:
   - Log in as analyst1 (if possible)
   - Attempt to create a cluster
   - Should see permission denied or option unavailable

---

## Part 4: Admin Role Management (10 minutes)

### Task 4.1: Review Admin Group

1. Open the `admins` group

2. Document current members:

| Admin | Added Method |
|-------|--------------|
| | Direct / Inherited |
| | |

### Task 4.2: Create Platform Admin Group

1. Create a new group: `training-platform-admins`

2. Add this group to the `admins` group:
   - Open `admins` group
   - Add `training-platform-admins` as member

3. This means anyone in `training-platform-admins` becomes a workspace admin

### Task 4.3: Document Admin Hierarchy

```
admins (built-in)
└── training-platform-admins (custom)
    └── (future platform team members)
```

---

## Part 5: Cleanup and Documentation (Optional)

### Task 5.1: Clean Up Test Resources

If this is a shared training environment, remove test users and groups:

1. Remove test users (or mark for removal)
2. Keep groups if they'll be reused

### Task 5.2: Create Access Documentation

Document your configuration for future reference:

**User Management Policy:**
```
- Users are provisioned via [SCIM/Manual]
- Entitlements are managed via groups
- Admin access requires approval from [role]
```

**Group Structure:**
```
admins
├── training-platform-admins
│
training-compute-users
├── training-engineers
└── training-scientists
│
training-analysts (no cluster access)
```

---

## Lab Validation Checklist

### User Management
- [ ] Created (or documented) test users
- [ ] Configured user entitlements
- [ ] Verified user details

### Group Management
- [ ] Created custom groups
- [ ] Configured group hierarchy
- [ ] Assigned users to groups
- [ ] Documented group structure

### Entitlements
- [ ] Configured group-level entitlements
- [ ] Verified inheritance works
- [ ] Tested permission restrictions

### Admin Roles
- [ ] Reviewed admin group membership
- [ ] Created platform admin group
- [ ] Documented admin hierarchy

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Can't create users | Check if you have admin access |
| User not appearing | Refresh the page, check filters |
| Entitlements not inheriting | Check group membership is saved |
| Can't add group to group | Verify target group exists |

---

## Challenge Exercise (Optional)

### Scenario: Department Reorganization

The Data Science team is splitting into two sub-teams:
- ML Engineers (need cluster creation)
- ML Researchers (SQL access only)

**Tasks:**
1. Create new groups: `ml-engineers`, `ml-researchers`
2. Move `training-scientists` members appropriately
3. Update the group hierarchy
4. Ensure entitlements are correct

**Document your solution:**

---

## Lab Summary

In this lab, you practiced:

1. **User creation** and entitlement configuration
2. **Group management** with hierarchical structure
3. **Entitlement inheritance** through groups
4. **Admin role management** using groups

### Key Takeaways

- Groups simplify permission management at scale
- Entitlements inherit through group membership
- Use group hierarchy for logical organization
- Document your access structure

---

*Lab Version: 2.0 | Databricks Platform Administration Training - Day 3*
