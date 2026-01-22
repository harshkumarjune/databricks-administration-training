# Databricks Platform Administration Training
## 20-Day Curriculum Structure (40 Hours Total)

**Version:** 3.0 | **Last Updated:** January 2026
**Delivery:** 20 Days × 2 Hours/Day | Virtual Instructor-Led Training
**Certification Alignment:** Databricks Certified Associate Platform Administrator

---

## Curriculum Overview

| Week | Days | Focus Area | Hours |
|------|------|------------|-------|
| **Week 1** | Days 1-5 | Platform Foundations & Workspace | 10 |
| **Week 2** | Days 6-10 | Data Governance & Unity Catalog | 10 |
| **Week 3** | Days 11-15 | Compute, Jobs & Operations | 10 |
| **Week 4** | Days 16-20 | Security, Cost & Capstone | 10 |

---

## Daily Schedule (2 Hours Each)

### WEEK 1: PLATFORM FOUNDATIONS & WORKSPACE

---

#### Day 1: Lakehouse Architecture Fundamentals
**Duration:** 2 Hours | **Level:** Beginner

| Time | Topic | Duration |
|------|-------|----------|
| 0:00 - 0:30 | Welcome & Course Overview | 30 min |
| 0:30 - 1:00 | Introduction to Data Lakehouse | 30 min |
| 1:00 - 1:15 | Break | 15 min |
| 1:15 - 1:45 | Databricks Platform Architecture | 30 min |
| 1:45 - 2:00 | Quiz & Day Wrap-up | 15 min |

**Learning Objectives:**
- Understand lakehouse architecture paradigm
- Identify Databricks platform components
- Recognize the value proposition of unified analytics

**Pre-Read:** Foundational Reading - Lakehouse Concepts
**Post-Read:** Databricks Architecture White Paper

---

#### Day 2: Control & Data Plane Deep Dive
**Duration:** 2 Hours | **Level:** Beginner

| Time | Topic | Duration |
|------|-------|----------|
| 0:00 - 0:30 | Control Plane Architecture | 30 min |
| 0:30 - 1:00 | Data Plane Architecture | 30 min |
| 1:00 - 1:15 | Break | 15 min |
| 1:15 - 1:45 | Cloud Provider Integrations (AWS/Azure/GCP) | 30 min |
| 1:45 - 2:00 | Quiz & Day Wrap-up | 15 min |

**Learning Objectives:**
- Differentiate control plane vs data plane components
- Understand cloud-specific deployment models
- Identify security boundaries in architecture

**Pre-Read:** Cloud Provider Fundamentals
**Post-Read:** Cloud Architecture Comparison Guide

---

#### Day 3: Workspace Navigation & Components
**Duration:** 2 Hours | **Level:** Beginner

| Time | Topic | Duration |
|------|-------|----------|
| 0:00 - 0:30 | Workspace UI Overview | 30 min |
| 0:30 - 1:00 | Core Workspace Components | 30 min |
| 1:00 - 1:15 | Break | 15 min |
| 1:15 - 2:00 | **Lab 1:** Workspace Navigation Exercise | 45 min |

**Learning Objectives:**
- Navigate Databricks workspace interface
- Identify workspace components (notebooks, clusters, jobs, SQL)
- Understand workspace organization best practices

**Lab:** Explore workspace, locate key components, create folders
**Assignment:** Workspace mapping exercise (Beginner)

---

#### Day 4: Administrator Personas & Responsibilities
**Duration:** 2 Hours | **Level:** Beginner-Intermediate

| Time | Topic | Duration |
|------|-------|----------|
| 0:00 - 0:30 | Account Admin vs Workspace Admin | 30 min |
| 0:30 - 1:00 | Administrator Responsibilities | 30 min |
| 1:00 - 1:15 | Break | 15 min |
| 1:15 - 1:45 | Admin Console Walkthrough | 30 min |
| 1:45 - 2:00 | Quiz & Day Wrap-up | 15 min |

**Learning Objectives:**
- Distinguish account-level from workspace-level administration
- Identify key administrator responsibilities
- Navigate the admin console

**Pre-Read:** Databricks Administration Guide
**Post-Read:** Admin Console Reference

---

#### Day 5: Workspace Configuration & Settings
**Duration:** 2 Hours | **Level:** Intermediate

| Time | Topic | Duration |
|------|-------|----------|
| 0:00 - 0:30 | Workspace Settings Deep Dive | 30 min |
| 0:30 - 1:00 | Feature Enablement & Controls | 30 min |
| 1:00 - 1:15 | Break | 15 min |
| 1:15 - 2:00 | **Lab 2:** Workspace Configuration Lab | 45 min |

**Learning Objectives:**
- Configure workspace settings
- Enable/disable workspace features
- Understand workspace limits and quotas

**Lab:** Configure workspace settings, review quotas
**Assignment:** Workspace configuration documentation (Intermediate)

---

### WEEK 2: DATA GOVERNANCE & UNITY CATALOG

---

#### Day 6: User & Group Management
**Duration:** 2 Hours | **Level:** Intermediate

| Time | Topic | Duration |
|------|-------|----------|
| 0:00 - 0:30 | User Lifecycle Management | 30 min |
| 0:30 - 1:00 | Group Creation & Hierarchy | 30 min |
| 1:00 - 1:15 | Break | 15 min |
| 1:15 - 2:00 | **Lab 3:** User & Group Administration | 45 min |

**Learning Objectives:**
- Manage user accounts and lifecycle
- Create and organize groups
- Implement group-based access patterns

**Lab:** Create users, groups, configure memberships
**Assignment:** Group strategy design (Intermediate)

---

#### Day 7: Access Levels & Entitlements
**Duration:** 2 Hours | **Level:** Intermediate

| Time | Topic | Duration |
|------|-------|----------|
| 0:00 - 0:30 | Workspace Access Levels | 30 min |
| 0:30 - 1:00 | Entitlements & Privilege Models | 30 min |
| 1:00 - 1:15 | Break | 15 min |
| 1:15 - 1:45 | Best Practices for Access Control | 30 min |
| 1:45 - 2:00 | Quiz & Day Wrap-up | 15 min |

**Learning Objectives:**
- Configure workspace access levels
- Assign appropriate entitlements
- Apply least-privilege principles

**Pre-Read:** RBAC Best Practices
**Post-Read:** Access Control Patterns Guide

---

#### Day 8: Spark Fundamentals for Administrators
**Duration:** 2 Hours | **Level:** Intermediate

| Time | Topic | Duration |
|------|-------|----------|
| 0:00 - 0:30 | Apache Spark Architecture | 30 min |
| 0:30 - 1:00 | Cluster Execution Model | 30 min |
| 1:00 - 1:15 | Break | 15 min |
| 1:15 - 2:00 | **Lab 4:** Spark Jobs & Execution Review | 45 min |

**Learning Objectives:**
- Understand Spark execution model
- Identify admin-relevant Spark concepts
- Monitor Spark job execution

**Lab:** Run Spark jobs, review Spark UI
**Assignment:** Spark execution analysis (Intermediate)

---

#### Day 9: Delta Lake Fundamentals
**Duration:** 2 Hours | **Level:** Intermediate

| Time | Topic | Duration |
|------|-------|----------|
| 0:00 - 0:30 | Delta Lake Architecture | 30 min |
| 0:30 - 1:00 | ACID Transactions & Time Travel | 30 min |
| 1:00 - 1:15 | Break | 15 min |
| 1:15 - 2:00 | **Lab 5:** Delta Tables & Versioning | 45 min |

**Learning Objectives:**
- Understand Delta Lake table format
- Apply ACID transaction concepts
- Use time travel for data recovery

**Lab:** Create Delta tables, explore versioning
**Assignment:** Delta table maintenance plan (Intermediate)

---

#### Day 10: Unity Catalog Architecture
**Duration:** 2 Hours | **Level:** Intermediate-Advanced

| Time | Topic | Duration |
|------|-------|----------|
| 0:00 - 0:30 | Unity Catalog Overview | 30 min |
| 0:30 - 1:00 | Three-Level Namespace (Catalog.Schema.Table) | 30 min |
| 1:00 - 1:15 | Break | 15 min |
| 1:15 - 1:45 | Metastore Concepts | 30 min |
| 1:45 - 2:00 | Quiz & Day Wrap-up | 15 min |

**Learning Objectives:**
- Understand Unity Catalog architecture
- Design catalog hierarchies
- Comprehend metastore role

**Pre-Read:** Unity Catalog Overview
**Post-Read:** Catalog Design Patterns

---

### WEEK 3: COMPUTE, JOBS & OPERATIONS

---

#### Day 11: Unity Catalog Setup & Configuration
**Duration:** 2 Hours | **Level:** Advanced

| Time | Topic | Duration |
|------|-------|----------|
| 0:00 - 0:30 | Storage Credentials & External Locations | 30 min |
| 0:30 - 1:00 | Managed vs External Tables | 30 min |
| 1:00 - 1:15 | Break | 15 min |
| 1:15 - 2:00 | **Lab 6:** Unity Catalog Setup | 45 min |

**Learning Objectives:**
- Configure storage credentials
- Create external locations
- Design table placement strategy

**Lab:** Configure Unity Catalog, create catalogs and schemas
**Assignment:** Unity Catalog architecture design (Advanced)

---

#### Day 12: Unity Catalog Security & Governance
**Duration:** 2 Hours | **Level:** Advanced

| Time | Topic | Duration |
|------|-------|----------|
| 0:00 - 0:30 | Privilege Model (GRANT/REVOKE) | 30 min |
| 0:30 - 1:00 | Row & Column Level Security | 30 min |
| 1:00 - 1:15 | Break | 15 min |
| 1:15 - 2:00 | **Lab 7:** Permissions & Governance | 45 min |

**Learning Objectives:**
- Implement data access permissions
- Configure row and column security
- Apply data governance policies

**Lab:** Assign permissions, implement security policies
**Assignment:** Security matrix design (Advanced)

---

#### Day 13: Identity Integration (IAM & SCIM)
**Duration:** 2 Hours | **Level:** Advanced

| Time | Topic | Duration |
|------|-------|----------|
| 0:00 - 0:30 | Account-Level Identity Management | 30 min |
| 0:30 - 1:00 | SCIM Provisioning Overview | 30 min |
| 1:00 - 1:15 | Break | 15 min |
| 1:15 - 2:00 | **Lab 8:** Identity Integration | 45 min |

**Learning Objectives:**
- Configure identity federation
- Implement SCIM provisioning
- Validate user synchronization

**Lab:** Review SCIM configuration, test sync
**Assignment:** Identity integration plan (Advanced)

---

#### Day 14: Cluster Architecture & Types
**Duration:** 2 Hours | **Level:** Intermediate

| Time | Topic | Duration |
|------|-------|----------|
| 0:00 - 0:30 | Cluster Types (All-Purpose vs Job) | 30 min |
| 0:30 - 1:00 | Cluster Sizing & Auto-scaling | 30 min |
| 1:00 - 1:15 | Break | 15 min |
| 1:15 - 1:45 | Databricks Runtime Versions | 30 min |
| 1:45 - 2:00 | Quiz & Day Wrap-up | 15 min |

**Learning Objectives:**
- Select appropriate cluster types
- Configure auto-scaling
- Choose runtime versions

**Pre-Read:** Cluster Best Practices
**Post-Read:** Runtime Selection Guide

---

#### Day 15: Cluster Policies & SQL Warehouses
**Duration:** 2 Hours | **Level:** Intermediate-Advanced

| Time | Topic | Duration |
|------|-------|----------|
| 0:00 - 0:30 | Cluster Policy Design | 30 min |
| 0:30 - 1:00 | SQL Warehouse Architecture | 30 min |
| 1:00 - 1:15 | Break | 15 min |
| 1:15 - 2:00 | **Lab 9:** Policies & Warehouses | 45 min |

**Learning Objectives:**
- Create restrictive cluster policies
- Configure SQL warehouses
- Implement compute governance

**Lab:** Create cluster policies, configure SQL warehouses
**Assignment:** Compute governance strategy (Advanced)

---

### WEEK 4: SECURITY, COST & CAPSTONE

---

#### Day 16: Job Orchestration & Workflows
**Duration:** 2 Hours | **Level:** Intermediate

| Time | Topic | Duration |
|------|-------|----------|
| 0:00 - 0:30 | Databricks Jobs Framework | 30 min |
| 0:30 - 1:00 | Task Dependencies & Scheduling | 30 min |
| 1:00 - 1:15 | Break | 15 min |
| 1:15 - 2:00 | **Lab 10:** Job Orchestration | 45 min |

**Learning Objectives:**
- Create multi-task workflows
- Configure job scheduling
- Implement retry policies

**Lab:** Create workflows with dependencies
**Assignment:** ETL workflow design (Intermediate)

---

#### Day 17: Monitoring & Troubleshooting
**Duration:** 2 Hours | **Level:** Intermediate-Advanced

| Time | Topic | Duration |
|------|-------|----------|
| 0:00 - 0:30 | System Tables for Observability | 30 min |
| 0:30 - 1:00 | Log Analysis & Diagnostics | 30 min |
| 1:00 - 1:15 | Break | 15 min |
| 1:15 - 2:00 | **Lab 11:** Monitoring & Log Analysis | 45 min |

**Learning Objectives:**
- Query system tables
- Analyze cluster and job logs
- Troubleshoot common issues

**Lab:** Analyze logs, investigate failures
**Assignment:** Monitoring dashboard design (Intermediate)

---

#### Day 18: Security & Compliance
**Duration:** 2 Hours | **Level:** Advanced

| Time | Topic | Duration |
|------|-------|----------|
| 0:00 - 0:30 | Network Security (VNet, Private Link) | 30 min |
| 0:30 - 1:00 | Data Security & Encryption | 30 min |
| 1:00 - 1:15 | Break | 15 min |
| 1:15 - 1:45 | Compliance Controls (SOC 2, GDPR) | 30 min |
| 1:45 - 2:00 | Quiz & Day Wrap-up | 15 min |

**Learning Objectives:**
- Configure network security
- Implement encryption strategies
- Apply compliance controls

**Pre-Read:** Security Best Practices
**Post-Read:** Compliance Framework Guide

---

#### Day 19: Cost Governance & Optimization
**Duration:** 2 Hours | **Level:** Intermediate-Advanced

| Time | Topic | Duration |
|------|-------|----------|
| 0:00 - 0:30 | DBU Pricing & Cost Drivers | 30 min |
| 0:30 - 1:00 | Tagging & Chargeback Strategies | 30 min |
| 1:00 - 1:15 | Break | 15 min |
| 1:15 - 2:00 | **Lab 12:** Cost Analysis & Optimization | 45 min |

**Learning Objectives:**
- Analyze cost consumption
- Implement resource tagging
- Optimize compute costs

**Lab:** Cost queries, optimization analysis
**Assignment:** Cost optimization plan (Advanced)

---

#### Day 20: Capstone Project & Certification Prep
**Duration:** 2 Hours | **Level:** All Levels

| Time | Topic | Duration |
|------|-------|----------|
| 0:00 - 0:15 | Capstone Overview & Setup | 15 min |
| 0:15 - 1:15 | **Capstone Project:** Enterprise Environment Design | 60 min |
| 1:15 - 1:30 | Break | 15 min |
| 1:30 - 1:45 | Certification Exam Overview | 15 min |
| 1:45 - 2:00 | Course Wrap-up & Next Steps | 15 min |

**Capstone Project:** Design enterprise Databricks environment for TechFlow Industries
- Beginner Track: Unity Catalog structure + basic permissions
- Intermediate Track: + Cluster policies + job workflows
- Advanced Track: + Full security + compliance + cost optimization

---

## Assessment Schedule

| Day | Assessment Type | Duration | Passing Score |
|-----|-----------------|----------|---------------|
| 1 | Pre-Assessment | 15 min | Baseline |
| 2, 4, 5, 7, 10, 14, 18 | Daily Quiz | 10 min | 70% |
| 10 | Week 2 Checkpoint | 15 min | 70% |
| 15 | Week 3 Checkpoint | 15 min | 70% |
| 19 | Practice Exam (45 questions) | 90 min | 70% |
| 20 | Capstone Project | 60 min | 70/100 pts |

---

## Difficulty Level Distribution

| Level | Days | Topics |
|-------|------|--------|
| **Beginner** | 1-3 | Lakehouse concepts, architecture basics, navigation |
| **Intermediate** | 4-9, 14, 16-17 | Administration, Spark, Delta, compute, jobs |
| **Advanced** | 10-13, 15, 18-19 | Unity Catalog, security, identity, compliance |
| **All Levels** | 20 | Capstone with tiered difficulty |

---

## Materials Per Day

Each day includes:
1. **Pre-Read** (15-30 min before class)
2. **Slides** (HTML presentation)
3. **Lab** (hands-on exercise, where applicable)
4. **Quiz** (knowledge check)
5. **Post-Read** (continued learning)
6. **Handout** (quick reference)
7. **Assignment** (optional homework, difficulty-tagged)

---

## Folder Structure

```
courseware/
├── CURRICULUM_20DAY_STRUCTURE.md (this file)
├── common/
│   ├── pre-requisites/
│   ├── lab-environment/
│   ├── pre-reads/
│   ├── post-reads/
│   └── handouts/
├── day01/ through day20/
│   ├── slides/
│   ├── labs/
│   ├── assessments/
│   ├── resources/
│   │   ├── prereads/
│   │   ├── postreads/
│   │   └── handouts/
│   └── assignments/
├── assessments/
│   ├── pre-test/
│   ├── checkpoints/
│   ├── practice-exam/
│   └── post-test/
├── capstone/
│   ├── beginner/
│   ├── intermediate/
│   ├── advanced/
│   ├── validation/
│   └── solutions/
└── trainer-guide/
```

---

*Document Version: 3.0 | 20-Day Curriculum Structure*
