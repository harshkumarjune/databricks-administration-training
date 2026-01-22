# Trainer Delivery Notes

## Databricks Platform Administration Training
### 20-Day Program - Day-by-Day Teaching Tips & Guidance

---

## General Teaching Tips

### Engagement Strategies for 2-Hour Sessions

- **Start with energy** - The first 5 minutes set the tone
- **Ask questions frequently** - Don't lecture for more than 8 minutes without interaction
- **Use real-world examples** - Connect concepts to participants' actual use cases
- **Encourage hands-on** - Let participants drive during demos when possible
- **Check understanding** - "Does this make sense?" is not enough; ask specific questions
- **End with action** - Summary + quiz keeps concepts fresh

### 2-Hour Session Pacing

| Activity | Time | Notes |
|----------|------|-------|
| Review & Objectives | 10 min | Quick recap of previous day |
| Concept Session 1 | 35 min | Core concepts, 2-3 key topics |
| Break | 10-15 min | **Don't skip!** Critical for attention |
| Concept Session 2 | 30 min | Applied concepts, demos |
| Hands-on Lab | 20-25 min | Guided practice |
| Summary & Quiz | 10 min | Reinforce key points |

### Handling Questions

- **Park complex questions** for later if off-topic
- **Redirect to labs** when answer is "let's try it"
- **Admit when unsure** and promise to follow up
- **Encourage peer answers** before providing your own

---

## Week 1: Platform Foundations (Days 1-5)

### Day 1: Lakehouse Architecture Fundamentals

**Key Messages:**
- Lakehouse = best of data lake + data warehouse
- Medallion architecture: Bronze (raw) → Silver (cleansed) → Gold (curated)
- Single source of truth for all data workloads

**Common Questions:**
- "How is this different from Snowflake?" → Focus on unified platform, ML integration
- "Where does my data actually live?" → Emphasize data remains in customer's cloud
- "What about costs?" → Preview Day 19, but mention DBU-based pricing

**Demo Suggestions:**
- Show a simple data flow diagram
- Navigate workspace data explorer
- Point out Unity Catalog namespace

**Time Traps:**
- Don't spend too long on architecture theory
- Keep interactive - ask what they currently use

---

### Day 2: Databricks Workspace & Control Plane

**Key Messages:**
- Control Plane (Databricks) vs Data Plane (your cloud)
- Your data never leaves your cloud account
- Account hierarchy: Account → Workspaces → Resources

**Common Questions:**
- "Is it secure if Databricks manages the control plane?" → SOC 2, encryption, no data access
- "How many workspaces do we need?" → Per environment (dev/staging/prod) or per team

**Demo Suggestions:**
- Navigate workspace sidebar
- Show notebooks, repos, jobs, SQL
- Demonstrate workspace settings

---

### Day 3: Platform Administration Essentials

**Key Messages:**
- Account Console vs Workspace Admin Console
- Account Admin = cross-workspace authority
- Workspace Admin = single workspace scope

**Common Questions:**
- "Who should be Account Admin?" → Small trusted group, typically platform team
- "Can someone be admin of one workspace only?" → Yes, workspace admin scope

**Demo Suggestions:**
- Navigate Admin Console
- Show workspace configuration
- Demonstrate user management interface

---

### Day 4: User & Group Management

**Key Messages:**
- Groups > individual permissions (always)
- Principle of least privilege
- Lifecycle: provision → use → deprovision

**Common Questions:**
- "How do groups sync from AD/Okta?" → Preview SCIM (Day 11)
- "What's a service principal?" → Machine identity for automation (Day 10)

**Demo Suggestions:**
- Create a group in workspace
- Add user to group
- Show permission inheritance

**Lab Tips:**
- Ensure participants have user management permissions
- Have backup screenshots if permissions limited

---

### Day 5: Roles, Permissions & Access Control

**Key Messages:**
- RBAC = Role-Based Access Control
- Entitlements control feature access
- Object permissions control resource access

**Common Questions:**
- "What's the difference between entitlements and permissions?" → Feature vs resource access
- "How granular can we get?" → Very - per object level

**Demo Suggestions:**
- Show entitlement settings
- Demonstrate object permission assignment
- Test permission denial

---

## Week 2: Data Governance (Days 6-10)

### Day 6: Apache Spark for Administrators

**Key Messages:**
- Administrators don't write Spark, but troubleshoot it
- Driver = coordinator, Workers = executors
- Jobs → Stages → Tasks

**Common Questions:**
- "Do I need to know Scala/Python?" → No, but understanding concepts helps
- "What causes Spark jobs to fail?" → Memory, skew, shuffle (preview Day 17)

**Demo Suggestions:**
- Run a simple Spark job
- Show Spark UI stages tab
- Explain execution plan basics

**Time Traps:**
- Don't turn this into a Spark development course
- Focus on monitoring/troubleshooting view

---

### Day 7: Delta Lake Fundamentals

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

### Day 8: Unity Catalog Architecture

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

### Day 9: Unity Catalog Permissions & Governance

**Key Messages:**
- USAGE privilege is the gatekeeper
- Permissions cascade down but require USAGE at each level
- Data lineage is automatic

**Common Questions:**
- "Why can't my user see a table?" → Check USAGE on catalog AND schema
- "How do I see who accessed what?" → System tables (Day 17)

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

### Day 10: IAM & Identity Federation

**Key Messages:**
- Cloud IAM integration varies by provider
- Service principals for automation
- OAuth M2M tokens for programmatic access

**Common Questions:**
- "Do we need separate service principals per job?" → Best practice, yes
- "Can we use managed identities?" → Yes, on Azure

**Demo Suggestions:**
- Create a service principal
- Assign permissions to service principal
- Show token generation (if permitted)

---

## Week 3: Security & Compute (Days 11-15)

### Day 11: SCIM Provisioning & SSO

**Key Messages:**
- SCIM = automated user/group sync
- SSO = single sign-on via SAML/OIDC
- Reduces manual identity management

**Common Questions:**
- "How does SSO work?" → SAML flow explanation
- "Can we use Azure AD/Okta/Ping?" → Yes, all major IdPs supported

**Demo Suggestions:**
- Show SCIM configuration interface
- Walk through SSO setup steps
- Show user sync in action (if available)

**Lab Alternative:**
- If SCIM not available, use walkthrough with screenshots

---

### Day 12: Network Security & Private Connectivity

**Key Messages:**
- VNet injection = network isolation
- Private Link = no public internet
- IP access lists = allowlist protection

**Common Questions:**
- "Do we need Private Link?" → Depends on compliance requirements
- "Can we restrict by IP?" → Yes, IP access lists

**Demo Suggestions:**
- Show IP access list configuration
- Diagram network architecture
- Explain data plane isolation

---

### Day 13: Data Security & Encryption

**Key Messages:**
- CMK = you control the keys
- Column masking = hide sensitive data
- Row-level security = filter by user

**Common Questions:**
- "Is data encrypted at rest?" → Yes, always; CMK for key control
- "How does masking work?" → Functions that transform output

**Demo Suggestions:**
- Create secret scope
- Show column masking function
- Demonstrate row-level security

---

### Day 14: Cluster Architecture & Types

**Key Messages:**
- All-Purpose = interactive development
- Job Cluster = scheduled workloads (cost-efficient)
- Autoscaling = dynamic resource adjustment

**Common Questions:**
- "What size cluster should we use?" → Start small, scale based on workload
- "Why not always use all-purpose?" → Cost - job clusters terminate automatically

**Demo Suggestions:**
- Create clusters of different types
- Show autoscaling configuration
- Compare startup times

**Key Decisions to Highlight:**
- Driver sizing vs worker sizing
- Spot instances for workers
- Auto-termination settings

---

### Day 15: Cluster Policies & SQL Warehouses

**Key Messages:**
- Policies = governance + cost control
- Policy JSON syntax is specific
- SQL Warehouses = serverless SQL compute

**Common Questions:**
- "Can users override policies?" → No, that's the point
- "Serverless vs Pro?" → Serverless for simplicity, Pro for control

**Demo Suggestions:**
- Write policy JSON live
- Show policy enforcement
- Configure SQL warehouse

**Key Policy Elements:**
```json
{
  "spark_version": {"type": "fixed", "value": "14.3.x-scala2.12"},
  "num_workers": {"type": "range", "minValue": 1, "maxValue": 4},
  "custom_tags.Team": {"type": "unlimited", "isOptional": false}
}
```

---

## Week 4: Operations & Capstone (Days 16-20)

### Day 16: Job Orchestration & Workflows

**Key Messages:**
- Multi-task jobs = orchestrated pipelines
- Dependencies: all_succeeded, at_least_one, all_done
- CRON syntax for scheduling

**Common Questions:**
- "Can jobs trigger other jobs?" → Yes, via task dependencies or API
- "What if a task fails?" → Depends on dependency type and retry settings

**Demo Suggestions:**
- Create multi-task workflow
- Configure dependencies
- Set up CRON schedule

**CRON Quick Reference:**
```
0 2 * * *     → Daily at 2 AM
0 0 * * 1     → Weekly Monday midnight
0 */4 * * *   → Every 4 hours
```

---

### Day 17: Monitoring & Troubleshooting

**Key Messages:**
- System tables = source of truth
- Four Golden Signals: Latency, Traffic, Errors, Saturation
- Systematic debugging approach

**Common Questions:**
- "Where do I find logs?" → Spark UI, driver logs, system tables
- "Why is my job slow?" → Check shuffle, skew, memory

**Demo Suggestions:**
- Query system.billing.usage
- Query system.access.audit
- Walk through Spark UI for slow job

**Key Queries:**
```sql
SELECT * FROM system.access.audit
WHERE event_date = current_date();

SELECT SUM(usage_quantity) as dbus,
       custom_tags['Team'] as team
FROM system.billing.usage
WHERE usage_date >= current_date() - 7
GROUP BY custom_tags['Team'];
```

---

### Day 18: Security & Compliance Frameworks

**Key Messages:**
- SOC 2 Type II = security controls
- GDPR = data privacy (EU)
- Audit logs support compliance

**Common Questions:**
- "Are we SOC 2 compliant?" → Databricks is; your configuration matters too
- "How do we implement GDPR?" → Row-level security, deletion tracking

**Demo Suggestions:**
- Map Databricks features to SOC 2 controls
- Show audit log queries
- Demonstrate compliance reporting

**Compliance Mapping Exercise:**
- Have participants map their requirements to Databricks features

---

### Day 19: Cost Governance & Optimization

**Key Messages:**
- DBU = Databricks billing unit
- Tags enable chargeback
- Optimization: right-size, auto-terminate, Spot

**Common Questions:**
- "How do we know who's spending?" → Tags + system.billing.usage
- "What's the biggest cost driver?" → Typically compute (clusters)

**Demo Suggestions:**
- Query billing system tables
- Show cost breakdown by team
- Calculate tag compliance

**Key Cost Queries:**
```sql
-- Cost by team
SELECT custom_tags['Team'], SUM(usage_quantity * 0.55) as cost
FROM system.billing.usage
WHERE usage_date >= current_date() - 30
GROUP BY custom_tags['Team'];

-- Tag compliance
SELECT
  100.0 * SUM(CASE WHEN custom_tags['Team'] IS NOT NULL
              THEN usage_quantity ELSE 0 END)
       / SUM(usage_quantity) as compliance_pct
FROM system.billing.usage;
```

---

### Day 20: Capstone Project & Certification Prep

**Session Flow:**

| Time | Activity | Trainer Role |
|------|----------|--------------|
| 0:00-0:15 | Capstone overview, track selection | Explain tracks, answer questions |
| 0:15-1:15 | Capstone work time | Circulate, assist, observe |
| 1:15-1:35 | Validation & peer review | Facilitate sharing |
| 1:35-1:50 | Certification prep | Tips, exam format |
| 1:50-2:00 | Wrap-up | Celebrate, next steps |

**Capstone Track Guidance:**

| Track | For Whom | Key Deliverables |
|-------|----------|------------------|
| **Beginner** | New to Databricks | Catalog structure, permissions |
| **Intermediate** | Some experience | + Policies, workflows |
| **Advanced** | Production experience | + Security, compliance, cost |

**Capstone Tips:**
- Let participants choose their track
- Have sample solutions ready (don't show until after)
- Celebrate completions publicly
- Provide personalized feedback

**Certification Tips to Share:**
- Practice with certification guide
- Know the UI navigation
- Understand "why" not just "how"
- ~90 seconds per question average

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
- Extra support for struggling participants
- Supplementary reading for background

### Technical Failures

Recovery approaches:
1. **Cluster won't start**: Use SQL warehouse or screenshots
2. **Workspace down**: Switch to concepts and discussion
3. **Lab failing**: Troubleshoot as group learning opportunity
4. **Network issues**: Have mobile hotspot backup

---

## Capstone Validation

### Running Validation

```bash
# Participants can validate their submissions
python run_validation.py --track beginner --submission submission.json
python run_validation.py --track intermediate --submission submission.json
python run_validation.py --track advanced --submission submission.json
```

### Grading Scale

| Grade | Score | Feedback Focus |
|-------|-------|----------------|
| A (90%+) | Certification ready | Minor polish suggestions |
| B (80-89%) | Strong foundation | Specific improvement areas |
| C (70-79%) | Meets minimum | Key gaps to address |
| NC (<70%) | Resubmission needed | Structured remediation |

---

## Post-Training Follow-Up

### Same Week
- Send certificate of completion
- Share slides and resources
- Provide practice exam access

### Within 2 Weeks
- Check certification exam registration
- Answer lingering questions
- Share additional resources

### Ongoing
- Invite to community channels
- Share new feature announcements
- Offer advanced training paths

---

*Delivery Notes Version: 3.0 | 20-Day Databricks Platform Administration Training*
