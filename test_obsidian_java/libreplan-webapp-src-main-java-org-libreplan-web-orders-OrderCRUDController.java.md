# libreplan-webapp/src/main/java/org/libreplan/web/orders/OrderCRUDController.java

## Explanation
*No explanation provided in source code.*

## Metrics
**Extension:** `.java`
**Size:** 67123 bytes
**Centrality Score:** 0.0003

## Imports (Dependencies)
- [[ganttzk-src-main-java-org-zkoss-ganttz-util-LongOperationFeedback.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-calendars-entities-BaseCalendar.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-Configuration.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-Registry.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-exceptions-InstanceNotFoundException.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-externalcompanies-entities-DeadlineCommunication.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-externalcompanies-entities-DeliverDateComparator.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-externalcompanies-entities-EndDateCommunication.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-externalcompanies-entities-ExternalCompany.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-daos-IOrderDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-entities-Order.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-entities-OrderElement.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-entities-OrderStatusEnum.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-PositionConstraintType.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-entities-Criterion.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-templates-entities-OrderTemplate.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-users-entities-User.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-users-entities-UserRole.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-common-ConfirmCloseUtil.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-common-FilterUtils.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-common-IMessagesForUser.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-common-Level.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-common-MessagesForUser.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-common-OnlyOneVisible.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-common-Util.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-common-components-bandboxsearch-BandboxMultipleSearch.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-common-components-bandboxsearch-BandboxSearch.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-common-components-finders-FilterPair.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-common-components-finders-OrderFilterEnum.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-common-components-finders-TaskGroupFilterEnum.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-orders-criterionrequirements-AssignedCriterionRequirementToOrderElementController.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-orders-criterionrequirements-OrderElementCriterionRequirementComponent.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-orders-files-OrderFilesController.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-orders-labels-AssignedLabelsToOrderElementController.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-orders-labels-LabelsAssignmentToOrderElementComponent.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-orders-materials-AssignedMaterialsToOrderElementController.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-orders-materials-OrderElementMaterialAssignmentsComponent.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-order-IOrderPlanningGate.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-security-SecurityUtils.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-templates-IOrderTemplatesControllerEntryPoints.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-tree-TreeComponent.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-users-OrderAuthorizationController.java]]

## Imported By (Dependents)
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-order-OrderPlanningController.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-tabs-MultipleTabsPlannerController.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-tabs-OrdersTabCreator.java]]