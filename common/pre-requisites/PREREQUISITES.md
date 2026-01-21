# Databricks Platform Administration Training
## Pre-requisites Guide

---

## Technical Requirements

### Hardware Requirements

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| **RAM** | 8 GB | 16 GB |
| **Display** | Single monitor | Dual monitors |
| **Internet** | 5 Mbps stable | 10+ Mbps |
| **Storage** | 10 GB free | 20 GB free |

### Software Requirements

| Software | Version | Purpose |
|----------|---------|---------|
| **Web Browser** | Chrome 90+ / Firefox 88+ / Edge 90+ | Databricks UI access |
| **Terminal** | Built-in or iTerm2/Windows Terminal | CLI operations |
| **Text Editor** | VS Code (recommended) | Configuration editing |
| **Git Client** | Git 2.30+ | Version control |

### Cloud Provider Access (One of the following)

- **AWS**: Basic understanding of IAM, S3, VPC
- **Azure**: Basic understanding of Azure AD, Blob Storage, VNet
- **GCP**: Basic understanding of IAM, Cloud Storage, VPC

---

## Knowledge Prerequisites

### Required Knowledge (Must Have)

1. **Cloud Computing Fundamentals**
   - Understanding of cloud service models (IaaS, PaaS, SaaS)
   - Basic networking concepts (VPC, subnets, security groups)
   - Identity and access management concepts

2. **Data Concepts**
   - Understanding of structured vs unstructured data
   - Basic SQL knowledge (SELECT, JOIN, WHERE)
   - Familiarity with data formats (CSV, JSON, Parquet)

3. **Basic Administration Skills**
   - User and group management
   - Permission and access control concepts
   - Basic troubleshooting methodology

### Recommended Knowledge (Nice to Have)

1. **Apache Spark Basics**
   - Understanding of distributed computing
   - Spark architecture concepts
   - Basic PySpark or Scala

2. **Data Engineering Concepts**
   - ETL/ELT pipelines
   - Data lakehouse architecture
   - Delta Lake basics

3. **DevOps/Automation**
   - REST API concepts
   - Infrastructure as Code basics
   - CI/CD fundamentals

---

## Pre-Assessment Checklist

### Self-Assessment Questions

Rate your comfort level (1-5) with each topic:

| Topic | Rating (1-5) | Required Level |
|-------|--------------|----------------|
| Cloud console navigation | ___ | 3+ |
| User/Group management | ___ | 3+ |
| SQL queries | ___ | 3+ |
| REST APIs | ___ | 2+ |
| Networking basics | ___ | 3+ |
| Security concepts | ___ | 3+ |

**Scoring:**
- 18-30: Well prepared
- 12-17: Review recommended topics
- Below 12: Complete foundational training first

---

## Pre-Training Setup Tasks

### 1. Databricks Account Access (Provided by Trainer)
- [ ] Receive workspace URL
- [ ] Receive login credentials
- [ ] Successfully log in to workspace
- [ ] Navigate to Admin Console

### 2. Cloud Provider Console Access
- [ ] Verify access to cloud console (AWS/Azure/GCP)
- [ ] Confirm IAM permissions for viewing resources
- [ ] Locate storage account/bucket used by Databricks

### 3. Development Environment Setup
- [ ] Install VS Code or preferred editor
- [ ] Install Databricks CLI (optional but recommended)
- [ ] Configure Git client
- [ ] Set up SSH keys (if required)

### 4. Network Connectivity
- [ ] Verify VPN connection (if corporate network)
- [ ] Confirm no firewall blocking Databricks domains
- [ ] Test video conferencing tool

---

## Recommended Pre-Reading

### Essential Reading (Complete Before Day 1)

1. **Databricks Architecture Overview**
   - [What is Databricks?](https://docs.databricks.com/en/introduction/index.html)
   - Time: 30 minutes

2. **Lakehouse Concept**
   - [What is a Data Lakehouse?](https://www.databricks.com/glossary/data-lakehouse)
   - Time: 20 minutes

3. **Unity Catalog Introduction**
   - [Unity Catalog Overview](https://docs.databricks.com/en/data-governance/unity-catalog/index.html)
   - Time: 30 minutes

### Optional Deep Dives

1. **Cloud-Specific Documentation**
   - AWS: [Databricks on AWS](https://docs.databricks.com/en/getting-started/index.html)
   - Azure: [Azure Databricks](https://learn.microsoft.com/en-us/azure/databricks/)
   - GCP: [Databricks on GCP](https://docs.gcp.databricks.com/)

2. **Administration Guide**
   - [Account and Workspace Administration](https://docs.databricks.com/en/admin/index.html)
   - Time: 45 minutes

---

## Troubleshooting Common Setup Issues

### Cannot Access Databricks Workspace

1. **Check URL format**: `https://<workspace-name>.cloud.databricks.com`
2. **Verify credentials**: Case-sensitive
3. **Check network**: Try different network (non-VPN)
4. **Clear browser cache**: Force refresh (Ctrl+Shift+R)

### Cloud Console Access Issues

1. **IAM Permissions**: Contact your cloud admin
2. **MFA Issues**: Ensure authenticator app is synced
3. **Session Timeout**: Re-authenticate

### Browser Compatibility Issues

1. **Use supported browser**: Chrome or Firefox recommended
2. **Disable conflicting extensions**: Ad blockers may interfere
3. **Enable JavaScript**: Required for Databricks UI

---

## Contact Information

### Training Support

- **Trainer Email**: [To be provided]
- **Training Portal**: [To be provided]
- **Technical Support**: Create support ticket in training portal

### Emergency Contacts

- **Training Coordinator**: [To be provided]
- **IT Support**: [To be provided]

---

*Document Version: 1.0 | Last Updated: January 2026*
