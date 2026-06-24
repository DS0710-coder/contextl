# libreplan-webapp/src/main/java/org/libreplan/web/orders/OrderModel.java

## Explanation
*No explanation provided in source code.*

## Metrics
**Extension:** `.java`
**Size:** 33881 bytes
**Centrality Score:** 0.0002

## Imports (Dependencies)
- [[ganttzk-src-main-java-org-zkoss-ganttz-IPredicate.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-advance-entities-AdvanceMeasurement.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-advance-entities-DirectAdvanceAssignment.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-advance-entities-IndirectAdvanceAssignment.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-calendars-daos-IBaseCalendarDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-calendars-entities-BaseCalendar.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-IntegrationEntity.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-daos-IConfigurationDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-entities-Configuration.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-entities-EntityNameEnum.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-exceptions-InstanceNotFoundException.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-email-entities-EmailNotification.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-externalcompanies-daos-IExternalCompanyDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-externalcompanies-entities-EndDateCommunication.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-externalcompanies-entities-ExternalCompany.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-labels-daos-ILabelDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-labels-entities-Label.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-daos-IOrderDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-daos-IOrderElementDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-entities-HoursGroup.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-entities-Order.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-entities-OrderElement.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-entities-OrderLineGroup.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-entities-OrderStatusEnum.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-PositionConstraintType.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-TaskElement.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-qualityforms-daos-IQualityFormDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-qualityforms-entities-QualityForm.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-requirements-entities-DirectCriterionRequirement.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-daos-ICriterionDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-daos-ICriterionTypeDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-entities-Criterion.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-entities-CriterionType.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-scenarios-IScenarioManager.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-scenarios-daos-IOrderVersionDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-scenarios-daos-IScenarioDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-scenarios-entities-OrderVersion.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-scenarios-entities-Scenario.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-templates-daos-IOrderElementTemplateDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-templates-entities-OrderElementTemplate.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-templates-entities-OrderTemplate.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-users-daos-IOrderAuthorizationDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-users-daos-IUserDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-users-entities-OrderAuthorization.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-users-entities-OrderAuthorizationType.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-users-entities-User.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-users-entities-UserRole.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-calendars-BaseCalendarModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-common-IntegrationEntityModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-common-concurrentdetection-OnConcurrentModification.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-email-IEmailNotificationModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-logs-IIssueLogModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-logs-IRiskLogModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-orders-files-IOrderFileModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-orders-labels-LabelsOnConversation.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-order-PlanningStateCreator.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-security-SecurityUtils.java]]

## Imported By (Dependents)
*Not imported by any file*