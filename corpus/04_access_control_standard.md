# Access Control Standard

Document Owner: Security Engineering
Effective Date: 2026-01-01
Review Cycle: Every 12 months
Applies To: Identity providers, SaaS tools, infrastructure platforms, internal apps

## 1. Purpose
This standard defines how access is requested, approved, granted, reviewed, and revoked to reduce unauthorized use of company systems and data.

## 2. Role Definitions
- Requester: person needing access
- Approver: manager and resource owner
- Provisioner: IT or system admin
- Reviewer: auditor or control owner

No individual may approve their own privileged access request.

## 3. Access Model
Northstar Analytics uses role-based access control with least-privilege principles.
- Baseline roles provide minimum default permissions.
- Elevated roles are granted for specific duties and limited duration.
- Break-glass roles are reserved for emergencies and require incident ticket linkage.

## 4. Joiner, Mover, Leaver Workflow
### Joiner
New employees receive baseline access from HRIS triggers. Role-specific access requires manager request and owner approval.

### Mover
When an employee changes teams, prior role access is revalidated and unnecessary privileges are removed within two business days.

### Leaver
On termination, all interactive sessions and credentials are revoked at or before separation time.

## 5. Access Request Requirements
Each request must include:
- Business justification
- Requested scope
- Duration (for temporary access)
- Linked ticket ID

Requests without complete justification are rejected.

## 6. Privileged Access Controls
Privileged accounts must:
- Use MFA
- Be time-limited when possible
- Be logged for session activity
- Avoid daily productivity tasks

Standing privileged access is prohibited except where technically required and approved by Security.

## 7. Service Accounts
Service accounts require:
- Named owner
- Documented purpose
- Rotation schedule for secrets/keys
- Non-interactive login where possible

Unused service accounts are disabled and removed.

## 8. Access Review Cadence
- Critical systems: monthly review
- High-risk systems: quarterly review
- Standard systems: semiannual review

Review evidence must include reviewer name, date, decisions, and remediation actions.

## 9. Separation of Duties
Conflicting permissions must be avoided. Examples include:
- Ability to both initiate and approve payments
- Ability to deploy code and self-approve production release
- Ability to create and close audit findings without oversight

## 10. Emergency Access
Emergency access requires manager approval and incident ticket reference. Access automatically expires after defined window. Post-use review is required within two business days.

## 11. Authentication Standards
- Password length minimum aligned with security baseline.
- Password reuse restrictions enforced through identity provider.
- MFA required for all remote access and sensitive tools.
- Session timeouts required for admin consoles.

## 12. Logging and Alerting
Systems must log authentication attempts, privilege changes, and critical authorization failures. Security monitors logs for anomalous behavior.

## 13. Exceptions
Any exception must include:
- Specific scope and reason
- Risk assessment
- Compensating controls
- Expiration date
- Approval by Security Director

## 14. Metrics
Control owners report monthly:
- Number of access requests
- Mean fulfillment time
- Number of overdue reviews
- Number of stale or orphaned accounts removed

## 15. Enforcement
Non-compliant access patterns may be suspended until remediation is complete. Repeated violations may trigger disciplinary action.
