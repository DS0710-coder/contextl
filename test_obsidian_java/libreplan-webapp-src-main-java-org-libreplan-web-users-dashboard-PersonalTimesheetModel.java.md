# libreplan-webapp/src/main/java/org/libreplan/web/users/dashboard/PersonalTimesheetModel.java

## Explanation
*No explanation provided in source code.*

## Metrics
**Extension:** `.java`
**Size:** 22256 bytes
**Centrality Score:** 0.0002

## Imports (Dependencies)
- [[libreplan-business-src-main-java-org-libreplan-business-calendars-entities-ResourceCalendar.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-daos-IConfigurationDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-daos-IEntitySequenceDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-entities-EntityNameEnum.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-entities-PersonalTimesheetsPeriodicityEnum.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-exceptions-InstanceNotFoundException.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-costcategories-entities-TypeOfWorkHours.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-daos-IOrderDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-daos-ISumChargedEffortDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-entities-Order.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-entities-OrderElement.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-daos-IResourceAllocationDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-SpecificResourceAllocation.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-entities-Resource.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-entities-Worker.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-scenarios-IScenarioManager.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-users-daos-IUserDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-users-entities-User.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-workingday-EffortDuration.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-workreports-daos-IWorkReportDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-workreports-daos-IWorkReportLineDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-workreports-daos-IWorkReportTypeDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-workreports-entities-PredefinedWorkReportTypes.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-workreports-entities-WorkReport.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-workreports-entities-WorkReportLine.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-workreports-entities-WorkReportType.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-UserUtil.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-calendars-BaseCalendarModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-common-Util.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-common-concurrentdetection-OnConcurrentModification.java]]

## Imported By (Dependents)
*Not imported by any file*