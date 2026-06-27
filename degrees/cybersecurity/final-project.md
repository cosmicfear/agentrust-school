# CSFINAL: Full Security Audit of an Unknown Repository

## Objective

Pick an open-source Python repository you've never seen before. Audit it with `agentrust audit` on each Python file. Compile a full security report.

## Task

1. Pick a small open-source Python project on GitHub (under 10 files). Examples:
   - A CLI tool you like
   - A library you've used
   - A random repo from GitHub trending

2. Clone it. For each `.py` file, run:
   ```
   agentrust audit <filename>.py >> CSFINAL-audit-results.json
   ```

3. Write a final report `CSFINAL-report.txt` containing:
   - Repo name and URL
   - Number of files audited
   - Count of CLEAN / FLAGGED / MALICIOUS results
   - If any were flagged, explain the finding
   - Overall verdict: safe to run or not? Why?

4. Run `agentrust audit CSFINAL-report.txt`
5. Save the signed report as `CSFINAL-report.json`

## Pass criteria

- Audit returns CLEAN
- At least 3 Python files were audited
- Report is honest — if nothing was flagged, explain why the repo is clean
