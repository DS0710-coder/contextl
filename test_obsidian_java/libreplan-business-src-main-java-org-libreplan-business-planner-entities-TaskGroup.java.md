# libreplan-business/src/main/java/org/libreplan/business/planner/entities/TaskGroup.java

## Explanation
*No explanation provided in source code.*

## Metrics
**Extension:** `.java`
**Size:** 12770 bytes
**Centrality Score:** 0.0026

## Imports (Dependencies)
- [[libreplan-business-src-main-java-org-libreplan-business-common-entities-ProgressType.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-entities-TaskSource.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-daos-IResourcesSearcher.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-scenarios-entities-Scenario.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-util-TaskElementVisitor.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-workingday-EffortDuration.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-workingday-IntraDayDate.java]]

## Imported By (Dependents)
- [[libreplan-business-src-main-java-org-libreplan-business-hibernate-notification-PredefinedDatabaseSnapshots.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-entities-Order.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-entities-OrderLineGroup.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-entities-TaskSource.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-daos-ITaskElementDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-daos-TaskElementDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-visitors-AccumulateTasksDeadlineStatusVisitor.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-visitors-AccumulateTasksStatusVisitor.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-visitors-CalculateFinishedTasksEstimationDeviationVisitor.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-visitors-CalculateFinishedTasksLagInCompletionVisitor.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-visitors-ResetTasksStatusVisitor.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-util-TaskElementVisitor.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-planner-daos-TaskElementDAOTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-planner-entities-TaskElementTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-planner-entities-TaskGroupTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-planner-entities-TaskTest.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-importers-IOrderImporter.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-importers-OrderImporterMPXJ.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-common-components-finders-TaskGroupFilterEnum.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-common-components-finders-TaskGroupsMultipleFiltersFinder.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-dashboard-DashboardModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-importers-ProjectImportController.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-montecarlo-MonteCarloCriticalPathBuilder.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-TaskElementAdapter.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-TaskGroupPredicate.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-advances-AdvanceAssignmentPlanningCommand.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-company-CompanyPlanningModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-milestone-AddMilestoneCommand.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-order-PlanningStateCreator.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-order-SaveCommandBuilder.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-tabs-AdvancedAllocationTabCreator.java]]
- [[libreplan-webapp-src-test-java-org-libreplan-web-test-ws-email-EmailTest.java]]