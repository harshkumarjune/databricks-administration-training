# Lab 08: Identity Configuration

## Databricks Platform Administration Training
### Duration: 45 Minutes | Difficulty: Intermediate

---

## Lab Overview

Explore identity management in Databricks, including account-level settings, groups, service principals, and authentication methods.

### Learning Objectives

- Navigate Account Console identity settings
- Create and manage groups
- Create and configure service principals
- Generate and test OAuth credentials
- Review identity-related audit logs

---

## Part 1: Explore Account Console Identity (10 minutes)

### Task 1.1: Access Account Console

1. Navigate to [accounts.cloud.databricks.com](https://accounts.cloud.databricks.com)
2. Sign in with your account admin credentials
3. Observe the main navigation sections

### Task 1.2: Review User Management

1. Click **User management** → **Users**
2. Document the current user inventory:

| Metric | Count |
|--------|-------|
| Total Users | |
| Active Users | |
| Pending Invitations | |

3. Click on a user to view their details
4. Note the available tabs: Overview, Groups, Roles, Workspaces

### Task 1.3: Review SSO Settings

1. Navigate to **Settings** → **Single sign-on**
2. Document the current SSO configuration:

| Setting | Value |
|---------|-------|
| SSO Enabled | Yes/No |
| Identity Provider | |
| Protocol (SAML/OIDC) | |
| Allow Password Login | Yes/No |

### Task 1.4: Review SCIM Settings

1. Navigate to **Settings** → **User provisioning**
2. Document SCIM configuration:

| Setting | Value |
|---------|-------|
| SCIM Enabled | Yes/No |
| SCIM Endpoint | |
| Token Status | Active/Expired |

---

## Part 2: Group Management (10 minutes)

### Task 2.1: View Existing Groups

1. Navigate to **User management** → **Groups**
2. List the existing groups:

| Group Name | Member Count | Type (Account/Workspace) |
|------------|--------------|--------------------------|
| | | |
| | | |
| | | |

### Task 2.2: Create a New Group

1. Click **Add group**
2. Create a group with these settings:
   - **Name**: `lab_data_analysts`
   - **Description**: `Training lab - Data analyst group`
3. Click **Create**

### Task 2.3: Add Members to Group

1. Select the `lab_data_analysts` group
2. Click **Add members**
3. Add yourself or a test user to the group
4. Verify the member appears in the group

### Task 2.4: Create Nested Group Structure

1. Create another group: `lab_all_users`
2. Add the `lab_data_analysts` group as a member of `lab_all_users`
3. This creates a nested group structure

**Document the hierarchy:**
```
lab_all_users
└── lab_data_analysts
    └── [your user]
```

### Task 2.5: Assign Group to Workspace

1. Select the `lab_data_analysts` group
2. Click the **Workspaces** tab
3. Click **Assign to workspaces**
4. Select a workspace and assign the group
5. Note the entitlement options (User, Admin)

---

## Part 3: Service Principal Creation (10 minutes)

### Task 3.1: Create Service Principal

1. Navigate to **User management** → **Service principals**
2. Click **Add service principal**
3. Configure:
   - **Name**: `lab-cicd-pipeline`
   - **Add to groups**: Select `lab_data_analysts`
4. Click **Create**

### Task 3.2: Document Service Principal Details

| Property | Value |
|----------|-------|
| Display Name | |
| Application ID | |
| Status | Active/Inactive |
| Groups | |

### Task 3.3: Assign to Workspace

1. Select the `lab-cicd-pipeline` service principal
2. Click **Workspaces** tab
3. Assign to a workspace with appropriate entitlements

### Task 3.4: Generate OAuth Secret

1. Click **Generate secret** (or **Manage secrets**)
2. Add a description: `Lab test secret`
3. Set expiration (e.g., 90 days)
4. **IMPORTANT**: Copy and save the secret immediately!
   - Client ID: `_________________________`
   - Client Secret: `_________________________`

⚠️ **Warning**: The secret is only shown once. Store it securely!

---

## Part 4: API Authentication Testing (10 minutes)

### Task 4.1: Test OAuth M2M Authentication

Using the OAuth credentials, obtain an access token:

```bash
# Replace with your values
ACCOUNT_ID="your-account-id"
CLIENT_ID="your-client-id"
CLIENT_SECRET="your-client-secret"

# Request access token
curl -X POST \
  "https://accounts.cloud.databricks.com/oidc/accounts/${ACCOUNT_ID}/v1/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=client_credentials" \
  -d "client_id=${CLIENT_ID}" \
  -d "client_secret=${CLIENT_SECRET}" \
  -d "scope=all-apis"
```

**Document the response:**
| Field | Value |
|-------|-------|
| access_token | (first 20 chars) |
| token_type | |
| expires_in | |

### Task 4.2: Use Token to Call API

```bash
# Use the access token to list workspaces
ACCESS_TOKEN="your-access-token"

curl -X GET \
  "https://accounts.cloud.databricks.com/api/2.0/accounts/${ACCOUNT_ID}/workspaces" \
  -H "Authorization: Bearer ${ACCESS_TOKEN}"
```

### Task 4.3: Test Workspace API

```bash
# Get workspace URL from previous response
WORKSPACE_URL="https://your-workspace.cloud.databricks.com"

# List clusters in workspace
curl -X GET \
  "${WORKSPACE_URL}/api/2.0/clusters/list" \
  -H "Authorization: Bearer ${ACCESS_TOKEN}"
```

**Document the results:**
- [ ] Successfully obtained OAuth token
- [ ] Successfully called Account API
- [ ] Successfully called Workspace API

---

## Part 5: Personal Access Tokens (5 minutes)

### Task 5.1: Review Token Policies

1. In Account Console, go to **Settings** → **Feature enablement**
2. Or in Workspace Admin Console → **Settings** → **Developer**
3. Check the token settings:

| Setting | Value |
|---------|-------|
| PAT Creation Enabled | Yes/No |
| Max Token Lifetime | |
| Comment Required | Yes/No |

### Task 5.2: Create a PAT (Workspace Level)

1. In your workspace, click your username → **Settings**
2. Click **Developer** → **Access tokens**
3. Click **Generate new token**
4. Set:
   - Comment: `Lab test token`
   - Lifetime: 7 days
5. Copy and save the token

### Task 5.3: Test PAT Authentication

```bash
WORKSPACE_URL="https://your-workspace.cloud.databricks.com"
PAT="dapi..."

curl -X GET \
  "${WORKSPACE_URL}/api/2.0/clusters/list" \
  -H "Authorization: Bearer ${PAT}"
```

---

## Part 6: Audit Log Review (5 minutes)

### Task 6.1: Query Identity-Related Audit Events

In a Databricks SQL warehouse or notebook:

```sql
-- View recent identity-related events
SELECT
    event_time,
    action_name,
    user_identity.email as actor,
    request_params,
    response.status_code
FROM system.access.audit
WHERE
    event_date >= current_date() - 1
    AND action_name IN (
        'createUser',
        'deleteUser',
        'updateUser',
        'createGroup',
        'addPrincipalToGroup',
        'createServicePrincipal',
        'generateOAuthSecret'
    )
ORDER BY event_time DESC
LIMIT 20;
```

### Task 6.2: Track Service Principal Activity

```sql
-- Find all actions by service principals
SELECT
    event_time,
    action_name,
    user_identity.email as service_principal,
    source_ip_address,
    request_params
FROM system.access.audit
WHERE
    event_date >= current_date() - 1
    AND user_identity.email LIKE '%@%'
    AND user_identity.email NOT LIKE '%@%.%'  -- Filter for SP IDs
ORDER BY event_time DESC
LIMIT 20;
```

### Task 6.3: Document Findings

| Event Type | Count (Today) |
|------------|---------------|
| User Created | |
| Group Modified | |
| Service Principal Activity | |
| Token Generated | |

---

## Part 7: Cleanup

### Task 7.1: Clean Up Lab Resources

1. **Revoke OAuth secrets**:
   - Go to the service principal → Secrets
   - Delete the test secret

2. **Revoke PAT**:
   - Go to User Settings → Developer → Access tokens
   - Revoke the lab test token

3. **Optionally remove test groups**:
   - Delete `lab_data_analysts` (if not needed)
   - Delete `lab_all_users` (if not needed)

4. **Optionally delete service principal**:
   - Delete `lab-cicd-pipeline` (if not needed)

---

## Lab Validation Checklist

- [ ] Explored Account Console identity settings
- [ ] Documented SSO and SCIM configuration status
- [ ] Created account-level groups
- [ ] Configured nested group structure
- [ ] Created service principal
- [ ] Generated OAuth credentials
- [ ] Successfully authenticated via OAuth M2M
- [ ] Called Databricks APIs with tokens
- [ ] Reviewed identity audit logs
- [ ] Cleaned up test resources

---

## Challenge Exercise

Create a complete identity automation script:

1. **Service Principal Rotation Script**:
   - Check for secrets expiring within 30 days
   - Generate new secrets
   - Update CI/CD systems with new credentials
   - Revoke old secrets

2. **Group Membership Audit**:
   - Query all groups and members
   - Identify users in sensitive groups
   - Generate compliance report

3. **Token Hygiene Check**:
   - Find tokens older than 90 days
   - Identify tokens with no activity
   - Generate list for revocation review

---

## Lab Summary

You learned:
1. Navigating Account Console identity settings
2. Creating and managing groups with nesting
3. Creating service principals for automation
4. Generating and using OAuth M2M credentials
5. Testing API authentication with tokens
6. Querying identity audit logs

---

*Lab Version: 2.0 | Databricks Platform Administration Training - Day 8*
