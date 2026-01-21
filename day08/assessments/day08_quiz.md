# Day 8 Quiz: IAM, SCIM & Identity Integration

## Databricks Platform Administration Training
### Duration: 10 Minutes | 10 Questions | 70% to Pass

---

### Question 1
What does SCIM stand for?

- [ ] A) Secure Cloud Identity Manager
- [ ] B) System for Cross-domain Identity Management
- [ ] C) Single Cloud Identity Module
- [ ] D) Synchronized Credential Identity Mapping

---

### Question 2
Where should users and groups be managed for Unity Catalog to work properly?

- [ ] A) Workspace level only
- [ ] B) Account level
- [ ] C) Cluster level
- [ ] D) Catalog level

---

### Question 3
What is the primary benefit of SCIM provisioning?

- [ ] A) Faster query performance
- [ ] B) Automatic user provisioning and deprovisioning
- [ ] C) Better data encryption
- [ ] D) Lower storage costs

---

### Question 4
What type of identity is used for CI/CD pipelines and automation?

- [ ] A) Regular user account
- [ ] B) Admin user account
- [ ] C) Service principal
- [ ] D) Guest account

---

### Question 5
Which authentication method is recommended for service principals?

- [ ] A) Username and password
- [ ] B) Personal Access Token (PAT)
- [ ] C) OAuth machine-to-machine (M2M)
- [ ] D) SAML assertion

---

### Question 6
What protocol is commonly used for enterprise SSO with Databricks?

- [ ] A) FTP
- [ ] B) SAML 2.0
- [ ] C) SMTP
- [ ] D) SSH

---

### Question 7
What happens when a user is removed from the IdP with SCIM enabled?

- [ ] A) Nothing, manual intervention required
- [ ] B) User is automatically deactivated in Databricks
- [ ] C) User's data is deleted
- [ ] D) User is promoted to admin

---

### Question 8
What is the purpose of a Personal Access Token (PAT)?

- [ ] A) To encrypt data at rest
- [ ] B) To authenticate API requests
- [ ] C) To create new users
- [ ] D) To configure SSO

---

### Question 9
Which identity provider is NOT typically supported for Databricks SSO?

- [ ] A) Microsoft Entra ID (Azure AD)
- [ ] B) Okta
- [ ] C) Local file-based authentication
- [ ] D) Ping Identity

---

### Question 10
What should you always maintain when configuring SSO?

- [ ] A) Multiple SCIM tokens
- [ ] B) A backup admin account with password login
- [ ] C) Duplicate service principals
- [ ] D) Expired OAuth secrets

---

## Answer Key

| Q | Answer | Explanation |
|---|--------|-------------|
| 1 | B | SCIM = System for Cross-domain Identity Management |
| 2 | B | Unity Catalog requires account-level identity management |
| 3 | B | SCIM automates user provisioning when users join/leave in IdP |
| 4 | C | Service principals are non-human identities for automation |
| 5 | C | OAuth M2M provides better security with managed credentials |
| 6 | B | SAML 2.0 is the standard protocol for enterprise SSO |
| 7 | B | SCIM automatically syncs user deactivation from IdP to Databricks |
| 8 | B | PATs are bearer tokens used to authenticate API requests |
| 9 | C | Databricks requires enterprise IdPs, not local file-based auth |
| 10 | B | Always keep a backup admin with password login during SSO setup |

---

*Quiz Version: 2.0 | Databricks Platform Administration Training - Day 8*
