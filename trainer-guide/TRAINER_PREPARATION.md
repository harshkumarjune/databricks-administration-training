# Trainer Preparation Guide

## Databricks Platform Administration Training
### Pre-Training Checklist & Setup Instructions

---

## Overview

This guide helps trainers prepare for delivering the 13-day Databricks Platform Administration Training. Complete all items at least 1 week before training begins.

---

## Pre-Training Checklist

### 2 Weeks Before Training

- [ ] **Confirm participant list** and send calendar invites
- [ ] **Review all course materials** for currency and accuracy
- [ ] **Verify Databricks workspace access** for all participants
- [ ] **Test all lab exercises** in the training environment
- [ ] **Coordinate with IT** for any network/firewall requirements

### 1 Week Before Training

- [ ] **Send welcome email** with pre-requisites and login instructions
- [ ] **Confirm participant permissions** (workspace access, Unity Catalog)
- [ ] **Prepare backup plans** for potential technical issues
- [ ] **Review participant backgrounds** to customize examples
- [ ] **Set up monitoring** for the training workspace

### Day Before Training

- [ ] **Test presentation equipment** (screen sharing, audio)
- [ ] **Verify workspace connectivity** from your training location
- [ ] **Prepare Day 1 materials** and have them ready
- [ ] **Send reminder email** with join link and start time
- [ ] **Review Day 1 agenda** and timing

---

## Environment Setup

### Training Workspace Requirements

| Requirement | Specification |
|-------------|---------------|
| Workspace Tier | Premium (Unity Catalog support) |
| Unity Catalog | Enabled with metastore attached |
| Compute | At least 1 all-purpose cluster available |
| SQL Warehouse | Serverless or Pro warehouse for SQL labs |
| Participants | Workspace access with appropriate roles |

### Participant Permission Levels

For full lab experience, participants need:

| Permission | Minimum Level | Ideal Level |
|------------|---------------|-------------|
| Workspace | User | Admin (for full experience) |
| Unity Catalog | Can Use Catalog | Can Create Catalog |
| Compute | Can Attach | Can Create |
| SQL Warehouse | Can Use | Can Manage |

### Creating Training Catalogs

If participants cannot create catalogs, pre-create:

```sql
-- Create participant sandboxes
CREATE CATALOG IF NOT EXISTS training_sandbox;
CREATE SCHEMA training_sandbox.participant_01;
CREATE SCHEMA training_sandbox.participant_02;
-- ... repeat for all participants

-- Grant appropriate permissions
GRANT USAGE, CREATE TABLE, CREATE VIEW
ON SCHEMA training_sandbox.participant_01
TO `participant01@company.com`;
```

---

## Technical Setup

### Presentation Setup

1. **Browser**: Use Chrome or Firefox (latest version)
2. **Screen Resolution**: 1920x1080 recommended for slides
3. **Dual Monitors**: One for presenting, one for demos
4. **Backup**: Have slides downloaded locally as PDF backup

### Demo Environment

Prepare the following for live demonstrations:

| Day | Demo Resources Needed |
|-----|----------------------|
| 1 | Clean workspace, sample notebook |
| 4-5 | Sample Spark job, Delta table |
| 6-7 | Unity Catalog catalog with sample data |
| 8 | SCIM configuration access (or screenshots) |
| 9 | Cluster policies, SQL warehouse |
| 10 | Sample workflow job |
| 11 | Access to system tables |
| 12 | Billing/usage data |

### Sample Data Preparation

Create sample datasets for labs:

```sql
-- Create sample customer data
CREATE TABLE IF NOT EXISTS training_demo.customers (
    customer_id INT,
    name STRING,
    email STRING,
    region STRING,
    created_date DATE
);

INSERT INTO training_demo.customers VALUES
    (1, 'Acme Corp', 'contact@acme.com', 'US-West', '2024-01-15'),
    (2, 'Global Inc', 'info@global.com', 'US-East', '2024-01-20'),
    (3, 'Tech Ltd', 'hello@tech.com', 'EU-West', '2024-02-01');

-- Create sample orders data
CREATE TABLE IF NOT EXISTS training_demo.orders (
    order_id INT,
    customer_id INT,
    amount DECIMAL(10,2),
    order_date DATE
);

INSERT INTO training_demo.orders VALUES
    (101, 1, 1500.00, '2024-02-10'),
    (102, 2, 2300.50, '2024-02-12'),
    (103, 1, 890.25, '2024-02-15');
```

---

## Participant Communication

### Welcome Email Template

```
Subject: Databricks Admin Training - Getting Started

Dear [Participant Name],

Welcome to the Databricks Platform Administration Training!

Training Details:
- Dates: [Start Date] to [End Date]
- Time: [Time] [Timezone]
- Format: Virtual Instructor-Led
- Platform: [Meeting Link]

Before Day 1, please:
1. Verify your Databricks workspace access: [Workspace URL]
2. Review the prerequisites document (attached)
3. Complete the pre-assessment: [Link]
4. Test your audio/video for virtual sessions

Technical Requirements:
- Modern web browser (Chrome/Firefox recommended)
- Stable internet connection
- Access to [Workspace URL]

If you have any access issues, please contact [Support Email].

Looking forward to training with you!

[Trainer Name]
```

### Pre-Requisites Document

Ensure participants have:

**Technical Knowledge:**
- Basic SQL skills (SELECT, INSERT, UPDATE)
- Understanding of cloud concepts (storage, compute)
- Familiarity with data concepts (tables, schemas)

**Access Requirements:**
- Databricks workspace credentials
- Browser: Chrome or Firefox
- Screen resolution: 1920x1080 minimum

**Optional (Helpful):**
- Python basics
- JSON/YAML familiarity
- Git fundamentals

---

## Daily Preparation

### Before Each Day

1. **Review day's content** (30 min before start)
2. **Test any demos** you plan to show
3. **Open all tabs** you'll need (slides, workspace, docs)
4. **Join meeting early** to test tech
5. **Have backup slides** ready (PDF)

### During Breaks

1. **Address parking lot items** if time permits
2. **Check participant questions** in chat
3. **Prepare next section's demos**
4. **Stay available** for 1:1 questions

### After Each Day

1. **Send recap email** with key takeaways
2. **Share any additional resources** requested
3. **Review quiz results** if applicable
4. **Note areas needing emphasis** for next day
5. **Update any materials** based on feedback

---

## Contingency Planning

### Common Issues and Solutions

| Issue | Solution |
|-------|----------|
| Workspace down | Use screenshots, PDF slides, discuss concepts |
| Cluster won't start | Use SQL warehouse or pre-started cluster |
| Participant can't access | Have IT support contact ready |
| Network issues | Have backup meeting link (different platform) |
| Labs failing | Have solution code ready, pair participants |

### Backup Plans

1. **No internet**: Local PDF of all slides
2. **Workspace issues**: Pre-recorded demos
3. **Time running short**: Prioritized topic list
4. **Ahead of schedule**: Challenge exercises ready

---

## Post-Training

### After Training Completes

- [ ] Send course completion certificates
- [ ] Distribute post-training survey
- [ ] Provide certification exam guidance
- [ ] Share additional learning resources
- [ ] Clean up training workspace resources
- [ ] Collect and document feedback

### Follow-Up Resources

Share with participants:
- Databricks documentation links
- Certification study guides
- Community forum access
- Additional training paths

---

## Contact Information

| Role | Contact |
|------|---------|
| Training Coordinator | [Email] |
| Technical Support | [Email/Ticket System] |
| Databricks Partner Support | [Partner Portal] |
| Emergency Contact | [Phone] |

---

*Trainer Preparation Guide Version: 2.0 | Databricks Platform Administration Training*
