# libreplan-business/src/main/java/org/libreplan/business/common/daos/IIntegrationEntityDAO.java

## Explanation
*No explanation provided in source code.*

## Metrics
**Extension:** `.java`
**Size:** 2475 bytes
**Centrality Score:** 0.0192

## Imports (Dependencies)
- [[libreplan-business-src-main-java-org-libreplan-business-common-IntegrationEntity.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-exceptions-InstanceNotFoundException.java]]

## Imported By (Dependents)
- [[libreplan-business-src-main-java-org-libreplan-business-calendars-daos-IBaseCalendarDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-calendars-daos-ICalendarAvailabilityDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-calendars-daos-ICalendarDataDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-calendars-daos-ICalendarExceptionDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-calendars-daos-ICalendarExceptionTypeDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-IntegrationEntity.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-entities-EntityNameEnum.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-costcategories-daos-ICostCategoryDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-costcategories-daos-IHourCostDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-costcategories-daos-IResourcesCostCategoryAssignmentDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-costcategories-daos-ITypeOfWorkHoursDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-expensesheet-daos-IExpenseSheetDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-expensesheet-daos-IExpenseSheetLineDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-expensesheet-entities-ExpenseSheetLine.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-labels-daos-ILabelDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-labels-daos-ILabelTypeDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-logs-daos-IIssueLogDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-logs-daos-IProjectLogDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-logs-daos-IRiskLogDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-logs-entities-IssueLog.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-logs-entities-ProjectLog.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-logs-entities-RiskLog.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-materials-daos-IMaterialCategoryDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-materials-daos-IMaterialDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-materials-daos-IUnitTypeDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-daos-IHoursGroupDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-daos-IOrderDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-daos-IOrderElementDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-entities-HoursGroup.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-entities-OrderElement.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-daos-ICriterionDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-daos-ICriterionSatisfactionDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-daos-ICriterionTypeDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-daos-IMachineDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-daos-IResourceDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-daos-IWorkerDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-workreports-daos-IWorkReportDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-workreports-daos-IWorkReportLineDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-workreports-daos-IWorkReportTypeDAO.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-calendarexceptiontypes-impl-CalendarExceptionTypeServiceREST.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-common-impl-GenericRESTService.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-costcategories-impl-CostCategoryServiceREST.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-expensesheets-impl-ExpenseSheetServiceREST.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-labels-impl-LabelServiceREST.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-materials-impl-MaterialServiceREST.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-orders-impl-OrderElementServiceREST.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-resources-criterion-impl-CriterionServiceREST.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-resources-impl-ResourceServiceREST.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-typeofworkhours-impl-TypeOfWorkHoursServiceREST.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-unittypes-impl-UnitTypeServiceREST.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-workreports-impl-WorkReportServiceREST.java]]
- [[libreplan-webapp-src-test-java-org-libreplan-web-test-ws-workreports-WorkReportServiceTest.java]]