# libreplan-webapp/src/main/java/org/libreplan/ws/subcontract/impl/SubcontractServiceREST.java

## Explanation
*No explanation provided in source code.*

## Metrics
**Extension:** `.java`
**Size:** 17789 bytes
**Centrality Score:** 0.0002

## Imports (Dependencies)
- [[libreplan-business-src-main-java-org-libreplan-business-calendars-entities-BaseCalendar.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-IAdHocTransactionService.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-IOnTransaction.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-Registry.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-daos-IConfigurationDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-daos-IEntitySequenceDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-entities-EntityNameEnum.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-entities-EntitySequence.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-exceptions-InstanceNotFoundException.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-exceptions-ValidationException.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-externalcompanies-daos-ICustomerCommunicationDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-externalcompanies-daos-IExternalCompanyDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-externalcompanies-entities-CommunicationType.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-externalcompanies-entities-CustomerCommunication.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-externalcompanies-entities-DeadlineCommunication.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-externalcompanies-entities-ExternalCompany.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-daos-IOrderElementDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-entities-Order.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-entities-OrderElement.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-entities-OrderStatusEnum.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-entities-TaskSource.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-daos-ITaskSourceDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-scenarios-daos-IScenarioDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-scenarios-entities-OrderVersion.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-scenarios-entities-Scenario.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-subcontract-UpdateDeliveringDateDTO.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-common-api-InstanceConstraintViolationsDTO.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-common-api-InstanceConstraintViolationsDTOId.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-common-api-InstanceConstraintViolationsListDTO.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-common-api-OrderDTO.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-common-api-OrderElementDTO.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-common-impl-ConfigurationOrderElementConverter.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-common-impl-ConstraintViolationConverter.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-common-impl-DateConverter.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-common-impl-OrderElementConverter.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-common-impl-Util.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-subcontract-api-ISubcontractService.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-subcontract-api-SubcontractedTaskDataDTO.java]]

## Imported By (Dependents)
*Not imported by any file*