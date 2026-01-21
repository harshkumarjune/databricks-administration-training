# Day 8 Pre-Reading Materials

## Databricks Platform Administration Training
### IAM, SCIM & Identity Integration

---

## Overview

Day 8 covers enterprise identity integration, including SCIM provisioning, SSO configuration, and service principals. These are critical for managing identity at scale in enterprise environments.

**Estimated Reading Time**: 30-35 minutes

---

## Required Reading

### 1. Identity Federation with SCIM

**Source**: Databricks Documentation

**Key Concepts to Understand**:
- What is SCIM and why use it?
- How users/groups sync from IdP to Databricks
- SCIM vs manual provisioning

**Read**: [Sync users and groups from your identity provider](https://docs.databricks.com/en/admin/users-groups/scim/index.html)

**Focus Areas**:
- Supported identity providers
- SCIM token configuration
- Attribute mapping

### 2. Single Sign-On (SSO)

**Source**: Databricks Documentation

**Key Concepts to Understand**:
- SAML 2.0 flow for authentication
- SSO vs password-based login
- Multi-factor authentication

**Read**: [Single sign-on](https://docs.databricks.com/en/admin/account-settings/sso.html)

**Focus Areas**:
- SAML configuration steps
- IdP metadata and certificates
- Testing SSO configuration

### 3. Service Principals

**Source**: Databricks Documentation

**Key Concepts to Understand**:
- What is a service principal?
- When to use service principals vs users
- OAuth token management

**Read**: [Manage service principals](https://docs.databricks.com/en/admin/users-groups/service-principals.html)

**Focus Areas**:
- Creating service principals
- Assigning permissions
- OAuth M2M authentication

---

## Key Terminology

| Term | Definition |
|------|------------|
| **SCIM** | System for Cross-domain Identity Management - automated user provisioning |
| **SAML** | Security Assertion Markup Language - SSO authentication protocol |
| **IdP** | Identity Provider (e.g., Azure AD, Okta, Ping) |
| **Service Principal** | Machine identity for automated processes |
| **OAuth 2.0** | Authorization framework for API access |
| **M2M Token** | Machine-to-Machine token for service authentication |
| **MFA** | Multi-Factor Authentication |
| **JIT Provisioning** | Just-In-Time user creation on first login |

---

## SCIM Architecture

```
Identity Provider (Azure AD, Okta, etc.)
         │
         │ SCIM API (HTTPS)
         ▼
Databricks Account
         │
         │ Automatic Sync
         ▼
    ┌────────────┐
    │   Users    │
    │   Groups   │
    └────────────┘
         │
         │ Workspace Assignment
         ▼
    Workspaces
```

---

## SSO Authentication Flow

```
1. User → Databricks login page
2. Databricks → Redirect to IdP
3. User → Authenticate with IdP (+ MFA)
4. IdP → SAML assertion to Databricks
5. Databricks → Validate assertion, create session
6. User → Access granted
```

---

## Self-Assessment Questions

1. What's the difference between SCIM and SSO?
2. Why would you use a service principal instead of a user account for CI/CD?
3. What happens if you disable SCIM sync - are existing users deleted?
4. How do OAuth M2M tokens differ from personal access tokens?

---

## Recommended Additional Reading

- [Configure SCIM provisioning for Azure AD](https://docs.databricks.com/en/admin/users-groups/scim/aad.html)
- [Configure SCIM provisioning for Okta](https://docs.databricks.com/en/admin/users-groups/scim/okta.html)
- [OAuth machine-to-machine (M2M) authentication](https://docs.databricks.com/en/dev-tools/auth/oauth-m2m.html)
- [Manage personal access tokens](https://docs.databricks.com/en/dev-tools/auth/pat.html)

---

## Security Best Practices

| Practice | Reason |
|----------|--------|
| Use SCIM for user provisioning | Automates onboarding/offboarding |
| Enable SSO | Centralizes authentication |
| Require MFA | Adds security layer |
| Use service principals for automation | Avoids user credential dependencies |
| Rotate tokens regularly | Limits exposure from compromised tokens |
| Audit access periodically | Ensures least privilege compliance |

---

*Pre-reading materials for Databricks Platform Administration Training - Day 8*
