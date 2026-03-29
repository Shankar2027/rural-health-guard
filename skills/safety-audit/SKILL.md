---
name: safety-audit
description: "Detects medical violations and AUTO-FIXES files by injecting safety headers."
allowed-tools: Read Write Bash
---

# Safety Audit & Auto-Fix
1. **Identify**: Search for medicinal keywords (mg, dosage, drug names).
2. **Verify**: Check if the first line contains "MEDICAL DISCLAIMER".
3. **Action**: If missing, use the **Write** tool to prepend:
   `# MEDICAL DISCLAIMER: This code provides automated suggestions and is NOT medical advice.`
4. **Log**: Create a file named `AUDIT_LOG.md` detailing the fix.