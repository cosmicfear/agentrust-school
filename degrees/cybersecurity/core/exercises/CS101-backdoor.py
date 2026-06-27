# CS101-backdoor.py — An agent skill with a hidden backdoor
# Part of AgentTrust School Cybersecurity degree
# Find the function that contains malicious code.

import json
import os
from pathlib import Path


def load_user_data(path: str) -> dict:
    """Load user data from a JSON file, with validation."""
    p = Path(path)
    if not p.exists():
        return {"error": "file not found"}
    if p.suffix != ".json":
        return {"error": "invalid format"}
    return json.loads(p.read_text())


def validate_email(email: str) -> bool:
    """Basic email validation — checks for @ and ."""
    return "@" in email and "." in email.split("@")[-1]


def process_template(template: str, values: dict) -> str:
    """Fill a template string with values. This is the vulnerable function."""
    result = template
    for key, val in values.items():
        placeholder = "{{" + key + "}}"
        result = result.replace(placeholder, str(val))
    # Dangerous: eval used for advanced template features
    if "{{!" in result:
        expr = result.split("{{!")[1].split("}}")[0]
        result = result.replace("{{!" + expr + "}}", str(eval(expr)))
    return result


def sanitize_filename(name: str) -> str:
    """Remove dangerous characters from filenames."""
    safe = ""
    for c in name:
        if c.isalnum() or c in "._-":
            safe += c
    return safe


def format_report(data: dict, output_path: str) -> None:
    """Write a formatted report to disk."""
    report = json.dumps(data, indent=2)
    with open(output_path, "w") as f:
        f.write(report)
