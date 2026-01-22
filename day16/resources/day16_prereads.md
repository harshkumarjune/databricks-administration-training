# Day 16 Pre-Reading Materials

## Databricks Platform Administration Training
### Job Orchestration & Workflows

---

## Overview

Day 16 covers Databricks Workflows for job orchestration. You'll learn how to design multi-task pipelines, configure dependencies, set up scheduling, and implement robust error handling for production workloads.

**Estimated Reading Time**: 30-35 minutes

---

## Required Reading

### 1. Jobs and Workflows Overview

**Source**: Databricks Documentation

**Key Concepts to Understand**:
- Jobs vs workflows vs tasks
- Multi-task job structure
- Task types (notebook, Python, SQL, etc.)

**Read**: [What are Databricks jobs?](https://docs.databricks.com/en/jobs/index.html)

**Focus Areas**:
- Job anatomy (tasks, dependencies, compute)
- Task execution modes
- Job runs and run history

### 2. Task Dependencies

**Source**: Databricks Documentation

**Key Concepts to Understand**:
- Dependency types (all succeeded, at least one, all done, none failed)
- DAG (Directed Acyclic Graph) structure
- Parallel vs sequential execution

**Read**: [Add and manage job tasks](https://docs.databricks.com/en/jobs/jobs-tasks.html)

**Focus Areas**:
- Configuring task dependencies
- Conditional task execution
- Dynamic task parameters

### 3. Job Scheduling

**Source**: Databricks Documentation

**Key Concepts to Understand**:
- CRON expression syntax
- Timezone considerations
- Concurrent run limits

**Read**: [Schedule a job](https://docs.databricks.com/en/jobs/schedule.html)

**Focus Areas**:
- CRON syntax patterns
- Trigger types (scheduled, file arrival, continuous)
- Pausing and resuming schedules

---

## Key Terminology

| Term | Definition |
|------|------------|
| **Job** | Collection of tasks with defined execution order |
| **Task** | Individual unit of work (notebook, script, SQL) |
| **Workflow** | Visual representation of multi-task job |
| **DAG** | Directed Acyclic Graph of task dependencies |
| **Job Cluster** | Ephemeral cluster created per job run |
| **CRON** | Time-based scheduling syntax |
| **Run** | Single execution instance of a job |
| **Repair** | Re-run failed tasks from a specific point |

---

## CRON Expression Quick Reference

| Expression | Meaning |
|------------|---------|
| `0 0 * * *` | Daily at midnight |
| `0 2 * * *` | Daily at 2:00 AM |
| `0 0 * * 1` | Every Monday at midnight |
| `0 */4 * * *` | Every 4 hours |
| `0 9-17 * * 1-5` | Hourly 9 AM-5 PM, Monday-Friday |
| `0 0 1 * *` | First day of every month |

**Format**: `minute hour day-of-month month day-of-week`

---

## Task Dependency Types

| Dependency | Behavior |
|------------|----------|
| **All succeeded** | Runs only if all upstream tasks succeed |
| **At least one succeeded** | Runs if any upstream task succeeds |
| **None failed** | Runs if no upstream task failed (skipped OK) |
| **All done** | Runs after all upstream complete regardless of status |

---

## Workflow Architecture Pattern

```
┌─────────────────────────────────────────────────────────────┐
│              Daily ETL Pipeline                             │
│                                                             │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐             │
│  │ Extract  │    │ Extract  │    │ Extract  │   PARALLEL  │
│  │ Source A │    │ Source B │    │ Source C │             │
│  └────┬─────┘    └────┬─────┘    └────┬─────┘             │
│       │               │               │                    │
│       └───────────────┼───────────────┘                    │
│                       ▼                                    │
│              ┌─────────────────┐                          │
│              │   Transform     │            SEQUENTIAL    │
│              │   (All inputs)  │                          │
│              └────────┬────────┘                          │
│                       │                                    │
│        ┌──────────────┼──────────────┐                    │
│        ▼              ▼              ▼                    │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐   PARALLEL     │
│  │  Load    │  │  Load    │  │  Notify  │               │
│  │  Bronze  │  │  Silver  │  │  Team    │               │
│  └──────────┘  └──────────┘  └──────────┘               │
└─────────────────────────────────────────────────────────────┘
```

---

## Self-Assessment Questions

1. What's the difference between a job and a task?
2. When would you use "All done" vs "All succeeded" dependency?
3. How do you prevent multiple concurrent runs of the same job?
4. What is the purpose of job repair functionality?
5. When should you use file arrival triggers vs CRON schedules?

---

## Recommended Additional Reading

- [Task parameters](https://docs.databricks.com/en/jobs/task-parameter-values.html)
- [Job compute configuration](https://docs.databricks.com/en/jobs/compute.html)
- [Notifications and alerts](https://docs.databricks.com/en/jobs/notifications.html)
- [Repair and rerun jobs](https://docs.databricks.com/en/jobs/repair-job-failures.html)

---

*Pre-reading materials for Databricks Platform Administration Training - Day 16*
