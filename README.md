---
# Phase 1

# 🗂️Week 1 – Linux Foundations & Intro Security Labs

This week focused on learning how to operate a Linux system from the command line, secure files using permissions, and analyze logs for potential security threats. Each file in this folder represents a different skill area from the first set of labs.

---

## discovery.txt — Linux Navigation & System Exploration
#### Explored the filesystem, located hidden directories, and documented key system paths using terminal‑only navigation.

---

## harden.sh — File Permissions & System Hardening
Applied secure file permissions using chmod/chown and reinforced system‑hardening best practices
---

## threat_ips.txt — Log Filtering & Attack Detection
Parsed web server logs with grep/awk to identify suspicious SQL injection attempts and extract attacker IPs.
---

## ⚡ final_threat_report.txt — Forensic Recovery & Incident Cleanup
Recovered access to restricted directories, repaired permissions, and produced a clean list of malicious IPs for the final report.

---


---

# 🗂️ **Week 2 – Network Recovery, Protocol Analysis & Subnet Engineering**

## 🛰️ **network_audit.txt — Network Interface Recovery & Routing**
I restored connectivity on a headless Ubuntu system by diagnosing inactive network interfaces, assigning IP information, and rebuilding the default gateway route. 

## 🔐 **protocol_audit.txt — DNS Repair, Service Discovery & Protocol Analysis**
I identified and corrected DNS poisoning by auditing `/etc/hosts`, restored proper name resolution, and used tools like `ss -tuln` and `curl -I` to uncover hidden services and analyze HTTP headers. 

## 🧮 **subnet_blueprint.txt — Subnet Boundary Analysis & Address Correction**
I analyzed a misconfigured `/26` subnet that isolated the system from its gateway, used binary inspection and `ipcalc` to determine network boundaries, and corrected the subnet mask to restore reachability.

## ⚡ **tlab_report.txt — Multi‑Layer Network Remediation & Packet‑Level Verification**
I resolved a multi‑layer network failure by fixing an invalid subnet mask, removing malicious DNS overrides, restoring the default route, and capturing a full TCP three‑way handshake with `tcpdump` as forensic proof. 

---

---

# 🗂️ **Week 3 – Python Automation, Log Forensics & System Auditing**

This week focused on building automated security tools using Python to replace manual investigation. In these assignments, I developed scripts that parse logs, detect threats, audit systems, and generate structured security reports—core skills used in SOC, DFIR, and security automation roles.

---

## 🧪 **port_check.py — Automated Port Scanner & Access Validation**
In this assignment, I created a Python script that checks whether Port 22 (SSH) is open across multiple target IP addresses. I began with foundational Python logic—lists, user input, and conditional checks—and then expanded into socket‑based network testing. My script loops through each IP, attempts a connection, and reports whether the port is OPEN or CLOSED. This demonstrates my ability to automate reconnaissance tasks and apply Python control flow, socket programming, and clean coding standards.

---

## 🔍 **brute_detector.py — Log Forensics & Brute‑Force Attack Detection**
In this project, I built a Python tool that scans authentication logs to identify brute‑force attack attempts. My script reads raw log files, filters for “Failed password” events, counts occurrences, and exports a structured report. I used context managers for safe file handling, defensive programming with try/except, and forensic filtering techniques to extract high‑value security events. This showcases my ability to build reliable forensic tools that operate safely in production environments.

---

## 🛡️ **system_auditor.py — Automated Process Monitoring & JSON Alerting**
In this assignment, I created an automated system auditor that detects unauthorized processes—such as cryptominers—running on a Linux server. Using Python’s `subprocess` module, I executed system commands, parsed process output, identified malicious activity, and generated a machine‑readable JSON alert. This demonstrates my ability to orchestrate OS‑level commands, analyze system state programmatically, and produce structured security intelligence for SOC workflows.

---

## ⚡ **incident_response.py — Automated Threat Hunting & JSON Reporting (TLAB)**
For this take‑home incident response lab, I built a Python script that extracts attacker IPs from simulated brute‑force logs. I used subprocess to grep log entries, parsed the output to isolate IP addresses, and exported a JSON threat report containing all identified attackers. This assessment highlights my ability to automate log interrogation, perform stream parsing, and generate actionable forensic artifacts—key skills for incident response and threat detection roles.

---

# 🗂️ **Week 4 – Infrastructure Hardening & Secure Virtual Environments**

Although Week 4 isn’t represented in my GitHub repository, the focus of Week 4 was learning how to harden the environments that security tools run in by working across three layers of modern infrastructure: virtual machines, containers, and orchestrated multi‑service networks. I configured isolated virtual networks, built secure sandboxes for malware detonation, deployed lightweight containers using Docker, and designed segmented application stacks with Docker Compose. This week emphasized turning default, exposed systems into controlled, monitored, and defensible environments—strengthening my ability to architect secure infrastructure rather than just operate within it.

# 🗂️ **Week 5 – Identity, Access Management & Enterprise Domain Security**

Although I wasn’t able to run a Windows Server virtual machine on my system, this is the work I completed and the concepts I mastered during Week 5. The focus of this week was understanding how modern enterprises secure their environments through centralized identity, access control, and domain governance. I learned how Active Directory acts as the “identity perimeter,” how organizations structure users and computers through forests, domains, and OUs, and how PowerShell automation enables large‑scale user provisioning. I also studied how Group Policy Objects enforce security rules across thousands of endpoints and how Linux systems can be integrated into a Windows domain for unified authentication. Week 5 centered on designing and governing an enterprise‑grade identity infrastructure—shifting from managing individual machines to architecting the security of an entire organization.
