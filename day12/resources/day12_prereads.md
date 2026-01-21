# Day 12 Pre-Reading Materials

## Databricks Platform Administration Training
### Infrastructure, Compliance & Cost Governance

---

## Overview

Day 12 covers network security architecture, compliance frameworks, and cost management strategies. These topics are critical for enterprise Databricks deployments.

**Estimated Reading Time**: 30-35 minutes

---

## Required Reading

### 1. Network Security

**Source**: Databricks Documentation

**Key Concepts to Understand**:
- Control Plane vs Data Plane networking
- Private Link / Private Endpoints
- Secure Cluster Connectivity (SCC)

**Read**: [Network security](https://docs.databricks.com/en/security/network/index.html)

**Focus Areas**:
- Customer-managed VPC deployment
- IP access lists
- Private connectivity options

### 2. Encryption and Keys

**Source**: Databricks Documentation

**Key Concepts to Understand**:
- Data encryption at rest and in transit
- Customer-managed keys (CMK)
- Key management options

**Read**: [Encryption](https://docs.databricks.com/en/security/encryption/index.html)

**Focus Areas**:
- Default encryption behavior
- CMK for managed services
- Key rotation considerations

### 3. Cost Management

**Source**: Databricks Documentation

**Key Concepts to Understand**:
- DBU pricing model
- Cost optimization strategies
- Billing usage analysis

**Read**: [Manage costs](https://docs.databricks.com/en/admin/account-settings/usage.html)

**Focus Areas**:
- SKU types and costs
- Spot instance usage
- Reserved capacity options

---

## Key Terminology

| Term | Definition |
|------|------------|
| **Private Link** | Secure connectivity without public internet |
| **SCC** | Secure Cluster Connectivity - no public IPs on nodes |
| **CMK** | Customer-Managed Keys for encryption |
| **IP Access List** | Allowlist/blocklist for workspace access |
| **DBU** | Databricks Unit - compute consumption metric |
| **Spot Instance** | Discounted, preemptible cloud compute |
| **Chargeback** | Allocating costs back to teams/projects |
| **SOC 2** | Security compliance certification |

---

## Network Architecture Options

| Option | Description | Security Level |
|--------|-------------|----------------|
| **Default** | Databricks-managed VPC | Basic |
| **Customer VPC** | Your own VPC/VNet | Enhanced |
| **Private Link** | No public internet traffic | Maximum |
| **SCC** | No public IPs on cluster nodes | Enhanced |

---

## DBU Pricing Tiers

```
SKU Comparison (Relative Cost):

Jobs Compute         $ (lowest for batch)
Jobs Light           $ (simpler jobs)
All-Purpose          $$ (interactive)
SQL Classic/Pro      $$ (SQL analytics)
SQL Serverless       $$$ (managed, instant)
```

---

## Cost Optimization Checklist

```
□ Auto-termination enabled on all dev clusters
□ Job clusters used for production jobs
□ Spot instances for fault-tolerant workloads
□ Cluster policies enforce limits
□ Mandatory tagging for cost allocation
□ Regular usage review and optimization
□ Reserved capacity for predictable workloads
```

---

## Recommended Tag Schema

| Tag Key | Purpose | Example |
|---------|---------|---------|
| Team | Cost allocation | data-engineering |
| Project | Project tracking | customer-360 |
| Environment | Dev/Prod separation | production |
| CostCenter | Finance allocation | CC-12345 |
| Owner | Accountability | alice@company.com |

---

## Self-Assessment Questions

1. What is the difference between Private Link and Secure Cluster Connectivity?
2. What cloud resources are billed separately from DBUs?
3. Why shouldn't you use spot instances for the driver node?
4. How do tags help with cost management?

---

## Compliance Frameworks Supported

| Framework | Industry | Key Requirements |
|-----------|----------|-----------------|
| SOC 2 Type II | General | Security controls |
| ISO 27001 | General | Information security |
| HIPAA | Healthcare | Protected health info |
| PCI DSS | Finance | Payment card data |
| FedRAMP | Government | Federal data |
| GDPR | EU | Data privacy |

---

## Recommended Additional Reading

- [Private Link setup](https://docs.databricks.com/en/security/network/private-link/index.html)
- [IP access lists](https://docs.databricks.com/en/security/network/front-end/ip-access-list.html)
- [Customer-managed keys](https://docs.databricks.com/en/security/encryption/cmk/index.html)
- [Best practices for cost optimization](https://docs.databricks.com/en/admin/account-settings/usage-best-practices.html)

---

*Pre-reading materials for Databricks Platform Administration Training - Day 12*
