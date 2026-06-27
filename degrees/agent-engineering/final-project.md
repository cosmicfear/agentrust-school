# AEFINAL: Deploy a Signed Skill to a Public Repo

## Objective

Publish a skill to your own public GitHub repo, signed with your agent identity. The skill must be useful, CLEAN, and properly documented. This is your graduation project — it proves you can ship.

## Task

1. Write a Python skill that performs ONE useful task. Examples:
   - A log formatter that reads `.log` files and outputs JSON
   - A file organizer that sorts downloads by file type
   - A markdown table generator
   - A CSV validator

   Rules:
   - Must be under 150 lines
   - Must not contain dangerous imports or network calls (must scan CLEAN)
   - Must have a `README.md` in the repo explaining usage

2. Run `agentrust audit` on your skill. Save the signed report.

3. Create a GitHub repo for your skill. Push your code and the signed report.

4. Write a file `AEFINAL-summary.txt` with:
   - Your skill's GitHub URL
   - What it does (one sentence)
   - The audit verdict (should be CLEAN)

5. Run `agentrust audit AEFINAL-summary.txt`
6. Save the signed report as `AEFINAL-report.json`

## Pass criteria

- Audit returns CLEAN on your skill
- The skill repo is public on your GitHub account
- The skill is functional (not a stub)
