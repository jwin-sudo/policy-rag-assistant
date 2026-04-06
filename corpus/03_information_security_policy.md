# Information Security Policy

Document Owner: Security and IT
Effective Date: 2026-01-01
Review Cycle: Annual or after major incidents
Applies To: All workforce members, systems, and data handled by Northstar Analytics

## 1. Purpose
This policy defines baseline information security requirements to protect confidentiality, integrity, and availability of company and customer data.

## 2. Security Principles
- Least privilege access
- Defense in depth
- Secure by default configuration
- Continuous monitoring and rapid response
- Measured risk acceptance with documented approvals

## 3. Asset Inventory
IT maintains an inventory of hardware, software, cloud resources, and data stores. Owners must be assigned for each critical asset. Unmanaged assets are not permitted on production networks.

## 4. Identity and Authentication
- Unique user IDs are required.
- Shared accounts are prohibited except approved service accounts.
- Multi-factor authentication is required for all business-critical applications.
- Passwords must meet complexity and rotation standards or use approved passwordless methods.

## 5. Access Control
Access is granted based on business need and approved by asset owners. Privileged access must be time-bound and logged. Access reviews are performed at least quarterly.

## 6. Endpoint Security
Company-managed devices must include:
- Full disk encryption
- EDR or anti-malware protection
- Screen lock timeout
- OS and browser auto-updates
- Restricted local admin permissions

Lost or stolen devices must be reported within one hour of discovery.

## 7. Network Security
Production environments must use segmented networks, firewall controls, and monitored ingress points. Public exposure of services requires risk review and security approval.

## 8. Data Protection
Data must be encrypted in transit and at rest using approved algorithms and key management practices. Sensitive data may not be copied to unmanaged personal devices or unapproved storage locations.

## 9. Logging and Monitoring
Security-relevant logs must be retained per retention requirements and protected from tampering. Critical alerts are routed to on-call responders and triaged according to severity.

## 10. Vulnerability and Patch Management
- Critical vulnerabilities: patch or mitigate within 7 days.
- High vulnerabilities: patch within 30 days.
- Medium vulnerabilities: patch within 90 days.

Exceptions require documented risk acceptance and compensating controls.

## 11. Secure Development
Engineering teams must apply secure coding practices and perform:
- Pull request review
- Dependency vulnerability scanning
- Secret scanning
- Static analysis for critical services

Production deployments must be traceable to approved change records.

## 12. Third-Party Security
Vendors with access to sensitive data must pass security due diligence and contractual controls before onboarding. High-risk vendors require annual reassessment.

## 13. Incident Management
Suspected security events must be reported immediately through the incident channel. Investigation, containment, communication, and post-incident review follow the Incident Response Playbook.

## 14. Business Continuity
Critical systems require backup, recovery testing, and continuity planning. Recovery objectives are defined by system tier and business impact.

## 15. Security Awareness
All workforce members must complete annual security awareness training and role-specific training where required.

## 16. Compliance and Enforcement
Policy violations may result in corrective action up to and including termination, legal action, or contract termination. Compliance is assessed through audits, controls testing, and periodic security reviews.
