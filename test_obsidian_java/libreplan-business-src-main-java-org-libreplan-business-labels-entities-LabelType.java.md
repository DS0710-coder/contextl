# libreplan-business/src/main/java/org/libreplan/business/labels/entities/LabelType.java

## Explanation
*No explanation provided in source code.*

## Metrics
**Extension:** `.java`
**Size:** 6363 bytes
**Centrality Score:** 0.0033

## Imports (Dependencies)
- [[libreplan-business-src-main-java-org-libreplan-business-common-IHumanIdentifiable.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-IntegrationEntity.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-Registry.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-entities-EntitySequence.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-exceptions-InstanceNotFoundException.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-labels-daos-ILabelTypeDAO.java]]

## Imported By (Dependents)
- [[libreplan-business-src-main-java-org-libreplan-business-hibernate-notification-PredefinedDatabaseSnapshots.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-labels-daos-ILabelDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-labels-daos-ILabelTypeDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-labels-daos-LabelDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-labels-daos-LabelTypeDAO.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-workreports-entities-WorkReport.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-workreports-entities-WorkReportLabelTypeAssignment.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-workreports-entities-WorkReportLine.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-workreports-entities-WorkReportType.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-labels-daos-LabelDAOTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-labels-daos-LabelTypeDAOTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-orders-daos-OrderElementDAOTest.java]]
- [[libreplan-business-src-test-java-org-libreplan-business-test-workreports-daos-AbstractWorkReportTest.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-common-components-finders-LabelTypeFinder.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-common-components-finders-OrderElementsMultipleFiltersFinder.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-common-components-finders-OrdersMultipleFiltersFinder.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-common-components-finders-TaskElementsMultipleFiltersFinder.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-common-components-finders-TaskGroupsMultipleFiltersFinder.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-labels-ILabelTypeModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-labels-LabelTypeCRUDController.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-labels-LabelTypeModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-orders-labels-AssignedLabelsController.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-orders-labels-AssignedLabelsModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-orders-labels-IAssignedLabelsModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-workreports-IWorkReportModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-workreports-IWorkReportTypeModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-workreports-WorkReportCRUDController.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-workreports-WorkReportModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-workreports-WorkReportTypeCRUDController.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-web-workreports-WorkReportTypeModel.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-labels-api-LabelTypeDTO.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-labels-api-LabelTypeListDTO.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-labels-impl-LabelConverter.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-labels-impl-LabelServiceREST.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-workreports-impl-WorkReportConverter.java]]
- [[libreplan-webapp-src-test-java-org-libreplan-web-orders-OrderElementTreeModelTest.java]]
- [[libreplan-webapp-src-test-java-org-libreplan-web-test-ws-labels-api-LabelServiceTest.java]]
- [[libreplan-webapp-src-test-java-org-libreplan-web-test-ws-orders-OrderElementServiceTest.java]]
- [[libreplan-webapp-src-test-java-org-libreplan-web-test-ws-workreports-WorkReportServiceTest.java]]