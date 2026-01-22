# Databricks Platform Administration Training Courseware

## Comprehensive 20-Day Training Program
### Aligned with Databricks Certified Associate Platform Administrator Exam

---

## Course Overview

| Attribute | Details |
|-----------|---------|
| **Duration** | 20 Days (40 Hours) |
| **Schedule** | 2 hours per day |
| **Mode** | Virtual Instructor-Led Training + Guided Labs |
| **Certification** | Databricks Certified Associate Platform Administrator |
| **Version** | 3.0 (January 2026) |

### Training Schedule
- **Days 1–20**: 2 hours/day
- **Total**: 40 hours
- **Capstone**: Day 20 (multi-track project)

---

## Courseware Structure

```
courseware/
├── README.md                      # This file
├── CURRICULUM_20DAY_STRUCTURE.md  # Detailed curriculum mapping
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
├── day01/                         # Lakehouse Architecture Fundamentals
├── day02/                         # Databricks Workspace & Control Plane
├── day03/                         # Platform Administration Essentials
├── day04/                         # User & Group Management
├── day05/                         # Roles, Permissions & Access Control
├── day06/                         # Apache Spark for Administrators
├── day07/                         # Delta Lake Fundamentals
├── day08/                         # Unity Catalog Architecture
├── day09/                         # Unity Catalog Permissions & Governance
├── day10/                         # IAM & Identity Federation
├── day11/                         # SCIM Provisioning & SSO
├── day12/                         # Network Security & Private Connectivity
├── day13/                         # Data Security & Encryption
├── day14/                         # Cluster Architecture & Types
├── day15/                         # Cluster Policies & SQL Warehouses
├── day16/                         # Job Orchestration & Workflows
├── day17/                         # Monitoring & Troubleshooting
├── day18/                         # Security & Compliance Frameworks
├── day19/                         # Cost Governance & Optimization
├── day20/                         # Capstone Project & Certification Prep
│
├── capstone/
│   ├── beginner/
│   │   └── CAPSTONE_BEGINNER.md   # 30-min Unity Catalog focus
│   ├── intermediate/
│   │   └── CAPSTONE_INTERMEDIATE.md # 45-min + Compute governance
│   ├── advanced/
│   │   └── CAPSTONE_ADVANCED.md   # 60-min Enterprise architecture
│   ├── validation/
│   │   ├── capstone_validator.py  # Automated validation script
│   │   ├── run_validation.py      # CLI runner
│   │   └── sample_submission.json # Sample submission
│   └── solutions/                 # Reference solutions (trainer only)
│
└── trainer-guide/
    ├── TRAINER_PREPARATION.md     # Pre-training checklist
    ├── DELIVERY_NOTES.md          # Teaching tips per day
    └── TROUBLESHOOTING.md         # Common issues and solutions
```

---

## Curriculum Overview (4 Weeks)

### Week 1: Foundations (Days 1-5)
| Day | Topic | Focus |
|-----|-------|-------|
| 1 | Lakehouse Architecture Fundamentals | Architecture, medallion pattern |
| 2 | Databricks Workspace & Control Plane | Control/data plane, workspace components |
| 3 | Platform Administration Essentials | Admin console, workspace settings |
| 4 | User & Group Management | Users, groups, admin privileges |
| 5 | Roles, Permissions & Access Control | RBAC, entitlements, best practices |

### Week 2: Data Governance (Days 6-10)
| Day | Topic | Focus |
|-----|-------|-------|
| 6 | Apache Spark for Administrators | Execution model, driver/executor |
| 7 | Delta Lake Fundamentals | ACID, time travel, versioning |
| 8 | Unity Catalog Architecture | Metastore, catalogs, schemas |
| 9 | Unity Catalog Permissions & Governance | Grants, inheritance, auditing |
| 10 | IAM & Identity Federation | Cloud IAM, Azure AD, AWS IAM |

### Week 3: Security & Compute (Days 11-15)
| Day | Topic | Focus |
|-----|-------|-------|
| 11 | SCIM Provisioning & SSO | User sync, SSO configuration |
| 12 | Network Security & Private Connectivity | VNet injection, Private Link |
| 13 | Data Security & Encryption | CMK, column masking, RLS |
| 14 | Cluster Architecture & Types | All-purpose, job, autoscaling |
| 15 | Cluster Policies & SQL Warehouses | Policy JSON, warehouse config |

### Week 4: Operations & Capstone (Days 16-20)
| Day | Topic | Focus |
|-----|-------|-------|
| 16 | Job Orchestration & Workflows | Multi-task jobs, CRON, dependencies |
| 17 | Monitoring & Troubleshooting | System tables, log analysis |
| 18 | Security & Compliance Frameworks | SOC 2, GDPR, audit controls |
| 19 | Cost Governance & Optimization | DBU pricing, tagging, chargeback |
| 20 | Capstone Project & Certification | Multi-track project, exam prep |

---

## Daily Schedule Format (2 Hours)

Each day follows this structure:

| Time | Activity | Duration |
|------|----------|----------|
| 0:00 - 0:10 | Review & Objectives | 10 min |
| 0:10 - 0:45 | Concept Session 1 | 35 min |
| 0:45 - 1:00 | Break | 15 min |
| 1:00 - 1:30 | Concept Session 2 | 30 min |
| 1:30 - 1:50 | Hands-on Lab | 20 min |
| 1:50 - 2:00 | Summary & Quiz | 10 min |

---

## Capstone Project Tracks

### Track Selection Matrix

| Track | Duration | Prerequisites | Focus Areas |
|-------|----------|---------------|-------------|
| **Beginner** | 30 min | Days 1-9 | Unity Catalog structure, basic permissions |
| **Intermediate** | 45 min | Days 1-15 | + Cluster policies, job workflows |
| **Advanced** | 60 min | Days 1-19 | + Security, compliance, cost governance |

### Capstone Validation

Run locally or in Databricks:
```bash
# Validate beginner track submission
python run_validation.py --track beginner --submission my_submission.json

# Validate intermediate track
python run_validation.py --track intermediate --submission my_submission.json

# Validate advanced track
python run_validation.py --track advanced --submission my_submission.json
```

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

## Assessment Structure

### Daily Quizzes
- 10 questions each day
- 10 minutes duration
- 70% pass rate required
- Covers that day's topics

### Practice Exam (Day 20)
- 45 questions
- 90 minutes
- Aligned with certification exam
- Detailed answer explanations

### Capstone Evaluation

| Grade | Percentage | Status |
|-------|------------|--------|
| A | 90%+ | Certification Ready |
| B | 80-89% | Strong Foundation |
| C | 70-79% | Meets Minimum |
| NC | <70% | Requires Resubmission |

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

## Certification Alignment

| Exam Domain | Training Days |
|-------------|---------------|
| Databricks Lakehouse Platform | Days 1-2, 7 |
| Workspace Administration | Days 3-5 |
| Identity and Access Management | Days 4-5, 10-11 |
| Unity Catalog | Days 8-9 |
| Compute Management | Days 6, 14-15 |
| Jobs and Workflows | Day 16 |
| Security and Networking | Days 12-13, 18 |
| Monitoring and Optimization | Days 17, 19 |

---

## Folder Contents (Per Day)

Each day folder contains:

```
dayNN/
├── slides/
│   └── dayNN-topic-name.html      # Presentation slides
├── labs/
│   └── LAB_NN_Lab_Name.md         # Hands-on lab instructions
├── assessments/
│   └── dayNN_quiz.md              # Daily quiz
└── resources/
    └── dayNN_prereads.md          # Pre-reading materials
```

---

## Support Resources

### Databricks Documentation
- [Administration Guide](https://docs.databricks.com/en/admin/index.html)
- [Unity Catalog](https://docs.databricks.com/en/data-governance/unity-catalog/index.html)
- [Security Best Practices](https://docs.databricks.com/en/security/index.html)
- [Cluster Policies](https://docs.databricks.com/en/admin/clusters/policies.html)
- [System Tables](https://docs.databricks.com/en/administration-guide/system-tables/index.html)

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
| 3.0 | January 2026 | Restructured to 20-day × 2-hour format with multi-track capstone |

---

*© 2026 Databricks Platform Administration Training*
