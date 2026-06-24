# libreplan-business/src/main/java/org/libreplan/business/IDataBootstrap.java

## Explanation
*No explanation provided in source code.*

## Metrics
**Extension:** `.java`
**Size:** 1000 bytes
**Centrality Score:** 0.0039

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[libreplan-business-src-main-java-org-libreplan-business-advance-bootstrap-DefaultAdvanceTypesBootstrapListener.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-calendars-entities-ICalendarBootstrap.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-entities-IConfigurationBootstrap.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-entities-IConfigurationTypeOfWorkHoursBootstrap.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-entities-IConnectorBootstrap.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-costcategories-entities-ITypeOfWorkHoursBootstrap.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-labels-entities-ILabelBootstrap.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-materials-bootstrap-IMaterialCategoryBootstrap.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-materials-bootstrap-UnitTypeBootstrap.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-bootstrap-ICriterionsBootstrap.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-scenarios-bootstrap-IScenariosBootstrap.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-users-bootstrap-IProfileBootstrap.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-workreports-entities-IWorkReportTypeBootstrap.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-advance-bootstrap-DefaultAdvanceTypesBootstrapListenerTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-calendars-daos-BaseCalendarDAOTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-externalcompanies-daos-ExternalCompanyDAOTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-materials-daos-MaterialAssignmentDAOTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-materials-daos-MaterialDAOTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-orders-daos-OrderElementDAOTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-orders-entities-AddAdvanceAssignmentsToOrderElementTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-orders-entities-OrderElementTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-orders-entities-OrderLineTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-orders-entities-OrderTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-planner-daos-TaskElementDAOTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-planner-entities-MoneyCostCalculatorTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-planner-entities-TaskElementTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-planner-entities-TaskTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-resources-bootstrap-CriterionsBootstrapTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-resources-daos-CriterionSatisfactionDAOTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-resources-daos-MachineDAOTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-resources-daos-ResourceDAOTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-scenarios-bootstrap-ScenariosBootstrapTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-scenarios-daos-ScenarioDAOTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-scenarios-entities-ScenarioTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-users-daos-OrderAuthorizationDAOTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-workreports-daos-WorkReportLineDAOTest.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-bootstrap-BootstrapListener.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-users-bootstrap-IUsersBootstrapInDB.java]]
- [[libreplan-webapp-src-test-java-org-libreplan-importers-ExportTimesheetsToTimTest.java]]
- [[libreplan-webapp-src-test-java-org-libreplan-importers-ImportRosterFromTimTest.java]]
- [[libreplan-webapp-src-test-java-org-libreplan-importers-JiraOrderElementSynchronizerTest.java]]
- [[libreplan-webapp-src-test-java-org-libreplan-importers-JiraTimesheetSynchronizerTest.java]]
- [[libreplan-webapp-src-test-java-org-libreplan-web-calendars-BaseCalendarModelTest.java]]
- [[libreplan-webapp-src-test-java-org-libreplan-web-orders-OrderElementTreeModelTest.java]]
- [[libreplan-webapp-src-test-java-org-libreplan-web-orders-OrderModelTest.java]]
- [[libreplan-webapp-src-test-java-org-libreplan-web-planner-chart-ChartFillerTest.java]]
- [[libreplan-webapp-src-test-java-org-libreplan-web-scenarios-ScenarioModelTest.java]]
- [[libreplan-webapp-src-test-java-org-libreplan-web-scenarios-TransferOrdersModelTest.java]]
- [[libreplan-webapp-src-test-java-org-libreplan-web-test-ws-materials-MaterialServiceTest.java]]
- [[libreplan-webapp-src-test-java-org-libreplan-web-test-ws-orders-OrderElementServiceTest.java]]
- [[libreplan-webapp-src-test-java-org-libreplan-web-test-ws-subcontract-ReportAdvancesServiceTest.java]]
- [[libreplan-webapp-src-test-java-org-libreplan-web-test-ws-subcontract-SubcontractServiceTest.java]]
- [[libreplan-webapp-src-test-java-org-libreplan-web-test-ws-unittypes-UnitTypeServiceTest.java]]
- [[libreplan-webapp-src-test-java-org-libreplan-web-test-ws-workreports-WorkReportServiceTest.java]]