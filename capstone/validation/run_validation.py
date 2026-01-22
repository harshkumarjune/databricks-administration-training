#!/usr/bin/env python3
"""
Capstone Validation Runner
Databricks Platform Administration Training

This script runs validation on capstone project submissions.
Can be run locally or in a Databricks notebook.

Usage:
    python run_validation.py --track beginner --submission submission.json
    python run_validation.py --track intermediate --catalog-sql catalog.sql --policy dev_policy.json

Author: Training Team
Version: 3.0
"""

import argparse
import json
import sys
from pathlib import Path

# Import validator (adjust path as needed)
try:
    from capstone_validator import CapstonValidator
except ImportError:
    # For Databricks notebook execution
    import sys
    sys.path.append('/Workspace/Users/.../capstone/validation')
    from capstone_validator import CapstonValidator


def load_file(filepath: str) -> str:
    """Load content from a file."""
    with open(filepath, 'r') as f:
        return f.read()


def run_validation(args):
    """Run capstone validation based on command line arguments."""

    # Build submission dictionary
    submission = {}

    if args.submission:
        # Load full submission from JSON file
        with open(args.submission, 'r') as f:
            submission = json.load(f)
    else:
        # Build from individual files
        if args.catalog_sql:
            submission["catalog_sql"] = load_file(args.catalog_sql)
        if args.permission_sql:
            submission["permission_sql"] = load_file(args.permission_sql)
        if args.dev_policy:
            submission["dev_policy"] = load_file(args.dev_policy)
        if args.prod_policy:
            submission["prod_policy"] = load_file(args.prod_policy)
        if args.ml_policy:
            submission["ml_policy"] = load_file(args.ml_policy)

    # Validate
    validator = CapstonValidator(track=args.track)
    results = validator.validate_all(submission)

    # Output
    if args.output_json:
        # Output as JSON
        output = {
            "track": results["track"],
            "total_score": results["total_score"],
            "max_score": results["max_score"],
            "percentage": results["percentage"],
            "grade": results["grade"],
            "passed_checks": results["passed_checks"],
            "total_checks": results["total_checks"],
            "results": [
                {
                    "passed": r.passed,
                    "message": r.message,
                    "score": r.score,
                    "max_score": r.max_score
                }
                for r in results["results"]
            ]
        }
        print(json.dumps(output, indent=2))
    else:
        # Print formatted report
        validator.print_report(results)

    # Return exit code based on pass/fail
    return 0 if results["percentage"] >= 70 else 1


def main():
    parser = argparse.ArgumentParser(
        description="Validate Databricks Capstone Project submissions"
    )

    parser.add_argument(
        "--track",
        choices=["beginner", "intermediate", "advanced"],
        default="beginner",
        help="Capstone track to validate against"
    )

    parser.add_argument(
        "--submission",
        help="Path to full submission JSON file"
    )

    parser.add_argument(
        "--catalog-sql",
        help="Path to Unity Catalog SQL file"
    )

    parser.add_argument(
        "--permission-sql",
        help="Path to permission GRANT SQL file"
    )

    parser.add_argument(
        "--dev-policy",
        help="Path to development cluster policy JSON"
    )

    parser.add_argument(
        "--prod-policy",
        help="Path to production cluster policy JSON"
    )

    parser.add_argument(
        "--ml-policy",
        help="Path to ML cluster policy JSON"
    )

    parser.add_argument(
        "--output-json",
        action="store_true",
        help="Output results as JSON"
    )

    args = parser.parse_args()

    # Validate we have something to validate
    if not args.submission and not any([
        args.catalog_sql, args.permission_sql,
        args.dev_policy, args.prod_policy, args.ml_policy
    ]):
        parser.error("Must provide either --submission or individual component files")

    sys.exit(run_validation(args))


if __name__ == "__main__":
    main()
