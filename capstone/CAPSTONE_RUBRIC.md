# Capstone Project Evaluation Rubric

## Databricks Platform Administration Training
### Detailed Scoring Criteria for Evaluators

---

## Evaluation Overview

| Category | Points | Weight |
|----------|--------|--------|
| Unity Catalog Design | 15 | 15% |
| Access Control | 15 | 15% |
| Compute Governance | 15 | 15% |
| Job Design | 10 | 10% |
| Cost Monitoring | 10 | 10% |
| Security Configuration | 15 | 15% |
| Documentation | 10 | 10% |
| Best Practices | 10 | 10% |
| **Total** | **100** | **100%** |

---

## Category 1: Unity Catalog Design (15 Points)

### Catalog Structure (5 points)

| Score | Criteria |
|-------|----------|
| 5 | Logical environment separation (dev/staging/prod), clear domain organization, proper medallion layers, sandbox for experimentation |
| 4 | Good structure with minor issues (e.g., missing one environment or inconsistent naming) |
| 3 | Basic structure present but missing key elements (e.g., no medallion architecture) |
| 2 | Incomplete structure, significant gaps in design |
| 1 | Minimal attempt, major design flaws |
| 0 | Not attempted |

### Storage Locations (5 points)

| Score | Criteria |
|-------|----------|
| 5 | Appropriate external locations defined, clear separation by environment/purpose, follows cloud best practices |
| 4 | Good location design with minor omissions |
| 3 | Basic locations defined but missing environment separation |
| 2 | Incomplete or poorly organized locations |
| 1 | Minimal attempt |
| 0 | Not attempted |

### Table Strategy (5 points)

| Score | Criteria |
|-------|----------|
| 5 | Clear rationale for managed vs external tables, appropriate choices for each data type, compliance considerations addressed |
| 4 | Good strategy with minor gaps in reasoning |
| 3 | Basic strategy without clear justification |
| 2 | Incomplete or inconsistent approach |
| 1 | Minimal attempt |
| 0 | Not attempted |

---

## Category 2: Access Control (15 Points)

### Group Structure (5 points)

| Score | Criteria |
|-------|----------|
| 5 | Role-based groups aligned with organizational structure, clear purpose for each group, supports principle of least privilege |
| 4 | Good group structure with minor issues |
| 3 | Basic groups defined but not role-aligned |
| 2 | Incomplete or poorly organized groups |
| 1 | Minimal attempt |
| 0 | Not attempted |

### Permission Matrix (5 points)

| Score | Criteria |
|-------|----------|
| 5 | Complete matrix showing all groups/environments, appropriate permission levels, least privilege enforced, Finance data properly restricted |
| 4 | Good matrix with minor gaps |
| 3 | Basic matrix incomplete or overly permissive |
| 2 | Significant gaps or security issues |
| 1 | Minimal attempt |
| 0 | Not attempted |

### SQL Statements (5 points)

| Score | Criteria |
|-------|----------|
| 5 | Syntactically correct GRANT statements, proper use of USAGE and data privileges, includes all required groups |
| 4 | Mostly correct with minor syntax issues |
| 3 | Basic statements with notable errors |
| 2 | Incomplete or largely incorrect |
| 1 | Minimal attempt |
| 0 | Not attempted |

---

## Category 3: Compute Governance (15 Points)

### Development Policy (5 points)

| Score | Criteria |
|-------|----------|
| 5 | Cost-controlled (small instances, auto-terminate, worker limits), flexible runtime, proper tagging required |
| 4 | Good policy with minor oversights |
| 3 | Basic policy missing key cost controls |
| 2 | Incomplete or ineffective policy |
| 1 | Minimal attempt |
| 0 | Not attempted |

### Production Policy (5 points)

| Score | Criteria |
|-------|----------|
| 5 | Stable configuration (LTS runtime), appropriate scaling, fixed tags, no excessive restrictions that impact production |
| 4 | Good policy with minor issues |
| 3 | Basic policy with stability concerns |
| 2 | Incomplete or inappropriate for production |
| 1 | Minimal attempt |
| 0 | Not attempted |

### ML/Data Science Policy (5 points)

| Score | Criteria |
|-------|----------|
| 5 | ML runtime specified, GPU option available, appropriate auto-terminate for long-running experiments, proper tagging |
| 4 | Good policy with minor gaps |
| 3 | Basic ML policy missing key features |
| 2 | Incomplete or not suitable for ML workloads |
| 1 | Minimal attempt |
| 0 | Not attempted |

---

## Category 4: Job Design (10 Points)

### Workflow Structure (5 points)

| Score | Criteria |
|-------|----------|
| 5 | Logical task dependencies, appropriate task types, proper cluster allocation, clear execution flow |
| 4 | Good workflow with minor issues |
| 3 | Basic workflow with unclear dependencies |
| 2 | Incomplete or poorly structured |
| 1 | Minimal attempt |
| 0 | Not attempted |

### Job Configuration (5 points)

| Score | Criteria |
|-------|----------|
| 5 | Appropriate trigger type, sensible concurrent run limits, retry policy defined, alerts configured, timeout set |
| 4 | Good configuration with minor omissions |
| 3 | Basic configuration missing key settings |
| 2 | Incomplete or inappropriate settings |
| 1 | Minimal attempt |
| 0 | Not attempted |

---

## Category 5: Cost Monitoring (10 Points)

### Monitoring Queries (5 points)

| Score | Criteria |
|-------|----------|
| 5 | Syntactically correct SQL, queries system.billing.usage appropriately, meaningful aggregations by team/environment, tag compliance check included |
| 4 | Good queries with minor issues |
| 3 | Basic queries with errors or missing key dimensions |
| 2 | Incomplete or largely incorrect |
| 1 | Minimal attempt |
| 0 | Not attempted |

### Dashboard & Alerts (5 points)

| Score | Criteria |
|-------|----------|
| 5 | Dashboard design includes key metrics (daily trend, by team, by SKU, compliance), alerts have appropriate thresholds and recipients |
| 4 | Good design with minor gaps |
| 3 | Basic design missing key elements |
| 2 | Incomplete or unfocused |
| 1 | Minimal attempt |
| 0 | Not attempted |

---

## Category 6: Security Configuration (15 Points)

### Network Security (5 points)

| Score | Criteria |
|-------|----------|
| 5 | Private Link considered, SCC enabled, IP access lists configured, VPC peering addressed, clear justifications provided |
| 4 | Good configuration with minor gaps |
| 3 | Basic security missing key features |
| 2 | Incomplete or insecure configuration |
| 1 | Minimal attempt |
| 0 | Not attempted |

### Data Security (5 points)

| Score | Criteria |
|-------|----------|
| 5 | Encryption at rest and in transit addressed, CMK considered for compliance, column/row-level security designed for sensitive data |
| 4 | Good security with minor omissions |
| 3 | Basic security missing advanced features |
| 2 | Incomplete or insufficient protection |
| 1 | Minimal attempt |
| 0 | Not attempted |

### Compliance Controls (5 points)

| Score | Criteria |
|-------|----------|
| 5 | SOC 2 audit logging addressed, GDPR data access controls, retention policies defined, access review process documented |
| 4 | Good compliance coverage with minor gaps |
| 3 | Basic compliance missing key requirements |
| 2 | Incomplete or non-compliant |
| 1 | Minimal attempt |
| 0 | Not attempted |

---

## Category 7: Documentation (10 Points)

### Architecture Summary (5 points)

| Score | Criteria |
|-------|----------|
| 5 | Clear executive summary, covers key decisions and rationale, appropriate for stakeholder communication |
| 4 | Good summary with minor improvements needed |
| 3 | Basic summary lacking key elements |
| 2 | Incomplete or unclear |
| 1 | Minimal attempt |
| 0 | Not attempted |

### Runbook Outline (5 points)

| Score | Criteria |
|-------|----------|
| 5 | Comprehensive outline covering daily/weekly/monthly tasks and incident response, actionable and clear |
| 4 | Good outline with minor gaps |
| 3 | Basic outline missing key operational tasks |
| 2 | Incomplete or not actionable |
| 1 | Minimal attempt |
| 0 | Not attempted |

---

## Category 8: Best Practices (10 Points)

### Industry Standards (5 points)

| Score | Criteria |
|-------|----------|
| 5 | Follows Databricks recommended practices, uses established patterns (medallion, least privilege), considers scalability |
| 4 | Good adherence with minor deviations |
| 3 | Basic adherence with notable gaps |
| 2 | Multiple deviations from best practices |
| 1 | Minimal adherence |
| 0 | Not attempted |

### Completeness & Consistency (5 points)

| Score | Criteria |
|-------|----------|
| 5 | All sections complete, consistent naming conventions throughout, logical integration across components |
| 4 | Mostly complete with minor inconsistencies |
| 3 | Notable gaps or inconsistencies |
| 2 | Multiple incomplete sections |
| 1 | Largely incomplete |
| 0 | Not attempted |

---

## Grading Scale

| Total Score | Grade | Interpretation |
|-------------|-------|----------------|
| 90-100 | A | Exceptional - Demonstrates mastery of platform administration concepts |
| 80-89 | B | Proficient - Strong understanding with minor gaps |
| 70-79 | C | Competent - Meets requirements with areas for improvement |
| 60-69 | D | Developing - Significant gaps requiring additional study |
| < 60 | F | Insufficient - Does not meet minimum requirements |

---

## Feedback Template

```markdown
# Capstone Evaluation: [Participant Name]

## Overall Score: [X]/100 ([Grade])

### Strengths
-
-
-

### Areas for Improvement
-
-
-

### Category Scores

| Category | Score | Notes |
|----------|-------|-------|
| Unity Catalog Design | /15 | |
| Access Control | /15 | |
| Compute Governance | /15 | |
| Job Design | /10 | |
| Cost Monitoring | /10 | |
| Security Configuration | /15 | |
| Documentation | /10 | |
| Best Practices | /10 | |

### Recommendations for Further Study
-
-

### Certification Readiness
[ ] Ready for certification exam
[ ] Ready with minor review
[ ] Additional preparation recommended
```

---

## Evaluator Notes

### Common Deductions

| Issue | Typical Deduction |
|-------|-------------------|
| Missing environment separation | -2 to -4 |
| Overly permissive access | -3 to -5 |
| No cost controls in cluster policies | -2 to -4 |
| Missing compliance considerations | -2 to -4 |
| Incomplete SQL syntax | -1 to -3 |
| No tag strategy | -2 to -3 |
| Missing incident response | -2 |

### Bonus Considerations

Evaluators may award up to 5 bonus points for:
- Innovative solutions to complex requirements
- Exceptional documentation quality
- Additional security measures beyond requirements
- Cost optimization strategies beyond the basics

---

*Rubric Version: 2.0 | Databricks Platform Administration Training*
