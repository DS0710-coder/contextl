# libreplan-webapp/src/test/java/org/libreplan/web/test/ws/orders/OrderElementServiceTest.java

## Explanation
*No explanation provided in source code.*

## Metrics
**Extension:** `.java`
**Size:** 79570 bytes
**Centrality Score:** 0.0002

## Imports (Dependencies)
- [[libreplan-business-src-main-java-org-libreplan-business-IDataBootstrap.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-advance-entities-AdvanceMeasurement.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-advance-entities-DirectAdvanceAssignment.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-IAdHocTransactionService.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-IOnTransaction.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-exceptions-InstanceNotFoundException.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-labels-daos-ILabelTypeDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-labels-entities-Label.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-labels-entities-LabelType.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-materials-entities-MaterialAssignment.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-daos-IOrderDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-daos-IOrderElementDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-entities-HoursGroup.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-entities-OrderElement.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-orders-entities-OrderLine.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-requirements-entities-CriterionRequirement.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-requirements-entities-DirectCriterionRequirement.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-daos-ICriterionTypeDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-daos-IResourceDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-entities-PredefinedCriterionTypes.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-entities-ResourceEnum.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-scenarios-bootstrap-IScenariosBootstrap.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-workreports-daos-IWorkReportDAO.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-common-api-AdvanceMeasurementDTO.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-common-api-ConstraintViolationDTO.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-common-api-CriterionRequirementDTO.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-common-api-DirectCriterionRequirementDTO.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-common-api-HoursGroupDTO.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-common-api-IncompatibleTypeException.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-common-api-IndirectCriterionRequirementDTO.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-common-api-InstanceConstraintViolationsDTO.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-common-api-LabelReferenceDTO.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-common-api-MaterialAssignmentDTO.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-common-api-OrderDTO.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-common-api-OrderLineDTO.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-common-api-OrderLineGroupDTO.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-common-api-ResourceEnumDTO.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-common-impl-DateConverter.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-orders-api-IOrderElementService.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-orders-api-OrderListDTO.java]]
- [[libreplan-webapp-src-test-java-org-libreplan-web-orders-OrderElementTreeModelTest.java]]

## Imported By (Dependents)
*Not imported by any file*