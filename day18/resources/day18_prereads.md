# Day 18 Pre-Reading Materials

## Databricks Platform Administration Training
### Security & Compliance

---

## Overview

Day 18 covers enterprise security configuration and compliance frameworks. You'll learn about network isolation, data protection, identity management, and how to implement controls for SOC 2 and GDPR compliance.

**Estimated Reading Time**: 35-40 minutes

---

## Required Reading

### 1. Network Security

**Source**: Databricks Documentation

**Key Concepts to Understand**:
- VNet injection (network isolation)
- Private Link (private connectivity)
- IP access lists

**Read**: [Configure a VNet-injected workspace](https://docs.databricks.com/en/security/network/classic/vnet-inject.html) (Azure) or [VPC configuration](https://docs.databricks.com/en/security/network/classic/customer-managed-vpc.html) (AWS)

**Focus Areas**:
- Network architecture for compliance
- Private endpoint configuration
- Secure cluster connectivity (no public IPs)

### 2. Data Security

**Source**: Databricks Documentation

**Key Concepts to Understand**:
- Encryption at rest (CMK)
- Encryption in transit (TLS)
- Column masking and row-level security

**Read**: [Data encryption](https://docs.databricks.com/en/security/keys/index.html)

**Focus Areas**:
- Customer-managed keys (CMK)
- Secret management
- Unity Catalog security features

### 3. Identity and Access Management

**Source**: Databricks Documentation

**Key Concepts to Understand**:
- SCIM provisioning
- SSO configuration
- Service principals

**Read**: [Identity and access management](https://docs.databricks.com/en/admin/users-groups/index.html)

**Focus Areas**:
- User/group synchronization
- Role-based access control
- Service principal authentication

---

## Key Terminology

| Term | Definition |
|------|------------|
| **VNet Injection** | Deploying compute in your virtual network |
| **Private Link** | Private connectivity to Databricks services |
| **IP Access List** | Allowlist of IP addresses for workspace access |
| **CMK** | Customer-Managed Keys for encryption |
| **SCIM** | Protocol for automatic user/group provisioning |
| **SSO** | Single Sign-On via SAML/OIDC |
| **Service Principal** | Machine identity for automation |
| **Column Masking** | Dynamic data redaction based on permissions |
| **Row-Level Security** | Filter rows based on user attributes |

---

## Security Layers

```
┌─────────────────────────────────────────────────────────────┐
│                    NETWORK SECURITY                         │
│  VNet Injection │ Private Link │ IP Access Lists           │
├─────────────────────────────────────────────────────────────┤
│                    IDENTITY & ACCESS                        │
│  SSO/SCIM │ RBAC │ Service Principals │ Groups             │
├─────────────────────────────────────────────────────────────┤
│                    DATA SECURITY                            │
│  CMK Encryption │ Column Masking │ Row-Level Security      │
├─────────────────────────────────────────────────────────────┤
│                    AUDIT & COMPLIANCE                       │
│  Audit Logs │ System Tables │ Compliance Reporting         │
└─────────────────────────────────────────────────────────────┘
```

---

## Compliance Framework Mapping

### SOC 2 Type II Controls

| Control Area | Databricks Implementation |
|--------------|---------------------------|
| Access Control | Unity Catalog RBAC, SCIM, SSO |
| Change Management | Repos, CI/CD, Terraform |
| Logging | System tables, audit logs (90+ days) |
| Data Protection | CMK encryption, masking |
| Incident Response | Alerts, PagerDuty integration |

### GDPR Controls

| Requirement | Databricks Implementation |
|-------------|---------------------------|
| Data Minimization | Row-level security, column masking |
| Right to Erasure | Delta DELETE with compliance tracking |
| Consent Tracking | Metadata tables for consent status |
| Data Location | Regional catalogs, storage locations |
| Access Audit | Unity Catalog audit logs |

---

## Column Masking Example

```sql
-- Create masking function
CREATE OR REPLACE FUNCTION mask_ssn(ssn STRING)
RETURNS STRING
RETURN CASE
    WHEN is_account_group_member('pii_full_access') THEN ssn
    ELSE CONCAT('XXX-XX-', RIGHT(ssn, 4))
END;

-- Apply to column
ALTER TABLE customers
ALTER COLUMN ssn SET MASK mask_ssn;
```

---

## Self-Assessment Questions

1. What is the purpose of VNet injection?
2. How does Private Link improve security?
3. What's the difference between CMK and default encryption?
4. How does SCIM help with identity management?
5. What Unity Catalog features support GDPR compliance?

---

## Recommended Additional Reading

- [Secure cluster connectivity](https://docs.databricks.com/en/security/network/secure-cluster-connectivity.html)
- [Secret management](https://docs.databricks.com/en/security/secrets/index.html)
- [Row filters and column masks](https://docs.databricks.com/en/data-governance/unity-catalog/row-and-column-filters.html)
- [Audit log schema](https://docs.databricks.com/en/administration-guide/account-settings/audit-logs.html)

---

*Pre-reading materials for Databricks Platform Administration Training - Day 18*
