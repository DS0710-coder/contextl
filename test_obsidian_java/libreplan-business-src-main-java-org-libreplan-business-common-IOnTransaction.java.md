# libreplan-business/src/main/java/org/libreplan/business/common/IOnTransaction.java

## Explanation
*No explanation provided in source code.*

## Metrics
**Extension:** `.java`
**Size:** 1095 bytes
**Centrality Score:** 0.0015

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[libreplan-business-src-main-java-org-libreplan-business-orders-daos-OrderDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-daos-SumChargedEffortDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-daos-SumExpensesDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-daos-ResourcesSearcher.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-entities-Resource.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-expensesheet-daos-ExpenseSheetTestDAO.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-externalcompanies-daos-ExternalCompanyDAOTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-orders-daos-OrderDAOTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-planner-daos-TaskElementDAOTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-planner-entities-MoneyCostCalculatorTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-resources-daos-CriterionDAOTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-resources-daos-CriterionTypeDAOTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-resources-daos-MachineDAOTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-scenarios-daos-ScenarioDAOTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-users-daos-UserDAOTest.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-importers-ExportTimesheetsToTim.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-importers-ImportRosterFromTim.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-importers-JiraOrderElementSynchronizer.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-common-TemplateModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-limitingresources-LimitingResourcesController.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-orders-labels-AssignedLabelsModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-TaskElementAdapter.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-allocation-ResourceAllocationModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-company-CompanyPlanningModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-limiting-allocation-LimitingResourceAllocationModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-order-OrderPlanningModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-order-SaveCommandBuilder.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-reassign-ReassignCommand.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-tabs-AdvancedAllocationTabCreator.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-tabs-CriticalPathBuilder.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-tabs-DashboardTabCreator.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-resourceload-ResourceLoadController.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-resources-search-NewAllocationSelectorController.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-templates-OrderTemplatesModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-templates-historicalAssignment-OrderElementHistoricalAssignmentComponent.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-templates-historicalStatistics-OrderElementHistoricalStatisticsComponent.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-users-services-LDAPCustomAuthenticationProvider.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-boundusers-impl-BoundUserServiceREST.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-common-impl-GenericRESTService.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-subcontract-impl-SubcontractServiceREST.java]]
- [[libreplan-webapp-src-test-java-org-libreplan-importers-ExportTimesheetsToTimTest.java]]
- [[libreplan-webapp-src-test-java-org-libreplan-importers-ImportRosterFromTimTest.java]]
- [[libreplan-webapp-src-test-java-org-libreplan-importers-JiraOrderElementSynchronizerTest.java]]
- [[libreplan-webapp-src-test-java-org-libreplan-importers-JiraTimesheetSynchronizerTest.java]]
- [[libreplan-webapp-src-test-java-org-libreplan-web-calendars-BaseCalendarModelTest.java]]
- [[libreplan-webapp-src-test-java-org-libreplan-web-orders-OrderModelTest.java]]
- [[libreplan-webapp-src-test-java-org-libreplan-web-planner-chart-ChartFillerTest.java]]
- [[libreplan-webapp-src-test-java-org-libreplan-web-resources-CriterionModelTest.java]]
- [[libreplan-webapp-src-test-java-org-libreplan-web-scenarios-ScenarioModelTest.java]]
- [[libreplan-webapp-src-test-java-org-libreplan-web-scenarios-TransferOrdersModelTest.java]]
- [[libreplan-webapp-src-test-java-org-libreplan-web-test-ws-basecalendars-BaseCalendarServiceTest.java]]
- [[libreplan-webapp-src-test-java-org-libreplan-web-test-ws-costcategories-CostCategoryServiceTest.java]]
- [[libreplan-webapp-src-test-java-org-libreplan-web-test-ws-labels-api-LabelServiceTest.java]]
- [[libreplan-webapp-src-test-java-org-libreplan-web-test-ws-materials-MaterialServiceTest.java]]
- [[libreplan-webapp-src-test-java-org-libreplan-web-test-ws-orders-OrderElementServiceTest.java]]
- [[libreplan-webapp-src-test-java-org-libreplan-web-test-ws-resources-api-ResourceServiceTest.java]]
- [[libreplan-webapp-src-test-java-org-libreplan-web-test-ws-subcontract-ReportAdvancesServiceTest.java]]
- [[libreplan-webapp-src-test-java-org-libreplan-web-test-ws-typeofworkhours-TypeOfWorkHoursServiceTest.java]]
- [[libreplan-webapp-src-test-java-org-libreplan-web-test-ws-unittypes-UnitTypeServiceTest.java]]