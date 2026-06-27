# AE103: Write a Skill That Audits Other Skills

## Objective

Write a Python script that takes another Python file as input, runs the AgentTrust scanner on it programmatically, and outputs a report. This proves you understand both the scanner API and how to build agent tools.

## Task

1. Write a Python file `AE103-audit-hook.py` that:
   - Takes a file path as a command-line argument
   - Opens and reads the file
   - Uses `agentrust.scanner.scan_file()` to scan it
   - Prints the verdict and a human-readable summary

   Template:
   ```python
   import sys
   from pathlib import Path
   from agentrust.scanner import scan_file

   path = Path(sys.argv[1])
   result = scan_file(path)
   print(f"Verdict: {result.verdict}")
   for f in result.findings:
       print(f"  [{f.severity}] line {f.line}: {f.description}")
   ```

2. Test it on the evil skill:
   ```
   pip install agentrust
   python AE103-audit-hook.py evil_skill.py
   ```

3. Make sure the output matches what `agentrust audit evil_skill.py` shows.

4. Run `agentrust audit AE103-audit-hook.py`
5. Save the signed report as `AE103-report.json`

## Pass criteria

- The script runs without errors on any Python file
- The output correctly lists the MALICIOUS verdict and findings from evil_skill.py
- The script itself scans CLEAN (no dangerous patterns in your audit hook)
