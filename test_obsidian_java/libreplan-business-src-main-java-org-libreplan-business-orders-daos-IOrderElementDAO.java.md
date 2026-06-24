# libreplan-business/src/main/java/org/libreplan/business/orders/daos/IOrderElementDAO.java

## Explanation
*No explanation provided in source code.*

## Metrics
**Extension:** `.java`
**Size:** 5189 bytes
**Centrality Score:** 0.0013

## Imports (Dependencies)
- [[libreplan-business-src-main-java-org-libreplan-business-common-daos-IIntegrationEntityDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-exceptions-InstanceNotFoundException.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-labels-entities-Label.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-entities-OrderElement.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-entities-Criterion.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-templates-entities-OrderElementTemplate.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-workingday-EffortDuration.java]]

## Imported By (Dependents)
- [[libreplan-business-src-main-java-org-libreplan-business-common-Registry.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-expensesheet-daos-ExpenseSheetTestDAO.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-orders-daos-OrderElementDAOTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-planner-daos-ResourceAllocationDAOTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-planner-entities-MoneyCostCalculatorTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-workreports-daos-AbstractWorkReportTest.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-common-components-finders-OrderElementBandboxFinder.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-common-components-finders-OrderElementInExpenseSheetBandboxFinder.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-common-converters-OrderElementConverter.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-orders-AssignedHoursToOrderElementModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-orders-AssignedTaskQualityFormsToOrderElementModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-orders-ManageOrderElementAdvancesModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-orders-OrderElementModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-orders-OrderModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-orders-criterionrequirements-AssignedCriterionRequirementToOrderElementModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-orders-labels-AssignedLabelsToOrderElementModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-orders-materials-AssignedMaterialsToOrderElementModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-TaskElementAdapter.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-advances-AdvanceAssignmentPlanningModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-consolidations-AdvanceConsolidationModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-order-SaveCommandBuilder.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-reports-ProjectStatusReportModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-reports-SchedulingProgressPerOrderModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-reports-TimeLineRequiredMaterialModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-scenarios-ScenarioModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-subcontract-ReportAdvancesModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-subcontract-SubcontractedTasksModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-templates-OrderElementsOnConversation.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-templates-OrderTemplatesModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-templates-historicalAssignment-OrderElementHistoricalAssignmentComponent.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-templates-historicalStatistics-OrderElementHistoricalStatisticsComponent.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-workreports-WorkReportModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-boundusers-impl-BoundUserServiceREST.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-orders-impl-OrderElementServiceREST.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-subcontract-impl-ReportAdvancesServiceREST.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-subcontract-impl-SubcontractServiceREST.java]]
- [[libreplan-webapp-src-test-java-org-libreplan-web-orders-OrderFilesTest.java]]
- [[libreplan-webapp-src-test-java-org-libreplan-web-test-ws-orders-OrderElementServiceTest.java]]
- [[libreplan-webapp-src-test-java-org-libreplan-web-test-ws-subcontract-ReportAdvancesServiceTest.java]]
- [[libreplan-webapp-src-test-java-org-libreplan-web-test-ws-workreports-WorkReportServiceTest.java]]