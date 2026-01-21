# Lab 13: Capstone Project - DataCorp Analytics Environment

## Databricks Platform Administration Training
### Duration: 60 Minutes | Difficulty: Advanced

---

## Project Overview

Design and implement a complete Databricks environment for **DataCorp Analytics**, a fictional company with three teams and three environments. This capstone project integrates all concepts learned throughout the course.

### Company Profile: DataCorp Analytics

- **Industry**: Financial Services
- **Teams**: Data Engineering, Data Science, Analytics
- **Employees**: 150 (50 Databricks users)
- **Environments**: Development, Staging, Production
- **Compliance**: SOC 2, data residency requirements

---

## Project Requirements

### 1. Unity Catalog Structure

Design a catalog hierarchy that:
- Separates environments (dev, staging, prod)
- Organizes data by domain (sales, customers, finance)
- Supports medallion architecture (bronze, silver, gold)

### 2. Access Control

Implement permissions that:
- Data Engineers: Full access to all environments
- Data Scientists: Read production, write to dev/staging
- Analysts: Read-only access to gold layer

### 3. Compute Governance

Create cluster policies for:
- Development (cost-controlled, auto-terminate)
- Production (stable, no auto-terminate)
- Data Science (ML runtime, GPU optional)

### 4. Cost Management

Implement:
- Mandatory tagging strategy
- Cost tracking by team
- Budget monitoring

---

## Part 1: Unity Catalog Design (15 minutes)

### Task 1.1: Design Catalog Structure

Document your design:

```
Metastore: datacorp_metastore
│
├── Catalog: dev_datacorp
│   ├── Schema: bronze_sales
│   ├── Schema: bronze_customers
│   ├── Schema: silver_sales
│   ├── Schema: silver_customers
│   ├── Schema: gold_analytics
│   └── Schema: sandbox
│
├── Catalog: staging_datacorp
│   ├── Schema: bronze_sales
│   ├── Schema: silver_sales
│   └── Schema: gold_analytics
│
└── Catalog: prod_datacorp
    ├── Schema: bronze_sales
    ├── Schema: bronze_customers
    ├── Schema: silver_sales
    ├── Schema: silver_customers
    ├── Schema: gold_analytics
    └── Schema: gold_reporting
```

### Task 1.2: Create Catalogs and Schemas

```sql
-- Development Catalog
CREATE CATALOG IF NOT EXISTS dev_datacorp
COMMENT 'Development environment for DataCorp';

CREATE SCHEMA IF NOT EXISTS dev_datacorp.bronze_sales;
CREATE SCHEMA IF NOT EXISTS dev_datacorp.bronze_customers;
CREATE SCHEMA IF NOT EXISTS dev_datacorp.silver_sales;
CREATE SCHEMA IF NOT EXISTS dev_datacorp.silver_customers;
CREATE SCHEMA IF NOT EXISTS dev_datacorp.gold_analytics;
CREATE SCHEMA IF NOT EXISTS dev_datacorp.sandbox;

-- Production Catalog (similar structure)
CREATE CATALOG IF NOT EXISTS prod_datacorp
COMMENT 'Production environment for DataCorp';

CREATE SCHEMA IF NOT EXISTS prod_datacorp.bronze_sales;
CREATE SCHEMA IF NOT EXISTS prod_datacorp.silver_sales;
CREATE SCHEMA IF NOT EXISTS prod_datacorp.gold_analytics;
CREATE SCHEMA IF NOT EXISTS prod_datacorp.gold_reporting;
```

---

## Part 2: Group & Permission Setup (15 minutes)

### Task 2.1: Create Groups

```
Groups to create:
- datacorp_data_engineers
- datacorp_data_scientists
- datacorp_analysts
- datacorp_admins
```

Document group structure:
| Group | Members | Purpose |
|-------|---------|---------|
| datacorp_data_engineers | | ETL development & production |
| datacorp_data_scientists | | ML & experimentation |
| datacorp_analysts | | Reporting & analytics |
| datacorp_admins | | Platform administration |

### Task 2.2: Grant Permissions

```sql
-- Data Engineers: Full access
GRANT USAGE ON CATALOG dev_datacorp TO `datacorp_data_engineers`;
GRANT ALL PRIVILEGES ON CATALOG dev_datacorp TO `datacorp_data_engineers`;

GRANT USAGE ON CATALOG prod_datacorp TO `datacorp_data_engineers`;
GRANT ALL PRIVILEGES ON CATALOG prod_datacorp TO `datacorp_data_engineers`;

-- Data Scientists: Dev full access, Prod read-only
GRANT USAGE ON CATALOG dev_datacorp TO `datacorp_data_scientists`;
GRANT ALL PRIVILEGES ON CATALOG dev_datacorp TO `datacorp_data_scientists`;

GRANT USAGE ON CATALOG prod_datacorp TO `datacorp_data_scientists`;
GRANT USAGE ON SCHEMA prod_datacorp.gold_analytics TO `datacorp_data_scientists`;
GRANT SELECT ON SCHEMA prod_datacorp.gold_analytics TO `datacorp_data_scientists`;

-- Analysts: Read-only on gold layers
GRANT USAGE ON CATALOG prod_datacorp TO `datacorp_analysts`;
GRANT USAGE ON SCHEMA prod_datacorp.gold_analytics TO `datacorp_analysts`;
GRANT USAGE ON SCHEMA prod_datacorp.gold_reporting TO `datacorp_analysts`;
GRANT SELECT ON SCHEMA prod_datacorp.gold_analytics TO `datacorp_analysts`;
GRANT SELECT ON SCHEMA prod_datacorp.gold_reporting TO `datacorp_analysts`;
```

### Task 2.3: Verify Permissions

```sql
-- Check grants for each group
SHOW GRANTS TO `datacorp_data_engineers`;
SHOW GRANTS TO `datacorp_data_scientists`;
SHOW GRANTS TO `datacorp_analysts`;
```

---

## Part 3: Cluster Policy Creation (15 minutes)

### Task 3.1: Development Policy

```json
{
  "name": "datacorp-dev-policy",
  "definition": {
    "spark_version": {
      "type": "regex",
      "pattern": "13\\.[0-9]+\\.x-scala.*|14\\.[0-9]+\\.x-scala.*",
      "defaultValue": "13.3.x-scala2.12"
    },
    "node_type_id": {
      "type": "allowlist",
      "values": ["i3.xlarge", "i3.2xlarge", "m5.xlarge"],
      "defaultValue": "i3.xlarge"
    },
    "num_workers": {
      "type": "range",
      "minValue": 0,
      "maxValue": 4,
      "defaultValue": 1
    },
    "autotermination_minutes": {
      "type": "range",
      "minValue": 10,
      "maxValue": 60,
      "defaultValue": 30
    },
    "custom_tags.Team": {
      "type": "fixed",
      "value": "${user.team}"
    },
    "custom_tags.Environment": {
      "type": "fixed",
      "value": "development"
    },
    "custom_tags.CostCenter": {
      "type": "regex",
      "pattern": "CC-[0-9]{5}"
    }
  }
}
```

### Task 3.2: Production Policy

```json
{
  "name": "datacorp-prod-policy",
  "definition": {
    "spark_version": {
      "type": "regex",
      "pattern": "13\\.3\\.x-scala.*",
      "defaultValue": "13.3.x-scala2.12"
    },
    "node_type_id": {
      "type": "allowlist",
      "values": ["i3.xlarge", "i3.2xlarge", "r5.xlarge"],
      "defaultValue": "i3.xlarge"
    },
    "num_workers": {
      "type": "range",
      "minValue": 2,
      "maxValue": 20
    },
    "custom_tags.Team": {
      "type": "fixed",
      "value": "data-engineering"
    },
    "custom_tags.Environment": {
      "type": "fixed",
      "value": "production"
    },
    "custom_tags.CostCenter": {
      "type": "fixed",
      "value": "CC-10001"
    }
  }
}
```

### Task 3.3: Data Science Policy

```json
{
  "name": "datacorp-ds-policy",
  "definition": {
    "spark_version": {
      "type": "regex",
      "pattern": "13\\.[0-9]+\\.x-.*-ml-scala.*",
      "defaultValue": "13.3.x-cpu-ml-scala2.12"
    },
    "node_type_id": {
      "type": "allowlist",
      "values": ["i3.xlarge", "i3.2xlarge", "p3.2xlarge"],
      "defaultValue": "i3.xlarge"
    },
    "num_workers": {
      "type": "range",
      "minValue": 0,
      "maxValue": 8
    },
    "autotermination_minutes": {
      "type": "range",
      "minValue": 30,
      "maxValue": 120,
      "defaultValue": 60
    },
    "custom_tags.Team": {
      "type": "fixed",
      "value": "data-science"
    },
    "custom_tags.Environment": {
      "type": "fixed",
      "value": "development"
    }
  }
}
```

---

## Part 4: Cost Monitoring Dashboard (10 minutes)

### Task 4.1: Create Cost Queries

```sql
-- Query 1: Daily cost by team
SELECT
    usage_date,
    COALESCE(usage_metadata.custom_tags['Team'], 'Untagged') AS team,
    SUM(usage_quantity) AS total_dbus
FROM system.billing.usage
WHERE usage_date >= current_date() - 30
GROUP BY 1, 2
ORDER BY 1 DESC, 3 DESC;

-- Query 2: Cost by environment
SELECT
    COALESCE(usage_metadata.custom_tags['Environment'], 'Unknown') AS environment,
    sku_name,
    SUM(usage_quantity) AS total_dbus
FROM system.billing.usage
WHERE usage_date >= current_date() - 30
GROUP BY 1, 2
ORDER BY total_dbus DESC;

-- Query 3: Tag compliance
SELECT
    ROUND(
        SUM(CASE WHEN usage_metadata.custom_tags['Team'] IS NOT NULL THEN usage_quantity ELSE 0 END) * 100.0 /
        SUM(usage_quantity), 2
    ) AS tagged_pct
FROM system.billing.usage
WHERE usage_date >= current_date() - 7;
```

### Task 4.2: Build Dashboard

1. Create dashboard: `DataCorp Cost Governance`
2. Add widgets for:
   - Daily DBU trend (line chart)
   - Cost by team (bar chart)
   - Cost by environment (pie chart)
   - Tag compliance (counter)

---

## Part 5: Documentation (5 minutes)

### Task 5.1: Complete Design Document

Fill out this template:

```markdown
# DataCorp Analytics - Databricks Environment Design

## Overview
- Environment: [AWS/Azure/GCP]
- Region: [Primary region]
- Workspaces: [Count and names]

## Unity Catalog Structure
- Metastore: datacorp_metastore
- Catalogs: dev_datacorp, staging_datacorp, prod_datacorp
- Schema naming: {layer}_{domain}

## Access Control Model
- Group-based permissions
- Principle of least privilege
- Production data read-only for most users

## Cluster Policies
- Development: Cost-controlled, 30-min auto-terminate
- Production: LTS only, no auto-terminate
- Data Science: ML runtime, GPU allowed

## Cost Governance
- Mandatory tags: Team, Environment, CostCenter
- Budget alerts at $X/day threshold
- Monthly chargeback reports

## Security Configuration
- SSO: [Enabled/Provider]
- SCIM: [Enabled/Provider]
- IP Access Lists: [Corporate ranges]
- Encryption: [Default/CMK]
```

---

## Deliverables Checklist

- [ ] Unity Catalog structure created (catalogs, schemas)
- [ ] Groups created and documented
- [ ] Permissions granted following least privilege
- [ ] Cluster policies defined (dev, prod, DS)
- [ ] Cost monitoring queries created
- [ ] Dashboard built with key metrics
- [ ] Design document completed

---

## Evaluation Criteria

| Criteria | Points |
|----------|--------|
| Catalog design follows best practices | 20 |
| Permissions implement least privilege | 20 |
| Cluster policies enforce governance | 20 |
| Cost tracking implemented correctly | 20 |
| Documentation complete and clear | 20 |
| **Total** | **100** |

---

## Extension Challenges

If time permits:

1. **Add audit monitoring**: Create query to track sensitive data access
2. **Implement data classification**: Add tags for PII columns
3. **Create job workflow**: Build sample ETL job with proper configuration
4. **Set up alerts**: Configure alerts for failures and budget thresholds

---

*Capstone Project Version: 2.0 | Databricks Platform Administration Training - Day 13*
