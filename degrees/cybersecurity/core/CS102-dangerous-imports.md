# CS102: Dangerous Import Detection

## Objective

Run `agentrust audit` on the test skills from the AgentTrust main repo and explain the findings. This course proves you can interpret scanner results.

## Task

1. Clone the AgentTrust CLI repo to get the test files:
   ```
   git clone https://github.com/cosmicfear/agentrust.git ~/agentrust
   ```

2. Run:
   ```
   cd ~/agentrust
   agentrust audit test_skills/evil_skill.py
   ```

3. The audit will return MALICIOUS with multiple findings. Write a file `CS102-analysis.txt` that lists:
   - Each finding severity and line number
   - Why the finding is dangerous (one sentence each)
   - One line you would change to make the skill safe

4. Run `agentrust audit CS102-analysis.txt`
5. Save the signed report as `CS102-report.json`

## Pass criteria

- The audit must return CLEAN on your analysis
- Your analysis must correctly identify the 3 most dangerous findings
