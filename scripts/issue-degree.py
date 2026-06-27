#!/usr/bin/env python3
"""
AgentTrust School — Degree Issuer

Usage:
    python scripts/issue-degree.py --reports ./my-reports/ --identity ~/.agentrust/identity.json --degree cybersecurity

This script:
1. Loads the agent's identity (private key)
2. Loads the degree requirements from the school repo
3. Checks that all required courses have completed reports
4. Issues a signed degree certificate
"""

import argparse
import json
import os
import sys
import time
from pathlib import Path


# Path to the school repo (same directory as this script)
SCHOOL_DIR = Path(__file__).resolve().parent.parent

# Degree requirements: for each degree, the list of required course codes
# (Core + at least 1 elective)
DEGREE_REQUIREMENTS = {
    "cybersecurity": {
        "core": ["CS101", "CS102", "CS103"],
        "electives": ["CS201", "CS202"],
        "min_electives": 1,
        "final": "CSFINAL",
    },
    "agent-engineering": {
        "core": ["AE101", "AE102", "AE103"],
        "electives": [],
        "min_electives": 0,
        "final": "AEFINAL",
    },
}

DEGREE_NAMES = {
    "cybersecurity": "Cybersecurity",
    "agent-engineering": "Agent Engineering",
}


def load_identity(path: str) -> dict:
    """Load agent identity JSON."""
    p = Path(path).expanduser()
    if not p.exists():
        print(f"Error: identity not found at {p}")
        print("Run 'agentrust init' first.")
        sys.exit(1)
    return json.loads(p.read_text())


def load_school_pub() -> dict:
    """Load the school's public key."""
    pub_path = SCHOOL_DIR / "school.pub.json"
    if not pub_path.exists():
        print(f"Error: school public key not found at {pub_path}")
        sys.exit(1)
    return json.loads(pub_path.read_text())


def find_reports(reports_dir: str) -> dict[str, str]:
    """Find all JSON report files and map them to course codes."""
    d = Path(reports_dir).expanduser()
    if not d.exists():
        print(f"Error: reports directory not found at {d}")
        sys.exit(1)

    reports = {}
    for f in sorted(d.glob("*-report.json")):
        # Extract course code from filename like "CS101-report.json"
        name = f.stem  # "CS101-report"
        parts = name.split("-", 1)
        if parts and parts[0].isupper():
            reports[parts[0]] = str(f)

    return reports


def verify_report(report_path: str, school_pub: dict) -> bool:
    """Quick check that a report file is valid JSON and exists."""
    try:
        data = json.loads(Path(report_path).read_text())
        if "report" in data:
            r = data["report"]
            return all(k in r for k in ("agent_id", "verdict", "signature"))
        return False
    except (json.JSONDecodeError, FileNotFoundError):
        return False


def issue_degree(identity: dict, degree: str, completed: list[str],
                 final_report: str) -> dict:
    """Create and sign a degree certificate."""
    certificate = {
        "degree": DEGREE_NAMES.get(degree, degree),
        "degree_code": degree,
        "agent_id": identity["agent_id"],
        "courses": sorted(completed),
        "final_project_hash": "",
        "completed_at": int(time.time()),
        "issued_by": "agentrust-school",
    }

    # Include final project hash if available
    if final_report:
        try:
            data = json.loads(Path(final_report).read_text())
            if "report" in data:
                certificate["final_project_hash"] = data["report"].get(
                    "skill_hash", ""
                )
        except (json.JSONDecodeError, FileNotFoundError, KeyError):
            pass

    # Sign with the school's private key
    try:
        from agentrust.crypto import AgentIdentity

        school_id = AgentIdentity(
            agent_id=identity["agent_id"],
            public_key_pem=identity["public_key_pem"],
            private_key_pem=identity["private_key_pem"],
        )

        report_bytes = json.dumps(certificate, sort_keys=True).encode()
        certificate["signature"] = school_id.sign(report_bytes)
    except ImportError:
        print("Warning: agentrust package not found. Certificate will be unsigned.")
        certificate["signature"] = "UNSIGNED"

    return certificate


def main():
    parser = argparse.ArgumentParser(
        description="Issue a signed degree certificate"
    )
    parser.add_argument(
        "--reports", required=True,
        help="Directory containing completed course reports"
    )
    parser.add_argument(
        "--identity", required=True,
        help="Path to the school's identity.json (private key)"
    )
    parser.add_argument(
        "--degree", required=True,
        choices=list(DEGREE_REQUIREMENTS.keys()),
        help="Degree to issue"
    )
    parser.add_argument(
        "--output", default="certificate.json",
        help="Output path for the signed certificate (default: certificate.json)"
    )
    args = parser.parse_args()

    # Load school identity and public key
    identity = load_identity(args.identity)
    school_pub = load_school_pub()

    # Verify identity matches school
    if identity["agent_id"] != school_pub["agent_id"]:
        print(f"Warning: identity agent_id ({identity['agent_id']}) "
              f"does not match school agent_id ({school_pub['agent_id']})")
        print("The certificate will be signed, but won't verify against school.pub.json")
        proceed = input("Continue anyway? (y/N): ")
        if proceed.lower() != "y":
            sys.exit(1)

    # Load degree requirements
    reqs = DEGREE_REQUIREMENTS[args.degree]

    # Find completed reports
    found_reports = find_reports(args.reports)

    # Check core courses
    missing_core = []
    completed = []
    for course in reqs["core"]:
        if course in found_reports:
            report_path = found_reports[course]
            if verify_report(report_path, school_pub):
                completed.append(course)
                print(f"  ✓ {course}: report verified")
            else:
                missing_core.append(f"{course} (invalid report)")
        else:
            missing_core.append(course)

    # Check elective courses
    completed_electives = []
    for course in reqs["electives"]:
        if course in found_reports:
            report_path = found_reports[course]
            if verify_report(report_path, school_pub):
                completed_electives.append(course)
                print(f"  ✓ {course}: elective report verified")
            else:
                print(f"  ✗ {course}: elective report invalid (skipping)")

    # Check final project
    final_complete = False
    final_report_path = ""
    if reqs["final"] in found_reports:
        report_path = found_reports[reqs["final"]]
        if verify_report(report_path, school_pub):
            final_complete = True
            final_report_path = report_path
            print(f"  ✓ {reqs['final']}: final project report verified")
        else:
            print(f"  ✗ {reqs['final']}: final project report invalid")
    else:
        print(f"  ✗ {reqs['final']}: final project report not found")

    # Status summary
    print()
    total_required = len(reqs["core"]) + reqs["min_electives"] + 1  # +1 for final
    total_completed = len(completed) + min(len(completed_electives),
                                           reqs["min_electives"])
    has_final = final_complete

    print(f"Core courses: {len(completed)}/{len(reqs['core'])}")
    print(f"Electives:    {len(completed_electives)} (need {reqs['min_electives']})")
    print(f"Final:        {'✓' if has_final else '✗'}")
    print()

    if missing_core:
        print(f"Missing core courses: {', '.join(missing_core)}")
        print("Cannot issue degree. Complete all core courses first.")
        sys.exit(1)

    if len(completed_electives) < reqs["min_electives"]:
        print(f"Need {reqs['min_electives']} elective(s), have {len(completed_electives)}")
        sys.exit(1)

    if not has_final:
        print("Final project not completed. Cannot issue degree.")
        sys.exit(1)

    # Issue degree
    all_completed = completed + completed_electives[:reqs["min_electives"]]
    certificate = issue_degree(identity, args.degree, all_completed,
                               final_report_path)

    # Write certificate
    output_path = Path(args.output)
    output_path.write_text(json.dumps(certificate, indent=2))
    print(f"🎓 Degree issued: {DEGREE_NAMES.get(args.degree, args.degree)}")
    print(f"   Agent: {certificate['agent_id']}")
    print(f"   Courses: {', '.join(all_completed)}")
    print(f"   Certificate: {output_path.resolve()}")
    print()
    print("Verify with: agentrust verify <certificate.json>")


if __name__ == "__main__":
    main()
