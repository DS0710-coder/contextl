# libreplan-business/src/main/java/org/libreplan/business/externalcompanies/entities/ExternalCompany.java

## Explanation
*No explanation provided in source code.*

## Metrics
**Extension:** `.java`
**Size:** 5705 bytes
**Centrality Score:** 0.0027

## Imports (Dependencies)
- [[libreplan-business-src-main-java-org-libreplan-business-common-BaseEntity.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-IHumanIdentifiable.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-Registry.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-exceptions-InstanceNotFoundException.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-externalcompanies-daos-IExternalCompanyDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-users-entities-User.java]]

## Imported By (Dependents)
- [[libreplan-business-src-main-java-org-libreplan-business-externalcompanies-daos-ExternalCompanyDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-externalcompanies-daos-IExternalCompanyDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-hibernate-notification-PredefinedDatabaseSnapshots.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-daos-IOrderDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-daos-OrderDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-entities-Order.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-SubcontractedTaskData.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-Task.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-TaskElement.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-externalcompanies-daos-ExternalCompanyDAOTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-planner-daos-SubcontractorCommunicationDAOTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-planner-daos-TaskElementDAOTest.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-common-components-finders-ExternalCompanyBandboxFinder.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-common-components-finders-OrdersMultipleFiltersFinder.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-common-components-finders-TaskGroupsMultipleFiltersFinder.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-externalcompanies-ExternalCompanyCRUDController.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-externalcompanies-ExternalCompanyDTO.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-externalcompanies-ExternalCompanyModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-externalcompanies-IExternalCompanyModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-orders-IOrderModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-orders-OrderCRUDController.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-orders-OrderModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-orders-OrderPredicate.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-orders-ProjectDetailsController.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-TaskGroupPredicate.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-company-CompanyPlanningModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-order-ISubcontractModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-order-SubcontractController.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-order-SubcontractModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-subcontract-ReportAdvancesModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-subcontract-SubcontractedTasksModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-subcontract-impl-ReportAdvancesServiceREST.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-subcontract-impl-SubcontractServiceREST.java]]
- [[libreplan-webapp-src-test-java-org-libreplan-web-orders-OrderModelTest.java]]
- [[libreplan-webapp-src-test-java-org-libreplan-web-test-ws-subcontract-ReportAdvancesServiceTest.java]]
- [[libreplan-webapp-src-test-java-org-libreplan-web-test-ws-subcontract-SubcontractServiceTest.java]]