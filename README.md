---

# 🗂️We Wkek 1 – Linux Foundations & Intro Security Labs

This week focused on learning how to operate a Linux system from the command line, secure files using permissions, and analyze logs for potential security threats. Each file in this folder represents a different skill area from the first set of labs.

---

## discovery.txt — Linux Navigation & System Exploration
This assignment introduced working in a headless Linux environment using only terminal commands. The goal was to explore the filesystem, locate hidden directories, inspect system logs, and document the exact paths to important files. It demonstrates early skills in Linux navigation, understanding the Filesystem Hierarchy Standard, and gathering system information without a graphical interface.

---

## harden.sh — File Permissions & System Hardening
This script applies secure Linux file permissions using the user/group/other model. The assignment focused on understanding read, write, and execute permissions, how octal values like 755 or 644 work, and why overly open permissions are unsafe. It shows foundational skills in system hardening, using `chmod` and `chown`, and applying best practices for securing files and directories.

---

## threat_ips.txt — Log Filtering & Attack Detection
This assignment involved analyzing a web server access log to identify potential SQL injection attempts. Using tools like `grep`, `awk`, `sort`, and `uniq`, the task was to filter for suspicious “UNION SELECT” entries and extract a clean list of attacker IP addresses. It demonstrates beginner‑level log analysis, pattern matching, and Linux text‑processing skills used in real security investigations.

---

## final_threat_report.txt — Forensic Recovery & Incident Cleanup
This assignment simulated a compromised server where an attacker hid evidence and broke file permissions. The task was to restore access to a locked directory, repair permissions, and extract critical log entries. Using `grep`, `sed`, and `awk`, the final output is a clean list of unique malicious IP addresses. This file represents the completed forensic report and shows skills in navigation, permission repair, and stream editing for incident response.

---

