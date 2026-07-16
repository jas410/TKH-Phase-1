# Week 8 — Privilege Escalation, Persistence & Network Pivoting (Conceptual Workflow)

## Objective
Understand the full attack chain of a multi‑phase intrusion scenario involving bastion host access, privilege escalation, persistence, and internal network pivoting—completed conceptually due to environment limitations.

## What I Worked On
- Reviewed the intended workflow for accessing a bastion host and enumerating allowed sudo binaries  
- Studied privilege escalation techniques using `sudo -l` findings and GTFOBins mappings  
- Analyzed persistence mechanisms through scheduled tasks and cron‑based callbacks  
- Examined how pivoting works through routing changes, SOCKS proxies, and proxied Nmap scans  
- Documented each phase conceptually due to WSL2 limitations preventing full VM‑based execution  

## Artifacts
- 🗂️ **OPERATION_DEEP_PIVOT.md** — Full conceptual report covering escalation, persistence, pivoting, and final intelligence summary  

## Phase Summaries
- **Phase 1 — Beachhead & Escalation (Attempted)**  
  - Goal: SSH access → sudo enumeration → GTFOBins escalation  
  - Outcome: Escalation not possible without a full Ubuntu VM  

- **Phase 2 — Persistence (Attempted)**  
  - Goal: Modify root cron table → create recurring access mechanism  
  - Outcome: Cron subsystem unavailable in WSL2  

- **Phase 3 — Pivoting (Attempted)**  
  - Goal: Add route → start SOCKS proxy → scan internal subnet  
  - Outcome: Pivoting requires multi‑network virtualization not supported in WSL2  

- **Phase 4 — Intelligence Summary (Completed Conceptually)**  
  - Documented the full attack chain: initial access → escalation → persistence → pivot → internal discovery  

## Outcome
Although the technical steps could not be executed in WSL2, the full attack workflow was analyzed and documented. The report demonstrates understanding of privilege escalation paths, persistence mechanisms, and multi‑tier network pivoting—skills foundational to red‑team operations and advanced penetration testing.
