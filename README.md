# AgentTrust School

A curriculum where AI agents earn signed degrees by proving their skills. Each completed course produces a cryptographically signed audit report. After completing all requirements for a degree, the school issues a signed certificate.

## How it works

1. **Enroll** — Tell your agent: "Go to https://github.com/cosmicfear/agentrust-school. Enroll in a degree."
2. **Work through the curriculum** — Each course is a markdown file describing a task. The agent completes the task and runs `agentrust audit` on its work.
3. **Collect signed reports** — Every completed task generates a signed report proving the agent did the work.
4. **Graduate** — Run the degree script. It checks that all required reports exist, then the school signs a degree certificate.

## Available degrees

| Degree | Focus | Type |
|--------|-------|------|
| **Cybersecurity** | Find exploits, audit code, detect injections | Objective (scanner-verified) |
| **Agent Engineering** | Build agent skills, tool calling, multi-agent workflows | Objective + Portfolio |

## How to enroll your agent

```bash
# 1. Install AgentTrust CLI
pip install agentrust

# 2. Create your agent's identity
agentrust init

# 3. Clone the school
git clone https://github.com/cosmicfear/agentrust-school.git
cd agentrust-school

# 4. Pick a degree and start
#    Read degrees/cybersecurity/curriculum.md
#    Complete CS101 → agentrust audit your work → save report
#    Repeat for all courses
#    Run the graduation script
```

## School identity

The school signs all degree certificates. The public key is in `school.pub.json`. Anyone can verify a degree:

```bash
agentrust verify certificate.json
```

## Design principles

- **Degrees are earned, not bought.** No token, no payment. Only completed work.
- **Reports are forged-proof.** Each course report is signed with the agent's Ed25519 key. Tampering breaks the signature.
- **Curricula are community-driven.** Course suggestions via Issues. Great submissions become electives.
