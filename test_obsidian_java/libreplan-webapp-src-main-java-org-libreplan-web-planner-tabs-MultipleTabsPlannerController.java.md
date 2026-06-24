# libreplan-webapp/src/main/java/org/libreplan/web/planner/tabs/MultipleTabsPlannerController.java

## Explanation
*No explanation provided in source code.*

## Metrics
**Extension:** `.java`
**Size:** 20526 bytes
**Centrality Score:** 0.0003

## Imports (Dependencies)
- [[ganttzk-src-main-java-org-zkoss-ganttz-TabSwitcher.java]]
- [[ganttzk-src-main-java-org-zkoss-ganttz-TabsRegistry.java]]
- [[ganttzk-src-main-java-org-zkoss-ganttz-adapters-State.java]]
- [[ganttzk-src-main-java-org-zkoss-ganttz-adapters-TabsConfiguration.java]]
- [[ganttzk-src-main-java-org-zkoss-ganttz-extensions-ITab.java]]
- [[ganttzk-src-main-java-org-zkoss-ganttz-extensions-TabProxy.java]]
- [[ganttzk-src-main-java-org-zkoss-ganttz-util-LongOperationFeedback.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-IAdHocTransactionService.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-daos-IConfigurationDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-daos-IOrderDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-entities-Order.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-entities-OrderElement.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-TaskElement.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-daos-IResourcesSearcher.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-templates-entities-OrderTemplate.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-users-entities-UserRole.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-common-ConfirmCloseUtil.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-common-GatheredUsageStats.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-common-entrypoints-EntryPointsHandler.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-common-entrypoints-URLHandlerRegistry.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-dashboard-DashboardController.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-dashboard-DashboardControllerGlobal.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-limitingresources-LimitingResourcesController.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-logs-LogsController.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-montecarlo-MonteCarloController.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-orders-OrderCRUDController.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-company-CompanyPlanningController.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-order-IOrderPlanningGate.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-order-OrderPlanningController.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-order-PlanningStateCreator.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-resourceload-ResourceLoadController.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-security-SecurityUtils.java]]

## Imported By (Dependents)
- [[libreplan-webapp-src-main-java-org-libreplan-importers-notifications-ComposeMessage.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-orders-ProjectDetailsController.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-company-CompanyPlanningController.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-company-CompanyPlanningModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-company-ICompanyPlanningModel.java]]