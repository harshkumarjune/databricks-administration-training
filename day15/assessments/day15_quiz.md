# Day 15 Quiz: Cluster Policies & SQL Warehouses

## Databricks Platform Administration Training
### Duration: 10 Minutes | 10 Questions | 70% to Pass

---

### Question 1
What is the primary purpose of a cluster policy?

- [ ] A) To increase cluster performance
- [ ] B) To enforce governance rules and cost controls on cluster configurations
- [ ] C) To monitor cluster usage
- [ ] D) To automatically terminate clusters

---

### Question 2
In a cluster policy, what does the "fixed" attribute type do?

- [ ] A) Makes the attribute optional
- [ ] B) Sets a value that users cannot change
- [ ] C) Allows any value within a range
- [ ] D) Hides the attribute from the UI

---

### Question 3
Which policy attribute type allows users to select from a predefined list?

- [ ] A) fixed
- [ ] B) range
- [ ] C) allowlist
- [ ] D) unlimited

---

### Question 4
What is the benefit of requiring custom tags in a cluster policy?

- [ ] A) Faster cluster startup
- [ ] B) Better query performance
- [ ] C) Cost allocation and chargeback tracking
- [ ] D) Increased security

---

### Question 5
What is the key difference between SQL Warehouse Serverless and Pro?

- [ ] A) Serverless supports larger data volumes
- [ ] B) Serverless eliminates infrastructure management and provides faster startup
- [ ] C) Pro is always faster
- [ ] D) Serverless costs 10x more

---

### Question 6
How do you increase concurrent query capacity for a SQL Warehouse?

- [ ] A) Decrease the warehouse size
- [ ] B) Increase the cluster count (horizontal scaling)
- [ ] C) Reduce auto-stop timeout
- [ ] D) Enable query caching only

---

### Question 7
What does the `isOptional: false` setting enforce in a policy attribute?

- [ ] A) The attribute is hidden from users
- [ ] B) Users must provide a value for this attribute
- [ ] C) The attribute has no default value
- [ ] D) The attribute only applies to admins

---

### Question 8
Which warehouse size is recommended for ad-hoc analyst queries?

- [ ] A) 2X-Small (always)
- [ ] B) Large or X-Large (always)
- [ ] C) Small to Medium with auto-scaling
- [ ] D) Serverless is not recommended

---

### Question 9
What is the purpose of the `hidden: true` setting in a policy attribute?

- [ ] A) Removes the attribute entirely
- [ ] B) Shows the attribute but prevents changes
- [ ] C) Hides the attribute from the UI while enforcing its value
- [ ] D) Allows admins only to see it

---

### Question 10
How can you grant users permission to use a specific cluster policy?

- [ ] A) Add them to workspace admins
- [ ] B) Grant CAN_USE permission on the policy
- [ ] C) Policies are automatically available to all users
- [ ] D) Users cannot be granted policy permissions

---

## Answer Key

| Q | Answer | Explanation |
|---|--------|-------------|
| 1 | B | Policies enforce constraints on cluster configs for governance and cost control |
| 2 | B | Fixed type sets a specific value that cannot be changed by users |
| 3 | C | Allowlist provides a defined set of valid options for users to select |
| 4 | C | Tags enable cost allocation, department chargeback, and resource tracking |
| 5 | B | Serverless eliminates management overhead and provides instant startup |
| 6 | B | Adding clusters (horizontal scaling) increases concurrent query capacity |
| 7 | B | isOptional: false makes the field required - users must provide a value |
| 8 | C | Small/Medium with auto-scaling balances cost and performance for ad-hoc use |
| 9 | C | Hidden attributes are enforced without appearing in the cluster creation UI |
| 10 | B | CAN_USE permission grants users ability to create clusters with that policy |

---

*Quiz Version: 3.0 | Databricks Platform Administration Training - Day 15*
