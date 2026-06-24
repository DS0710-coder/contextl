# libreplan-webapp/src/main/java/org/libreplan/web/limitingresources/LimitingResourceQueueModel.java

## Explanation
*No explanation provided in source code.*

## Metrics
**Extension:** `.java`
**Size:** 47556 bytes
**Centrality Score:** 0.0002

## Imports (Dependencies)
- [[ganttzk-src-main-java-org-zkoss-ganttz-timetracker-zoom-ZoomLevel.java]]
- [[ganttzk-src-main-java-org-zkoss-ganttz-util-Interval.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-calendars-entities-BaseCalendar.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-calendars-entities-CalendarAvailability.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-calendars-entities-CalendarData.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-calendars-entities-CalendarException.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-exceptions-InstanceNotFoundException.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-daos-IOrderDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-entities-HoursGroup.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-entities-Order.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-entities-OrderElement.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-entities-TaskSource.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-daos-IDependencyDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-daos-ITaskElementDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-DayAssignment.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-Dependency.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-GenericResourceAllocation.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-ResourceAllocation.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-Task.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-TaskElement.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-limiting-daos-ILimitingResourceQueueDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-limiting-daos-ILimitingResourceQueueDependencyDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-limiting-daos-ILimitingResourceQueueElementDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-limiting-entities-AllocationSpec.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-limiting-entities-DateAndHour.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-limiting-entities-Gap.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-limiting-entities-InsertionRequirements.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-limiting-entities-LimitingResourceAllocator.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-limiting-entities-LimitingResourceQueueDependency.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-limiting-entities-LimitingResourceQueueElement.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-entities-Criterion.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-entities-CriterionSatisfaction.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-entities-LimitingResourceQueue.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-entities-Resource.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-scenarios-bootstrap-PredefinedScenarios.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-scenarios-entities-Scenario.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-users-daos-IOrderAuthorizationDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-users-daos-IUserDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-users-entities-OrderAuthorization.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-users-entities-OrderAuthorizationType.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-users-entities-User.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-users-entities-UserRole.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-workingday-EffortDuration.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-workingday-IntraDayDate.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-common-concurrentdetection-OnConcurrentModification.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-order-SaveCommandBuilder.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-security-SecurityUtils.java]]

## Imported By (Dependents)
*Not imported by any file*