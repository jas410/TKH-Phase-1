
---

# **Perimeter_Assessment.md**

## **Phase 1 — Perimeter Discovery**

A full subnet sweep was conducted using:

```
nmap -sn 172.88.0.0/24
```

The scan identified multiple live hosts, but only two responded with accessible web services relevant to the assessment. A targeted port scan was then performed:

```
nmap -p 80,6379 <hosts>
```

From this, two hosts were confirmed to be running web services on port 80:

- **172.88.0.28** — Apache/2.4.66 (Debian)  
- **172.88.0.44** — BusyBox httpd 1.13 (embedded device web server)

These two hosts were selected for further vulnerability auditing.

---

## **Phase 2 — Vulnerability Auditing**

Nikto was used to assess each web server for common misconfigurations and security weaknesses.

### **Host: 172.88.0.28 — Apache/2.4.66 (Debian)**  
**Finding:** Server leaks inode values via ETag headers  
**Impact:** ETag inode disclosure can assist attackers with resource fingerprinting and cache manipulation.  
**Recommendation:** Disable ETag generation or configure Apache to use only `FileETag MTime Size`.

---

### **Host: 172.88.0.44 — BusyBox httpd 1.13**  
**Finding:** Missing `X‑Frame‑Options` header  
**Impact:** The site is vulnerable to clickjacking attacks, allowing malicious framing of the interface.  
**Recommendation:** Add `X‑Frame‑Options: DENY` or `SAMEORIGIN` to HTTP responses.

---

## **Phase 3 — Risk Triage**

### **Host: 172.88.0.28 — Apache/2.4.66**  
**Risk Level:** **Medium**  
**Justification:**  
Inode leakage through ETag headers does not directly compromise the system but increases the accuracy of targeted attacks. It can support cache poisoning, session fixation, or resource fingerprinting.  
**Recommended Action:**  
Disable or restrict ETag generation to prevent inode exposure.

---

### **Host: 172.88.0.44 — BusyBox httpd 1.13**  
**Risk Level:** **Medium**  
**Justification:**  
The absence of clickjacking protection allows attackers to embed the interface within malicious pages, potentially tricking users into performing unintended actions. This is especially relevant for embedded or IoT devices with administrative interfaces.  
**Recommended Action:**  
Implement `X‑Frame‑Options` or `Content‑Security‑Policy: frame‑ancestors` to prevent framing attacks.

---

### **Overall Perimeter Risk Summary**  
The perimeter hosts exhibit **medium‑severity misconfigurations** that weaken the security posture but do not indicate immediate compromise. Both findings relate to web server hardening and can be remediated through configuration changes without requiring system downtime. No critical vulnerabilities (e.g., RCE, directory traversal, authentication bypass) were identified during this assessment.

---
