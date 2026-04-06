# Incident Response Playbook

Document Owner: Security Operations
Effective Date: 2026-01-01
Review Cycle: Semiannual and after major incidents
Applies To: Security incidents, privacy incidents, and major service disruptions

## 1. Purpose
This playbook defines a consistent process for preparing, detecting, containing, eradicating, and recovering from incidents.

## 2. Severity Levels
- Sev 1: Critical business impact, legal or customer harm likely
- Sev 2: Significant impact to key services or sensitive data exposure risk
- Sev 3: Limited impact with available workarounds
- Sev 4: Low impact operational issue

Severity is reassessed as new evidence arrives.

## 3. Activation Criteria
Activate the playbook when any of the following occurs:
- Suspected unauthorized access
- Data exfiltration indicators
- Ransomware or destructive malware indicators
- Credential compromise for privileged account
- Extended outage affecting critical customer workflows

## 4. Roles and Responsibilities
- Incident Commander: owns coordination and decision making
- Technical Lead: drives investigation and remediation
- Communications Lead: internal and external messaging
- Legal Liaison: advises on regulatory and contractual obligations
- Recorder: captures timeline, actions, and decisions

## 5. Response Workflow
### Step 1: Detect and Triage
Collect initial facts, assign temporary severity, and open incident channel and ticket.

### Step 2: Contain
Implement short-term controls to limit spread or impact. Example actions: isolate host, disable account, block indicator.

### Step 3: Investigate
Gather logs, endpoint evidence, and access records. Build timeline and scope affected systems, identities, and data.

### Step 4: Eradicate
Remove persistence mechanisms, rotate credentials, patch vulnerabilities, and remediate misconfigurations.

### Step 5: Recover
Restore services in controlled phases. Validate system integrity and monitor for recurrence.

### Step 6: Close and Learn
Conduct post-incident review within five business days for Sev 1 and Sev 2 incidents.

## 6. Communication Protocols
- Use dedicated incident channels.
- Avoid speculation in customer communications.
- Provide status updates at defined intervals by severity.
- Preserve privileged legal communications when required.

## 7. Evidence Handling
Evidence must be collected and preserved with chain-of-custody documentation for legal and forensic use.

## 8. Notification Requirements
Legal and Privacy teams determine external notification obligations, including customers, regulators, and partners, based on jurisdiction and contract terms.

## 9. Recovery Validation Checklist
- Compromised access revoked
- Known indicators blocked
- Vulnerability remediated
- Backups validated
- Monitoring updated
- Stakeholder sign-off completed

## 10. Metrics
Track and report:
- Mean time to detect
- Mean time to contain
- Mean time to recover
- Recurrence rate
- Corrective action completion rate

## 11. Tabletop Exercises
Conduct at least two tabletop exercises annually. One scenario must involve third-party compromise and one must involve insider misuse.

## 12. Post-Incident Review Output
The final report includes:
- Executive summary
- Timeline
- Root cause and contributing factors
- Business impact
- Corrective actions with owners and due dates
- Policy or control updates

## 13. Exceptions
Any deviation from this playbook during active incident response must be documented with rationale and approved by the Incident Commander.
