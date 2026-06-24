# libreplan-business/src/main/java/org/libreplan/business/resources/daos/IResourceDAO.java

## Explanation
*No explanation provided in source code.*

## Metrics
**Extension:** `.java`
**Size:** 3535 bytes
**Centrality Score:** 0.0017

## Imports (Dependencies)
- [[libreplan-business-src-main-java-org-libreplan-business-common-daos-IIntegrationEntityDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-labels-entities-Label.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-reports-dtos-HoursWorkedPerResourceDTO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-reports-dtos-HoursWorkedPerWorkerInAMonthDTO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-reports-dtos-LabelFilterType.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-entities-Criterion.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-entities-Machine.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-entities-Resource.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-entities-Worker.java]]

## Imported By (Dependents)
- [[libreplan-business-src-main-java-org-libreplan-business-common-Registry.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-hibernate-notification-PredefinedDatabaseSnapshots.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-entities-Resource.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-calendars-daos-BaseCalendarDAOTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-expensesheet-daos-ExpenseSheetTestDAO.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-planner-daos-ResourceAllocationDAOTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-planner-daos-TaskElementDAOTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-planner-entities-MoneyCostCalculatorTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-resources-bootstrap-CriterionsBootstrapTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-resources-daos-ResourceDAOTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-workreports-daos-AbstractWorkReportTest.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-common-components-finders-ResourceBandboxFinder.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-common-components-finders-ResourceFinder.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-common-components-finders-ResourceInExpenseSheetBandboxFinder.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-common-converters-ResourceConverter.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-costcategories-ResourcesCostCategoryAssignmentModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-allocation-ResourceAllocationModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-limiting-allocation-LimitingResourceAllocationModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-order-PlanningStateCreator.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-reports-HoursWorkedPerWorkerInAMonthModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-reports-HoursWorkedPerWorkerModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-resourceload-ResourceLoadModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-resources-criterion-CriterionsModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-resources-machine-AssignedMachineCriterionsModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-resources-machine-MachineCRUDController.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-resources-machine-MachineModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-resources-worker-AssignedCriterionsModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-resources-worker-WorkerCRUDController.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-resources-worker-WorkerModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-resources-impl-ResourceServiceREST.java]]
- [[libreplan-webapp-src-test-java-org-libreplan-web-orders-OrderElementTreeModelTest.java]]
- [[libreplan-webapp-src-test-java-org-libreplan-web-resources-WorkerModelTest.java]]
- [[libreplan-webapp-src-test-java-org-libreplan-web-test-ws-orders-OrderElementServiceTest.java]]
- [[libreplan-webapp-src-test-java-org-libreplan-web-test-ws-resources-api-ResourceServiceTest.java]]