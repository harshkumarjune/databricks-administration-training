# Training Handouts
## Databricks Platform Administration Training

---

## Overview

This folder contains supplementary handout materials for participants. Print or distribute digitally as needed.

---

## Quick Reference Cards

### Unity Catalog Namespace
```
metastore (regional)
└── catalog (environment/team)
    └── schema (domain)
        └── table/view/function
```

### Permission Hierarchy
```
USAGE → Required to access child objects
SELECT → Read data
MODIFY → Write data
CREATE → Create new objects
ALL PRIVILEGES → Full access
```

### Cluster Policy Attribute Types
| Type | Purpose | Example |
|------|---------|---------|
| `fixed` | Force specific value | Spark version |
| `range` | Numeric range | Workers 1-8 |
| `allowlist` | Predefined options | Instance types |
| `regex` | Pattern matching | Version pattern |
| `unlimited` | No restriction | Custom tags |

### CRON Syntax
```
┌───────────── minute (0-59)
│ ┌───────────── hour (0-23)
│ │ ┌───────────── day of month (1-31)
│ │ │ ┌───────────── month (1-12)
│ │ │ │ ┌───────────── day of week (0-6, Sun=0)
│ │ │ │ │
* * * * *

Examples:
0 2 * * *     = Daily at 2 AM
0 0 * * 1     = Weekly Monday midnight
0 */4 * * *   = Every 4 hours
0 0 1 * *     = Monthly on 1st
```

### Key System Tables
| Table | Purpose |
|-------|---------|
| `system.billing.usage` | DBU consumption |
| `system.access.audit` | User activity logs |
| `system.compute.clusters` | Cluster information |

---

## Certification Exam Quick Tips

1. **Know the UI** - Practice navigating Admin Console
2. **USAGE privilege** - Always required for catalog/schema access
3. **Job clusters** - Most cost-effective for scheduled workloads
4. **Managed tables** - DROP deletes underlying data
5. **CRON** - minute hour day month weekday (5 fields)

---

*Handouts Version: 3.0 | Databricks Platform Administration Training*
