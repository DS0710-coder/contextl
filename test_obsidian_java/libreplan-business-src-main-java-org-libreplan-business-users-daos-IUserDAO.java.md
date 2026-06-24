# libreplan-business/src/main/java/org/libreplan/business/users/daos/IUserDAO.java

## Explanation
*No explanation provided in source code.*

## Metrics
**Extension:** `.java`
**Size:** 3585 bytes
**Centrality Score:** 0.0023

## Imports (Dependencies)
- [[libreplan-business-src-main-java-org-libreplan-business-common-daos-IGenericDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-exceptions-InstanceNotFoundException.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-entities-Worker.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-scenarios-entities-Scenario.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-users-entities-OrderAuthorization.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-users-entities-User.java]]

## Imported By (Dependents)
- [[libreplan-business-src-main-java-org-libreplan-business-common-Registry.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-daos-OrderDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-entities-Worker.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-users-entities-User.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-externalcompanies-daos-ExternalCompanyDAOTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-resources-daos-ResourceDAOTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-users-daos-OrderAuthorizationDAOTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-users-daos-UserDAOTest.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-importers-notifications-realization-SendEmailOnMilestoneReached.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-StartupApplicationListener.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-common-GatheredUsageStats.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-common-TemplateModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-common-components-finders-UserBandboxFinder.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-common-components-finders-UserFinder.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-common-converters-UserConverter.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-limitingresources-LimitingResourceQueueModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-logs-IssueLogModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-logs-RiskLogModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-orders-OrderModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-orders-files-OrderFilesController.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-company-CompanyPlanningModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-order-OrderPlanningModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-resourceload-ResourceLoadModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-resources-worker-WorkerModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-scenarios-ScenarioModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-users-OrderAuthorizationModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-users-UserModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-users-bootstrap-UsersBootstrapInDB.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-users-dashboard-PersonalTimesheetModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-users-services-DBUserDetailsService.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-users-services-LDAPCustomAuthenticationProvider.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-users-services-LDAPUserDetailsService.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-users-settings-PasswordModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-users-settings-SettingsModel.java]]
- [[libreplan-webapp-src-test-java-org-libreplan-web-orders-OrderFilesTest.java]]
- [[libreplan-webapp-src-test-java-org-libreplan-web-test-users-bootstrap-UsersBootstrapInDBTest.java]]
- [[libreplan-webapp-src-test-java-org-libreplan-web-test-users-services-DBPasswordEncoderServiceTest.java]]
- [[libreplan-webapp-src-test-java-org-libreplan-web-test-ws-email-EmailTest.java]]