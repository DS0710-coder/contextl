# libreplan-business/src/main/java/org/libreplan/business/resources/daos/ICriterionTypeDAO.java

## Explanation
*No explanation provided in source code.*

## Metrics
**Extension:** `.java`
**Size:** 3411 bytes
**Centrality Score:** 0.0016

## Imports (Dependencies)
- [[libreplan-business-src-main-java-org-libreplan-business-common-daos-IIntegrationEntityDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-exceptions-InstanceNotFoundException.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-entities-CriterionType.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-entities-PredefinedCriterionTypes.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-entities-ResourceEnum.java]]

## Imported By (Dependents)
- [[libreplan-business-src-main-java-org-libreplan-business-common-Registry.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-hibernate-notification-PredefinedDatabaseSnapshots.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-bootstrap-CriterionsBootstrap.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-entities-CriterionSatisfaction.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-entities-CriterionType.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-orders-daos-OrderElementDAOTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-resources-bootstrap-CriterionsBootstrapTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-resources-daos-CriterionDAOTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-resources-daos-CriterionSatisfactionDAOTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-resources-daos-CriterionTypeDAOTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-resources-daos-MachineDAOTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-resources-daos-ResourceDAOTest.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-orders-OrderElementModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-orders-OrderModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-reassign-ReassignCommand.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-reports-CompletedEstimatedHoursPerTaskModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-reports-HoursWorkedPerWorkerModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-reports-OrderCostsPerResourceModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-reports-WorkingArrangementsPerOrderModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-reports-WorkingProgressPerTaskModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-resources-criterion-CriterionsModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-resources-machine-AssignedMachineCriterionsModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-resources-worker-AssignedCriterionsModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-templates-OrderTemplatesModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-resources-criterion-impl-CriterionServiceREST.java]]
- [[libreplan-webapp-src-test-java-org-libreplan-web-orders-OrderElementTreeModelTest.java]]
- [[libreplan-webapp-src-test-java-org-libreplan-web-orders-OrderModelTest.java]]
- [[libreplan-webapp-src-test-java-org-libreplan-web-resources-CriterionModelTest.java]]
- [[libreplan-webapp-src-test-java-org-libreplan-web-test-ws-orders-OrderElementServiceTest.java]]
- [[libreplan-webapp-src-test-java-org-libreplan-web-test-ws-resources-api-ResourceServiceTest.java]]
- [[libreplan-webapp-src-test-java-org-libreplan-web-test-ws-resources-criterion-api-CriterionServiceTest.java]]