# Day 12 Quiz: Infrastructure, Compliance & Cost Governance

## Databricks Platform Administration Training
### Duration: 10 Minutes | 10 Questions | 70% to Pass

---

### Question 1
What does Private Link provide in Databricks?

- [ ] A) Faster query performance
- [ ] B) Private connectivity without using public internet
- [ ] C) Lower storage costs
- [ ] D) Automatic data encryption

---

### Question 2
What is Secure Cluster Connectivity (SCC)?

- [ ] A) Encryption of data at rest
- [ ] B) Clusters without public IP addresses
- [ ] C) SSO configuration
- [ ] D) SCIM provisioning

---

### Question 3
Which compliance framework is specific to healthcare data?

- [ ] A) PCI DSS
- [ ] B) SOC 2
- [ ] C) HIPAA
- [ ] D) ISO 27001

---

### Question 4
What is the primary unit for measuring Databricks compute costs?

- [ ] A) CPU hours
- [ ] B) DBU (Databricks Unit)
- [ ] C) Memory GB
- [ ] D) Storage TB

---

### Question 5
Which instance type strategy provides the highest cost savings for batch workloads?

- [ ] A) On-demand instances
- [ ] B) Reserved instances
- [ ] C) Spot/Preemptible instances
- [ ] D) Dedicated hosts

---

### Question 6
What is the recommended approach for the driver node when using Spot instances?

- [ ] A) Use Spot for driver to maximize savings
- [ ] B) Keep driver on-demand for stability
- [ ] C) Don't use any driver node
- [ ] D) Use GPU instances for driver

---

### Question 7
What is the purpose of tagging clusters in Databricks?

- [ ] A) Improve query performance
- [ ] B) Enable cost allocation and chargeback
- [ ] C) Increase cluster capacity
- [ ] D) Speed up cluster startup

---

### Question 8
Which feature allows you to enforce tagging requirements on clusters?

- [ ] A) Unity Catalog
- [ ] B) Cluster Policies
- [ ] C) SQL Warehouses
- [ ] D) Delta Lake

---

### Question 9
What does Customer-Managed Keys (CMK) provide?

- [ ] A) Faster data access
- [ ] B) Control over encryption keys used for data protection
- [ ] C) Automatic backup
- [ ] D) Network routing

---

### Question 10
Where can you track DBU consumption for cost analysis?

- [ ] A) system.access.audit
- [ ] B) system.billing.usage
- [ ] C) system.compute.clusters
- [ ] D) system.workflow.jobs

---

## Answer Key

| Q | Answer | Explanation |
|---|--------|-------------|
| 1 | B | Private Link enables connectivity without traversing public internet |
| 2 | B | SCC ensures cluster nodes have no public IP addresses |
| 3 | C | HIPAA is the healthcare-specific compliance framework |
| 4 | B | DBU (Databricks Unit) is the standard compute billing metric |
| 5 | C | Spot instances provide 60-90% savings for interruptible workloads |
| 6 | B | Driver should be on-demand for stability; only workers use Spot |
| 7 | B | Tags enable cost allocation, tracking, and chargeback to teams |
| 8 | B | Cluster Policies enforce configuration standards including tags |
| 9 | B | CMK provides customer control over encryption keys |
| 10 | B | system.billing.usage contains DBU consumption data |

---

*Quiz Version: 2.0 | Databricks Platform Administration Training - Day 12*
