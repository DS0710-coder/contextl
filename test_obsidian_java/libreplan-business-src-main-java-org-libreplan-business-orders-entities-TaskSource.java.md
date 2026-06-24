# libreplan-business/src/main/java/org/libreplan/business/orders/entities/TaskSource.java

## Explanation
*No explanation provided in source code.*

## Metrics
**Extension:** `.java`
**Size:** 13414 bytes
**Centrality Score:** 0.0017

## Imports (Dependencies)
- [[libreplan-business-src-main-java-org-libreplan-business-common-BaseEntity.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-exceptions-InstanceNotFoundException.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-daos-ITaskElementDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-daos-ITaskSourceDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-Task.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-TaskElement.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-TaskGroup.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-util-deepcopy-OnCopy.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-util-deepcopy-Strategy.java]]

## Imported By (Dependents)
- [[libreplan-business-src-main-java-org-libreplan-business-orders-daos-OrderElementDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-daos-ITaskSourceDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-daos-TaskSourceDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-Task.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-TaskElement.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-TaskGroup.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-reports-dtos-ProjectStatusReportDTO.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-planner-daos-ResourceAllocationDAOTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-planner-daos-SubcontractorCommunicationDAOTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-planner-daos-TaskElementDAOTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-planner-entities-TaskElementTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-planner-entities-TaskGroupTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-planner-entities-TaskTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-scenarios-bootstrap-ScenariosBootstrapTest.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-importers-OrderImporterMPXJ.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-common-TemplateModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-limitingresources-LimitingResourceQueueModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-limiting-allocation-LimitingResourceAllocationModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-order-PlanningStateCreator.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-order-SaveCommandBuilder.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-tabs-GanttDiagramBuilder.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-reports-SchedulingProgressPerOrderModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-scenarios-TransferOrdersModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-subcontract-impl-SubcontractServiceREST.java]]
- [[libreplan-webapp-src-test-java-org-libreplan-web-orders-OrderModelTest.java]]
- [[libreplan-webapp-src-test-java-org-libreplan-web-test-ws-email-EmailTest.java]]
- [[libreplan-webapp-src-test-java-org-libreplan-web-test-ws-subcontract-ReportAdvancesServiceTest.java]]