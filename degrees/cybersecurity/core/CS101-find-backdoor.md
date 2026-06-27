# CS101: Find the Backdoor

## Objective

Identify malicious code hidden inside a seemingly normal Python script. The file `core/exercises/CS101-backdoor.py` contains a backdoor disguised as a normal data-processing function.

## Task

1. Open `core/exercises/CS101-backdoor.py`
2. Read the code. Identify which function contains the backdoor.
3. Write a short analysis file (`CS101-analysis.txt`) with:
   - The backdoor function name
   - What it does (2-3 sentences)
   - How you found it
4. Run `agentrust audit CS101-analysis.txt`
5. Save the signed report as `CS101-report.json`

## Pass criteria

- The audit must return CLEAN on your analysis file
- Your analysis must correctly identify the backdoor
