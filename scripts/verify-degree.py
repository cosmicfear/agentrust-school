#!/usr/bin/env python3
"""
Verify an AgentTrust School degree certificate.

Usage:
    python scripts/verify-degree.py certificate.json

This checks that the certificate was signed by the school's Ed25519 key.
"""

import argparse
import json
import sys
from pathlib import Path

# Path to the school repo
SCHOOL_DIR = Path(__file__).resolve().parent.parent


def main():
    parser = argparse.ArgumentParser(
        description="Verify an AgentTrust School degree certificate"
    )
    parser.add_argument("certificate", help="Path to the certificate JSON file")
    args = parser.parse_args()

    # Load certificate
    cert_path = Path(args.certificate)
    if not cert_path.exists():
        print(f"Error: certificate not found at {cert_path}")
        sys.exit(1)

    cert = json.loads(cert_path.read_text())

    if "signature" not in cert:
        print("✗ No signature found in certificate. This certificate is not valid.")
        sys.exit(1)

    signature = cert.pop("signature")

    # Load school public key
    pub_path = SCHOOL_DIR / "school.pub.json"
    if not pub_path.exists():
        print(f"Error: school public key not found at {pub_path}")
        print("Make sure you're running this from the agentrust-school repo.")
        sys.exit(1)

    pub = json.loads(pub_path.read_text())
    pub_key_pem = pub["public_key_pem"]

    # Rebuild canonical bytes
    cert_bytes = json.dumps(cert, sort_keys=True).encode()

    # Verify
    try:
        from agentrust.crypto import AgentIdentity
        valid = AgentIdentity.verify_any(cert_bytes, signature, pub_key_pem)
    except ImportError:
        # Fallback: suggest installing agentrust
        print("AgentTrust CLI not installed. Install with: pip install agentrust")
        print("Using built-in verification...")

        # Basic self-verification using cryptography
        import base64
        from cryptography.exceptions import InvalidSignature
        from cryptography.hazmat.primitives import serialization
        from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey

        try:
            public_key = serialization.load_pem_public_key(pub_key_pem.encode())
            assert isinstance(public_key, Ed25519PublicKey)
            public_key.verify(base64.b64decode(signature), cert_bytes)
            valid = True
        except (InvalidSignature, Exception):
            valid = False

    if valid:
        print("✓ CERTIFICATE VALID")
    else:
        print("✗ CERTIFICATE INVALID — signature does not match")
        sys.exit(1)

    print(f"   Student:     {cert.get('agent_id', '?')}")
    print(f"   Degree:      {cert.get('degree', '?')}")
    print(f"   Courses:     {', '.join(cert.get('courses', []))}")
    print(f"   Issued by:   {cert.get('issued_by', '?')}")
    print(f"   Completed:   {cert.get('completed_at', '?')}")
    print()
    print("This certificate proves the agent completed the course requirements")
    print("and the school's Ed25519 signature confirms it was issued legitimately.")


if __name__ == "__main__":
    main()
