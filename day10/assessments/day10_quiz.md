# Day 10 Quiz: Job Orchestration & CI/CD

## Databricks Platform Administration Training
### Duration: 10 Minutes | 10 Questions | 70% to Pass

---

### Question 1
What is the main difference between a job cluster and an all-purpose cluster for jobs?

- [ ] A) Job clusters are faster
- [ ] B) Job clusters are created per run and terminated after
- [ ] C) Job clusters support more languages
- [ ] D) All-purpose clusters cannot run jobs

---

### Question 2
What is a Databricks Workflow?

- [ ] A) A single notebook execution
- [ ] B) A multi-task job with dependencies between tasks
- [ ] C) A cluster configuration
- [ ] D) A data pipeline only

---

### Question 3
Which job trigger type automatically starts a job when new files arrive in cloud storage?

- [ ] A) Scheduled
- [ ] B) Manual
- [ ] C) File Arrival
- [ ] D) Continuous

---

### Question 4
What format is used for scheduled job triggers?

- [ ] A) ISO 8601 timestamps
- [ ] B) Cron expressions
- [ ] C) Unix timestamps
- [ ] D) Natural language

---

### Question 5
What is the recommended "Run As" identity for production jobs?

- [ ] A) Job creator's identity
- [ ] B) Admin user
- [ ] C) Service principal
- [ ] D) Anonymous

---

### Question 6
What are Databricks Asset Bundles (DABs)?

- [ ] A) Compressed notebook files
- [ ] B) Infrastructure as Code for Databricks resources
- [ ] C) Python packages
- [ ] D) Data storage containers

---

### Question 7
Which permission level allows a user to trigger and cancel job runs?

- [ ] A) CAN_VIEW
- [ ] B) CAN_MANAGE_RUN
- [ ] C) IS_OWNER
- [ ] D) CAN_EDIT

---

### Question 8
What happens when a task fails in a multi-task workflow?

- [ ] A) All tasks are cancelled immediately
- [ ] B) Downstream dependent tasks are not executed
- [ ] C) The job continues with all remaining tasks
- [ ] D) The cluster is terminated

---

### Question 9
Which CI/CD tool has native Databricks CLI setup action?

- [ ] A) Jenkins
- [ ] B) CircleCI
- [ ] C) GitHub Actions
- [ ] D) Bamboo

---

### Question 10
What is the purpose of the max_retries setting in a job task?

- [ ] A) Maximum number of parallel executions
- [ ] B) Number of times to retry a failed task
- [ ] C) Maximum runtime in hours
- [ ] D) Number of workers to allocate

---

## Answer Key

| Q | Answer | Explanation |
|---|--------|-------------|
| 1 | B | Job clusters are created when a job starts and terminated when it ends |
| 2 | B | Workflows are multi-task jobs with DAG-style dependencies |
| 3 | C | File Arrival trigger monitors cloud storage for new files |
| 4 | B | Cron expressions define the schedule pattern |
| 5 | C | Service principals provide consistent, auditable permissions |
| 6 | B | DABs are IaC for defining jobs, pipelines, and other resources |
| 7 | B | CAN_MANAGE_RUN allows triggering and cancelling runs |
| 8 | B | Downstream tasks depending on the failed task are skipped |
| 9 | C | GitHub Actions has the databricks/setup-cli action |
| 10 | B | max_retries specifies how many times to retry a failed task |

---

*Quiz Version: 2.0 | Databricks Platform Administration Training - Day 10*
