# Day 3 Pre-Reading Materials

## Databricks Platform Administration Training
### User, Group & Role Management

---

## Overview

Day 3 covers identity management within Databricks, including users, groups, and role-based access control. Understanding these concepts is fundamental to secure platform administration.

**Estimated Reading Time**: 25-30 minutes

---

## Required Reading

### 1. Identity Management Concepts

**Source**: Databricks Documentation

**Key Concepts to Understand**:
- Three identity types: users, groups, service principals
- How identities are provisioned (manual vs SCIM)
- Relationship between identity and permissions

**Read**: [Manage users and groups](https://docs.databricks.com/en/admin/users-groups/index.html)

**Focus Areas**:
- User lifecycle (provision, assign, deprovision)
- Group hierarchy and nesting
- Service principals for automation

### 2. Roles and Privileges

**Source**: Databricks Documentation

**Key Concepts to Understand**:
- Built-in roles (Account Admin, Workspace Admin, etc.)
- Principle of least privilege
- Role assignment best practices

**Read**: [Roles and entitlements](https://docs.databricks.com/en/admin/users-groups/roles.html)

**Focus Areas**:
- Admin roles and their scope
- User entitlements
- Delegating administration

### 3. Groups Best Practices

**Source**: Databricks Documentation

**Key Concepts to Understand**:
- Why groups are preferred over individual permissions
- Group naming conventions
- Mapping groups to organizational structure

**Read**: [Best practices for groups](https://docs.databricks.com/en/admin/users-groups/best-practices.html)

**Focus Areas**:
- Role-based group design
- Environment-based groups
- Nested group strategies

---

## Key Terminology

| Term | Definition |
|------|------------|
| **User** | Human identity that can log in interactively |
| **Group** | Collection of users and/or service principals |
| **Service Principal** | Machine identity for automation and CI/CD |
| **Entitlement** | Permission to access a feature or resource type |
| **Role** | Named collection of permissions |
| **SCIM** | Protocol for automated identity provisioning |
| **Principle of Least Privilege** | Grant only minimum permissions needed |

---

## Self-Assessment Questions

1. Why should permissions be granted to groups rather than individual users?
2. What is a service principal, and when would you use one?
3. What's the difference between a role and an entitlement?
4. How do nested groups simplify permission management?

---

## Recommended Additional Reading

- [Service principals](https://docs.databricks.com/en/admin/users-groups/service-principals.html)
- [Manage account-level groups](https://docs.databricks.com/en/admin/users-groups/groups.html)
- [Sync users and groups from your identity provider](https://docs.databricks.com/en/admin/users-groups/scim/index.html)

---

*Pre-reading materials for Databricks Platform Administration Training - Day 3*
