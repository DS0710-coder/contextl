# libreplan-business/src/main/java/org/libreplan/business/hibernate/notification/PredefinedDatabaseSnapshots.java

## Explanation
*No explanation provided in source code.*

## Metrics
**Extension:** `.java`
**Size:** 15117 bytes
**Centrality Score:** 0.0008

## Imports (Dependencies)
- [[libreplan-business-src-main-java-org-libreplan-business-advance-entities-DirectAdvanceAssignment.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-calendars-entities-CalendarAvailability.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-calendars-entities-CalendarData.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-calendars-entities-CalendarException.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-AdHocTransactionService.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-IAdHocTransactionService.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-costcategories-daos-ICostCategoryDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-costcategories-entities-CostCategory.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-externalcompanies-daos-IExternalCompanyDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-externalcompanies-entities-ExternalCompany.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-labels-daos-ILabelDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-labels-daos-ILabelTypeDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-labels-entities-Label.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-labels-entities-LabelType.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-daos-IOrderDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-entities-Order.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-chart-ResourceLoadChartData.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-daos-IDayAssignmentDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-daos-ITaskElementDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-DayAssignment.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-GenericResourceAllocation.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-ICostCalculator.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-ResourceAllocation.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-SpecificResourceAllocation.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-Task.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-TaskElement.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-TaskGroup.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-daos-ICriterionDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-daos-ICriterionTypeDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-daos-IResourceDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-daos-IWorkerDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-entities-Criterion.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-entities-CriterionType.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-entities-Machine.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-entities-Resource.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-entities-VirtualWorker.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-entities-Worker.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-scenarios-IScenarioManager.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-workreports-daos-IWorkReportLineDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-workreports-entities-WorkReportLine.java]]

## Imported By (Dependents)
- [[libreplan-business-src-main-java-org-libreplan-business-planner-chart-ResourceLoadChartData.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-CompanyEarnedValueCalculator.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-bootstrap-BootstrapListener.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-common-components-finders-CriterionMultipleFiltersFinder.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-common-components-finders-OrderElementsMultipleFiltersFinder.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-common-components-finders-OrdersMultipleFiltersFinder.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-common-components-finders-ResourceAllocationMultipleFiltersFinder.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-common-components-finders-ResourceMultipleFiltersFinderByResourceAndCriterion.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-common-components-finders-ResourcesMultipleFiltersFinder.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-common-components-finders-TaskElementsMultipleFiltersFinder.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-common-components-finders-TaskGroupsMultipleFiltersFinder.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-company-CompanyPlanningModel.java]]