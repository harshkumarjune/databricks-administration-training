# Day 10 Pre-Reading Materials

## Databricks Platform Administration Training
### Job Orchestration & CI/CD

---

## Overview

Day 10 covers Databricks workflows, job scheduling, and CI/CD practices. Understanding job orchestration is essential for managing production workloads.

**Estimated Reading Time**: 30-35 minutes

---

## Required Reading

### 1. Databricks Jobs

**Source**: Databricks Documentation

**Key Concepts to Understand**:
- Job types (notebook, Python, JAR, SQL)
- Triggers (scheduled, file arrival, continuous)
- Multi-task workflows

**Read**: [What are Databricks jobs?](https://docs.databricks.com/en/workflows/jobs/jobs.html)

**Focus Areas**:
- Task types and dependencies
- Job cluster vs all-purpose cluster
- Error handling and retries

### 2. Workflow Orchestration

**Source**: Databricks Documentation

**Key Concepts to Understand**:
- Task dependencies (DAG)
- Conditional execution
- Parameter passing

**Read**: [Create and run jobs](https://docs.databricks.com/en/workflows/jobs/create-run-jobs.html)

**Focus Areas**:
- Linear vs parallel task execution
- Job clusters for cost optimization
- Notifications and alerts

### 3. Databricks Asset Bundles

**Source**: Databricks Documentation

**Key Concepts to Understand**:
- Infrastructure as Code for Databricks
- Bundle configuration (databricks.yml)
- Deployment across environments

**Read**: [What are Databricks Asset Bundles?](https://docs.databricks.com/en/dev-tools/bundles/index.html)

**Focus Areas**:
- Bundle project structure
- Environment configuration
- CI/CD integration

---

## Key Terminology

| Term | Definition |
|------|------------|
| **Job** | Scheduled or triggered execution of tasks |
| **Workflow** | Multi-task job with dependencies |
| **Task** | Single unit of work in a job (notebook, script, etc.) |
| **Trigger** | What starts a job (schedule, file, API, continuous) |
| **DAB** | Databricks Asset Bundles - IaC for Databricks |
| **Job Cluster** | Ephemeral cluster created for a job run |
| **Run** | Single execution of a job |
| **Repair** | Re-run of failed tasks in a workflow |

---

## Workflow DAG Example

```
        ┌─────────────┐
        │   Ingest    │
        └──────┬──────┘
               │
       ┌───────┴───────┐
       ▼               ▼
┌─────────────┐  ┌─────────────┐
│ Transform A │  │ Transform B │
└──────┬──────┘  └──────┬──────┘
       │               │
       └───────┬───────┘
               ▼
        ┌─────────────┐
        │   Publish   │
        └─────────────┘
```

---

## Trigger Types

| Trigger | Use Case |
|---------|----------|
| **Manual** | Ad-hoc runs, testing |
| **Scheduled** | Regular batch processing (daily, hourly) |
| **File Arrival** | Process new files in cloud storage |
| **Continuous** | Real-time streaming processing |
| **API** | External orchestration, CI/CD |

---

## Self-Assessment Questions

1. What's the difference between a job cluster and an all-purpose cluster for jobs?
2. When would you use file arrival trigger vs scheduled trigger?
3. How do task dependencies work in a multi-task workflow?
4. What are the benefits of Databricks Asset Bundles for CI/CD?

---

## CI/CD Pipeline Example

```yaml
# GitHub Actions example
name: Deploy Databricks Jobs
on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Install Databricks CLI
        run: pip install databricks-cli

      - name: Deploy bundle
        run: databricks bundle deploy -t production
        env:
          DATABRICKS_HOST: ${{ secrets.DB_HOST }}
          DATABRICKS_TOKEN: ${{ secrets.DB_TOKEN }}
```

---

## Recommended Additional Reading

- [Schedule jobs](https://docs.databricks.com/en/workflows/jobs/schedule-jobs.html)
- [Job alerts](https://docs.databricks.com/en/workflows/jobs/job-notifications.html)
- [Repair job failures](https://docs.databricks.com/en/workflows/jobs/repair-job-failures.html)
- [Databricks CLI](https://docs.databricks.com/en/dev-tools/cli/index.html)

---

*Pre-reading materials for Databricks Platform Administration Training - Day 10*
