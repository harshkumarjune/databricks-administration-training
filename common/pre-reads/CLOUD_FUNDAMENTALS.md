# Cloud Fundamentals Pre-Reading

## Databricks Platform Administration Training
### Cloud Provider Foundations

---

## Overview

This document covers the cloud computing fundamentals needed for Databricks administration. Focus on the cloud provider relevant to your organization.

**Estimated Reading Time**: 45-60 minutes

---

## Required Knowledge by Cloud Provider

### AWS Fundamentals

**Key Services to Understand**:

| Service | Purpose in Databricks |
|---------|----------------------|
| **IAM** | Identity and access management |
| **S3** | Data storage (Data Plane) |
| **VPC** | Network isolation |
| **EC2** | Compute instances for clusters |
| **KMS** | Encryption key management |

**Essential Concepts**:
- IAM Roles vs IAM Users
- S3 bucket policies
- VPC subnets and security groups
- Cross-account access patterns

**Recommended Reading**:
- [AWS IAM Documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/)
- [Amazon S3 User Guide](https://docs.aws.amazon.com/s3/)

---

### Azure Fundamentals

**Key Services to Understand**:

| Service | Purpose in Databricks |
|---------|----------------------|
| **Azure AD** | Identity management |
| **Blob Storage / ADLS Gen2** | Data storage |
| **VNet** | Network isolation |
| **Key Vault** | Secret and key management |
| **Virtual Machines** | Compute for clusters |

**Essential Concepts**:
- Azure AD vs Entra ID
- Service Principals
- Managed Identities
- Storage account access tiers

**Recommended Reading**:
- [Azure Active Directory Documentation](https://docs.microsoft.com/en-us/azure/active-directory/)
- [Azure Storage Documentation](https://docs.microsoft.com/en-us/azure/storage/)

---

### GCP Fundamentals

**Key Services to Understand**:

| Service | Purpose in Databricks |
|---------|----------------------|
| **IAM** | Identity and access management |
| **Cloud Storage (GCS)** | Data storage |
| **VPC** | Network isolation |
| **Cloud KMS** | Encryption key management |
| **Compute Engine** | VMs for clusters |

**Essential Concepts**:
- Service Accounts
- IAM roles and bindings
- Organization and project hierarchy
- Workload Identity Federation

**Recommended Reading**:
- [Google Cloud IAM Documentation](https://cloud.google.com/iam/docs)
- [Cloud Storage Documentation](https://cloud.google.com/storage/docs)

---

## Common Cloud Concepts

### Identity and Access Management

```
Principal (Who?) → Permission (What?) → Resource (Where?)

Examples:
- User alice@company.com → Read access → S3 bucket data-lake
- Service Account databricks-sa → Admin → Workspace production
- Group data-engineers → ReadWrite → Schema sales.gold
```

---

### Cloud Networking Basics

```
VPC/VNet Structure:
┌─────────────────────────────────────────┐
│              VPC (10.0.0.0/16)          │
│  ┌───────────────┐  ┌───────────────┐   │
│  │ Public Subnet │  │ Private Subnet│   │
│  │ 10.0.1.0/24   │  │ 10.0.2.0/24   │   │
│  │               │  │               │   │
│  │ ┌───────────┐ │  │ ┌───────────┐ │   │
│  │ │ NAT GW    │ │  │ │ Databricks│ │   │
│  │ └───────────┘ │  │ │ Clusters  │ │   │
│  └───────────────┘  └───────────────┘   │
│                                         │
│  ┌───────────────────────────────────┐  │
│  │       Security Group / NSG         │  │
│  │  - Inbound: 443 from Control Plane │  │
│  │  - Outbound: 443 to Internet       │  │
│  └───────────────────────────────────┘  │
└─────────────────────────────────────────┘
```

---

### Cloud Storage Hierarchy

**AWS S3**:
```
Bucket → Folder (Prefix) → Object
s3://my-bucket/data/bronze/orders/file.parquet
```

**Azure ADLS Gen2**:
```
Storage Account → Container → Directory → Blob
abfss://container@account.dfs.core.windows.net/data/bronze/orders/file.parquet
```

**GCP Cloud Storage**:
```
Bucket → Object (with path)
gs://my-bucket/data/bronze/orders/file.parquet
```

---

## Key Terminology

| Term | Definition |
|------|------------|
| **IAM** | Identity and Access Management |
| **Principal** | Entity that can request access (user, group, service) |
| **Policy** | Document defining permissions |
| **Role** | Collection of permissions |
| **VPC/VNet** | Virtual Private Cloud/Network |
| **Subnet** | Segment of IP addresses within a VPC |
| **Security Group/NSG** | Virtual firewall for resources |
| **NAT Gateway** | Enables private subnet internet access |
| **Private Link/Endpoint** | Private connectivity to services |

---

## Self-Assessment Questions

1. What is the difference between IAM users and IAM roles?
2. How do security groups control network traffic?
3. What is the purpose of a NAT gateway?
4. How is cloud storage organized in your cloud provider?
5. What is a service principal / service account used for?

---

*Cloud Fundamentals Pre-Reading for Databricks Platform Administration Training*
