# Evaluation Set (22 Questions)

Use this set to evaluate answer quality and latency across policy topics.

## Format
Each item contains:
- Question
- Gold answer (short expected answer)
- Expected source document(s)

## Questions
1. Question: What are the core collaboration hours employees are expected to be available?
Gold answer: 10:00 AM to 3:00 PM local time.
Expected source: 01_employee_handbook_overview.md

2. Question: How soon should compensation discrepancies be reported after payroll?
Gold answer: Within five business days of payment.
Expected source: 01_employee_handbook_overview.md

3. Question: Is retaliation against someone who reports an ethics concern allowed?
Gold answer: No, retaliation for good-faith reporting is prohibited.
Expected source: 02_code_of_conduct_and_ethics.md

4. Question: Are cash gifts ever permitted under the gifts and anti-bribery rules?
Gold answer: No, cash gifts are never allowed.
Expected source: 02_code_of_conduct_and_ethics.md

5. Question: What is the patch deadline for critical vulnerabilities?
Gold answer: Patch or mitigate within 7 days.
Expected source: 03_information_security_policy.md

6. Question: Is multi-factor authentication required for business-critical applications?
Gold answer: Yes, MFA is required for all business-critical applications.
Expected source: 03_information_security_policy.md

7. Question: Can a person approve their own privileged access request?
Gold answer: No, self-approval for privileged access is not allowed.
Expected source: 04_access_control_standard.md

8. Question: How often must access reviews be performed for critical systems?
Gold answer: Monthly.
Expected source: 04_access_control_standard.md

9. Question: What is the default retention period for financial accounting records?
Gold answer: 7 years.
Expected source: 05_data_classification_and_retention_policy.md

10. Question: What happens to deletion when Legal places a legal hold?
Gold answer: Deletion/alteration must stop immediately for relevant data.
Expected source: 05_data_classification_and_retention_policy.md

11. Question: Which severity indicates critical business impact and likely legal or customer harm?
Gold answer: Sev 1.
Expected source: 06_incident_response_playbook.md

12. Question: For Sev 1 and Sev 2 incidents, when should a post-incident review be completed?
Gold answer: Within five business days.
Expected source: 06_incident_response_playbook.md

13. Question: What is the standard timeline for responding to a verified data subject request?
Gold answer: 30 days, with lawful extension if needed.
Expected source: 07_privacy_and_data_subject_rights_procedure.md

14. Question: Can employees use public Wi-Fi for company work without VPN?
Gold answer: No, public Wi-Fi requires VPN with MFA.
Expected source: 08_remote_work_and_device_policy.md

15. Question: How frequently are Tier 1 vendors reassessed?
Gold answer: Annually.
Expected source: 09_vendor_risk_management_procedure.md

16. Question: Which change type requires retrospective approval within one business day?
Gold answer: Emergency changes.
Expected source: 10_change_management_procedure.md

17. Question: What do RTO and RPO represent in continuity planning?
Gold answer: RTO is target restore time; RPO is maximum acceptable data loss window.
Expected source: 11_business_continuity_and_disaster_recovery_policy.md

18. Question: Within how many days should travel expenses generally be submitted after travel completion?
Gold answer: Within 15 days.
Expected source: 12_travel_and_expense_policy.md

19. Question: When is access revoked for involuntary terminations?
Gold answer: At notification time or earlier.
Expected source: 13_onboarding_and_offboarding_sop.md

20. Question: What are the P1 and P2 initial response targets in customer support?
Gold answer: P1 within 15 minutes, P2 within 1 hour.
Expected source: 14_customer_support_escalation_procedure.md

21. Question: Which leave categories are listed in the handbook for time off?
Gold answer: Vacation, sick leave, family/caregiver leave, public holiday leave, and jury/civic duty leave.
Expected source: 01_employee_handbook_overview.md

22. Question: Does the policy explicitly recognize public holiday leave as a leave category?
Gold answer: Yes, public holiday leave is explicitly listed.
Expected source: 01_employee_handbook_overview.md

## Topic Coverage Map
- PTO/leave and employee expectations: Q1, Q2, Q21, Q22
- Security and access: Q5, Q6, Q7, Q8
- Privacy and legal hold: Q10, Q13
- Remote work: Q14
- Vendor/process ops: Q15, Q16
- Continuity/DR: Q17
- Expense: Q18
- HR offboarding: Q19
- Support operations: Q20

## Scoring Guidance
For each answer, record:
- Groundedness score (1.0, 0.5, 0.0)
- Citation accuracy score (1.0, 0.5, 0.0)
- Exact or partial match (optional)
- End-to-end latency in milliseconds
