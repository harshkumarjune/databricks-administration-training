# Day 18 Quiz: Security & Compliance

## Databricks Platform Administration Training
### Duration: 10 Minutes | 10 Questions | 70% to Pass

---

### Question 1
What is the purpose of VNet injection (Network isolation) for Databricks?

- [ ] A) To increase query performance
- [ ] B) To deploy clusters within your own virtual network for network isolation
- [ ] C) To reduce storage costs
- [ ] D) To enable Unity Catalog

---

### Question 2
What does Private Link provide for Databricks connectivity?

- [ ] A) Faster public internet access
- [ ] B) Private connectivity without traversing the public internet
- [ ] C) Free network bandwidth
- [ ] D) Automatic DNS resolution only

---

### Question 3
What is the purpose of IP Access Lists in Databricks?

- [ ] A) To block all external traffic
- [ ] B) To restrict access to the workspace from approved IP addresses only
- [ ] C) To speed up network connections
- [ ] D) To manage DNS entries

---

### Question 4
What is Customer-Managed Keys (CMK) encryption used for?

- [ ] A) Encrypting network traffic only
- [ ] B) Encrypting data at rest with keys you control
- [ ] C) Encrypting user passwords
- [ ] D) Encrypting cluster policies

---

### Question 5
Which Unity Catalog feature masks sensitive columns based on user permissions?

- [ ] A) Row-level security
- [ ] B) Column masking (Dynamic Data Masking)
- [ ] C) Schema binding
- [ ] D) Table partitioning

---

### Question 6
What SOC 2 control requires audit logging of all data access?

- [ ] A) Change management
- [ ] B) Incident response
- [ ] C) Logging and monitoring
- [ ] D) Physical security

---

### Question 7
How does GDPR's "Right to Erasure" get implemented in Databricks?

- [ ] A) Automatic data deletion
- [ ] B) DELETE statements on Delta tables with compliance tracking
- [ ] C) Table drops only
- [ ] D) GDPR is not applicable to Databricks

---

### Question 8
What is the purpose of SCIM (System for Cross-domain Identity Management) integration?

- [ ] A) To manage cluster configurations
- [ ] B) To automatically sync users and groups from your identity provider
- [ ] C) To encrypt data at rest
- [ ] D) To schedule jobs

---

### Question 9
Which access mode in Unity Catalog provides row-level and column-level security?

- [ ] A) No Isolation Shared
- [ ] B) Single User or Shared mode
- [ ] C) Custom mode
- [ ] D) Legacy High Concurrency

---

### Question 10
What is the recommended retention period for audit logs in compliance frameworks?

- [ ] A) 7 days
- [ ] B) 30 days minimum
- [ ] C) 90 days to 1 year depending on framework
- [ ] D) No retention required

---

## Answer Key

| Q | Answer | Explanation |
|---|--------|-------------|
| 1 | B | VNet injection deploys compute in your VNet for network isolation and compliance |
| 2 | B | Private Link enables connectivity through private endpoints, not public internet |
| 3 | B | IP Access Lists whitelist approved IP ranges to restrict workspace access |
| 4 | B | CMK gives you control over encryption keys for data at rest |
| 5 | B | Column masking dynamically hides/redacts sensitive column values based on access |
| 6 | C | SOC 2 requires comprehensive logging of data access and system activities |
| 7 | B | DELETE operations with compliance tracking enable GDPR erasure requirements |
| 8 | B | SCIM automatically provisions/deprovisions users from IdP to Databricks |
| 9 | B | Single User and Shared modes support Unity Catalog's fine-grained security |
| 10 | C | Compliance frameworks typically require 90 days to 1 year audit log retention |

---

*Quiz Version: 3.0 | Databricks Platform Administration Training - Day 18*
