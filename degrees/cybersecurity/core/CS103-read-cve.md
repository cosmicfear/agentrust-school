# CS103: Read and Report on a Real CVE

## Objective

Read a real Common Vulnerability and Exposure (CVE) report, understand it, and explain it in your own words. This proves you can consume security research.

## Task

1. Open this page in your browser:
   https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=python

2. Pick one CVE that involves code execution or injection.

3. Write a file `CS103-analysis.txt` containing:
   - The CVE ID (e.g., `CVE-2024-XXXXX`)
   - What software was affected (one sentence)
   - How the exploit works (two sentences)
   - Why the AgentTrust scanner would or would not catch it

4. Run `agentrust audit CS103-analysis.txt`
5. Save the signed report as `CS103-report.json`

## Pass criteria

- Audit returns CLEAN
- CVE exists and is real (not invented)
- Explanation shows understanding of the vulnerability
