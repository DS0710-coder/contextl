# libreplan-webapp/src/main/java/org/libreplan/web/planner/TaskElementAdapter.java

## Explanation
*No explanation provided in source code.*

## Metrics
**Extension:** `.java`
**Size:** 51843 bytes
**Centrality Score:** 0.0004

## Imports (Dependencies)
- [[ganttzk-src-main-java-org-zkoss-ganttz-IDatesMapper.java]]
- [[ganttzk-src-main-java-org-zkoss-ganttz-ProjectStatusEnum.java]]
- [[ganttzk-src-main-java-org-zkoss-ganttz-adapters-DomainDependency.java]]
- [[ganttzk-src-main-java-org-zkoss-ganttz-adapters-IAdapterToTaskFundamentalProperties.java]]
- [[ganttzk-src-main-java-org-zkoss-ganttz-data-DependencyType.java]]
- [[ganttzk-src-main-java-org-zkoss-ganttz-data-GanttDate.java]]
- [[ganttzk-src-main-java-org-zkoss-ganttz-data-ITaskFundamentalProperties.java]]
- [[ganttzk-src-main-java-org-zkoss-ganttz-data-constraint-Constraint.java]]
- [[ganttzk-src-main-java-org-zkoss-ganttz-util-ReentranceGuard.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-calendars-entities-BaseCalendar.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-IAdHocTransactionService.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-IOnTransaction.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-daos-IConfigurationDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-entities-ProgressType.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-externalcompanies-daos-IExternalCompanyDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-labels-entities-Label.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-daos-IOrderElementDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-entities-Order.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-entities-OrderElement.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-entities-OrderStatusEnum.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-entities-SumChargedEffort.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-entities-SumExpenses.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-daos-IResourceAllocationDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-daos-ITaskElementDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-Dependency.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-GenericResourceAllocation.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-IMoneyCostCalculator.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-ITaskPositionConstrained.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-MoneyCostCalculator.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-PositionConstraintType.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-ResourceAllocation.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-SpecificResourceAllocation.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-Task.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-TaskElement.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-TaskGroup.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-TaskPositionConstraint.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-daos-ICriterionDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-daos-IResourcesSearcher.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-entities-Criterion.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-entities-Resource.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-scenarios-entities-Scenario.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-workingday-EffortDuration.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-workingday-IntraDayDate.java]]

## Imported By (Dependents)
- [[libreplan-webapp-src-main-java-org-libreplan-web-common-TemplateModelAdapter.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-company-CompanyPlanningModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-order-PlanningStateCreator.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-order-SaveCommandBuilder.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-reassign-ReassignConfiguration.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-resourceload-LoadPeriodGenerator.java]]