# libreplan-business/src/main/java/org/libreplan/business/workingday/IntraDayDate.java

## Explanation
*No explanation provided in source code.*

## Metrics
**Extension:** `.java`
**Size:** 18361 bytes
**Centrality Score:** 0.0057

## Imports (Dependencies)
- [[libreplan-business-src-main-java-org-libreplan-business-calendars-entities-Capacity.java]]

## Imported By (Dependents)
- [[libreplan-business-src-main-java-org-libreplan-business-calendars-entities-BaseCalendar.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-calendars-entities-ThereAreHoursOnWorkHoursCalculator.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-entities-OrderElement.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-AggregateOfResourceAllocations.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-GenericDayAssignmentsContainer.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-GenericResourceAllocation.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-IAllocatable.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-IDayAssignmentsContainer.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-ITaskPositionConstrained.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-ResourceAllocation.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-SpecificDayAssignmentsContainer.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-SpecificResourceAllocation.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-Task.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-TaskElement.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-TaskGroup.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-TaskMilestone.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-TaskPositionConstraint.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-allocationalgorithms-AllocatorForTaskDurationAndSpecifiedResourcesPerDay.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-allocationalgorithms-EffortModification.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-allocationalgorithms-ResourcesPerDayModification.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-allocationalgorithms-UntilFillingHoursAllocator.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-consolidations-CalculatedConsolidatedValue.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-consolidations-ConsolidatedValue.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-consolidations-NonCalculatedConsolidatedValue.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-limiting-entities-DateAndHour.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-limiting-entities-Gap.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-limiting-entities-InsertionRequirements.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-limiting-entities-LimitingResourceAllocator.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-limiting-entities-LimitingResourceQueueElement.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-entities-Resource.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-planner-daos-TaskElementDAOTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-planner-entities-DayAssignmentMatchers.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-planner-entities-GenericResourceAllocationTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-planner-entities-SpecificResourceAllocationTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-planner-entities-StretchesFunctionTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-planner-entities-TaskGroupTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-planner-entities-TaskTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-planner-entities-UntilFillingHoursAllocatorTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-workingday-IntraDayDateTest.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-importers-OrderImporterMPXJ.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-importers-notifications-realization-SendEmailOnTimesheetDataMissing.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-common-TemplateModelAdapter.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-limitingresources-LimitingResourceQueueModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-TaskElementAdapter.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-adaptplanning-AdaptPlanningCommand.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-allocation-AllocationResult.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-allocation-FormBinder.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-consolidations-AdvanceConsolidationModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-order-SaveCommandBuilder.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-order-SubcontractModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-reassign-ReassignConfiguration.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-taskedition-AdvancedAllocationTaskController.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-taskedition-TaskPropertiesController.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-resourceload-LoadPeriodGenerator.java]]
- [[libreplan-webapp-src-test-java-org-libreplan-web-test-ws-email-EmailTest.java]]