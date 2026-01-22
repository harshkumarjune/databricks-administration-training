"""
Capstone Project Validator
Databricks Platform Administration Training

This script validates capstone project deliverables by checking:
1. Unity Catalog structure (catalogs, schemas)
2. Permission grants
3. Cluster policy syntax
4. SQL warehouse configuration

Usage:
    - Run in Databricks notebook
    - Run locally with databricks-connect configured

Author: Training Team
Version: 3.0
"""

from typing import Dict, List, Tuple
import json
import re

# ============================================================================
# VALIDATION CLASSES
# ============================================================================

class ValidationResult:
    """Represents the result of a validation check."""

    def __init__(self, passed: bool, message: str, score: int = 0, max_score: int = 0):
        self.passed = passed
        self.message = message
        self.score = score
        self.max_score = max_score

    def __repr__(self):
        status = "✓ PASS" if self.passed else "✗ FAIL"
        return f"{status}: {self.message} ({self.score}/{self.max_score} pts)"


class CapstonValidator:
    """Validates capstone project deliverables."""

    def __init__(self, track: str = "beginner"):
        """
        Initialize validator for specific track.

        Args:
            track: One of 'beginner', 'intermediate', 'advanced'
        """
        self.track = track
        self.results: List[ValidationResult] = []
        self.total_score = 0
        self.max_total_score = 0

    # ========================================================================
    # UNITY CATALOG VALIDATION
    # ========================================================================

    def validate_catalog_structure(self, sql_statements: str) -> List[ValidationResult]:
        """
        Validate Unity Catalog SQL statements.

        Args:
            sql_statements: SQL statements as string

        Returns:
            List of validation results
        """
        results = []

        # Check for required catalogs
        required_catalogs = ["dev_techflow", "prod_techflow"]
        if self.track in ["intermediate", "advanced"]:
            required_catalogs.append("staging_techflow")

        for catalog in required_catalogs:
            if f"CREATE CATALOG" in sql_statements.upper() and catalog in sql_statements.lower():
                results.append(ValidationResult(
                    True, f"Catalog '{catalog}' creation found", 3, 3
                ))
            else:
                results.append(ValidationResult(
                    False, f"Catalog '{catalog}' creation NOT found", 0, 3
                ))

        # Check for required schemas
        required_schemas = ["sales", "customers"]
        if self.track in ["intermediate", "advanced"]:
            required_schemas.extend(["bronze", "silver", "gold"])

        for schema in required_schemas:
            if f"CREATE SCHEMA" in sql_statements.upper() and schema in sql_statements.lower():
                results.append(ValidationResult(
                    True, f"Schema '{schema}' creation found", 2, 2
                ))
            else:
                results.append(ValidationResult(
                    False, f"Schema '{schema}' creation NOT found", 0, 2
                ))

        return results

    def validate_permissions(self, sql_statements: str) -> List[ValidationResult]:
        """
        Validate permission GRANT statements.

        Args:
            sql_statements: SQL statements as string

        Returns:
            List of validation results
        """
        results = []

        # Check for required groups getting permissions
        required_groups = ["data_engineers", "data_analysts", "platform_admins"]
        if self.track in ["intermediate", "advanced"]:
            required_groups.extend(["data_scientists", "finance_team"])

        for group in required_groups:
            if group in sql_statements.lower():
                results.append(ValidationResult(
                    True, f"Permissions for '{group}' found", 3, 3
                ))
            else:
                results.append(ValidationResult(
                    False, f"Permissions for '{group}' NOT found", 0, 3
                ))

        # Check for GRANT statements
        grant_count = sql_statements.upper().count("GRANT ")
        min_grants = {"beginner": 3, "intermediate": 8, "advanced": 12}

        if grant_count >= min_grants[self.track]:
            results.append(ValidationResult(
                True, f"Sufficient GRANT statements ({grant_count} found)", 5, 5
            ))
        else:
            results.append(ValidationResult(
                False, f"Insufficient GRANT statements ({grant_count} found, need {min_grants[self.track]})",
                min(grant_count, min_grants[self.track]), 5
            ))

        return results

    # ========================================================================
    # CLUSTER POLICY VALIDATION
    # ========================================================================

    def validate_cluster_policy(self, policy_json: str, policy_type: str = "dev") -> List[ValidationResult]:
        """
        Validate cluster policy JSON.

        Args:
            policy_json: Policy definition as JSON string
            policy_type: One of 'dev', 'prod', 'ml'

        Returns:
            List of validation results
        """
        results = []

        try:
            policy = json.loads(policy_json)
        except json.JSONDecodeError:
            results.append(ValidationResult(
                False, "Invalid JSON syntax in cluster policy", 0, 5
            ))
            return results

        results.append(ValidationResult(
            True, "Valid JSON syntax", 2, 2
        ))

        # Check for required attributes
        required_attrs = {
            "dev": ["spark_version", "node_type_id", "num_workers", "autotermination_minutes"],
            "prod": ["spark_version", "node_type_id", "autoscale.min_workers", "autoscale.max_workers"],
            "ml": ["spark_version", "node_type_id", "cluster_type"]
        }

        definition = policy.get("definition", policy)

        for attr in required_attrs.get(policy_type, []):
            if attr in definition:
                results.append(ValidationResult(
                    True, f"Policy attribute '{attr}' present", 2, 2
                ))
            else:
                results.append(ValidationResult(
                    False, f"Policy attribute '{attr}' MISSING", 0, 2
                ))

        # Check for required tags (cost allocation)
        tag_attrs = [k for k in definition.keys() if k.startswith("custom_tags")]
        if tag_attrs:
            results.append(ValidationResult(
                True, f"Custom tags configured ({len(tag_attrs)} found)", 3, 3
            ))
        else:
            results.append(ValidationResult(
                False, "No custom tags configured for cost allocation", 0, 3
            ))

        # Check for mandatory tags
        team_tag = definition.get("custom_tags.Team", {})
        if team_tag.get("isOptional") == False:
            results.append(ValidationResult(
                True, "Team tag is mandatory", 3, 3
            ))
        else:
            results.append(ValidationResult(
                False, "Team tag should be mandatory (isOptional: false)", 0, 3
            ))

        return results

    # ========================================================================
    # ADVANCED VALIDATION (Security, Compliance)
    # ========================================================================

    def validate_security_config(self, config: Dict) -> List[ValidationResult]:
        """
        Validate security configuration (Advanced track only).

        Args:
            config: Security configuration dictionary

        Returns:
            List of validation results
        """
        results = []

        if self.track != "advanced":
            return results

        # Check network security
        network_features = ["vnet_injection", "private_link", "ip_access_lists", "secure_cluster_connectivity"]
        for feature in network_features:
            if config.get(feature, {}).get("enabled", False):
                results.append(ValidationResult(
                    True, f"Network feature '{feature}' enabled", 2, 2
                ))
            else:
                results.append(ValidationResult(
                    False, f"Network feature '{feature}' NOT configured", 0, 2
                ))

        # Check data security
        if config.get("encryption", {}).get("cmk_enabled", False):
            results.append(ValidationResult(
                True, "Customer-managed keys (CMK) enabled", 3, 3
            ))
        else:
            results.append(ValidationResult(
                False, "Customer-managed keys (CMK) NOT enabled", 0, 3
            ))

        return results

    def validate_compliance_controls(self, controls: Dict) -> List[ValidationResult]:
        """
        Validate compliance controls (Advanced track only).

        Args:
            controls: Compliance controls dictionary

        Returns:
            List of validation results
        """
        results = []

        if self.track != "advanced":
            return results

        # SOC 2 controls
        soc2_controls = ["access_control", "change_management", "logging", "data_protection"]
        soc2_configured = sum(1 for c in soc2_controls if c in controls.get("soc2", {}))

        results.append(ValidationResult(
            soc2_configured >= 3,
            f"SOC 2 controls: {soc2_configured}/4 configured",
            soc2_configured * 2, 8
        ))

        # GDPR controls
        gdpr_controls = ["data_minimization", "right_to_erasure", "consent_tracking", "audit_logging"]
        gdpr_configured = sum(1 for c in gdpr_controls if c in controls.get("gdpr", {}))

        results.append(ValidationResult(
            gdpr_configured >= 3,
            f"GDPR controls: {gdpr_configured}/4 configured",
            gdpr_configured * 2, 8
        ))

        return results

    # ========================================================================
    # MAIN VALIDATION METHOD
    # ========================================================================

    def validate_all(self, submission: Dict) -> Dict:
        """
        Run all validations for the capstone submission.

        Args:
            submission: Dictionary containing all submission components:
                - catalog_sql: Unity Catalog SQL statements
                - permission_sql: Permission GRANT statements
                - dev_policy: Development cluster policy JSON
                - prod_policy: Production cluster policy JSON
                - ml_policy: ML cluster policy JSON (intermediate/advanced)
                - security_config: Security configuration (advanced)
                - compliance_controls: Compliance controls (advanced)

        Returns:
            Dictionary with validation results and score
        """
        all_results = []

        # Validate catalog structure
        if "catalog_sql" in submission:
            all_results.extend(self.validate_catalog_structure(submission["catalog_sql"]))

        # Validate permissions
        if "permission_sql" in submission:
            all_results.extend(self.validate_permissions(submission["permission_sql"]))

        # Validate cluster policies
        if "dev_policy" in submission:
            all_results.extend(self.validate_cluster_policy(submission["dev_policy"], "dev"))

        if self.track in ["intermediate", "advanced"] and "prod_policy" in submission:
            all_results.extend(self.validate_cluster_policy(submission["prod_policy"], "prod"))

        if self.track == "advanced" and "ml_policy" in submission:
            all_results.extend(self.validate_cluster_policy(submission["ml_policy"], "ml"))

        # Validate security and compliance (advanced only)
        if self.track == "advanced":
            if "security_config" in submission:
                all_results.extend(self.validate_security_config(submission["security_config"]))
            if "compliance_controls" in submission:
                all_results.extend(self.validate_compliance_controls(submission["compliance_controls"]))

        # Calculate totals
        total_score = sum(r.score for r in all_results)
        max_score = sum(r.max_score for r in all_results)
        passed_checks = sum(1 for r in all_results if r.passed)
        total_checks = len(all_results)

        # Determine grade
        percentage = (total_score / max_score * 100) if max_score > 0 else 0
        if percentage >= 90:
            grade = "A (Certification Ready)"
        elif percentage >= 80:
            grade = "B (Strong Foundation)"
        elif percentage >= 70:
            grade = "C (Meets Minimum)"
        else:
            grade = "NC (Requires Resubmission)"

        return {
            "track": self.track,
            "results": all_results,
            "total_score": total_score,
            "max_score": max_score,
            "percentage": round(percentage, 1),
            "grade": grade,
            "passed_checks": passed_checks,
            "total_checks": total_checks
        }

    def print_report(self, validation_result: Dict):
        """Print a formatted validation report."""
        print("=" * 60)
        print(f"CAPSTONE VALIDATION REPORT - {self.track.upper()} TRACK")
        print("=" * 60)
        print()

        for result in validation_result["results"]:
            status = "✓" if result.passed else "✗"
            print(f"  {status} {result.message} ({result.score}/{result.max_score})")

        print()
        print("-" * 60)
        print(f"Total Score: {validation_result['total_score']}/{validation_result['max_score']} ({validation_result['percentage']}%)")
        print(f"Checks Passed: {validation_result['passed_checks']}/{validation_result['total_checks']}")
        print(f"Grade: {validation_result['grade']}")
        print("=" * 60)


# ============================================================================
# SAMPLE USAGE
# ============================================================================

if __name__ == "__main__":
    # Example submission for validation
    sample_submission = {
        "catalog_sql": """
            CREATE CATALOG IF NOT EXISTS dev_techflow;
            CREATE CATALOG IF NOT EXISTS prod_techflow;

            USE CATALOG dev_techflow;
            CREATE SCHEMA IF NOT EXISTS sales;
            CREATE SCHEMA IF NOT EXISTS customers;

            USE CATALOG prod_techflow;
            CREATE SCHEMA IF NOT EXISTS bronze;
            CREATE SCHEMA IF NOT EXISTS silver;
            CREATE SCHEMA IF NOT EXISTS gold;
        """,
        "permission_sql": """
            GRANT ALL PRIVILEGES ON CATALOG dev_techflow TO data_engineers;
            GRANT ALL PRIVILEGES ON CATALOG prod_techflow TO platform_admins;
            GRANT SELECT ON CATALOG prod_techflow TO data_analysts;
            GRANT SELECT ON SCHEMA prod_techflow.gold TO data_scientists;
            GRANT ALL PRIVILEGES ON SCHEMA prod_techflow.finance TO finance_team;
        """,
        "dev_policy": json.dumps({
            "name": "techflow-dev-policy",
            "definition": {
                "spark_version": {"type": "regex", "pattern": "^14.*"},
                "node_type_id": {"type": "allowlist", "values": ["Standard_DS3_v2"]},
                "num_workers": {"type": "range", "minValue": 1, "maxValue": 4},
                "autotermination_minutes": {"type": "range", "minValue": 15, "maxValue": 60},
                "custom_tags.Team": {"type": "unlimited", "isOptional": False},
                "custom_tags.Environment": {"type": "fixed", "value": "development"}
            }
        })
    }

    # Run validation
    validator = CapstonValidator(track="intermediate")
    results = validator.validate_all(sample_submission)
    validator.print_report(results)
