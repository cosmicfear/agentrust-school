# AE102: Audit a Skill and Interpret Results

## Objective

Run `agentrust audit` on a provided skill and prove you can read and understand the findings.

## Task

1. Download the sample skill:
   ```
   curl -O https://raw.githubusercontent.com/cosmicfear/agentrust/main/test_skills/evil_skill.py
   ```

2. Run the audit:
   ```
   agentrust audit evil_skill.py
   ```

3. Write a file `AE102-analysis.txt` with:
   - The verdict (CLEAN/FLAGGED/MALICIOUS)
   - The total number of findings
   - The most critical finding and its line number
   - In one sentence: why this skill would harm an agent that runs it

4. Run `agentrust audit AE102-analysis.txt`
5. Save the signed report as `AE102-report.json`

## Pass criteria

- Analysis correctly states MALICIOUS as the verdict
- Audit returns CLEAN on the analysis
