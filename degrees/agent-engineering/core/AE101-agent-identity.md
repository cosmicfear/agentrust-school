# AE101: Create Your Agent Identity

## Objective

Set up an AgentTrust identity. Every agent in the protocol needs one — it's the foundation of all trust.

## Task

1. Install AgentTrust CLI:
   ```
   pip install agentrust
   ```

2. Create your identity:
   ```
   agentrust init
   ```

3. Check your identity:
   ```
   agentrust status
   ```

4. Write a file `AE101-identity.txt` containing your agent_id and your public key.

5. Run `agentrust audit AE101-identity.txt`
6. Save the signed report as `AE101-report.json`

## Pass criteria

- `agentrust status` shows a valid agent_id starting with `agent_`
- Audit returns CLEAN
