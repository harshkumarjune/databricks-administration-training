# Trainer Delivery Notes

## Databricks Platform Administration Training
### Day-by-Day Teaching Tips & Guidance

---

## General Teaching Tips

### Engagement Strategies

- **Ask questions frequently** - Don't lecture for more than 10 minutes without interaction
- **Use real-world examples** - Connect concepts to participants' actual use cases
- **Encourage hands-on** - Let participants drive during demos when possible
- **Check understanding** - "Does this make sense?" is not enough; ask specific questions
- **Manage the room** - Balance between fast learners and those needing more time

### Pacing Guidelines

| Activity | Recommended Time |
|----------|-----------------|
| Concept explanation | 5-10 minutes per concept |
| Demo | 5-15 minutes |
| Lab exercise | 30-60 minutes |
| Q&A/Discussion | 5-10 minutes per section |
| Break | 10-15 minutes every 1.5 hours |

### Handling Questions

- **Park complex questions** for later if off-topic
- **Redirect to labs** when answer is "let's try it"
- **Admit when unsure** and promise to follow up
- **Encourage peer answers** before providing your own

---

## Day-by-Day Delivery Notes

### Day 1: Lakehouse & Workspace Foundations

**Key Messages:**
- Lakehouse = best of data lake + data warehouse
- Control Plane (Databricks) vs Data Plane (your cloud)
- Your data never leaves your cloud account

**Common Questions:**
- "How is this different from Snowflake?" → Focus on unified platform, ML integration
- "Where does my data actually live?" → Emphasize Data Plane in customer's cloud
- "What about costs?" → Preview Day 12, but mention DBU-based pricing

**Demo Suggestions:**
- Show workspace navigation live
- Create a simple notebook and run a cell
- Point out key sidebar elements

**Time Traps:**
- Don't spend too long on architecture diagrams
- Save deep Unity Catalog for Days 6-7

---

### Day 2: Platform Administration Overview

**Key Messages:**
- Account Console vs Workspace Admin Console
- Account Admin = cross-workspace authority
- Workspace Admin = single workspace scope

**Common Questions:**
- "Who should be Account Admin?" → Small trusted group, typically platform team
- "Can someone be admin of one workspace only?" → Yes, workspace admin scope

**Demo Suggestions:**
- Show Account Console navigation
- Demonstrate workspace settings
- Show user management interface

**Time Traps:**
- Don't deep-dive into IAM yet (Day 8)
- Keep Unity Catalog mentions brief (Days 6-7)

---

### Day 3: User, Group & Role Management

**Key Messages:**
- Groups > individual permissions (always)
- Principle of least privilege
- Service principals for automation

**Common Questions:**
- "How do groups sync from AD/Okta?" → Preview SCIM (Day 8)
- "What's the difference between user and service principal?" → Human vs machine identity

**Demo Suggestions:**
- Create a group in workspace
- Add user to group
- Show permission inheritance

**Lab Tips:**
- Ensure participants have user management permissions
- Have backup screenshots if permissions limited

---

### Day 4: Spark Fundamentals for Administrators

**Key Messages:**
- Administrators don't write Spark, but troubleshoot it
- Driver = coordinator, Workers = executors
- Jobs → Stages → Tasks

**Common Questions:**
- "Do I need to know Scala/Python?" → No, but understanding concepts helps
- "What causes Spark jobs to fail?" → Memory, skew, shuffle (preview Day 11)

**Demo Suggestions:**
- Run a simple Spark job
- Show Spark UI stages tab
- Explain execution plan basics

**Time Traps:**
- Don't turn this into a Spark development course
- Focus on monitoring/troubleshooting view

---

### Day 5: Delta Lake Fundamentals

**Key Messages:**
- Delta = Parquet + transaction log
- ACID transactions on data lake
- Time travel for debugging and auditing

**Common Questions:**
- "What's the difference from plain Parquet?" → ACID, time travel, schema enforcement
- "How long does history persist?" → Default 7 days, configurable

**Demo Suggestions:**
- Show DESCRIBE HISTORY output
- Demonstrate time travel query
- Run VACUUM and explain implications

**Key Commands to Practice:**
```sql
DESCRIBE HISTORY table_name;
SELECT * FROM table_name VERSION AS OF 5;
VACUUM table_name RETAIN 168 HOURS;
```

---

### Day 6: Unity Catalog Architecture

**Key Messages:**
- Metastore = top-level container (regional)
- Three-level namespace: catalog.schema.table
- Managed vs External tables (DROP behavior!)

**Common Questions:**
- "How many metastores do we need?" → One per region typically
- "What happens to hive_metastore?" → Still exists for legacy, consider migration

**Demo Suggestions:**
- Navigate Data Explorer
- Create catalog and schema
- Show three-level namespace in action

**Critical Warning:**
- Emphasize DROP managed table DELETES data!
- Demo this in sandbox if possible

---

### Day 7: Unity Catalog Security & Governance

**Key Messages:**
- USAGE privilege is the gatekeeper
- Permissions cascade down but require USAGE at each level
- Data lineage is automatic

**Common Questions:**
- "Why can't my user see a table?" → Check USAGE on catalog AND schema
- "How do I see who accessed what?" → System tables (preview Day 11)

**Demo Suggestions:**
- GRANT and REVOKE statements
- Show permission inheritance
- Navigate lineage view

**Key SQL to Practice:**
```sql
GRANT USAGE ON CATALOG catalog_name TO `group_name`;
GRANT USAGE ON SCHEMA catalog.schema TO `group_name`;
GRANT SELECT ON TABLE catalog.schema.table TO `group_name`;
SHOW GRANTS ON TABLE catalog.schema.table;
```

---

### Day 8: IAM, SCIM & Identity Integration

**Key Messages:**
- SCIM = automated user/group sync
- Service principals for CI/CD and automation
- OAuth M2M tokens for programmatic access

**Common Questions:**
- "How does SSO work?" → SAML flow explanation
- "Can we use Azure AD/Okta/Ping?" → Yes, all major IdPs supported

**Demo Suggestions:**
- Show SCIM configuration interface
- Create a service principal
- Generate OAuth token (if permitted)

**Lab Alternative:**
- If SCIM not available, use walkthrough with screenshots
- Focus on service principal creation

---

### Day 9: Cluster & SQL Warehouse Administration

**Key Messages:**
- Cluster policies = governance + cost control
- Auto-termination saves money
- SQL Warehouses = serverless SQL compute

**Common Questions:**
- "What size cluster should we use?" → Depends on workload; start small, scale up
- "Jobs cluster vs all-purpose?" → Jobs for scheduled, all-purpose for interactive

**Demo Suggestions:**
- Create cluster policy JSON
- Show policy enforcement
- Configure SQL warehouse scaling

**Key Policy Elements:**
```json
{
  "autotermination_minutes": {"type": "range", "minValue": 10, "maxValue": 60},
  "num_workers": {"type": "range", "minValue": 1, "maxValue": 4},
  "custom_tags.CostCenter": {"type": "regex", "pattern": "CC-[0-9]{5}"}
}
```

---

### Day 10: Job Orchestration & CI/CD

**Key Messages:**
- Workflows = orchestrated multi-task jobs
- Job clusters = cost efficient for scheduled work
- DABs = Infrastructure as Code for Databricks

**Common Questions:**
- "How do we promote code to production?" → Git integration, CI/CD pipelines
- "Can jobs trigger other jobs?" → Yes, via API or task dependencies

**Demo Suggestions:**
- Create multi-task workflow
- Show task dependencies
- Demonstrate file arrival trigger (if available)

**Time Management:**
- CI/CD concepts can expand infinitely; stay focused
- DABs is complex; high-level overview only

---

### Day 11: Monitoring & Troubleshooting

**Key Messages:**
- System tables = source of truth for monitoring
- Spark UI for job troubleshooting
- Data skew = most common performance issue

**Common Questions:**
- "Where do I find logs?" → Driver logs, event logs, system tables
- "Why is my job slow?" → Systematic approach: shuffle, skew, memory

**Demo Suggestions:**
- Query system.access.audit
- Show Spark UI for a slow job
- Identify skewed stage in Spark UI

**Key Queries:**
```sql
SELECT * FROM system.access.audit WHERE event_date = current_date();
SELECT * FROM system.billing.usage WHERE usage_date >= current_date() - 7;
```

---

### Day 12: Infrastructure, Compliance & Cost

**Key Messages:**
- Private Link = no public internet
- DBU = billing unit
- Tags enable cost allocation

**Common Questions:**
- "How much does this cost?" → Show DBU pricing, emphasize cloud costs separate
- "What compliance certifications?" → SOC 2, HIPAA, GDPR (depending on region)

**Demo Suggestions:**
- Query billing usage tables
- Show cost breakdown by SKU
- Calculate tag compliance percentage

**Time Allocation:**
- This is a dense day (3.5 hours)
- Don't rush through cost governance

---

### Day 13: Standards, Certification & Wrap-Up

**Key Messages:**
- Standards prevent chaos at scale
- Certification validates knowledge
- Continuous learning is essential

**Capstone Project:**
- Give participants autonomy
- Circulate and help as needed
- Review submissions at end

**Closing:**
- Summarize key learnings
- Certification exam tips
- Learning path forward

---

## Common Training Challenges

### Participants with Limited Access

If participants can't create resources:
1. Use shared training catalog
2. Demonstrate while they observe
3. Provide screenshots for reference
4. Assign homework with their own environment

### Mixed Skill Levels

Balance strategies:
- Challenge exercises for advanced
- Pair programming for labs
- Extra office hours for struggling participants
- Supplementary reading for background

### Technical Failures

Recovery approaches:
1. **Cluster won't start**: Use SQL warehouse or screenshots
2. **Workspace down**: Switch to concepts and discussion
3. **Lab failing**: Troubleshoot as group learning opportunity
4. **Network issues**: Have mobile hotspot backup

---

## Quiz Administration

### Daily Quizzes

- Administer at end of each day (10 minutes)
- Review answers briefly if time permits
- Use results to adjust next day's emphasis
- 70% pass rate recommended

### Final Assessment

- 90 minutes, 45 questions
- Simulates certification exam
- Review weak areas after completion
- Provide additional study resources

---

*Delivery Notes Version: 2.0 | Databricks Platform Administration Training*
