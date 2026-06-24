# libreplan-business/src/main/java/org/libreplan/business/planner/entities/GenericResourceAllocation.java

## Explanation
*No explanation provided in source code.*

## Metrics
**Extension:** `.java`
**Size:** 13704 bytes
**Centrality Score:** 0.0020

## Imports (Dependencies)
- [[libreplan-business-src-main-java-org-libreplan-business-calendars-entities-AvailabilityTimeLine.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-calendars-entities-Capacity.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-calendars-entities-ICalendar.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-allocationalgorithms-ResourcesPerDayModification.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-daos-IResourcesSearcher.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-entities-Criterion.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-entities-CriterionCompounder.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-entities-ICriterion.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-entities-Resource.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-entities-ResourceEnum.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-scenarios-entities-Scenario.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-util-deepcopy-OnCopy.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-util-deepcopy-Strategy.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-workingday-EffortDuration.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-workingday-IntraDayDate.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-workingday-ResourcesPerDay.java]]

## Imported By (Dependents)
- [[libreplan-business-src-main-java-org-libreplan-business-hibernate-notification-PredefinedDatabaseSnapshots.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-daos-IResourceAllocationDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-daos-ResourceAllocationDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-allocationalgorithms-EffortModification.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-allocationalgorithms-ResourcesPerDayModification.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-limiting-entities-AllocationSpec.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-limiting-entities-LimitingResourceAllocator.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-limiting-entities-LimitingResourceQueueElement.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-entities-Criterion.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-planner-daos-ResourceAllocationDAOTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-planner-entities-DerivedAllocationTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-planner-entities-GenericResourceAllocationTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-planner-entities-UntilFillingHoursAllocatorTest.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-limitingresources-LimitingResourceQueueModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-limitingresources-LimitingResourcesController.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-limitingresources-QueueComponent.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-limitingresources-QueuesState.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-TaskElementAdapter.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-TaskElementPredicate.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-TaskGroupPredicate.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-allocation-AdvancedAllocationController.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-allocation-AllocationResult.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-allocation-AllocationRow.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-allocation-GenericAllocationRow.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-limiting-allocation-LimitingAllocationRow.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-limiting-allocation-LimitingResourceAllocationModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-order-PlanningStateCreator.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-reassign-ReassignCommand.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-resourceload-ResourceLoadModel.java]]