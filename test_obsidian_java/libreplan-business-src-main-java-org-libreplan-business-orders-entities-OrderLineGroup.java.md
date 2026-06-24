# libreplan-business/src/main/java/org/libreplan/business/orders/entities/OrderLineGroup.java

## Explanation
*No explanation provided in source code.*

## Metrics
**Extension:** `.java`
**Size:** 42687 bytes
**Centrality Score:** 0.0022

## Imports (Dependencies)
- [[libreplan-business-src-main-java-org-libreplan-business-advance-bootstrap-PredefinedAdvancedTypes.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-advance-entities-AdvanceAssignment.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-advance-entities-AdvanceMeasurement.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-advance-entities-AdvanceMeasurementComparator.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-advance-entities-AdvanceType.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-advance-entities-DirectAdvanceAssignment.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-advance-entities-IndirectAdvanceAssignment.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-advance-exceptions-DuplicateAdvanceAssignmentForOrderElementException.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-advance-exceptions-DuplicateValueTrueReportGlobalAdvanceException.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-labels-entities-Label.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-materials-entities-MaterialAssignment.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-TaskElement.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-TaskGroup.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-qualityforms-entities-TaskQualityForm.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-scenarios-entities-OrderVersion.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-templates-entities-OrderElementTemplate.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-templates-entities-OrderLineGroupTemplate.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-trees-ITreeParentNode.java]]

## Imported By (Dependents)
- [[libreplan-business-src-main-java-org-libreplan-business-advance-entities-AdvanceAssignment.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-advance-entities-IndirectAdvanceAssignment.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-daos-SumChargedEffortDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-daos-SumExpensesDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-templates-entities-OrderElementTemplate.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-templates-entities-OrderLineGroupTemplate.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-templates-entities-OrderLineTemplate.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-templates-entities-OrderTemplate.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-orders-daos-OrderElementDAOTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-orders-entities-AddAdvanceAssignmentsToOrderElementTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-orders-entities-OrderElementTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-orders-entities-OrderLineTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-orders-entities-OrderTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-planner-entities-MoneyCostCalculatorTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-planner-entities-TaskElementTest.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-importers-OrderImporterMPXJ.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-expensesheet-ExpenseSheetModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-orders-HoursGroupWrapper.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-orders-IOrderModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-orders-OrderElementController.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-orders-OrderElementTreeController.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-orders-OrderModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-order-SaveCommandBuilder.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-workreports-WorkReportModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-common-api-OrderLineGroupDTO.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-common-impl-OrderElementConverter.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-orders-impl-OrderElementServiceREST.java]]
- [[libreplan-webapp-src-test-java-org-libreplan-web-orders-OrderElementTreeModelTest.java]]
- [[libreplan-webapp-src-test-java-org-libreplan-web-orders-OrderModelTest.java]]