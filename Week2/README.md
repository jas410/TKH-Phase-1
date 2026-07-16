# 🗂️ **Week 2 – Network Recovery, Protocol Analysis & Subnet Engineering**

## 🛰️ **network_audit.txt — Network Interface Recovery & Routing**
I restored connectivity on a headless Ubuntu system by diagnosing inactive network interfaces, assigning IP information, and rebuilding the default gateway route. 

## 🔐 **protocol_audit.txt — DNS Repair, Service Discovery & Protocol Analysis**
I identified and corrected DNS poisoning by auditing `/etc/hosts`, restored proper name resolution, and used tools like `ss -tuln` and `curl -I` to uncover hidden services and analyze HTTP headers. 

## 🧮 **subnet_blueprint.txt — Subnet Boundary Analysis & Address Correction**
I analyzed a misconfigured `/26` subnet that isolated the system from its gateway, used binary inspection and `ipcalc` to determine network boundaries, and corrected the subnet mask to restore reachability.

## ⚡ **tlab_report.txt — Multi‑Layer Network Remediation & Packet‑Level Verification**
I resolved a multi‑layer network failure by fixing an invalid subnet mask, removing malicious DNS overrides, restoring the default route, and capturing a full TCP three‑way handshake with `tcpdump` as forensic proof. 

