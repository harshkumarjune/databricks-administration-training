# Week 3 Checkpoint Assessment
## Databricks Platform Administration Training
### Security & Compute Management (Days 11-15)

**Duration:** 20 Minutes | 15 Questions | 70% to Pass (11/15)

---

## Instructions

This checkpoint assessment covers material from Week 3 (Days 11-15):
- Day 11: SCIM Provisioning & SSO
- Day 12: Network Security & Private Connectivity
- Day 13: Data Security & Encryption
- Day 14: Cluster Architecture & Types
- Day 15: Cluster Policies & SQL Warehouses

Complete all questions before checking the answer key.

---

### Question 1
What protocol does SCIM use for automatic user and group synchronization?

- [ ] A) LDAP
- [ ] B) REST API
- [ ] C) SOAP
- [ ] D) GraphQL

---

### Question 2
Which SSO protocol is most commonly used with Databricks for enterprise authentication?

- [ ] A) OAuth 1.0
- [ ] B) Kerberos
- [ ] C) SAML 2.0
- [ ] D) Basic Auth

---

### Question 3
What is the primary purpose of VNet/VPC injection in Databricks?

- [ ] A) Increase cluster performance
- [ ] B) Deploy clusters within customer's virtual network for network isolation
- [ ] C) Reduce storage costs
- [ ] D) Enable auto-scaling

---

### Question 4
Which connectivity option ensures Databricks traffic never traverses the public internet?

- [ ] A) IP access lists
- [ ] B) Private Link / PrivateLink
- [ ] C) VPN gateway
- [ ] D) Firewall rules

---

### Question 5
What does CMK (Customer Managed Keys) provide?

- [ ] A) Faster data processing
- [ ] B) Customer control over encryption keys used for data at rest
- [ ] C) Network security
- [ ] D) User authentication

---

### Question 6
Which feature allows different users to see different data in the same table based on their attributes?

- [ ] A) Column masking
- [ ] B) Row-level security
- [ ] C) Table partitioning
- [ ] D) Data caching

---

### Question 7
What is the main difference between All-Purpose and Job clusters?

- [ ] A) All-Purpose clusters are faster
- [ ] B) Job clusters automatically terminate after job completion; All-Purpose persist
- [ ] C) Job clusters support more workers
- [ ] D) All-Purpose clusters don't support Spark

---

### Question 8
Which cluster configuration is recommended for scheduled ETL production workloads?

- [ ] A) All-Purpose with auto-termination disabled
- [ ] B) Job clusters
- [ ] C) Single-node clusters
- [ ] D) High-concurrency clusters

---

### Question 9
What is the purpose of cluster autoscaling?

- [ ] A) Automatically upgrade Spark versions
- [ ] B) Dynamically adjust worker count based on workload
- [ ] C) Automatically restart failed clusters
- [ ] D) Scale storage capacity

---

### Question 10
In cluster policy JSON, which attribute type restricts values to a predefined list?

- [ ] A) `"type": "range"`
- [ ] B) `"type": "fixed"`
- [ ] C) `"type": "allowlist"`
- [ ] D) `"type": "unlimited"`

---

### Question 11
What does `"isOptional": false` mean in a cluster policy attribute?

- [ ] A) The attribute cannot be changed
- [ ] B) Users must provide a value for this attribute
- [ ] C) The attribute is hidden from users
- [ ] D) The attribute has a default value

---

### Question 12
Which SQL Warehouse type provides instant startup with no infrastructure management?

- [ ] A) Classic
- [ ] B) Pro
- [ ] C) Serverless
- [ ] D) Standard

---

### Question 13
What is the recommended auto-termination setting for development clusters to balance cost and convenience?

- [ ] A) 5 minutes
- [ ] B) 15-30 minutes
- [ ] C) 2 hours
- [ ] D) Auto-termination should be disabled

---

### Question 14
Which cloud feature provides cost savings by using spare compute capacity at reduced prices?

- [ ] A) Reserved instances
- [ ] B) Spot instances
- [ ] C) Dedicated hosts
- [ ] D) Burstable instances

---

### Question 15
In a cluster policy, how do you enforce a specific Spark version?

- [ ] A) `"spark_version": {"type": "unlimited", "value": "14.3.x"}`
- [ ] B) `"spark_version": {"type": "fixed", "value": "14.3.x-scala2.12"}`
- [ ] C) `"spark_version": {"type": "required", "value": "14.3.x"}`
- [ ] D) `"spark_version": {"type": "allowlist", "value": "14.3.x"}`

---

## Answer Key

| Q | Answer | Explanation |
|---|--------|-------------|
| 1 | B | SCIM uses REST API for cross-domain identity management |
| 2 | C | SAML 2.0 is the standard enterprise SSO protocol used with Databricks |
| 3 | B | VNet injection deploys clusters in customer's network for isolation |
| 4 | B | Private Link provides private connectivity without public internet |
| 5 | B | CMK gives customers control over encryption keys for data at rest |
| 6 | B | Row-level security filters table data based on user attributes |
| 7 | B | Job clusters auto-terminate after job completion; All-Purpose persist |
| 8 | B | Job clusters are recommended for scheduled workloads (cost-effective) |
| 9 | B | Autoscaling dynamically adjusts worker count based on workload |
| 10 | C | Allowlist restricts values to a predefined list of options |
| 11 | B | isOptional: false makes the attribute mandatory (user must provide value) |
| 12 | C | Serverless SQL Warehouses provide instant startup, no management |
| 13 | B | 15-30 minutes balances cost savings with development convenience |
| 14 | B | Spot instances use spare capacity at 60-90% discount |
| 15 | B | type: fixed with value enforces a specific Spark version |

---

## Score Interpretation

| Score | Interpretation | Recommendation |
|-------|----------------|----------------|
| 13-15 (87-100%) | Excellent | Ready for Week 4 material |
| 11-12 (70-80%) | Good | Review weak areas before continuing |
| 8-10 (53-67%) | Needs Improvement | Review Days 11-15 materials |
| <8 (<53%) | Requires Remediation | Revisit Week 3 content before continuing |

---

## Topics to Review if Struggling

### If Questions 1-2 Were Difficult:
Review Day 11 - SCIM & SSO:
- SCIM protocol and purpose
- SAML SSO flow
- IdP configuration

### If Questions 3-4 Were Difficult:
Review Day 12 - Network Security:
- VNet/VPC injection benefits
- Private Link configuration
- IP access lists

### If Questions 5-6 Were Difficult:
Review Day 13 - Data Security:
- CMK (Customer Managed Keys)
- Column masking functions
- Row-level security policies

### If Questions 7-9 Were Difficult:
Review Day 14 - Cluster Architecture:
- Cluster types and use cases
- All-Purpose vs Job clusters
- Autoscaling configuration

### If Questions 10-15 Were Difficult:
Review Day 15 - Cluster Policies & SQL Warehouses:
- Policy JSON syntax (fixed, range, allowlist, regex)
- Policy attribute options
- SQL Warehouse types (Serverless, Pro, Classic)

---

## Cluster Policy Quick Reference

| Attribute Type | Purpose | Example |
|----------------|---------|---------|
| `fixed` | Force specific value | Version lock |
| `range` | Allow numeric range | Worker count 2-8 |
| `allowlist` | Limit to predefined options | Instance types |
| `regex` | Pattern matching | Version patterns |
| `unlimited` | No restrictions | Custom tags |

---

*Checkpoint Version: 3.0 | Databricks Platform Administration Training - Week 3*
