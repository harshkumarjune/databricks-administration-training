# Day 2 Quiz: Platform Administration Overview

## Databricks Platform Administration Training
### Duration: 10 Minutes | 10 Questions | 70% to Pass

---

## Instructions

- Select the **best** answer for each question
- Some questions may have multiple correct answers - select ALL that apply where indicated
- You need **70% (7/10)** to pass

---

### Question 1
What is the primary difference between Account Console and Workspace Admin Console?

- [ ] A) Account Console is for users, Workspace Admin Console is for admins
- [ ] B) Account Console manages organization-wide settings, Workspace Admin Console manages single workspace settings
- [ ] C) Account Console is for Azure only, Workspace Admin Console is for AWS
- [ ] D) There is no difference; they are the same interface

---

### Question 2
Who can provision (create) new Databricks workspaces?

- [ ] A) Any workspace user
- [ ] B) Workspace admins only
- [ ] C) Account admins only
- [ ] D) Service principals only

---

### Question 3
Which of the following are managed at the Account level? (Select ALL that apply)

- [ ] A) SSO/SAML configuration
- [ ] B) Cluster policies
- [ ] C) Unity Catalog metastores
- [ ] D) Workspace creation
- [ ] E) Personal access token policies

---

### Question 4
What is a best practice for assigning permissions in Databricks?

- [ ] A) Assign permissions directly to individual users
- [ ] B) Assign permissions to groups, not individuals
- [ ] C) Give all users admin access for convenience
- [ ] D) Create a new user for each permission level

---

### Question 5
Why is workspace naming important during provisioning?

- [ ] A) Names can be changed easily at any time
- [ ] B) Names cannot be changed after creation
- [ ] C) Names are not visible to users
- [ ] D) Names don't matter for organization

---

### Question 6
Which section of the Workspace Admin Console would you use to restrict cluster configurations?

- [ ] A) Users
- [ ] B) Groups
- [ ] C) Cluster Policies
- [ ] D) Workspace Settings

---

### Question 7
What are the two built-in groups in every Databricks workspace?

- [ ] A) `admins` and `users`
- [ ] B) `administrators` and `readers`
- [ ] C) `owners` and `guests`
- [ ] D) `super-admins` and `regular-users`

---

### Question 8
Which workspace strategy provides clear separation between development and production environments?

- [ ] A) Single workspace for everything
- [ ] B) Separate workspaces by environment (dev/staging/prod)
- [ ] C) Separate folders within one workspace
- [ ] D) Using different clusters in one workspace

---

### Question 9
What enables data sharing between multiple workspaces without data duplication?

- [ ] A) Manual data copying
- [ ] B) Unity Catalog
- [ ] C) Personal access tokens
- [ ] D) Instance pools

---

### Question 10
Which of the following are typically managed at the Workspace level? (Select ALL that apply)

- [ ] A) User and group management within the workspace
- [ ] B) SCIM identity provider configuration
- [ ] C) Cluster policies
- [ ] D) SQL warehouse configuration
- [ ] E) SSO/SAML setup

---

## Answer Key

| Question | Correct Answer(s) | Explanation |
|----------|-------------------|-------------|
| 1 | B | Account Console manages all workspaces and org-wide settings; Workspace Admin Console manages a single workspace |
| 2 | C | Only Account Admins can create new workspaces through the Account Console |
| 3 | A, C, D | SSO, metastores, and workspace creation are account-level. Cluster policies and token policies are workspace-level |
| 4 | B | Always assign permissions to groups for easier management, auditing, and scalability |
| 5 | B | Workspace names are permanent and cannot be changed after creation |
| 6 | C | Cluster Policies define and restrict allowed cluster configurations |
| 7 | A | Every workspace has built-in `admins` and `users` groups |
| 8 | B | Separate workspaces provide clear isolation between environments |
| 9 | B | Unity Catalog enables cross-workspace data governance and sharing |
| 10 | A, C, D | Workspace-level includes users/groups (local), policies, and warehouses. SCIM and SSO are account-level |

---

## Scoring

| Score | Result |
|-------|--------|
| 9-10 | Excellent! Strong understanding of platform administration |
| 7-8 | Passed. Review any missed topics |
| 5-6 | Needs improvement. Review slides before Day 3 |
| Below 5 | Recommended: Re-review Day 2 materials |

---

*Quiz Version: 2.0 | Databricks Platform Administration Training - Day 2*
