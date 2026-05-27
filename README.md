---
# Phase 1

# 🗂️Week 1 – Linux Foundations & Intro Security Labs

This week focused on learning how to operate a Linux system from the command line, secure files using permissions, and analyze logs for potential security threats. Each file in this folder represents a different skill area from the first set of labs.

---

## 🔗 **discovery.txt — Linux Navigation & System Exploration**
#### I explored the filesystem, located hidden directories, and documented key system paths using terminal‑only navigation.

---

## 🛜 **harden.sh — File Permissions & System Hardening**
#### I applied secure file permissions using chmod/chown and reinforced system‑hardening best practices
---

## 🔎 **threat_ips.txt — Log Filtering & Attack Detection**
#### I parsed web server logs with grep/awk to identify suspicious SQL injection attempts and extract attacker IPs.
---

## ⚡ **final_threat_report.txt — Forensic Recovery & Incident Cleanup**
#### I recovered access to restricted directories, repaired permissions, and produced a clean list of malicious IPs for the final report.

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
I wrote a Python script that checks whether Port 22 is open across multiple IPs. I used lists, loops, and socket connections to test each host and report if the port was open or closed.

---

## 🔍 **brute_detector.py — Log Forensics & Brute‑Force Attack Detection**
II built a script that scans authentication logs for brute‑force attempts. I filtered for “Failed password” events, counted occurrences, and exported a clean report using safe file handling and defensive programming.

---

## 🛡️ **system_auditor.py — Automated Process Monitoring & JSON Alerting**
I created a system auditor that detects unauthorized processes on a Linux server. I used subprocess to run system commands, parsed the output, and generated a JSON alert when suspicious activity appeared.

---

## ⚡ **incident_response.py — Automated Threat Hunting & JSON Reporting (TLAB)**
#### For this lab, I automated the extraction of attacker IPs from simulated brute‑force logs. I used subprocess and stream parsing to isolate malicious IPs and export a structured JSON threat report.
---

# 🗂️ **Week 4 – Infrastructure Hardening & Secure Virtual Environments**

Although Week 4 isn’t represented in my GitHub repository, the focus of Week 4 was learning how to harden the environments that security tools run in by working across three layers of modern infrastructure: virtual machines, containers, and orchestrated multi‑service networks. I configured isolated virtual networks, built secure sandboxes for malware detonation, deployed lightweight containers using Docker, and designed segmented application stacks with Docker Compose. This week emphasized turning default, exposed systems into controlled, monitored, and defensible environments—strengthening my ability to architect secure infrastructure rather than just operate within it.

# 🗂️ **Week 5 – Identity, Access Management & Enterprise Domain Security**

Although I wasn’t able to run a Windows Server virtual machine on my system, this is the work I completed and the concepts I mastered during Week 5. The focus of this week was understanding how modern enterprises secure their environments through centralized identity, access control, and domain governance. I learned how Active Directory acts as the “identity perimeter,” how organizations structure users and computers through forests, domains, and OUs, and how PowerShell automation enables large‑scale user provisioning. I also studied how Group Policy Objects enforce security rules across thousands of endpoints and how Linux systems can be integrated into a Windows domain for unified authentication. Week 5 centered on designing and governing an enterprise‑grade identity infrastructure—shifting from managing individual machines to architecting the security of an entire organization.

# 📁 **Week 6 – OSI Troubleshooting, Diagnostics & Infrastructure Hardening**

Although I wasn’t able to fully complete the Week 6 labs due to not having access to a persistent, full‑featured Ubuntu VM, this week centered on learning how to diagnose and repair failures across multiple OSI layers while working inside a simulated production environment. The assignments walked through real‑world troubleshooting scenarios such as fixing broken file permissions, resolving Docker port conflicts, identifying firewall rules blocking outbound traffic, and performing root‑level log forensics. I also studied how to deploy hardened infrastructure through SSH lockdowns, UFW firewall policies, Python‑based system auditors, and multi‑container Docker Compose stacks.

Because I was working inside an Ubuntu playground environment rather than a true VM, I couldn’t execute the full practical components. The playground lacked support for systemd services, Docker Engine networking, UFW firewall rules, SSH daemon configuration, and root‑owned filesystem operations — all of which were required to complete the missions. However, I worked through each scenario conceptually, documented the correct commands, and gained a strong understanding of how to approach OSI‑layer troubleshooting, container diagnostics, and infrastructure hardening in a real environment.

# 📁 **Week 7 – Enterprise Monitoring, SIEM Operations & Threat Correlation**

Although I wasn’t able to complete the Week 7 assignments, this week focused on learning how enterprise security teams use SIEM platforms to detect, investigate, and correlate threats across large environments. The labs introduced how to build index patterns, analyze log sources, pivot across events, and trace attacker activity through alerts, network telemetry, and host‑level artifacts. I also studied how SIEM tools support real‑time detection engineering, threat hunting workflows, and incident response escalation.

I wasn’t able to complete the practical components because the SIEM environment required a persistent Ubuntu VM capable of running Docker Engine, systemd services, and the full ELK stack. At the time, I was working inside a temporary playground environment that could not host long‑running containers or maintain the SIEM state needed for log ingestion and correlation. Without a real VM, Kibana could not boot, the enterprise logs could not be indexed, and the alerting pipeline could not be accessed. However, I reviewed the full workflow conceptually and documented the correct steps for SIEM setup, alert investigation, and threat correlation.

# 📁 **Week 8 – Exploitation Fundamentals, Reverse Shells & Metasploit Verification**

Although I wasn’t able to complete the Week 8 “Verification Protocol (Samba Conquest)” assignment, this week focused on understanding how attackers establish remote access and how security professionals verify and test vulnerabilities in controlled environments. The lab introduced the mechanics of reverse shells using Netcat, the fundamentals of exploit development, and the use of the Metasploit Framework to validate real-world vulnerabilities such as the Samba usermap_script exploit (CVE‑2007‑2447). I studied how reverse shells work at the network level, how Metasploit modules are configured, and how exploitation frameworks automate privilege escalation and remote command execution.

I wasn’t able to complete the practical components because the provisioning script required a persistent Ubuntu VM capable of running Docker Engine, systemd services, and the full Metasploit environment. At the time, I was working inside a temporary playground environment that could not host long‑running containers, vulnerable Samba targets, or the Metasploit Framework. Without a real VM, the Samba target container could not be deployed, the exploit module could not be executed, and the reverse shell session could not be established. However, I reviewed the full workflow conceptually and documented the correct steps for reverse shell creation, Metasploit configuration, and exploit execution.



# 📁 **Week 10 – Full‑Scope Incident Response & Disk Forensics**

Although I wasn’t able to fully complete the Week 10 “Operation Phantom Pursuit” investigation, this week focused on learning how to perform a complete end‑to‑end incident response workflow inside an enterprise‑grade environment. The assignment combined SIEM log correlation, live triage on a quarantined host, chain‑of‑custody hashing, and deep disk forensics using The Sleuth Kit. I studied how to trace an attacker’s entry point through Kibana, identify active command‑and‑control processes on a compromised machine, generate cryptographic evidence hashes, and recover deleted malware from a raw disk image by extracting files directly from their inode records.

I wasn’t able to complete the practical components because the provisioning script requires a persistent Ubuntu VM capable of running Docker Engine, systemd services, ELK stack containers, and full disk‑image tooling. At the time, I was working inside a temporary playground environment that didn’t support long‑running containers, SIEM services, or forensic tools like `fls` and `icat`. Without a real VM, the SIEM couldn’t boot, the quarantined host container couldn’t be accessed, and the disk image tools couldn’t be executed. However, I worked through the investigation steps conceptually and documented the correct commands and methodology for each phase of the breach lifecycle.
