# Change Management Procedure

Document Owner: Engineering Operations
Effective Date: 2026-01-01
Review Cycle: Annual
Applies To: Production systems, infrastructure, and customer-facing services

## 1. Purpose
This procedure ensures changes are planned, reviewed, tested, and deployed with controlled risk.

## 2. Change Categories
- Standard change: pre-approved low-risk recurring change
- Normal change: requires review and approval
- Emergency change: urgent fix for active incident or critical risk

## 3. Required Change Record Fields
Each change record must include:
- Description and rationale
- Systems affected
- Risk assessment
- Test evidence
- Rollback plan
- Implementation window
- Owner and approvers

## 4. Review and Approval
Normal changes require approval from technical owner and service owner. Security review is required for authentication, authorization, or data protection impacts.

## 5. Testing Expectations
Changes must be tested in non-production where feasible. Tests should cover:
- Functional behavior
- Error handling
- Security considerations
- Performance impacts

## 6. Deployment Controls
- Use approved CI/CD pipelines
- Tag and version releases
- Restrict direct production changes
- Log deployment actor, time, and artifact

## 7. Rollback and Contingency
All changes require rollback or compensating plan. Teams must verify ability to restore service prior to implementation for high-risk changes.

## 8. Change Freeze Windows
Change freeze periods may be announced for critical business windows. Emergency changes remain allowed with Incident Commander approval.

## 9. Emergency Changes
Emergency changes require immediate implementation notes and retrospective approval within one business day.

## 10. Post-Implementation Review
For high-risk or failed changes, complete review within three business days covering root cause and prevention actions.

## 11. Segregation of Duties
Where practical, the change requester should not be the sole approver and deployer for production changes.

## 12. Documentation Retention
Change records and evidence are retained for audit and incident analysis per retention policy.

## 13. Metrics
Track and review:
- Change success rate
- Rollback rate
- Emergency change rate
- Mean time to recover after failed change

## 14. Exceptions
Exceptions require approval by Engineering Director and Security lead with explicit risk treatment.
