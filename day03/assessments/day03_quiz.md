# Day 3 Quiz: User, Group & Role Management

## Databricks Platform Administration Training
### Duration: 10 Minutes | 10 Questions | 70% to Pass

---

## Instructions

- Select the **best** answer for each question
- Some questions may have multiple correct answers - select ALL that apply where indicated
- You need **70% (7/10)** to pass

---

### Question 1
What are the three main identity types in Databricks?

- [ ] A) Admins, Users, and Guests
- [ ] B) Users, Groups, and Service Principals
- [ ] C) Owners, Contributors, and Readers
- [ ] D) Humans, Machines, and Bots

---

### Question 2
Which identity type should be used for CI/CD pipeline automation?

- [ ] A) Shared human user account
- [ ] B) Personal Access Token from any user
- [ ] C) Service Principal
- [ ] D) Admin account

---

### Question 3
What are the two built-in groups in every Databricks workspace?

- [ ] A) `owners` and `viewers`
- [ ] B) `admins` and `users`
- [ ] C) `administrators` and `members`
- [ ] D) `super-users` and `regular-users`

---

### Question 4
According to best practices, how should permissions be assigned?

- [ ] A) Directly to individual users for precise control
- [ ] B) To groups, never to individual users
- [ ] C) Only through service principals
- [ ] D) Randomly to distribute access

---

### Question 5
What is the "Principle of Least Privilege"?

- [ ] A) Give all users admin access for convenience
- [ ] B) Grant only the minimum permissions needed for job functions
- [ ] C) Restrict access to only one user per resource
- [ ] D) Remove all permissions and add them back one by one

---

### Question 6
Which admin role has the broadest scope?

- [ ] A) Workspace Admin
- [ ] B) Metastore Admin
- [ ] C) Account Admin/Owner
- [ ] D) Data Owner

---

### Question 7
What entitlement controls whether a user can create clusters?

- [ ] A) Workspace access
- [ ] B) Databricks SQL access
- [ ] C) Allow cluster creation
- [ ] D) Admin privileges

---

### Question 8
How does entitlement inheritance work with nested groups?

- [ ] A) Entitlements do not inherit through groups
- [ ] B) Only direct group members get entitlements
- [ ] C) Members inherit entitlements from all parent groups
- [ ] D) Inheritance must be manually enabled for each group

---

### Question 9
Which of the following are recommended practices for access reviews? (Select ALL that apply)

- [ ] A) Conduct reviews quarterly at minimum
- [ ] B) Review admin privileges regularly
- [ ] C) Check for inactive users
- [ ] D) Never remove access without a support ticket
- [ ] E) Document review decisions

---

### Question 10
What is a common anti-pattern in Databricks access management?

- [ ] A) Using groups for permission management
- [ ] B) Assigning permissions directly to individual users
- [ ] C) Using service principals for automation
- [ ] D) Conducting regular access reviews

---

## Answer Key

| Question | Correct Answer(s) | Explanation |
|----------|-------------------|-------------|
| 1 | B | Users (human), Groups (collections), and Service Principals (automation) |
| 2 | C | Service Principals are designed for non-human, automated access |
| 3 | B | `admins` for workspace administrators, `users` for all workspace users |
| 4 | B | Always assign to groups for scalability and auditability |
| 5 | B | Grant minimum necessary permissions to reduce risk |
| 6 | C | Account Admin/Owner manages the entire Databricks account |
| 7 | C | "Allow cluster creation" entitlement controls cluster creation ability |
| 8 | C | Group members inherit entitlements from all groups they belong to (directly or nested) |
| 9 | A, B, C, E | All are best practices except D - access should be removable by admins |
| 10 | B | Direct user permissions don't scale and are hard to audit |

---

## Scoring

| Score | Result |
|-------|--------|
| 9-10 | Excellent! Strong understanding of access management |
| 7-8 | Passed. Review any missed topics |
| 5-6 | Needs improvement. Review slides before Day 4 |
| Below 5 | Recommended: Re-review Day 3 materials |

---

*Quiz Version: 2.0 | Databricks Platform Administration Training - Day 3*
