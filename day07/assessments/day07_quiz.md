# Day 7 Quiz: Unity Catalog Security & Governance

## Databricks Platform Administration Training
### Duration: 10 Minutes | 10 Questions | 70% to Pass

---

### Question 1
What SQL command is used to give a user access to a Unity Catalog object?

- [ ] A) PERMIT
- [ ] B) ALLOW
- [ ] C) GRANT
- [ ] D) ENABLE

---

### Question 2
Which privilege is REQUIRED to access any child objects within a catalog or schema?

- [ ] A) SELECT
- [ ] B) USAGE
- [ ] C) READ
- [ ] D) ACCESS

---

### Question 3
To allow a user to SELECT from a table, what minimum permissions are needed?

- [ ] A) SELECT on the table only
- [ ] B) USAGE on catalog + SELECT on table
- [ ] C) USAGE on catalog + USAGE on schema + SELECT on table
- [ ] D) ALL PRIVILEGES on the table

---

### Question 4
What happens when you grant SELECT on a SCHEMA?

- [ ] A) User can select from that specific schema object
- [ ] B) User can select from all current and future tables in that schema
- [ ] C) User can only select from tables created before the grant
- [ ] D) Nothing, SELECT cannot be granted on schemas

---

### Question 5
Which function checks if the current user belongs to a specific group?

- [ ] A) in_group('group_name')
- [ ] B) member_of('group_name')
- [ ] C) is_member_of('group_name')
- [ ] D) belongs_to('group_name')

---

### Question 6
What does Unity Catalog data lineage track?

- [ ] A) Only table creation times
- [ ] B) User login history
- [ ] C) How data flows from source to destination through transformations
- [ ] D) Storage costs per table

---

### Question 7
Where can you view data lineage in Databricks?

- [ ] A) Admin Console only
- [ ] B) Cluster settings page
- [ ] C) Data Explorer, under the Lineage tab
- [ ] D) Job scheduler

---

### Question 8
What SQL command shows the current permissions on a table?

- [ ] A) DESCRIBE PERMISSIONS table_name
- [ ] B) SHOW GRANTS ON TABLE table_name
- [ ] C) LIST PERMISSIONS table_name
- [ ] D) VIEW ACCESS table_name

---

### Question 9
Which admin role can create new catalogs in Unity Catalog?

- [ ] A) Workspace Admin
- [ ] B) Cluster Admin
- [ ] C) Metastore Admin
- [ ] D) SQL Admin

---

### Question 10
What is the recommended approach for managing permissions in Unity Catalog?

- [ ] A) Grant permissions to individual users
- [ ] B) Grant permissions to groups
- [ ] C) Use ALL PRIVILEGES for everyone
- [ ] D) Avoid using GRANT statements

---

## Answer Key

| Q | Answer | Explanation |
|---|--------|-------------|
| 1 | C | GRANT is the standard SQL command for giving permissions |
| 2 | B | USAGE is required on containers (catalog, schema) to access any children |
| 3 | C | Users need USAGE on catalog, USAGE on schema, and SELECT on the table |
| 4 | B | Schema-level grants apply to all current and future objects in that schema |
| 5 | C | is_member_of('group_name') returns true if user belongs to the group |
| 6 | C | Lineage tracks data flow from sources through transformations to destinations |
| 7 | C | Lineage is visible in Data Explorer under the Lineage tab for tables/views |
| 8 | B | SHOW GRANTS ON TABLE displays all permissions on that table |
| 9 | C | Metastore Admin has the authority to create catalogs |
| 10 | B | Best practice is to grant permissions to groups, not individual users |

---

*Quiz Version: 2.0 | Databricks Platform Administration Training - Day 7*
