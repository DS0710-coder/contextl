# libreplan-business/src/test/java/org/libreplan/business/test/planner/daos/TaskElementDAOTest.java

## Explanation
*No explanation provided in source code.*

## Metrics
**Extension:** `.java`
**Size:** 22322 bytes
**Centrality Score:** 0.0002

## Imports (Dependencies)
- [[libreplan-business-src-main-java-org-libreplan-business-IDataBootstrap.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-IAdHocTransactionService.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-IOnTransaction.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-daos-IConfigurationDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-exceptions-InstanceNotFoundException.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-exceptions-ValidationException.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-externalcompanies-daos-IExternalCompanyDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-externalcompanies-entities-ExternalCompany.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-daos-IOrderDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-entities-HoursGroup.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-entities-Order.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-entities-OrderLine.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-entities-SchedulingDataForVersion.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-entities-TaskSource.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-daos-ISubcontractedTaskDataDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-daos-ITaskElementDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-daos-ITaskSourceDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-daos-TaskElementDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-Dependency.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-SpecificResourceAllocation.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-SubcontractedTaskData.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-SubcontractorDeliverDate.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-Task.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-TaskElement.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-TaskGroup.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-TaskMilestone.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-daos-IResourceDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-entities-Worker.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-scenarios-IScenarioManager.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-scenarios-bootstrap-IScenariosBootstrap.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-scenarios-entities-OrderVersion.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-workingday-IntraDayDate.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-externalcompanies-daos-ExternalCompanyDAOTest.java]]

## Imported By (Dependents)
*Not imported by any file*