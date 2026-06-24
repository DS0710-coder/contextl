# libreplan-business/src/main/java/org/libreplan/business/planner/entities/DayAssignment.java

## Explanation
*No explanation provided in source code.*

## Metrics
**Extension:** `.java`
**Size:** 11248 bytes
**Centrality Score:** 0.0024

## Imports (Dependencies)
- [[libreplan-business-src-main-java-org-libreplan-business-common-BaseEntity.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-entities-Resource.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-scenarios-entities-Scenario.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-util-deepcopy-AfterCopy.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-util-deepcopy-OnCopy.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-util-deepcopy-Strategy.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-workingday-EffortDuration.java]]

## Imported By (Dependents)
- [[libreplan-business-src-main-java-org-libreplan-business-hibernate-notification-PredefinedDatabaseSnapshots.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-entities-Order.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-chart-ContiguousDaysLine.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-chart-ResourceLoadChartData.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-daos-DayAssignmentDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-daos-IDayAssignmentDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-AggregateOfDayAssignments.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-allocationalgorithms-ResourcesPerDayModification.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-allocationalgorithms-UntilFillingHoursAllocator.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-limiting-entities-AllocationSpec.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-limiting-entities-LimitingResourceAllocator.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-limiting-entities-LimitingResourceQueueElement.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-reports-dtos-CompletedEstimatedHoursPerTaskDTO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-reports-dtos-SchedulingProgressPerOrderDTO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-reports-dtos-WorkingArrangementsPerOrderDTO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-reports-dtos-WorkingProgressPerTaskDTO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-daos-ResourceLoadRatiosCalculator.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-entities-IAssignmentsOnResourceCalculator.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-entities-Resource.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-planner-entities-DayAssignmentMatchers.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-planner-entities-DerivedAllocationGeneratorTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-planner-entities-SpecificResourceAllocationTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-planner-entities-UntilFillingHoursAllocatorTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-resources-entities-ResourceTest.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-limitingresources-ILimitingResourceQueueModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-limitingresources-LimitingResourceQueueModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-limitingresources-QueueComponent.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-allocation-ResourceAllocationModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-chart-ChartFiller.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-order-PlanningStateCreator.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-order-SaveCommandBuilder.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-resourceload-ResourceLoadDisplayData.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-resourceload-ResourceLoadModel.java]]