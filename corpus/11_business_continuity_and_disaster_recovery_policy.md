# Business Continuity and Disaster Recovery Policy

Document Owner: Reliability Engineering
Effective Date: 2026-01-01
Review Cycle: Annual
Applies To: Critical business functions and technology services

## 1. Purpose
This policy establishes continuity and recovery expectations for disruptions affecting critical operations.

## 2. Definitions
- Business Continuity (BC): sustaining critical business activities during disruptions
- Disaster Recovery (DR): restoring technology services after major failure
- RTO: target time to restore service
- RPO: maximum acceptable data loss window

## 3. Service Tiering
Systems are classified by business impact.
- Tier 0: mission-critical services
- Tier 1: high-impact core services
- Tier 2: moderate-impact services
- Tier 3: low-impact services

Each tier has defined RTO and RPO targets.

## 4. Continuity Requirements
Business units must document:
- Critical processes
- Dependencies and fallback workflows
- Communication chains
- Minimum staffing requirements

## 5. Backup Requirements
Critical data must be backed up regularly with encrypted storage and periodic restore testing.

## 6. DR Environment Strategy
Critical services require redundant architecture where feasible and documented failover plans.

## 7. Testing and Exercises
BC and DR plans must be tested at least annually. Tier 0 systems require at least one failover simulation per year.

## 8. Incident Coordination
During major disruptions, BC and DR teams coordinate with Incident Response and Executive leadership for prioritization and communication.

## 9. Third-Party Dependencies
Critical vendors must have continuity capabilities aligned with company resilience expectations.

## 10. Documentation and Ownership
Each critical system must maintain:
- System owner
- Runbook
- Recovery procedure
- Contact roster
- Dependency map

## 11. Post-Event Review
After significant disruptions, teams perform review to capture timeline, impact, lessons learned, and resilience improvements.

## 12. Compliance
Compliance with this policy is monitored through control testing, recovery drills, and audit sampling.

## 13. Exceptions
Any exception to RTO/RPO or testing cadence requires formal risk acceptance by executive owner.
