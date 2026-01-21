# Day 7 Pre-Reading Materials

## Databricks Platform Administration Training
### Unity Catalog: Security & Governance

---

## Overview

Day 7 dives deep into Unity Catalog permissions, data lineage, and governance features. Mastering these concepts is critical for implementing secure, compliant data access.

**Estimated Reading Time**: 30-35 minutes

---

## Required Reading

### 1. Privilege Model

**Source**: Databricks Documentation

**Key Concepts to Understand**:
- GRANT and REVOKE SQL syntax
- Privilege inheritance
- The critical USAGE privilege

**Read**: [Manage privileges in Unity Catalog](https://docs.databricks.com/en/data-governance/unity-catalog/manage-privileges/index.html)

**Focus Areas**:
- Privilege types (USAGE, SELECT, MODIFY, etc.)
- Inheritance from parent to child objects
- Owner privileges

### 2. Data Access Patterns

**Source**: Databricks Documentation

**Key Concepts to Understand**:
- Column-level security (column masks)
- Row-level security (row filters)
- Dynamic views for data masking

**Read**: [Row filters and column masks](https://docs.databricks.com/en/data-governance/unity-catalog/row-and-column-filters.html)

**Focus Areas**:
- Use cases for fine-grained access control
- Implementation patterns
- Performance considerations

### 3. Data Lineage

**Source**: Databricks Documentation

**Key Concepts to Understand**:
- How lineage is captured automatically
- Reading lineage graphs
- Lineage for compliance and impact analysis

**Read**: [Capture and view data lineage](https://docs.databricks.com/en/data-governance/unity-catalog/data-lineage.html)

**Focus Areas**:
- Table-level and column-level lineage
- Lineage across notebooks and jobs
- Using lineage for impact analysis

---

## Key Terminology

| Term | Definition |
|------|------------|
| **USAGE** | Privilege required to access child objects in a container |
| **SELECT** | Privilege to read data from a table |
| **MODIFY** | Privilege to add, update, delete data |
| **ALL PRIVILEGES** | Grants all applicable privileges |
| **Owner** | User or group with full control over an object |
| **Row Filter** | Function that filters rows based on user context |
| **Column Mask** | Function that transforms column values based on user |
| **Lineage** | Tracking of data flow and transformations |

---

## Permission Inheritance Example

```
GRANT USAGE ON CATALOG sales TO `analysts`
  └── Allows entry to catalog

GRANT USAGE ON SCHEMA sales.gold TO `analysts`
  └── Allows entry to schema

GRANT SELECT ON TABLE sales.gold.orders TO `analysts`
  └── Allows reading the table

All three grants are required for analysts to query sales.gold.orders!
```

---

## Self-Assessment Questions

1. Why is USAGE needed at every level of the hierarchy?
2. If a user has SELECT on a table but no USAGE on its schema, can they query it?
3. How does Unity Catalog capture lineage automatically?
4. What's the difference between a row filter and a column mask?

---

## Key SQL Commands

```sql
-- Grant access
GRANT USAGE ON CATALOG catalog_name TO `group_name`;
GRANT USAGE ON SCHEMA catalog.schema TO `group_name`;
GRANT SELECT ON TABLE catalog.schema.table TO `group_name`;

-- Check grants
SHOW GRANTS ON TABLE catalog.schema.table;
SHOW GRANTS TO `user@example.com`;

-- Revoke access
REVOKE SELECT ON TABLE catalog.schema.table FROM `group_name`;
```

---

## Recommended Additional Reading

- [Unity Catalog privileges and securable objects](https://docs.databricks.com/en/data-governance/unity-catalog/manage-privileges/privileges.html)
- [Create dynamic views](https://docs.databricks.com/en/data-governance/unity-catalog/create-views.html)
- [Unity Catalog audit logs](https://docs.databricks.com/en/admin/account-settings/audit-logs.html)

---

*Pre-reading materials for Databricks Platform Administration Training - Day 7*
