# Day 16 Quiz: Job Orchestration & Workflows

## Databricks Platform Administration Training
### Duration: 10 Minutes | 10 Questions | 70% to Pass

---

### Question 1
What is a multi-task job in Databricks?

- [ ] A) A job that runs on multiple clusters simultaneously
- [ ] B) A workflow that orchestrates multiple dependent tasks with defined execution order
- [ ] C) A job that processes multiple tables at once
- [ ] D) A job that requires multiple users to complete

---

### Question 2
Which task dependency type means a task runs regardless of upstream task success or failure?

- [ ] A) All succeeded
- [ ] B) At least one succeeded
- [ ] C) None failed
- [ ] D) All done

---

### Question 3
What is the CRON expression `0 2 * * *` scheduling?

- [ ] A) Every 2 minutes
- [ ] B) At 2:00 AM every day
- [ ] C) On the 2nd day of every month
- [ ] D) Every 2 hours

---

### Question 4
What is the benefit of using job clusters over all-purpose clusters for scheduled jobs?

- [ ] A) Better interactive notebook experience
- [ ] B) Automatic provisioning and termination, cost-efficient for batch workloads
- [ ] C) Support for more users concurrently
- [ ] D) Faster startup time

---

### Question 5
How does the retry policy help with transient failures?

- [ ] A) It skips failed tasks
- [ ] B) It automatically re-runs failed tasks a specified number of times
- [ ] C) It sends alerts only
- [ ] D) It rolls back database changes

---

### Question 6
What happens when a task in a workflow fails and has no retry policy?

- [ ] A) The entire workflow restarts
- [ ] B) Downstream dependent tasks are skipped; parallel tasks continue
- [ ] C) All other tasks are immediately cancelled
- [ ] D) The job waits indefinitely for manual intervention

---

### Question 7
Which trigger type is best for processing files as they arrive in cloud storage?

- [ ] A) Scheduled (CRON)
- [ ] B) Manual
- [ ] C) File arrival trigger
- [ ] D) Continuous trigger

---

### Question 8
What is the purpose of job repair/retry functionality?

- [ ] A) To fix syntax errors in notebooks
- [ ] B) To rerun only failed tasks from a specific point without re-running successful tasks
- [ ] C) To update job configurations
- [ ] D) To delete and recreate the job

---

### Question 9
How do you prevent multiple concurrent runs of the same job?

- [ ] A) Use single-user clusters only
- [ ] B) Set max_concurrent_runs to 1
- [ ] C) Delete previous runs manually
- [ ] D) This cannot be controlled

---

### Question 10
What notification channel is recommended for critical production job failures?

- [ ] A) No notifications needed
- [ ] B) Email only to a distribution list
- [ ] C) Multiple channels: email, Slack/Teams, and PagerDuty for SEV1
- [ ] D) Console logs only

---

## Answer Key

| Q | Answer | Explanation |
|---|--------|-------------|
| 1 | B | Multi-task jobs define workflows with multiple tasks and dependencies |
| 2 | D | "All done" means the task runs after upstreams complete regardless of status |
| 3 | B | CRON `0 2 * * *` = minute 0, hour 2, any day, any month, any weekday |
| 4 | B | Job clusters are created/terminated per job, optimizing cost for batch workloads |
| 5 | B | Retry policy automatically re-attempts failed tasks based on configured count |
| 6 | B | Dependent tasks skip; independent parallel tasks continue execution |
| 7 | C | File arrival trigger monitors cloud storage and starts jobs when files appear |
| 8 | B | Repair allows selective re-execution from failure point, saving time and cost |
| 9 | B | max_concurrent_runs = 1 prevents overlapping job executions |
| 10 | C | Critical jobs should use multiple notification channels for reliability |

---

*Quiz Version: 3.0 | Databricks Platform Administration Training - Day 16*
