# Databricks Administrator Quick Reference Guide

## Databricks Platform Administration Training
### Post-Course Reference Card

---

## Unity Catalog Quick Reference

### Object Hierarchy

```
Account
  └── Metastore (regional)
        ├── Catalog
        │     └── Schema
        │           ├── Table
        │           ├── View
        │           ├── Function
        │           └── Model
        ├── Storage Credential
        ├── External Location
        └── Share
```

### Common SQL Commands

```sql
-- Create catalog
CREATE CATALOG IF NOT EXISTS prod_sales;

-- Create schema
CREATE SCHEMA IF NOT EXISTS prod_sales.gold;

-- Grant permissions
GRANT USAGE ON CATALOG prod_sales TO `data_analysts`;
GRANT USAGE ON SCHEMA prod_sales.gold TO `data_analysts`;
GRANT SELECT ON TABLE prod_sales.gold.orders TO `data_analysts`;

-- Show grants
SHOW GRANTS ON CATALOG prod_sales;
SHOW GRANTS ON SCHEMA prod_sales.gold;
SHOW GRANTS TO `alice@company.com`;

-- Revoke permissions
REVOKE SELECT ON TABLE prod_sales.gold.orders FROM `data_analysts`;

-- Transfer ownership
ALTER CATALOG prod_sales OWNER TO `catalog_owners`;
```

### Permission Types

| Permission | Applicable To | Description |
|------------|---------------|-------------|
| USAGE | Catalog, Schema | Access child objects |
| SELECT | Table, View | Read data |
| MODIFY | Table | Insert, update, delete |
| CREATE | Schema | Create tables/views |
| ALL PRIVILEGES | Any | All applicable permissions |

---

## System Tables Quick Reference

### Billing & Cost

```sql
-- Daily DBU usage
SELECT usage_date, sku_name, SUM(usage_quantity) AS total_dbus
FROM system.billing.usage
WHERE usage_date >= current_date() - 30
GROUP BY 1, 2 ORDER BY 1, 3 DESC;

-- Cost by workspace
SELECT workspace_id, SUM(usage_quantity) AS dbus
FROM system.billing.usage
WHERE usage_date >= current_date() - 30
GROUP BY 1 ORDER BY 2 DESC;
```

### Audit & Security

```sql
-- Recent login activity
SELECT event_time, user_identity.email, action_name, response.status_code
FROM system.access.audit
WHERE action_name = 'login' AND event_date >= current_date() - 7
ORDER BY event_time DESC;

-- Permission changes
SELECT event_time, user_identity.email, action_name, request_params
FROM system.access.audit
WHERE action_name IN ('grant', 'revoke')
ORDER BY event_time DESC LIMIT 100;
```

### Compute & Jobs

```sql
-- Job failure analysis
SELECT job_name, result_state, COUNT(*) as runs
FROM system.workflow.job_runs
WHERE end_time >= current_date() - 7
GROUP BY 1, 2 ORDER BY 3 DESC;

-- Cluster usage
SELECT cluster_name, state, start_time,
       TIMESTAMPDIFF(HOUR, start_time, COALESCE(end_time, current_timestamp())) as hours
FROM system.compute.clusters
WHERE start_time >= current_date() - 7
ORDER BY hours DESC;
```

---

## Cluster Policy Attributes

### Attribute Types

| Type | Description | Example |
|------|-------------|---------|
| fixed | Cannot change | `"value": "13.3.x-scala2.12"` |
| range | Min/max bounds | `"minValue": 1, "maxValue": 4` |
| allowlist | Specific values | `"values": ["dev", "prod"]` |
| blocklist | Prohibited values | `"values": ["ml-gpu"]` |
| regex | Pattern match | `"pattern": "CC-[0-9]{5}"` |
| unlimited | No restriction | (no constraint) |

### Common Policy Patterns

```json
{
  "spark_version": {
    "type": "regex",
    "pattern": "13\\.[0-9]+\\.x-scala.*"
  },
  "num_workers": {
    "type": "range",
    "minValue": 1,
    "maxValue": 4
  },
  "autotermination_minutes": {
    "type": "range",
    "minValue": 10,
    "maxValue": 60,
    "defaultValue": 30
  },
  "custom_tags.CostCenter": {
    "type": "regex",
    "pattern": "CC-[0-9]{5}"
  }
}
```

---

## CLI Quick Reference

### Authentication

```bash
# Configure CLI
databricks configure --host https://workspace.cloud.databricks.com

# Using environment variables
export DATABRICKS_HOST=https://workspace.cloud.databricks.com
export DATABRICKS_TOKEN=dapi...
```

### Common Commands

```bash
# Workspace operations
databricks workspace list /Users
databricks workspace import /local/file.py /Users/user@company.com/file.py

# Cluster operations
databricks clusters list
databricks clusters get --cluster-id 1234-567890-abc123
databricks clusters start --cluster-id 1234-567890-abc123

# Jobs operations
databricks jobs list
databricks jobs run-now --job-id 12345

# Unity Catalog
databricks unity-catalog catalogs list
databricks unity-catalog schemas list --catalog-name my_catalog
```

---

## API Endpoints Quick Reference

### Base URL
```
https://<workspace>.cloud.databricks.com/api/2.0/
```

### Common Endpoints

| Resource | Endpoint | Method |
|----------|----------|--------|
| Clusters | `/clusters/list` | GET |
| Clusters | `/clusters/create` | POST |
| Jobs | `/jobs/list` | GET |
| Jobs | `/jobs/run-now` | POST |
| Unity Catalog | `/unity-catalog/catalogs` | GET/POST |
| Users | `/preview/scim/v2/Users` | GET/POST |
| Groups | `/preview/scim/v2/Groups` | GET/POST |

---

## Network Security Checklist

```
Identity & Access:
□ SSO enabled
□ SCIM provisioning configured
□ Personal access tokens restricted
□ Service principals for automation
□ Group-based permissions

Network:
□ IP access lists configured
□ Secure Cluster Connectivity enabled
□ Private Link (if required)
□ Customer-managed VPC (if required)

Data:
□ Encryption at rest (default)
□ Customer-managed keys (if required)
□ Audit logging enabled
□ Unity Catalog enforced
```

---

## Troubleshooting Quick Guide

### Cluster Won't Start
1. Check policy compliance
2. Verify cloud quota
3. Check instance availability
4. Review cluster event log

### Permission Denied
1. Verify USAGE on parent containers
2. Check direct grants on object
3. Verify group membership
4. Check owner permissions

### Job Failed
1. Review task logs
2. Check cluster logs
3. Verify data access
4. Check compute availability

### Slow Query
1. Check data skew
2. Review Spark UI stages
3. Verify partition pruning
4. Check join strategies

---

## Key URLs

| Resource | URL |
|----------|-----|
| Documentation | docs.databricks.com |
| Admin Console | `<workspace>/settings/admin` |
| System Tables | `system.*` catalog |
| API Reference | docs.databricks.com/api |
| Community | community.databricks.com |
| Support | help.databricks.com |

---

*Quick Reference Guide for Databricks Platform Administration*
