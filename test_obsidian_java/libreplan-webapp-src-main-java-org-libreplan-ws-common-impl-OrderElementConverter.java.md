# libreplan-webapp/src/main/java/org/libreplan/ws/common/impl/OrderElementConverter.java

## Explanation
*No explanation provided in source code.*

## Metrics
**Extension:** `.java`
**Size:** 36315 bytes
**Centrality Score:** 0.0003

## Imports (Dependencies)
- [[libreplan-business-src-main-java-org-libreplan-business-advance-entities-AdvanceMeasurement.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-advance-entities-DirectAdvanceAssignment.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-advance-exceptions-DuplicateAdvanceAssignmentForOrderElementException.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-advance-exceptions-DuplicateValueTrueReportGlobalAdvanceException.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-calendars-entities-BaseCalendar.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-Registry.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-exceptions-InstanceNotFoundException.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-exceptions-ValidationException.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-externalcompanies-entities-EndDateCommunication.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-labels-entities-Label.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-materials-bootstrap-PredefinedMaterialCategories.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-materials-entities-Material.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-materials-entities-MaterialAssignment.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-materials-entities-MaterialCategory.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-daos-IHoursGroupDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-entities-HoursGroup.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-entities-ICriterionRequirable.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-entities-Order.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-entities-OrderElement.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-entities-OrderLine.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-entities-OrderLineGroup.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-requirements-entities-CriterionRequirement.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-requirements-entities-DirectCriterionRequirement.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-requirements-entities-IndirectCriterionRequirement.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-entities-Criterion.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-entities-ResourceEnum.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-scenarios-entities-OrderVersion.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-scenarios-entities-Scenario.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-common-api-AdvanceMeasurementDTO.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-common-api-CriterionRequirementDTO.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-common-api-DirectCriterionRequirementDTO.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-common-api-HoursGroupDTO.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-common-api-IndirectCriterionRequirementDTO.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-common-api-LabelReferenceDTO.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-common-api-MaterialAssignmentDTO.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-common-api-OrderDTO.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-common-api-OrderElementDTO.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-common-api-OrderLineDTO.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-common-api-OrderLineGroupDTO.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-common-api-ResourceEnumDTO.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-subcontract-api-EndDateCommunicationToCustomerDTO.java]]

## Imported By (Dependents)
- [[libreplan-webapp-src-main-java-org-libreplan-web-subcontract-ReportAdvancesModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-subcontract-SubcontractedTasksModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-orders-impl-OrderElementServiceREST.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-subcontract-impl-ReportAdvancesServiceREST.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-subcontract-impl-SubcontractServiceREST.java]]