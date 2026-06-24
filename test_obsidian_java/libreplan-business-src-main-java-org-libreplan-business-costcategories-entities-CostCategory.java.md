# libreplan-business/src/main/java/org/libreplan/business/costcategories/entities/CostCategory.java

## Explanation
*No explanation provided in source code.*

## Metrics
**Extension:** `.java`
**Size:** 15225 bytes
**Centrality Score:** 0.0041

## Imports (Dependencies)
- [[libreplan-business-src-main-java-org-libreplan-business-common-IHumanIdentifiable.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-IntegrationEntity.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-Registry.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-entities-EntitySequence.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-exceptions-InstanceNotFoundException.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-exceptions-ValidationException.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-costcategories-daos-ICostCategoryDAO.java]]

## Imported By (Dependents)
- [[libreplan-business-src-main-java-org-libreplan-business-costcategories-daos-CostCategoryDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-costcategories-daos-HourCostDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-costcategories-daos-ICostCategoryDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-costcategories-daos-IHourCostDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-costcategories-daos-IResourcesCostCategoryAssignmentDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-costcategories-daos-ResourcesCostCategoryAssignmentDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-hibernate-notification-PredefinedDatabaseSnapshots.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-entities-OrderElement.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-daos-CriterionDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-daos-ICriterionDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-entities-Criterion.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-entities-Resource.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-costcategories-daos-CostCategoryDAOTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-costcategories-daos-HourCostDAOTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-costcategories-daos-ResourcesCostCategoryAssignmentDAOTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-planner-entities-MoneyCostCalculatorTest.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-common-components-finders-CostCategoryFinder.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-common-components-finders-ResourcesMultipleFiltersFinder.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-costcategories-CostCategoryCRUDController.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-costcategories-CostCategoryModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-costcategories-ICostCategoryModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-costcategories-ResourcesCostCategoryAssignmentController.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-costcategories-ResourcesCostCategoryAssignmentModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-orders-OrderElementModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-resources-criterion-CriterionTreeController.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-resources-search-ResourcePredicate.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-costcategories-api-CostCategoryDTO.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-costcategories-impl-CostCategoryConverter.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-costcategories-impl-CostCategoryServiceREST.java]]
- [[libreplan-webapp-src-test-java-org-libreplan-web-test-ws-costcategories-CostCategoryServiceTest.java]]
- [[libreplan-webapp-src-test-java-org-libreplan-web-test-ws-resources-api-ResourceServiceTest.java]]