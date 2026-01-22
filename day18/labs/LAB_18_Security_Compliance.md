# Lab 18: Security & Compliance Controls
## Databricks Platform Administration Training

**Duration:** 45 minutes
**Difficulty:** Advanced
**Prerequisites:** Days 14-17 completed

---

## Lab Overview

In this lab, you will configure network security controls, implement data protection mechanisms, and map Databricks features to compliance frameworks. You'll learn to secure an enterprise Databricks environment following SOC 2 and GDPR requirements.

---

## Learning Objectives

By completing this lab, you will be able to:
- Configure IP access lists for workspace protection
- Implement column-level masking functions
- Create row-level security policies
- Map Databricks features to compliance controls
- Generate compliance audit reports

---

## Part 1: IP Access Lists (10 minutes)

### Task 1.1: Review Current IP Access Configuration

1. Navigate to **Admin Settings** → **Security**
2. Click on **IP Access Lists**
3. Review current configuration:
   - Is IP filtering enabled?
   - What IP ranges are currently allowed?

### Task 1.2: Configure IP Allowlist (Demo/Discussion)

**Note:** Changing IP access lists can lock you out. Practice in sandbox only.

**Conceptual Configuration:**

```json
{
  "label": "Corporate Network",
  "ip_addresses": [
    "10.0.0.0/8",
    "192.168.1.0/24",
    "203.0.113.50/32"
  ],
  "list_type": "ALLOW"
}
```

**Best Practices:**
- Always include your current IP first
- Use CIDR notation for ranges
- Test with a single user before company-wide rollout
- Have emergency override plan documented

### Task 1.3: Document Network Security Controls

Complete the following checklist for your environment:

| Control | Status | Notes |
|---------|--------|-------|
| IP access lists enabled | [ ] Yes [ ] No | |
| VNet/VPC injection | [ ] Yes [ ] No | |
| Private Link configured | [ ] Yes [ ] No | |
| NAT gateway for egress | [ ] Yes [ ] No | |

---

## Part 2: Column Masking (15 minutes)

### Task 2.1: Create Masking Functions

1. Navigate to **SQL Editor**
2. Create a schema for security functions:

```sql
-- Create schema for security functions (if not exists)
CREATE SCHEMA IF NOT EXISTS training_catalog.security_functions;
```

3. Create masking functions:

```sql
-- Email masking function
CREATE OR REPLACE FUNCTION training_catalog.security_functions.mask_email(email STRING)
RETURNS STRING
LANGUAGE SQL
DETERMINISTIC
RETURN CONCAT(
  SUBSTRING(email, 1, 2),
  '***@',
  SPLIT(email, '@')[1]
);

-- SSN masking function (shows last 4 digits)
CREATE OR REPLACE FUNCTION training_catalog.security_functions.mask_ssn(ssn STRING)
RETURNS STRING
LANGUAGE SQL
DETERMINISTIC
RETURN CONCAT('***-**-', RIGHT(REPLACE(ssn, '-', ''), 4));

-- Credit card masking function
CREATE OR REPLACE FUNCTION training_catalog.security_functions.mask_credit_card(card_num STRING)
RETURNS STRING
LANGUAGE SQL
DETERMINISTIC
RETURN CONCAT('****-****-****-', RIGHT(REPLACE(card_num, '-', ''), 4));
```

### Task 2.2: Test Masking Functions

```sql
-- Test the masking functions
SELECT
  'john.doe@company.com' as original_email,
  training_catalog.security_functions.mask_email('john.doe@company.com') as masked_email;

SELECT
  '123-45-6789' as original_ssn,
  training_catalog.security_functions.mask_ssn('123-45-6789') as masked_ssn;

SELECT
  '4111-1111-1111-1234' as original_card,
  training_catalog.security_functions.mask_credit_card('4111-1111-1111-1234') as masked_card;
```

### Task 2.3: Apply Masking to Table (Conceptual)

**Note:** Applying column masks requires appropriate permissions.

```sql
-- Apply mask to column (Unity Catalog syntax)
ALTER TABLE training_catalog.hr.employees
ALTER COLUMN email
SET MASK training_catalog.security_functions.mask_email;

-- Verify mask is applied
DESCRIBE TABLE EXTENDED training_catalog.hr.employees;
```

---

## Part 3: Row-Level Security (10 minutes)

### Task 3.1: Create Row Filter Function

```sql
-- Row filter function: Users see only their department's data
CREATE OR REPLACE FUNCTION training_catalog.security_functions.department_filter(dept STRING)
RETURNS BOOLEAN
LANGUAGE SQL
DETERMINISTIC
RETURN (
  -- Check if user has full access (admins)
  IS_ACCOUNT_GROUP_MEMBER('data_admins')
  OR
  -- Or if their department matches
  dept = CURRENT_USER_ATTRIBUTE('department')
);
```

### Task 3.2: Apply Row Filter (Conceptual)

```sql
-- Apply row filter to table
ALTER TABLE training_catalog.hr.employees
SET ROW FILTER training_catalog.security_functions.department_filter ON (department);
```

### Task 3.3: Test Row-Level Security

Test as different users to verify filtering:

```sql
-- Check what current user can see
SELECT
  CURRENT_USER() as logged_in_user,
  COUNT(*) as visible_rows
FROM training_catalog.hr.employees;

-- View current user attributes (if configured)
SELECT
  CURRENT_USER_ATTRIBUTE('department') as user_department;
```

---

## Part 4: Compliance Mapping (10 minutes)

### Task 4.1: SOC 2 Control Mapping

Map Databricks features to SOC 2 Trust Service Criteria:

| SOC 2 Control | Databricks Feature | Configuration |
|---------------|-------------------|---------------|
| CC6.1 - Logical Access | Unity Catalog permissions | GRANT/REVOKE |
| CC6.6 - System Boundaries | VNet injection, Private Link | Network isolation |
| CC6.7 - Transmission Protection | TLS 1.2+, encryption in transit | Default enabled |
| CC7.1 - System Monitoring | Audit logs, system tables | Enabled by default |
| CC8.1 - Change Management | Git integration, notebooks versioning | Workspace settings |

### Task 4.2: GDPR Compliance Checklist

Complete the GDPR readiness assessment:

| GDPR Requirement | Databricks Feature | Status |
|------------------|-------------------|--------|
| Data minimization | Column masking | [ ] Implemented |
| Purpose limitation | Row-level security | [ ] Implemented |
| Access requests | Audit logs query | [ ] Query ready |
| Right to erasure | DELETE capability | [ ] Process documented |
| Data portability | EXPORT capability | [ ] Process documented |
| Consent tracking | Custom audit tables | [ ] Designed |

### Task 4.3: Generate Compliance Report Query

```sql
-- Compliance audit: Data access summary
SELECT
    DATE(event_time) as access_date,
    user_identity.email as user_email,
    action_name,
    request_params.table_full_name as table_accessed,
    COUNT(*) as access_count
FROM system.access.audit
WHERE event_time >= current_date() - 30
  AND action_name LIKE '%Table%'
  AND request_params.table_full_name LIKE '%pii%'  -- PII tables
GROUP BY
    DATE(event_time),
    user_identity.email,
    action_name,
    request_params.table_full_name
ORDER BY access_date DESC, access_count DESC;

-- Data modification tracking for GDPR
SELECT
    event_time,
    user_identity.email,
    action_name,
    request_params.table_full_name,
    response.status_code
FROM system.access.audit
WHERE action_name IN ('DELETE', 'UPDATE', 'TRUNCATE')
  AND event_time >= current_date() - 90
ORDER BY event_time DESC;
```

---

## Cleanup

```sql
-- Remove test functions (if created in non-production)
DROP FUNCTION IF EXISTS training_catalog.security_functions.mask_email;
DROP FUNCTION IF EXISTS training_catalog.security_functions.mask_ssn;
DROP FUNCTION IF EXISTS training_catalog.security_functions.mask_credit_card;
DROP FUNCTION IF EXISTS training_catalog.security_functions.department_filter;
DROP SCHEMA IF EXISTS training_catalog.security_functions;
```

---

## Lab Validation Checklist

- [ ] Reviewed IP access list configuration
- [ ] Created column masking functions
- [ ] Tested masking function output
- [ ] Understood row-level security concepts
- [ ] Completed SOC 2 control mapping
- [ ] Completed GDPR compliance checklist
- [ ] Wrote compliance audit query

---

## Discussion Questions

1. How would you implement "break glass" access for emergency situations?
2. What's the difference between column masking and column-level permissions?
3. How often should compliance reports be generated and reviewed?
4. What additional controls are needed for PCI-DSS compliance?
5. How do you balance security with data science productivity?

---

## Assignment (Optional - Advanced)

**Security Architecture Document**

Create a security architecture document for a hypothetical healthcare organization (HIPAA compliance required):

1. **Data Classification Scheme**
   - PHI data handling
   - De-identification approach
   - Access tiers

2. **Technical Controls Matrix**
   - Network security
   - Data encryption
   - Access controls
   - Audit logging

3. **Compliance Mapping**
   - HIPAA Security Rule requirements
   - Databricks feature mapping
   - Gap analysis

4. **Incident Response Plan Outline**
   - Detection mechanisms
   - Response procedures
   - Notification requirements

---

*Lab Version: 3.0 | Day 18 - Security & Compliance Controls*
