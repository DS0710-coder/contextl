# libreplan-webapp/src/main/java/org/libreplan/ws/common/impl/GenericRESTService.java

## Explanation
*No explanation provided in source code.*

## Metrics
**Extension:** `.java`
**Size:** 8401 bytes
**Centrality Score:** 0.0005

## Imports (Dependencies)
- [[libreplan-business-src-main-java-org-libreplan-business-common-IAdHocTransactionService.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-IOnTransaction.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-IntegrationEntity.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-daos-IIntegrationEntityDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-exceptions-InstanceNotFoundException.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-exceptions-ValidationException.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-common-api-InstanceConstraintViolationsDTO.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-common-api-InstanceConstraintViolationsListDTO.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-common-api-IntegrationEntityDTO.java]]

## Imported By (Dependents)
- [[libreplan-webapp-src-main-java-org-libreplan-ws-calendarexceptiontypes-impl-CalendarExceptionTypeServiceREST.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-calendars-impl-CalendarServiceREST.java]]
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