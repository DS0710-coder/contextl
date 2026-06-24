# libreplan-webapp/src/test/java/org/libreplan/web/test/ws/subcontract/ReportAdvancesServiceTest.java

## Explanation
*No explanation provided in source code.*

## Metrics
**Extension:** `.java`
**Size:** 28392 bytes
**Centrality Score:** 0.0002

## Imports (Dependencies)
- [[libreplan-business-src-main-java-org-libreplan-business-IDataBootstrap.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-advance-entities-AdvanceMeasurement.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-advance-entities-DirectAdvanceAssignment.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-IAdHocTransactionService.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-IOnTransaction.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-daos-IConfigurationDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-exceptions-InstanceNotFoundException.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-externalcompanies-daos-IExternalCompanyDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-externalcompanies-entities-ExternalCompany.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-daos-IOrderDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-daos-IOrderElementDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-entities-HoursGroup.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-entities-Order.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-entities-OrderElement.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-entities-OrderLine.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-entities-SchedulingDataForVersion.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-entities-TaskSource.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-daos-ISubcontractedTaskDataDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-daos-ISubcontractorCommunicationDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-daos-ITaskElementDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-daos-ITaskSourceDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-SubcontractedTaskData.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-SubcontractorDeliverDate.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-Task.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-scenarios-IScenarioManager.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-scenarios-entities-OrderVersion.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-common-api-AdvanceMeasurementDTO.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-common-impl-DateConverter.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-subcontract-api-EndDateCommunicationToCustomerDTO.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-subcontract-api-IReportAdvancesService.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-subcontract-api-OrderElementWithAdvanceMeasurementsOrEndDateDTO.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-subcontract-api-OrderElementWithAdvanceMeasurementsOrEndDateListDTO.java]]
- [[libreplan-webapp-src-test-java-org-libreplan-web-orders-OrderModelTest.java]]

## Imported By (Dependents)
*Not imported by any file*