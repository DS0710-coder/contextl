# libreplan-business/src/test/java/org/libreplan/business/test/orders/daos/OrderElementDAOTest.java

## Explanation
*No explanation provided in source code.*

## Metrics
**Extension:** `.java`
**Size:** 28544 bytes
**Centrality Score:** 0.0002

## Imports (Dependencies)
- [[libreplan-business-src-main-java-org-libreplan-business-IDataBootstrap.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-advance-bootstrap-PredefinedAdvancedTypes.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-advance-entities-AdvanceMeasurement.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-advance-entities-AdvanceType.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-advance-entities-DirectAdvanceAssignment.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-advance-exceptions-DuplicateAdvanceAssignmentForOrderElementException.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-advance-exceptions-DuplicateValueTrueReportGlobalAdvanceException.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-calendars-daos-IBaseCalendarDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-calendars-entities-BaseCalendar.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-exceptions-InstanceNotFoundException.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-exceptions-ValidationException.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-labels-daos-ILabelDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-labels-daos-ILabelTypeDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-labels-entities-Label.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-labels-entities-LabelType.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-daos-IOrderElementDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-entities-Order.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-entities-OrderElement.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-entities-OrderLine.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-entities-OrderLineGroup.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-entities-SumChargedEffort.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-qualityforms-daos-IQualityFormDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-qualityforms-entities-QualityForm.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-qualityforms-entities-TaskQualityForm.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-requirements-entities-DirectCriterionRequirement.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-daos-ICriterionDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-daos-ICriterionTypeDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-entities-Criterion.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-entities-CriterionType.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-scenarios-IScenarioManager.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-scenarios-bootstrap-IScenariosBootstrap.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-scenarios-entities-OrderVersion.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-workingday-EffortDuration.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-calendars-entities-BaseCalendarTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-orders-entities-OrderElementTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-planner-daos-ResourceAllocationDAOTest.java]]

## Imported By (Dependents)
*Not imported by any file*