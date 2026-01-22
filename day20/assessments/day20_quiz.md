# Day 20 Quiz: Capstone Review & Certification Prep
## Databricks Platform Administration Training
### Duration: 10 Minutes | 10 Questions | 70% to Pass

---

### Question 1
When designing a Unity Catalog hierarchy for a multi-environment enterprise, what is the recommended approach?

- [ ] A) One catalog per table
- [ ] B) Separate catalogs per environment (dev, staging, prod)
- [ ] C) One catalog for all environments with schema-level separation
- [ ] D) Catalogs are not needed; use schemas only

---

### Question 2
Which cluster policy attribute type would you use to limit worker count to a specific range (e.g., 2-8 workers)?

- [ ] A) `"type": "fixed"`
- [ ] B) `"type": "range"`
- [ ] C) `"type": "allowlist"`
- [ ] D) `"type": "unlimited"`

---

### Question 3
What is the correct order of privilege inheritance in Unity Catalog?

- [ ] A) Table → Schema → Catalog → Metastore
- [ ] B) Metastore → Catalog → Schema → Table
- [ ] C) Schema → Catalog → Table → Metastore
- [ ] D) Catalog → Metastore → Schema → Table

---

### Question 4
For SOC 2 compliance, which Databricks feature provides evidence of access control implementation?

- [ ] A) Cluster autoscaling logs
- [ ] B) Unity Catalog audit logs (system.access.audit)
- [ ] C) Job scheduling history
- [ ] D) Spark executor metrics

---

### Question 5
What CRON expression schedules a job to run at 2:00 AM every day?

- [ ] A) `* 2 * * *`
- [ ] B) `0 2 * * *`
- [ ] C) `2 0 * * *`
- [ ] D) `0 0 2 * *`

---

### Question 6
Which approach is most cost-effective for scheduled ETL workloads?

- [ ] A) All-Purpose clusters with auto-termination disabled
- [ ] B) Job clusters that terminate after each run
- [ ] C) SQL Warehouses in Classic mode
- [ ] D) Interactive clusters shared across teams

---

### Question 7
To implement GDPR's "right to erasure," which Databricks capability is most relevant?

- [ ] A) Time travel to restore deleted data
- [ ] B) DELETE statements combined with VACUUM
- [ ] C) Column masking functions
- [ ] D) Row-level security policies

---

### Question 8
What is the purpose of the USAGE privilege in Unity Catalog?

- [ ] A) Allows users to read table data
- [ ] B) Allows users to write data to tables
- [ ] C) Grants access to browse and access objects within a securable
- [ ] D) Provides admin-level control over the object

---

### Question 9
Which cluster policy attribute enforces mandatory resource tagging for cost allocation?

- [ ] A) `"spark_conf.spark.databricks.tags"`
- [ ] B) `"custom_tags.Team": {"type": "unlimited", "isOptional": false}`
- [ ] C) `"cost_allocation": {"type": "required"}`
- [ ] D) `"billing_tags": {"type": "mandatory"}`

---

### Question 10
When troubleshooting a failed Spark job, what is the recommended first step?

- [ ] A) Immediately increase cluster size
- [ ] B) Delete and recreate the job
- [ ] C) Review error messages, check for recent changes, analyze Spark UI
- [ ] D) Switch to a different Spark version

---

## Answer Key

| Q | Answer | Explanation |
|---|--------|-------------|
| 1 | B | Separate catalogs per environment provides clear isolation and simplified permission management |
| 2 | B | `"type": "range"` with `minValue` and `maxValue` restricts to a numeric range |
| 3 | B | Inheritance flows from Metastore → Catalog → Schema → Table (top-down) |
| 4 | B | Audit logs provide evidence of who accessed what data and when, essential for SOC 2 |
| 5 | B | CRON format: minute hour day month weekday. `0 2 * * *` = minute 0, hour 2, every day |
| 6 | B | Job clusters are cost-effective because they automatically terminate after job completion |
| 7 | B | DELETE removes data; VACUUM permanently removes it beyond time travel recovery |
| 8 | C | USAGE is a gatekeeper privilege required to access objects within catalogs/schemas |
| 9 | B | `isOptional: false` makes the tag mandatory; users must provide a value |
| 10 | C | Systematic debugging: understand the error before making changes |

---

## Certification Readiness Check

If you scored 70% or higher on this quiz AND completed the capstone project, you demonstrate readiness for the Databricks Certified Associate Platform Administrator exam.

### Key Exam Topics Review

| Topic | Weight | Days Covered |
|-------|--------|--------------|
| Databricks Lakehouse Platform | 15% | 1-2, 7 |
| Workspace Administration | 20% | 3-5 |
| Identity and Access Management | 20% | 4-5, 10-11 |
| Unity Catalog | 15% | 8-9 |
| Compute Management | 15% | 6, 14-15 |
| Jobs and Workflows | 5% | 16 |
| Security and Networking | 5% | 12-13, 18 |
| Monitoring and Optimization | 5% | 17, 19 |

### Exam Tips

1. **Know the UI** - Be familiar with navigating Admin Console
2. **Understand concepts** - Focus on "why" not just "how"
3. **Time management** - ~90 seconds per question average
4. **Read carefully** - Watch for "BEST" vs "correct" answer wording
5. **Use flags** - If unsure, flag and return later

---

*Quiz Version: 3.0 | Databricks Platform Administration Training - Day 20*
