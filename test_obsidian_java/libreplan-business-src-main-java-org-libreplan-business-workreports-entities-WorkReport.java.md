# libreplan-business/src/main/java/org/libreplan/business/workreports/entities/WorkReport.java

## Explanation
*No explanation provided in source code.*

## Metrics
**Extension:** `.java`
**Size:** 18410 bytes
**Centrality Score:** 0.0020

## Imports (Dependencies)
- [[libreplan-business-src-main-java-org-libreplan-business-common-IntegrationEntity.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-Registry.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-Util.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-entities-EntitySequence.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-entities-PersonalTimesheetsPeriodicityEnum.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-exceptions-InstanceNotFoundException.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-labels-entities-Label.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-labels-entities-LabelType.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-entities-OrderElement.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-entities-Resource.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-entities-Worker.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-workingday-EffortDuration.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-workreports-daos-IWorkReportDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-workreports-valueobjects-DescriptionField.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-workreports-valueobjects-DescriptionValue.java]]

## Imported By (Dependents)
- [[libreplan-business-src-main-java-org-libreplan-business-orders-daos-OrderElementDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-entities-SumChargedEffortRecalculator.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-reports-dtos-LabelFilterType.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-workreports-daos-IWorkReportDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-workreports-daos-IWorkReportLineDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-workreports-daos-WorkReportDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-workreports-daos-WorkReportLineDAO.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-planner-entities-MoneyCostCalculatorTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-workreports-daos-AbstractWorkReportTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-workreports-daos-WorkReportDAOTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-workreports-entities-WorkReportTest.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-importers-JiraTimesheetSynchronizer.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-importers-notifications-realization-SendEmailOnTimesheetDataMissing.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-common-converters-WorkReportConverter.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-costcategories-ITypeOfWorkHoursModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-materials-IMaterialsModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-orders-OrderPredicate.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-users-dashboard-IPersonalTimesheetModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-users-dashboard-IPersonalTimesheetsAreaModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-users-dashboard-PersonalTimesheetDTO.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-users-dashboard-PersonalTimesheetModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-users-dashboard-PersonalTimesheetsAreaModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-workreports-IWorkReportCRUDControllerEntryPoints.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-workreports-IWorkReportModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-workreports-IWorkReportTypeModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-workreports-WorkReportCRUDController.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-workreports-WorkReportDTO.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-workreports-WorkReportModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-workreports-WorkReportPredicate.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-workreports-WorkReportQueryController.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-workreports-WorkReportTypeModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-boundusers-impl-BoundUserServiceREST.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-workreports-api-WorkReportDTO.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-workreports-api-WorkReportListDTO.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-workreports-impl-WorkReportConverter.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-workreports-impl-WorkReportServiceREST.java]]
- [[libreplan-webapp-src-test-java-org-libreplan-web-orders-OrderElementTreeModelTest.java]]
- [[libreplan-webapp-src-test-java-org-libreplan-web-test-ws-workreports-WorkReportServiceTest.java]]