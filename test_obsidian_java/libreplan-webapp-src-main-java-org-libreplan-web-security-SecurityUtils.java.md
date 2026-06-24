# libreplan-webapp/src/main/java/org/libreplan/web/security/SecurityUtils.java

## Explanation
*No explanation provided in source code.*

## Metrics
**Extension:** `.java`
**Size:** 6577 bytes
**Centrality Score:** 0.0011

## Imports (Dependencies)
- [[libreplan-business-src-main-java-org-libreplan-business-common-Registry.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-exceptions-InstanceNotFoundException.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-entities-Order.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-users-entities-OrderAuthorization.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-users-entities-OrderAuthorizationType.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-users-entities-User.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-users-entities-UserRole.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-users-services-CustomUser.java]]

## Imported By (Dependents)
- [[libreplan-webapp-src-main-java-org-libreplan-web-StartupApplicationListener.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-UserUtil.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-common-ConfigurationController.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-common-CustomMenuController.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-common-IndexController.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-common-TemplateController.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-common-TemplateModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-expensesheet-ExpenseSheetCRUDController.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-limitingresources-LimitingResourceQueueModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-logs-IssueLogModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-logs-RiskLogModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-orders-OrderCRUDController.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-orders-OrderElementTreeController.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-orders-OrderModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-orders-files-OrderFilesController.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-orders-labels-AssignedLabelsController.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-company-CompanyPlanningController.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-company-CompanyPlanningModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-order-OrderPlanningModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-order-SaveCommandBuilder.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-tabs-LimitingResourcesTabCreator.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-tabs-LogsTabCreator.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-tabs-MultipleTabsPlannerController.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-tabs-OrdersTabCreator.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-tabs-PlanningTabCreator.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-tabs-ResourcesLoadTabCreator.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-reports-CompletedEstimatedHoursPerTaskModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-reports-OrderCostsPerResourceModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-reports-ProjectStatusReportModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-reports-SchedulingProgressPerOrderModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-reports-TimeLineRequiredMaterialModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-reports-WorkingArrangementsPerOrderModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-reports-WorkingProgressPerTaskModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-resourceload-ResourceLoadController.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-resourceload-ResourceLoadModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-resources-worker-WorkerCRUDController.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-scenarios-CurrentUserScenarioAwareManager.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-scenarios-ScenarioCRUDController.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-templates-historicalAssignment-OrderElementHistoricalAssignmentComponent.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-users-OrderAuthorizationModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-users-UserCRUDController.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-users-dashboard-PersonalTimesheetController.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-users-settings-PasswordModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-users-settings-SettingsModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-workreports-WorkReportCRUDController.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-workreports-WorkReportQueryController.java]]