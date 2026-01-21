# Databricks Platform Administration Training Courseware

## Comprehensive 13-Day Training Program
### Aligned with Databricks Certified Associate Platform Administrator Exam

---

## Course Overview

| **Attribute**     | **Details**                                           |
| ----------------- | ----------------------------------------------------- |
| **Duration**      | 13 Days (40 Hours)                                    |
| **Mode**          | Virtual Instructor-Led Training + Guided Labs         |
| **Certification** | Databricks Certified Associate Platform Administrator |
| **Version**       | 2.0 (January 2026)                                    |


### Daily Duration Pattern
- **Days 1–11**: 3 hours/day → 33 hours
- **Days 12–13**: 3.5 hours/day → 7 hours
- **Total**: 40 hours

---

## Courseware Structure

```
courseware/
├── README.md                      # This file
├── common/
│   ├── pre-requisites/
│   │   └── PREREQUISITES.md       # Technical and knowledge requirements
│   └── lab-environment/
│       └── LAB_ENVIRONMENT_SETUP.md  # Trainer & participant setup guide
│
├── assessments/
│   ├── pre-test/                  # Pre-training assessment
│   │   └── pre_assessment.md
│   └── post-test/                 # Post-training certification prep exam
│       └── practice_exam.md
│
├── day01/                         # Lakehouse & Workspace Foundations
│   ├── slides/
│   │   └── day01-lakehouse-workspace-foundations.html
│   ├── labs/
│   │   └── LAB_01_Workspace_Navigation.md
│   ├── assessments/
│   │   └── day01_quiz.md
│   └── resources/
│       └── day01_prereads.md
│
├── day02/                         # Platform Administration Overview
│   ├── slides/
│   │   └── day02-platform-administration.html
│   ├── labs/
│   │   └── LAB_02_Workspace_Configuration.md
│   ├── assessments/
│   │   └── day02_quiz.md
│   └── resources/
│
├── day03/                         # User, Group & Role Management
│   ├── slides/
│   │   └── day03-user-group-management.html
│   ├── labs/
│   │   └── LAB_03_User_Group_Admin.md
│   ├── assessments/
│   │   └── day03_quiz.md
│   └── resources/
│
├── day04/                         # Spark Fundamentals for Administrators
│   ├── slides/
│   │   └── day04-spark-fundamentals.html
│   ├── labs/
│   │   └── LAB_04_Spark_Jobs.md
│   ├── assessments/
│   │   └── day04_quiz.md
│   └── resources/
│
├── day05/                         # Delta Lake Fundamentals
│   ├── slides/
│   │   └── day05-delta-lake-fundamentals.html
│   ├── labs/
│   │   └── LAB_05_Delta_Tables.md
│   ├── assessments/
│   │   └── day05_quiz.md
│   └── resources/
│
├── day06/                         # Unity Catalog: Architecture & Setup
│   ├── slides/
│   │   └── day06-unity-catalog-architecture.html
│   ├── labs/
│   │   └── LAB_06_Unity_Catalog_Setup.md
│   ├── assessments/
│   │   └── day06_quiz.md
│   └── resources/
│
├── day07/                         # Unity Catalog: Security & Governance
│   ├── slides/
│   │   └── day07-unity-catalog-governance.html
│   ├── labs/
│   │   └── LAB_07_Permissions_Governance.md
│   ├── assessments/
│   │   └── day07_quiz.md
│   └── resources/
│
├── day08/                         # IAM, SCIM & Identity Integration
│   ├── slides/
│   │   └── day08-iam-scim-identity.html
│   ├── labs/
│   │   └── LAB_08_Identity_Integration.md
│   ├── assessments/
│   │   └── day08_quiz.md
│   └── resources/
│
├── day09/                         # Cluster & SQL Warehouse Administration
│   ├── slides/
│   │   └── day09-cluster-warehouse-admin.html
│   ├── labs/
│   │   └── LAB_09_Cluster_Policies.md
│   ├── assessments/
│   │   └── day09_quiz.md
│   └── resources/
│
├── day10/                         # Job Orchestration & CI/CD
│   ├── slides/
│   │   └── day10-jobs-cicd.html
│   ├── labs/
│   │   └── LAB_10_Job_Scheduling.md
│   ├── assessments/
│   │   └── day10_quiz.md
│   └── resources/
│
├── day11/                         # Monitoring & Troubleshooting
│   ├── slides/
│   │   └── day11-monitoring-troubleshooting.html
│   ├── labs/
│   │   └── LAB_11_Log_Analysis.md
│   ├── assessments/
│   │   └── day11_quiz.md
│   └── resources/
│
├── day12/                         # Infrastructure, Compliance & Cost
│   ├── slides/
│   │   └── day12-infrastructure-compliance-cost.html
│   ├── labs/
│   │   └── LAB_12_Cost_Analysis.md
│   ├── assessments/
│   │   └── day12_quiz.md
│   └── resources/
│
├── day13/                         # Standards, Certification & Wrap-Up
│   ├── slides/
│   │   └── day13-standards-certification.html
│   ├── labs/
│   │   └── LAB_13_Admin_Scenarios.md
│   ├── assessments/
│   │   └── day13_final_review.md
│   └── resources/
│
├── capstone/
│   ├── CAPSTONE_PROJECT.md        # Multi-team enterprise setup
│   └── CAPSTONE_RUBRIC.md         # Evaluation criteria
│
└── trainer-guide/
    ├── TRAINER_PREPARATION.md     # Pre-training checklist
    ├── DELIVERY_NOTES.md          # Teaching tips per day
    └── TROUBLESHOOTING.md         # Common issues and solutions
```

---

## Daily Schedule

### Day 1 (3 Hours) – Lakehouse & Workspace Foundations

| Time | Topic | Duration |
|------|-------|----------|
| 0:00 - 0:45 | Lakehouse Architecture | 45 min |
| 0:45 - 1:15 | Control Plane vs Data Plane | 30 min |
| 1:15 - 1:30 | Break | 15 min |
| 1:30 - 2:00 | Databricks Workspace Components | 30 min |
| 2:00 - 2:30 | Personas & Administrator Responsibilities | 30 min |
| 2:30 - 3:00 | **Lab**: Workspace Navigation | 30 min |

**Hands-on Focus**: Workspace navigation, notebooks, clusters, jobs, SQL warehouses

---

### Day 2 (3 Hours) – Platform Administration Overview

| Time | Topic | Duration |
|------|-------|----------|
| 0:00 - 0:45 | Account vs Workspace-Level Administration | 45 min |
| 0:45 - 1:15 | Workspace Provisioning & Configuration | 30 min |
| 1:15 - 1:30 | Break | 15 min |
| 1:30 - 2:15 | Admin Console Overview | 45 min |
| 2:15 - 2:30 | Workspace-Level Settings | 15 min |
| 2:30 - 3:00 | **Lab**: Workspace Configuration Walkthrough | 30 min |

**Hands-on Focus**: Workspace configuration walkthrough

---

### Day 3 (3 Hours) – User, Group & Role Management

| Time | Topic | Duration |
|------|-------|----------|
| 0:00 - 0:45 | User, Group, and Role Concepts | 45 min |
| 0:45 - 1:15 | Admin Privilege Models | 30 min |
| 1:15 - 1:30 | Break | 15 min |
| 1:30 - 2:00 | Best Practices for Access Management | 30 min |
| 2:00 - 3:00 | **Lab**: Create Users & Groups, Assign Privileges | 60 min |

**Hands-on Focus**: Create users & groups, assign admin privileges

---

### Day 4 (3 Hours) – Spark Fundamentals for Administrators

| Time | Topic | Duration |
|------|-------|----------|
| 0:00 - 0:45 | Apache Spark Execution Basics | 45 min |
| 0:45 - 1:15 | Cluster Architecture & Execution Flow | 30 min |
| 1:15 - 1:30 | Break | 15 min |
| 1:30 - 2:00 | Admin View of Spark Jobs | 30 min |
| 2:00 - 3:00 | **Lab**: Run Spark Jobs & Review Execution | 60 min |

**Hands-on Focus**: Run Spark jobs, review execution behavior

---

### Day 5 (3 Hours) – Delta Lake Fundamentals

| Time | Topic | Duration |
|------|-------|----------|
| 0:00 - 0:45 | Delta Lake Architecture | 45 min |
| 0:45 - 1:15 | ACID Transactions & Versioning | 30 min |
| 1:15 - 1:30 | Break | 15 min |
| 1:30 - 2:00 | Time Travel & Admin Implications | 30 min |
| 2:00 - 3:00 | **Lab**: Inspect Delta Tables & Versions | 60 min |

**Hands-on Focus**: Inspect Delta tables, review table versions

---

### Day 6 (3 Hours) – Unity Catalog: Architecture & Setup

| Time | Topic | Duration |
|------|-------|----------|
| 0:00 - 0:45 | Unity Catalog Architecture | 45 min |
| 0:45 - 1:15 | Metastore, Catalogs, Schemas, Tables | 30 min |
| 1:15 - 1:30 | Break | 15 min |
| 1:30 - 2:00 | Centralized Governance Model | 30 min |
| 2:00 - 3:00 | **Lab**: Configure Unity Catalog & Create Objects | 60 min |

**Hands-on Focus**: Configure Unity Catalog, create catalogs & schemas

---

### Day 7 (3 Hours) – Unity Catalog: Security & Governance

| Time | Topic | Duration |
|------|-------|----------|
| 0:00 - 0:45 | Privilege Model & Access Control | 45 min |
| 0:45 - 1:15 | Data Lineage Concepts | 30 min |
| 1:15 - 1:30 | Break | 15 min |
| 1:30 - 2:00 | Auditing & Governance Workflows | 30 min |
| 2:00 - 3:00 | **Lab**: Assign Permissions to Users & Groups | 60 min |

**Hands-on Focus**: Assign permissions to users & groups

---

### Day 8 (3 Hours) – IAM, SCIM & Identity Integration

| Time | Topic | Duration |
|------|-------|----------|
| 0:00 - 0:45 | IAM Fundamentals | 45 min |
| 0:45 - 1:15 | SCIM Provisioning Overview | 30 min |
| 1:15 - 1:30 | Break | 15 min |
| 1:30 - 2:00 | Azure AD Integration & Group Sync | 30 min |
| 2:00 - 3:00 | **Lab**: Review SCIM & Validate Sync | 60 min |

**Hands-on Focus**: Review SCIM configuration, validate user/group sync

---

### Day 9 (3 Hours) – Cluster & SQL Warehouse Administration

| Time | Topic | Duration |
|------|-------|----------|
| 0:00 - 0:45 | Cluster Types & Policies | 45 min |
| 0:45 - 1:15 | Job Clusters vs All-Purpose Clusters | 30 min |
| 1:15 - 1:30 | Break | 15 min |
| 1:30 - 2:00 | SQL Warehouse Configuration & Scaling | 30 min |
| 2:00 - 3:00 | **Lab**: Create Policies & Configure Warehouses | 60 min |

**Hands-on Focus**: Create cluster policies, configure SQL warehouses

---

### Day 10 (3 Hours) – Job Orchestration & CI/CD

| Time | Topic | Duration |
|------|-------|----------|
| 0:00 - 0:45 | Databricks Jobs Framework | 45 min |
| 0:45 - 1:15 | Scheduling & Dependencies | 30 min |
| 1:15 - 1:30 | Break | 15 min |
| 1:30 - 2:00 | CI/CD Concepts & Deployment Practices | 30 min |
| 2:00 - 3:00 | **Lab**: Create & Schedule Databricks Jobs | 60 min |

**Hands-on Focus**: Create & schedule Databricks jobs

---

### Day 11 (3 Hours) – Monitoring & Troubleshooting

| Time | Topic | Duration |
|------|-------|----------|
| 0:00 - 0:30 | Job & Cluster Monitoring | 30 min |
| 0:30 - 1:00 | Log Analysis | 30 min |
| 1:00 - 1:15 | Break | 15 min |
| 1:15 - 1:45 | Common Failure Scenarios | 30 min |
| 1:45 - 2:15 | Performance Troubleshooting & Alerting | 30 min |
| 2:15 - 3:00 | **Lab**: Analyze Failed Jobs & Review Logs | 45 min |

**Hands-on Focus**: Analyze failed jobs, review cluster logs

---

### Day 12 (3.5 Hours) – Infrastructure, Compliance & Cost Governance

| Time | Topic | Duration |
|------|-------|----------|
| 0:00 - 0:45 | Azure Databricks Architecture | 45 min |
| 0:45 - 1:15 | Workspace Deployment Models | 30 min |
| 1:15 - 1:30 | Break | 15 min |
| 1:30 - 2:00 | VNet Injection & Private Endpoints (Conceptual) | 30 min |
| 2:00 - 2:30 | Audit Logging & Compliance Monitoring | 30 min |
| 2:30 - 3:00 | Cost Drivers & DBU Pricing | 30 min |
| 3:00 - 3:30 | **Lab**: Cost Optimization Strategies | 30 min |

**Hands-on Focus**: Cost analysis and optimization review

---

### Day 13 (3.5 Hours) – Standards, Certification & Wrap-Up

| Time | Topic | Duration |
|------|-------|----------|
| 0:00 - 0:30 | Internal Standards & Governance | 30 min |
| 0:30 - 1:00 | Access Reviews & Naming Conventions | 30 min |
| 1:00 - 1:15 | Break | 15 min |
| 1:15 - 1:45 | Backup & Retention Policies | 30 min |
| 1:45 - 2:15 | Administrator Deliverables & Runbooks | 30 min |
| 2:15 - 2:45 | Databricks Certification Overview | 30 min |
| 2:45 - 3:15 | **Lab**: Admin Scenario Walkthroughs | 30 min |
| 3:15 - 3:30 | Q&A and Next Steps | 15 min |

**Hands-on Focus**: Admin scenario walkthroughs, Q&A

---

## Presentation Format

All slide decks are in **HTML format** with:
- Dark theme with Databricks orange/red branding
- Animated bullet points and diagrams
- Speaker notes (press 'N' to toggle)
- Keyboard navigation (← → arrows)
- Progress bar and slide counter
- Click navigation (click right/left half)

### How to Present

1. Open the `.html` file in a modern browser (Chrome/Firefox recommended)
2. Enter fullscreen mode (F11 or browser fullscreen)
3. Navigate with arrow keys or click
4. Press 'N' to show/hide speaker notes
5. Use 'Home' to go to first slide, 'End' for last

---

## Lab Requirements

### Technical Requirements
- Modern web browser
- Databricks workspace access (Premium tier or higher recommended)
- Workspace Admin access for labs
- Internet connectivity

### Lab Environment Options
1. **Databricks Partner Training Account** - Request from Databricks
2. **Customer's Existing Account** - Create dedicated training workspace
3. **Databricks Community Edition** - Limited (demos only)

---

## Assessment Structure

### Daily Quizzes
- 10-15 questions each day
- 10 minutes duration
- 70% pass rate required
- Covers that day's topics

### Practice Exam (Day 13)
- 45 questions
- 90 minutes
- Aligned with certification exam
- Detailed answer explanations

---

## Certification Alignment

| Exam Domain | Training Coverage |
|-------------|-------------------|
| Databricks Lakehouse Platform | Day 1, Day 5 |
| Workspace Administration | Day 2, Day 3 |
| Identity and Access Management | Day 3, Day 8 |
| Unity Catalog | Day 6, Day 7 |
| Compute Management | Day 4, Day 9 |
| Jobs and Workflows | Day 10 |
| Security and Networking | Day 8, Day 12 |
| Monitoring and Optimization | Day 11, Day 12 |

---

## Support Resources

### Databricks Documentation
- [Administration Guide](https://docs.databricks.com/en/admin/index.html)
- [Unity Catalog](https://docs.databricks.com/en/data-governance/unity-catalog/index.html)
- [Security Best Practices](https://docs.databricks.com/en/security/index.html)

### Training Support
- Training Portal: [To be provided]
- Trainer Email: [To be provided]
- Technical Support: Create support ticket

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | January 2026 | Initial release (5-day format) |
| 2.0 | January 2026 | Restructured to 13-day format |

---

*© 2026 Databricks Platform Administration Training*
