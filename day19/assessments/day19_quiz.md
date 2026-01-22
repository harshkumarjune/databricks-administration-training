# Day 19 Quiz: Cost Governance & Optimization

## Databricks Platform Administration Training
### Duration: 10 Minutes | 10 Questions | 70% to Pass

---

### Question 1
What is a DBU (Databricks Unit)?

- [ ] A) A unit of data storage
- [ ] B) A normalized unit of processing capability per hour
- [ ] C) A database backup unit
- [ ] D) A user license type

---

### Question 2
Which workload type typically has the highest DBU cost multiplier?

- [ ] A) Jobs Lite
- [ ] B) All-Purpose Compute
- [ ] C) SQL Warehouse Serverless
- [ ] D) Job clusters

---

### Question 3
What is the primary purpose of mandatory resource tagging?

- [ ] A) Improving query performance
- [ ] B) Enabling cost allocation and chargeback to teams
- [ ] C) Enhancing security
- [ ] D) Reducing storage costs

---

### Question 4
Which system table provides detailed billing and usage data?

- [ ] A) system.compute.clusters
- [ ] B) system.billing.usage
- [ ] C) system.access.audit
- [ ] D) system.tables.information

---

### Question 5
What cost optimization does auto-termination provide?

- [ ] A) Reduces storage costs
- [ ] B) Stops idle clusters to eliminate unnecessary compute charges
- [ ] C) Compresses data automatically
- [ ] D) Reduces network bandwidth usage

---

### Question 6
How can Spot instances reduce compute costs?

- [ ] A) They provide unlimited free compute
- [ ] B) They offer spare cloud capacity at 60-90% discount
- [ ] C) They are always faster than on-demand
- [ ] D) They eliminate the need for autoscaling

---

### Question 7
What is the recommended approach for cost alerts?

- [ ] A) No alerts needed - review monthly
- [ ] B) Alert only at 100% of budget
- [ ] C) Progressive thresholds: 50%, 75%, 90%, 100% of budget
- [ ] D) Alert only when budget is exceeded

---

### Question 8
What does tagging compliance percentage measure?

- [ ] A) Percentage of data that is encrypted
- [ ] B) Percentage of compute resources with proper cost allocation tags
- [ ] C) Percentage of users with MFA enabled
- [ ] D) Percentage of clusters using policies

---

### Question 9
Which cost optimization is best for SQL analytics workloads?

- [ ] A) Use all-purpose clusters
- [ ] B) Use serverless SQL warehouses with auto-scaling
- [ ] C) Disable caching
- [ ] D) Use the largest cluster policy

---

### Question 10
What is a chargeback report used for?

- [ ] A) Debugging query failures
- [ ] B) Billing back costs to individual teams or departments
- [ ] C) Monitoring security incidents
- [ ] D) Tracking user logins

---

## Answer Key

| Q | Answer | Explanation |
|---|--------|-------------|
| 1 | B | DBU is a normalized unit measuring processing capability per hour |
| 2 | B | All-Purpose clusters have higher DBU rates due to interactive capabilities |
| 3 | B | Tags enable tracking costs by team, project, environment for chargeback |
| 4 | B | system.billing.usage provides comprehensive billing data by SKU and tags |
| 5 | B | Auto-termination stops idle clusters, eliminating unnecessary compute costs |
| 6 | B | Spot instances use spare capacity at significant discounts (60-90% off) |
| 7 | C | Progressive thresholds enable proactive cost management before overspending |
| 8 | B | Tagging compliance measures what percentage of resources have required tags |
| 9 | B | Serverless SQL warehouses auto-scale and charge only for actual query time |
| 10 | B | Chargeback reports allocate costs back to the teams consuming resources |

---

*Quiz Version: 3.0 | Databricks Platform Administration Training - Day 19*
