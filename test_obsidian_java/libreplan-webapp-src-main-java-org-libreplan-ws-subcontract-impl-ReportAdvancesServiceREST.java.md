# libreplan-webapp/src/main/java/org/libreplan/ws/subcontract/impl/ReportAdvancesServiceREST.java

## Explanation
*No explanation provided in source code.*

## Metrics
**Extension:** `.java`
**Size:** 16084 bytes
**Centrality Score:** 0.0002

## Imports (Dependencies)
- [[libreplan-business-src-main-java-org-libreplan-business-advance-bootstrap-PredefinedAdvancedTypes.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-advance-entities-AdvanceAssignment.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-advance-entities-AdvanceMeasurement.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-advance-entities-DirectAdvanceAssignment.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-advance-exceptions-DuplicateAdvanceAssignmentForOrderElementException.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-advance-exceptions-DuplicateValueTrueReportGlobalAdvanceException.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-exceptions-InstanceNotFoundException.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-exceptions-ValidationException.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-externalcompanies-daos-IExternalCompanyDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-externalcompanies-entities-CommunicationType.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-externalcompanies-entities-EndDateCommunication.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-externalcompanies-entities-ExternalCompany.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-daos-IOrderDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-daos-IOrderElementDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-entities-Order.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-entities-OrderElement.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-daos-ISubcontractedTaskDataDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-daos-ISubcontractorCommunicationDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-SubcontractedTaskData.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-SubcontractorCommunication.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-SubcontractorCommunicationValue.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-Task.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-scenarios-bootstrap-PredefinedScenarios.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-scenarios-entities-OrderVersion.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-scenarios-entities-Scenario.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-common-api-AdvanceMeasurementDTO.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-common-api-InstanceConstraintViolationsDTO.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-common-api-InstanceConstraintViolationsListDTO.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-common-impl-ConstraintViolationConverter.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-common-impl-DateConverter.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-common-impl-OrderElementConverter.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-common-impl-Util.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-subcontract-api-EndDateCommunicationToCustomerDTO.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-subcontract-api-IReportAdvancesService.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-subcontract-api-OrderElementWithAdvanceMeasurementsOrEndDateDTO.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-subcontract-api-OrderElementWithAdvanceMeasurementsOrEndDateListDTO.java]]

## Imported By (Dependents)
*Not imported by any file*