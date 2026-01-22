# Capstone Project: Advanced Track
## Enterprise Databricks Environment Design - TechFlow Industries

**Duration:** 60 minutes
**Difficulty:** Advanced
**Focus:** Complete Enterprise Architecture with Security, Compliance & Cost Governance

---

## Scenario Overview

You are the lead Databricks platform engineer at **TechFlow Industries**. You must design a complete enterprise-grade environment meeting strict security and compliance requirements.

### Company Profile (Full)

| Attribute | Details |
|-----------|---------|
| **Industry** | Technology / SaaS |
| **Employees** | 500 total, 75 Databricks users |
| **Teams** | Data Engineering (10), Data Science (5), Analytics (15), Finance (5) |
| **Data Volume** | 50 TB, growing 5 TB/month |
| **Environments** | Development, Staging, Production |
| **Compliance** | SOC 2 Type II, GDPR |
| **Cloud** | AWS (primary), considering multi-cloud |

### Business Requirements

1. **Data Engineering** - ETL pipelines processing 10M+ records daily
2. **Data Science** - ML workloads with GPU access
3. **Analytics** - Self-service SQL access to curated datasets
4. **Finance** - Strict access controls for financial data
5. **All teams** - Cost visibility and chargeback

---

## Part 1: Unity Catalog Architecture (10 minutes)

*Include everything from Intermediate track PLUS:*

### Task 1.1: Storage Locations

| Location Name | Cloud Path | Purpose |
|---------------|------------|---------|
| raw_data | s3://techflow-raw-data/ | Raw data landing zone |
| processed_data | s3://techflow-processed/ | Transformed data storage |
| ml_artifacts | s3://techflow-ml-artifacts/ | ML models and features |
| finance_restricted | s3://techflow-finance-encrypted/ | Encrypted financial data |

### Task 1.2: Storage Credential & External Location SQL

```sql
-- Create storage credentials (requires admin)
CREATE STORAGE CREDENTIAL IF NOT EXISTS techflow_raw_credential
WITH (AWS_IAM_ROLE = 'arn:aws:iam::123456789:role/databricks-access-role');

-- Create external locations
CREATE EXTERNAL LOCATION IF NOT EXISTS raw_data
URL 's3://techflow-raw-data/'
WITH (STORAGE CREDENTIAL techflow_raw_credential);

CREATE EXTERNAL LOCATION IF NOT EXISTS finance_restricted
URL 's3://techflow-finance-encrypted/'
WITH (STORAGE CREDENTIAL techflow_finance_credential)
COMMENT 'Encrypted storage for financial data - SOX compliance';
```

---

## Part 2: Complete Permission Design (10 minutes)

*Include Intermediate track permission matrix PLUS:*

### Task 2.1: Service Principals

| Service Principal | Purpose | Permissions |
|-------------------|---------|-------------|
| sp-cicd-pipeline | CI/CD deployments | Manage jobs, deploy notebooks |
| sp-etl-scheduler | Automated ETL | Execute jobs, read/write tables |
| sp-ml-training | ML pipeline automation | Read data, write models |
| sp-reporting | BI tool connections | SELECT on gold schema |

### Task 2.2: Row-Level Security (Finance Data)

```sql
-- Create row filter function for regional access
CREATE OR REPLACE FUNCTION prod_techflow.finance.region_filter()
RETURNS BOOLEAN
RETURN CASE
    WHEN is_account_group_member('finance_global') THEN TRUE
    WHEN is_account_group_member('finance_us') AND region = 'US' THEN TRUE
    WHEN is_account_group_member('finance_eu') AND region = 'EU' THEN TRUE
    ELSE FALSE
END;

-- Apply row filter to sensitive table
ALTER TABLE prod_techflow.finance.transactions
SET ROW FILTER prod_techflow.finance.region_filter ON ();
```

### Task 2.3: Column Masking (PII)

```sql
-- Create masking function for SSN
CREATE OR REPLACE FUNCTION prod_techflow.gold.mask_ssn(ssn STRING)
RETURNS STRING
RETURN CASE
    WHEN is_account_group_member('pii_full_access') THEN ssn
    ELSE CONCAT('XXX-XX-', RIGHT(ssn, 4))
END;

-- Apply to customer table
ALTER TABLE prod_techflow.gold.customers
ALTER COLUMN ssn SET MASK prod_techflow.gold.mask_ssn;
```

---

## Part 3: ML Cluster Policy (5 minutes)

### Task 3.1: Data Science / ML Policy

```json
{
  "name": "techflow-ml-policy",
  "definition": {
    "cluster_type": {
      "type": "fixed",
      "value": "single_user"
    },
    "data_security_mode": {
      "type": "fixed",
      "value": "SINGLE_USER"
    },
    "spark_version": {
      "type": "regex",
      "pattern": "^14\\.[0-9]+-ml-.*$",
      "defaultValue": "14.3.x-gpu-ml-scala2.12"
    },
    "node_type_id": {
      "type": "allowlist",
      "values": [
        "Standard_NC6s_v3",
        "Standard_NC12s_v3",
        "Standard_DS13_v2"
      ],
      "defaultValue": "Standard_DS13_v2"
    },
    "num_workers": {
      "type": "range",
      "minValue": 0,
      "maxValue": 4
    },
    "autotermination_minutes": {
      "type": "range",
      "minValue": 30,
      "maxValue": 120,
      "defaultValue": 60
    },
    "custom_tags.Workload": {
      "type": "fixed",
      "value": "ml-training"
    },
    "custom_tags.Team": {
      "type": "unlimited",
      "isOptional": false
    }
  }
}
```

---

## Part 4: Security Configuration (10 minutes)

### Task 4.1: Network Security Design

| Feature | Configuration | Justification |
|---------|---------------|---------------|
| **VNet Injection** | Enable with dedicated subnets | Network isolation, compliance |
| **Private Link** | Front-end + Back-end | No public internet exposure |
| **IP Access Lists** | Corporate IPs only: 10.0.0.0/8, VPN egress | Restrict access to known sources |
| **Secure Cluster Connectivity** | Enable (No Public IPs) | Reduce attack surface |
| **NAT Gateway** | Outbound internet via NAT | Control egress traffic |

### Task 4.2: Data Security Configuration

| Feature | Configuration | Scope |
|---------|---------------|-------|
| **Encryption at Rest** | Customer-managed keys (CMK) | All storage |
| **Encryption in Transit** | TLS 1.2 enforced | All connections |
| **Secret Scopes** | Azure Key Vault backed | All credentials |
| **Column Masking** | PII fields (SSN, email) | gold.customers |
| **Row-Level Security** | Regional filtering | finance.transactions |

### Task 4.3: IP Access List Configuration

```json
{
  "list_type": "ALLOW",
  "ip_addresses": [
    {"value": "10.0.0.0/8", "label": "Corporate Network"},
    {"value": "172.16.0.0/12", "label": "VPN Egress"},
    {"value": "52.x.x.x/32", "label": "CI/CD Pipeline"}
  ]
}
```

---

## Part 5: Compliance Controls (10 minutes)

### Task 5.1: SOC 2 Type II Controls

| Control Area | Implementation |
|--------------|----------------|
| **Access Control** | RBAC via Unity Catalog, SCIM sync with Okta |
| **Change Management** | All changes via CI/CD, Terraform managed |
| **Logging** | Audit logs exported to SIEM (90-day retention) |
| **Data Protection** | CMK encryption, column masking |
| **Incident Response** | PagerDuty integration for alerts |

### Task 5.2: GDPR Controls

| Requirement | Implementation |
|-------------|----------------|
| **Data Minimization** | Row-level security limits data exposure |
| **Right to Erasure** | Delta table DELETE with compliance tracking |
| **Consent Tracking** | Metadata tables track consent status |
| **Data Location** | EU data stays in EU region (separate catalog) |
| **Access Audit** | Unity Catalog audit logs track all access |

### Task 5.3: Audit Configuration

```sql
-- Query for compliance reporting
SELECT
    event_time,
    user_identity.email,
    action_name,
    request_params.full_name_arg as object_accessed,
    source_ip_address
FROM system.access.audit
WHERE action_name IN ('getTable', 'selectFromTable', 'executeQuery')
  AND request_params.full_name_arg LIKE 'prod_techflow.finance.%'
  AND event_time >= current_date() - 30
ORDER BY event_time DESC;
```

---

## Part 6: Cost Governance (10 minutes)

### Task 6.1: Cost Monitoring Queries

```sql
-- Daily cost by team
SELECT
    DATE(usage_date) as day,
    custom_tags['Team'] as team,
    sku_name,
    SUM(usage_quantity) as total_dbus,
    ROUND(SUM(usage_quantity) * 0.55, 2) as estimated_cost_usd
FROM system.billing.usage
WHERE usage_date >= current_date() - 30
GROUP BY DATE(usage_date), custom_tags['Team'], sku_name
ORDER BY day DESC, estimated_cost_usd DESC;

-- Tagging compliance
SELECT
    ROUND(100.0 * SUM(CASE WHEN custom_tags['Team'] IS NOT NULL THEN usage_quantity ELSE 0 END)
          / SUM(usage_quantity), 2) as tag_compliance_pct
FROM system.billing.usage
WHERE usage_date >= current_date() - 7;

-- Budget alert check
SELECT
    custom_tags['Team'] as team,
    SUM(usage_quantity) * 0.55 as mtd_cost,
    CASE
        WHEN SUM(usage_quantity) * 0.55 > 5000 THEN 'OVER BUDGET'
        WHEN SUM(usage_quantity) * 0.55 > 4000 THEN 'WARNING'
        ELSE 'OK'
    END as budget_status
FROM system.billing.usage
WHERE usage_date >= DATE_TRUNC('month', current_date())
GROUP BY custom_tags['Team'];
```

### Task 6.2: Cost Dashboard Design

| Widget | Metric | Alert Threshold |
|--------|--------|-----------------|
| Monthly Spend | Total DBU cost | $15,000 |
| Daily Trend | DBU/day chart | 150% of 7-day avg |
| Team Breakdown | Cost by team | Team budget |
| SKU Distribution | Pie chart | - |
| Tag Compliance | Percentage | < 90% |
| Long-Running Clusters | List | > 8 hours |

### Task 6.3: Alert Configuration

| Alert | Threshold | Recipients | Frequency |
|-------|-----------|------------|-----------|
| Daily spend exceeds budget | > $800/day | platform-admins@, finance@ | Daily |
| Tag compliance below target | < 90% | platform-admins@ | Weekly |
| Untagged high-cost cluster | > 50 DBUs untagged | platform-admins@ | Daily |
| Job failure rate | > 10% in 24 hours | data-engineering@ | Hourly |

---

## Part 7: Administrator Runbook (5 minutes)

### Task 7.1: Runbook Outline

**1. Daily Tasks**
- Review overnight job failures
- Check cost alerts and anomalies
- Monitor cluster utilization
- Review security alerts

**2. Weekly Tasks**
- Generate team chargeback reports
- Review access audit logs
- Check tagging compliance
- Update documentation

**3. Monthly Tasks**
- User access review
- Cluster policy review
- Cost optimization analysis
- Security posture review

**4. Incident Response**
- Cluster failure: Check events, review logs, restart
- Job failure: Check task output, retry or escalate
- Security alert: Investigate audit logs, revoke if needed
- Cost overrun: Identify source, apply policies

---

## Deliverables Checklist

### Unity Catalog & Governance
- [ ] Complete catalog hierarchy with storage locations
- [ ] Storage credentials and external locations
- [ ] Full permission matrix with service principals
- [ ] Row-level and column-level security

### Compute Governance
- [ ] Development cluster policy
- [ ] Production cluster policy
- [ ] ML/GPU cluster policy
- [ ] SQL warehouse configuration

### Security
- [ ] Network security design
- [ ] Data security configuration
- [ ] IP access list configuration

### Compliance
- [ ] SOC 2 Type II controls mapping
- [ ] GDPR controls mapping
- [ ] Audit query for compliance reporting

### Cost Governance
- [ ] Cost monitoring SQL queries
- [ ] Dashboard design
- [ ] Alert configuration

### Operations
- [ ] Administrator runbook outline
- [ ] Architecture summary document

---

## Evaluation Criteria (Advanced)

| Criteria | Points | Your Score |
|----------|--------|------------|
| Unity Catalog Design (storage, locations) | 15 | |
| Access Control (permissions, RLS, masking) | 15 | |
| Compute Governance (3 policies) | 15 | |
| Security Configuration | 15 | |
| Compliance Controls | 10 | |
| Cost Governance | 15 | |
| Documentation & Runbook | 15 | |
| **Total** | **100** | |

**Passing Score:** 70 points
**Certification Ready:** 90+ points

---

*Capstone Advanced Track | Version 3.0*
