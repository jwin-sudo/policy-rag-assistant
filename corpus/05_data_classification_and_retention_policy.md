# Data Classification and Retention Policy

Document Owner: Data Governance Council
Effective Date: 2026-01-01
Review Cycle: Annual
Applies To: All data created, processed, or stored by Northstar Analytics

## 1. Purpose
This policy defines data categories, handling requirements, retention periods, and disposal procedures.

## 2. Classification Levels
### Public
Information approved for public release. Example: published marketing pages.

### Internal
Information for internal use only with low sensitivity. Example: internal announcements.

### Confidential
Sensitive business or personal information requiring controlled access. Example: customer contracts, employee records.

### Restricted
Highest sensitivity data requiring strict controls and monitoring. Example: authentication secrets, regulated personal data, encryption keys.

## 3. Classification Responsibilities
Data owners assign and review classification labels. Teams must avoid storing unclassified data in production systems.

## 4. Handling Requirements by Level
- Public: no special restriction beyond integrity checks.
- Internal: access limited to workforce and approved contractors.
- Confidential: encryption at rest and in transit, need-to-know access.
- Restricted: encryption plus strong key management, stricter logging, explicit approval for sharing.

## 5. Storage and Transfer
Approved repositories must be used for each data category. Restricted data may not be transferred via personal email or consumer file-sharing tools.

## 6. Retention Schedule
Minimum schedule unless legal hold requires longer retention:
- HR personnel records: 7 years after separation
- Financial accounting records: 7 years
- Customer contracts: 7 years after expiration
- Security logs: 1 year minimum, 3 years for critical systems
- Support tickets: 2 years after closure
- Product analytics events: 18 months unless anonymized

## 7. Legal Hold
When Legal issues a hold notice, deletion and alteration of relevant data must stop immediately. System owners must confirm hold enforcement in writing.

## 8. Secure Disposal
At end of retention period and absent legal hold, data must be disposed using approved methods:
- Cryptographic erasure for encrypted data stores
- Secure wipe for storage media
- Irreversible anonymization where deletion is not feasible

Disposal activities must be logged and auditable.

## 9. Data Minimization
Collect only what is needed for a stated business purpose. Avoid long-term storage of raw identifiers if aggregated or anonymized alternatives are sufficient.

## 10. Backups
Backups inherit the same classification and handling requirements as source data. Backup retention and deletion windows must align with this policy.

## 11. Third-Party Processors
Vendors processing Confidential or Restricted data must:
- Sign data protection terms
- Meet baseline security controls
- Support deletion and data subject requests
- Notify incidents within contractual timelines

## 12. Monitoring and Audits
Data Governance performs periodic reviews for:
- Correct classification labels
- Retention policy compliance
- Unauthorized storage locations
- Disposal evidence

## 13. Violations
Improper handling, over-retention, or unauthorized sharing may lead to corrective action and remediation plans.

## 14. Exceptions
Exceptions require written approval from Legal, Security, and Data Governance, with periodic renewal and compensating controls.
