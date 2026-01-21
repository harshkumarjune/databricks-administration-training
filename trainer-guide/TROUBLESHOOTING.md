# Troubleshooting Guide

## Databricks Platform Administration Training
### Common Issues & Solutions

---

## Quick Reference

| Issue | Quick Fix |
|-------|-----------|
| Can't login | Check URL, credentials, SSO status |
| Cluster won't start | Check quota, policy, permissions |
| Query fails | Check catalog, schema, permissions |
| Lab exercise blocked | Use alternative approach or demo |

---

## Authentication & Access Issues

### Cannot Login to Workspace

**Symptoms:**
- Login page shows error
- Redirect loops
- "Access Denied" message

**Solutions:**
1. **Verify workspace URL** - Ensure correct format:
   - AWS: `https://account.cloud.databricks.com`
   - Azure: `https://adb-xxx.azuredatabricks.net`
   - GCP: `https://xxx.gcp.databricks.com`

2. **Check SSO configuration** - If using SSO:
   - Clear browser cache and cookies
   - Try incognito/private window
   - Verify IdP session is active

3. **Verify user provisioning** - User may not be synced:
   - Check Account Console for user existence
   - Verify SCIM provisioning if enabled
   - Manually add user if needed

4. **Check IP access lists** - User's IP may be blocked:
   - Verify IP is in allowed range
   - Check VPN requirements

### User Cannot See Workspace

**Symptoms:**
- User can login to account but workspace not visible
- "No workspaces available" message

**Solutions:**
1. User needs workspace assignment:
   ```
   Account Console → Workspaces → [workspace] → Permissions → Add user
   ```

2. Check workspace entitlements are granted

3. Verify user is not disabled at account level

---

## Compute Issues

### Cluster Won't Start

**Symptoms:**
- Cluster stuck in "Pending" state
- Error message on cluster start

**Common Causes & Solutions:**

| Error | Solution |
|-------|----------|
| "Quota exceeded" | Request quota increase from cloud provider |
| "Invalid instance type" | Check instance type exists in region |
| "Policy violation" | Adjust cluster config to match policy |
| "Insufficient permissions" | Grant cluster create permission |
| "Network error" | Check VPC/VNet configuration |

**Debugging Steps:**
1. Check cluster event log for specific error
2. Verify cluster policy allows configuration
3. Try smaller instance type
4. Check cloud provider quota limits

### Cluster Terminates Unexpectedly

**Symptoms:**
- Cluster stops mid-job
- Auto-termination triggers too soon

**Solutions:**
1. **Check auto-termination setting** - May be set too low
2. **Review spot instance termination** - Spot can be reclaimed
3. **Check for OOM errors** - May need larger instances
4. **Review driver logs** - Look for error messages

### SQL Warehouse Not Responding

**Symptoms:**
- Queries timeout
- Warehouse shows "Starting" indefinitely

**Solutions:**
1. Check warehouse size and scaling
2. Verify serverless is available in region
3. Check network connectivity
4. Review warehouse event log

---

## Unity Catalog Issues

### Cannot See Catalog/Schema/Table

**Symptoms:**
- Object exists but user can't see it
- "Object not found" error
- Empty results in Data Explorer

**Solution - Check Permission Chain:**

```sql
-- Check user's grants
SHOW GRANTS TO `user@example.com`;

-- Check grants on specific objects
SHOW GRANTS ON CATALOG catalog_name;
SHOW GRANTS ON SCHEMA catalog_name.schema_name;
SHOW GRANTS ON TABLE catalog_name.schema_name.table_name;

-- Common fix: Grant USAGE
GRANT USAGE ON CATALOG catalog_name TO `user@example.com`;
GRANT USAGE ON SCHEMA catalog_name.schema_name TO `user@example.com`;
GRANT SELECT ON TABLE catalog_name.schema_name.table_name TO `user@example.com`;
```

**Remember:** USAGE is required at EVERY level of the hierarchy!

### Cannot Create Catalog

**Symptoms:**
- "Permission denied" when creating catalog
- CREATE CATALOG statement fails

**Solutions:**
1. User needs metastore admin role, or
2. User needs CREATE CATALOG privilege from metastore admin

```sql
-- Metastore admin grants permission
GRANT CREATE CATALOG ON METASTORE TO `user@example.com`;
```

### External Table Creation Fails

**Symptoms:**
- "Access denied to storage"
- "No external location found"

**Solutions:**
1. Verify storage credential exists and is accessible
2. Verify external location covers the path
3. User needs CREATE EXTERNAL TABLE on the location

```sql
-- Check external locations
SHOW EXTERNAL LOCATIONS;

-- Grant permission
GRANT CREATE EXTERNAL TABLE ON EXTERNAL LOCATION location_name
TO `user@example.com`;
```

---

## Query & SQL Issues

### Query Returns "Table Not Found"

**Symptoms:**
- Table exists but query fails
- Works for some users but not others

**Debugging Steps:**
1. Check fully qualified name: `catalog.schema.table`
2. Verify current catalog/schema context:
   ```sql
   SELECT current_catalog(), current_schema();
   ```
3. Check user has USAGE + SELECT permissions

### Query Timeout

**Symptoms:**
- Query runs for long time then fails
- "Operation timed out" error

**Solutions:**
1. Check query execution plan for issues
2. Look for data skew (one partition much larger)
3. Add filters to reduce data scanned
4. Check if table needs OPTIMIZE

### Delta Lake Time Travel Fails

**Symptoms:**
- "Version X not available" error
- Cannot query historical version

**Solutions:**
1. Check DESCRIBE HISTORY for available versions
2. Version may have been removed by VACUUM
3. Adjust retention period if needed:
   ```sql
   ALTER TABLE table_name
   SET TBLPROPERTIES ('delta.logRetentionDuration' = '30 days');
   ```

---

## Lab-Specific Issues

### Lab 01: Workspace Navigation

**Issue:** Participant can't see all sidebar items
**Solution:** Some items require specific permissions or features to be enabled

### Lab 06: Unity Catalog Setup

**Issue:** Cannot create catalog
**Solution:**
- Use instructor-provided training catalog
- Create schemas within existing catalog
- Use sandbox schema if available

### Lab 09: Cluster Policies

**Issue:** Cannot create cluster policy
**Solution:**
- Requires workspace admin privileges
- Demo the process and share policy JSON
- Use existing policies as examples

### Lab 11: System Tables

**Issue:** Cannot query system tables
**Solution:**
- System tables require specific privileges
- May need account admin to grant access
- Use provided sample data as alternative

### Lab 12: Cost Analysis

**Issue:** No billing data available
**Solution:**
- Billing tables may not be populated in training
- Use sample queries with mock data
- Discuss concepts without live data

---

## Performance Issues

### Slow Query Performance

**Investigation Steps:**

1. **Check query plan:**
   ```sql
   EXPLAIN SELECT * FROM table_name WHERE condition;
   ```

2. **Check table statistics:**
   ```sql
   ANALYZE TABLE table_name COMPUTE STATISTICS;
   ```

3. **Check for data skew:**
   - Look at Spark UI Stages tab
   - One task much longer than others = skew

4. **Check shuffle size:**
   - Spark UI shows shuffle read/write
   - Large shuffle = expensive

### Common Performance Fixes

| Problem | Solution |
|---------|----------|
| Data skew | Add salting, broadcast small table |
| Large shuffle | Reduce shuffle partitions, use broadcast |
| OOM errors | Increase memory, spill to disk |
| Slow VACUUM | Run during off-peak hours |
| Many small files | Run OPTIMIZE more frequently |

---

## Network & Connectivity Issues

### Cannot Connect from External Tools

**Symptoms:**
- JDBC/ODBC connection fails
- API calls timeout

**Solutions:**
1. Check cluster is running and accessible
2. Verify JDBC/ODBC port not blocked by firewall
3. Check personal access token is valid
4. Verify IP access lists allow connection

### Private Link Issues

**Symptoms:**
- Cannot connect via private endpoint
- "Connection refused" from within VPC

**Solutions:**
1. Verify Private Link is properly configured
2. Check DNS resolution for private endpoint
3. Verify security groups allow traffic
4. Check routing tables

---

## Emergency Contacts

| Issue Type | Contact |
|------------|---------|
| Training logistics | Training Coordinator: [email] |
| Workspace access | IT Support: [email/ticket] |
| Databricks platform | Databricks Support: [portal] |
| Cloud provider | AWS/Azure/GCP Support |

---

## Escalation Path

1. **Self-service**: Check this guide and Databricks docs
2. **Peer support**: Ask training cohort or instructor
3. **IT Support**: For access and permissions issues
4. **Databricks Support**: For platform issues
5. **Cloud Support**: For infrastructure issues

---

*Troubleshooting Guide Version: 2.0 | Databricks Platform Administration Training*
