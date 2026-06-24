# libreplan-business/src/test/java/org/libreplan/business/test/planner/entities/MoneyCostCalculatorTest.java

## Explanation
*No explanation provided in source code.*

## Metrics
**Extension:** `.java`
**Size:** 20552 bytes
**Centrality Score:** 0.0002

## Imports (Dependencies)
- [[libreplan-business-src-main-java-org-libreplan-business-IDataBootstrap.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-IAdHocTransactionService.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-IOnTransaction.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-exceptions-InstanceNotFoundException.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-costcategories-daos-ICostCategoryDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-costcategories-daos-ITypeOfWorkHoursDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-costcategories-entities-CostCategory.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-costcategories-entities-HourCost.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-costcategories-entities-ResourcesCostCategoryAssignment.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-costcategories-entities-TypeOfWorkHours.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-expensesheet-daos-IExpenseSheetDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-expensesheet-entities-ExpenseSheet.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-expensesheet-entities-ExpenseSheetLine.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-daos-IOrderElementDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-daos-ISumExpensesDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-entities-OrderElement.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-entities-OrderLine.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-entities-OrderLineGroup.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-IMoneyCostCalculator.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-MoneyCostCalculator.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-daos-IResourceDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-entities-Resource.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-entities-Worker.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-scenarios-IScenarioManager.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-scenarios-daos-IOrderVersionDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-scenarios-entities-OrderVersion.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-workingday-EffortDuration.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-workreports-daos-IWorkReportDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-workreports-daos-IWorkReportTypeDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-workreports-entities-WorkReport.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-workreports-entities-WorkReportLine.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-workreports-entities-WorkReportType.java]]

## Imported By (Dependents)
*Not imported by any file*