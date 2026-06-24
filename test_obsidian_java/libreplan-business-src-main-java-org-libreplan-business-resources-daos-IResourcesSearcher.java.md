# libreplan-business/src/main/java/org/libreplan/business/resources/daos/IResourcesSearcher.java

## Explanation
*No explanation provided in source code.*

## Metrics
**Extension:** `.java`
**Size:** 4096 bytes
**Centrality Score:** 0.0020

## Imports (Dependencies)
- [[libreplan-business-src-main-java-org-libreplan-business-resources-entities-Criterion.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-entities-CriterionType.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-entities-Machine.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-entities-Resource.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-entities-ResourceEnum.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-entities-ResourceType.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-entities-Worker.java]]

## Imported By (Dependents)
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-GenericResourceAllocation.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-ResourceAllocation.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-SpecificResourceAllocation.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-Task.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-TaskElement.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-TaskGroup.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-TaskMilestone.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-allocationalgorithms-AllocationModification.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-allocationalgorithms-EffortModification.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-planner-entities-allocationalgorithms-ResourcesPerDayModification.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-resources-daos-ResourceDAOTest.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-common-TemplateModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-common-TemplateModelAdapter.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-common-components-NewAllocationSelector.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-TaskElementAdapter.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-allocation-AllocationRow.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-allocation-GenericAllocationRow.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-allocation-ResourceAllocationModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-reassign-ReassignCommand.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-tabs-CriticalPathBuilder.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-tabs-DashboardTabCreator.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-tabs-MonteCarloTabCreator.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-planner-tabs-MultipleTabsPlannerController.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-resourceload-LoadPeriodGenerator.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-resourceload-ResourceLoadController.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-resourceload-ResourceLoadModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-resources-search-AllocationSelectorController.java]]