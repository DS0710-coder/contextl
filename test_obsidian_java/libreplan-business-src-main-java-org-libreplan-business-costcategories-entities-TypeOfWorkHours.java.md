# libreplan-business/src/main/java/org/libreplan/business/costcategories/entities/TypeOfWorkHours.java

## Explanation
*No explanation provided in source code.*

## Metrics
**Extension:** `.java`
**Size:** 5898 bytes
**Centrality Score:** 0.0033

## Imports (Dependencies)
- [[libreplan-business-src-main-java-org-libreplan-business-common-IHumanIdentifiable.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-IntegrationEntity.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-Registry.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-entities-Connector.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-entities-PredefinedConnectorProperties.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-entities-PredefinedConnectors.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-exceptions-InstanceNotFoundException.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-costcategories-daos-ITypeOfWorkHoursDAO.java]]

## Imported By (Dependents)
- [[libreplan-business-src-main-java-org-libreplan-business-common-entities-Configuration.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-entities-ConfigurationTypeOfWorkHoursBootstrap.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-costcategories-daos-HourCostDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-costcategories-daos-IHourCostDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-costcategories-daos-ITypeOfWorkHoursDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-costcategories-daos-TypeOfWorkHoursDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-daos-OrderDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-entities-OrderElement.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-reports-dtos-WorkReportLineDTO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-workreports-entities-WorkReportLine.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-costcategories-daos-CostCategoryDAOTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-costcategories-daos-HourCostDAOTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-costcategories-daos-TypeOfWorkHoursDAOTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-planner-entities-MoneyCostCalculatorTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-workreports-daos-AbstractWorkReportTest.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-importers-JiraTimesheetSynchronizer.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-common-ConfigurationController.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-common-ConfigurationModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-common-IConfigurationModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-common-components-finders-TypeOfWorkHoursBandboxFinder.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-common-components-finders-TypeOfWorkHoursFinder.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-costcategories-CostCategoryCRUDController.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-costcategories-CostCategoryModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-costcategories-ICostCategoryModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-costcategories-ITypeOfWorkHoursModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-costcategories-TypeOfWorkHoursCRUDController.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-costcategories-TypeOfWorkHoursModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-orders-OrderElementModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-reports-OrderCostsPerResourceModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-users-dashboard-PersonalTimesheetModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-workreports-IWorkReportModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-workreports-WorkReportCRUDController.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-workreports-WorkReportLinePredicate.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-workreports-WorkReportModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-workreports-WorkReportQueryController.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-costcategories-impl-CostCategoryConverter.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-typeofworkhours-api-TypeOfWorkHoursDTO.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-typeofworkhours-impl-TypeOfWorkHoursConverter.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-typeofworkhours-impl-TypeOfWorkHoursServiceREST.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-workreports-impl-WorkReportConverter.java]]
- [[libreplan-webapp-src-test-java-org-libreplan-web-test-ws-costcategories-CostCategoryServiceTest.java]]
- [[libreplan-webapp-src-test-java-org-libreplan-web-test-ws-typeofworkhours-TypeOfWorkHoursServiceTest.java]]
- [[libreplan-webapp-src-test-java-org-libreplan-web-test-ws-workreports-WorkReportServiceTest.java]]