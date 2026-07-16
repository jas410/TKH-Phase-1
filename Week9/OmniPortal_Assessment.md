## OMNI-PORTAL ASSESSMENT REPORT
**Operator:** Jasmine Adams
**Deadline:** April 5 @ 11:59 PM


## PHASE 1: AUTH BYPASS (SQLi)
**Payload Used:**  
' OR 1=1 --

**Result:**  
Successfully bypassed the login without a password.  
The “View My Orders” link appeared and the system issued a new `auth_token` cookie.


## PHASE 2: CLIENT-SIDE HIJACK (XSS)
**Stored XSS Payload:**  
<script>alert(document.cookie)</script>

**Secret Cookie Captured:**  
auth_token=SUPPORT-SESSION-44A91XZ

**Explanation:**  
Because this is stored XSS, the payload executes every time the Support Board loads, exposing the session cookie of any user who views the page.


## PHASE 3: API ENUMERATION (BOLA)
**Insecure Order ID:**  
503

**Confidential Data Leaked:**  
Order Type: Confidential Server Lease  
Amount: $125,000  
Details: Internal infrastructure lease agreement not intended for my account.

**Explanation:**  
The API does not verify whether the requesting user owns the order ID.  
Changing the ID in the URL exposes other users’ confidential financial data.


## PHASE 4: THE REMEDIATION
**Fix for SQLi:**  
Use prepared statements / parameterized queries so user input cannot modify SQL structure.

**Fix for XSS:**  
Sanitize and encode all user-supplied input before rendering. Never store or display raw HTML/JS.

**Fix for API BOLA:**  
Implement object-level authorization checks.  
The server must confirm that the authenticated user is authorized to access the requested order ID.
