# Day 19 Pre-Reading Materials

## Databricks Platform Administration Training
### Cost Governance & Optimization

---

## Overview

Day 19 focuses on cost management strategies for Databricks. You'll learn about DBU pricing, resource tagging, chargeback models, and optimization techniques to control cloud spending.

**Estimated Reading Time**: 25-30 minutes

---

## Required Reading

### 1. Databricks Pricing Model

**Source**: Databricks Documentation

**Key Concepts to Understand**:
- DBU (Databricks Unit) pricing
- SKU types and multipliers
- Cloud infrastructure costs (separate)

**Read**: [Databricks pricing](https://www.databricks.com/product/pricing)

**Focus Areas**:
- DBU rates by workload type
- Serverless vs provisioned pricing
- Commitment discounts

### 2. Cost Monitoring with System Tables

**Source**: Databricks Documentation

**Key Concepts to Understand**:
- `system.billing.usage` structure
- Querying for cost analysis
- Custom tag filtering

**Read**: [Monitor usage with system tables](https://docs.databricks.com/en/administration-guide/system-tables/billing.html)

**Focus Areas**:
- DBU consumption patterns
- Team-level cost allocation
- Anomaly detection queries

### 3. Cost Optimization Best Practices

**Source**: Databricks Documentation

**Key Concepts to Understand**:
- Cluster lifecycle management
- Spot instance strategies
- Right-sizing compute

**Read**: [Optimize costs](https://docs.databricks.com/en/optimizations/cost-optimization.html)

**Focus Areas**:
- Auto-termination configuration
- Job clusters vs all-purpose
- Photon acceleration ROI

---

## Key Terminology

| Term | Definition |
|------|------------|
| **DBU** | Databricks Unit - normalized compute pricing unit |
| **SKU** | Stock Keeping Unit - specific product/service type |
| **Chargeback** | Allocating costs to consuming teams/departments |
| **Showback** | Displaying costs without actual billing |
| **Tagging** | Metadata for resource categorization |
| **Spot Instance** | Spare cloud capacity at discount |
| **Commitment** | Pre-purchased capacity at discount |
| **FinOps** | Cloud financial operations discipline |

---

## DBU Pricing by Workload Type

| Workload | Relative Cost | Use Case |
|----------|---------------|----------|
| Jobs Lite | Low | Simple scheduled jobs |
| Jobs | Medium | Production ETL |
| All-Purpose | Higher | Interactive development |
| SQL Serverless | Premium | Instant SQL analytics |
| SQL Pro | High | SQL with management control |

*Note: Exact rates vary by cloud and region*

---

## Cost Optimization Strategies

| Strategy | Potential Savings | Implementation |
|----------|-------------------|----------------|
| Auto-termination | 20-40% | Set 15-30 min timeout |
| Job clusters | 30-50% | Use for scheduled workloads |
| Spot instances | 60-90% | Workers with fallback |
| Right-sizing | 10-30% | Match instance to workload |
| Photon | Variable | Enable for SQL-heavy work |
| Serverless SQL | Variable | Eliminates idle costs |

---

## Cost Monitoring Query

```sql
-- Monthly cost summary by team
SELECT
    DATE_TRUNC('month', usage_date) as month,
    custom_tags['Team'] as team,
    sku_name,
    SUM(usage_quantity) as total_dbus,
    ROUND(SUM(usage_quantity) * 0.55, 2) as estimated_cost
FROM system.billing.usage
WHERE usage_date >= DATE_SUB(current_date(), 90)
GROUP BY DATE_TRUNC('month', usage_date),
         custom_tags['Team'],
         sku_name
ORDER BY month DESC, estimated_cost DESC;

-- Tagging compliance check
SELECT
    ROUND(100.0 * SUM(CASE WHEN custom_tags['Team'] IS NOT NULL
                      THEN usage_quantity ELSE 0 END)
          / SUM(usage_quantity), 2) as tag_compliance_pct
FROM system.billing.usage
WHERE usage_date >= current_date() - 30;
```

---

## Chargeback Model Design

```
┌─────────────────────────────────────────────────────────────┐
│                   COST ALLOCATION MODEL                     │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  RESOURCE TAGGING           BILLING DATA                   │
│  ┌─────────────┐           ┌─────────────┐                │
│  │ Team        │───────────│ system.     │                │
│  │ Environment │           │ billing.    │                │
│  │ Project     │           │ usage       │                │
│  │ CostCenter  │           └──────┬──────┘                │
│  └─────────────┘                  │                        │
│                                   ▼                        │
│                         ┌─────────────────┐                │
│                         │   CHARGEBACK    │                │
│                         │   REPORTS       │                │
│                         └────────┬────────┘                │
│                                  │                         │
│         ┌────────────────────────┼────────────────────┐   │
│         ▼                        ▼                    ▼   │
│  ┌────────────┐          ┌────────────┐       ┌──────────┐│
│  │ Engineering│          │  Finance   │       │   Data   ││
│  │   $8,500   │          │   $2,300   │       │  $5,200  ││
│  └────────────┘          └────────────┘       └──────────┘│
└─────────────────────────────────────────────────────────────┘
```

---

## Self-Assessment Questions

1. What is a DBU and how is it calculated?
2. Why is resource tagging critical for cost governance?
3. How do Spot instances reduce costs and what are the risks?
4. What's the difference between chargeback and showback?
5. How do you query system tables for team-level cost analysis?

---

## Recommended Additional Reading

- [Billing and account management](https://docs.databricks.com/en/admin/account-settings/account.html)
- [Cluster policies for cost control](https://docs.databricks.com/en/admin/clusters/policies.html)
- [Spot instances](https://docs.databricks.com/en/compute/configure.html#spot-instances)
- [FinOps Foundation](https://www.finops.org/) (external)

---

*Pre-reading materials for Databricks Platform Administration Training - Day 19*
