# libreplan-webapp/src/main/java/org/libreplan/ws/resources/impl/ResourceConverter.java

## Explanation
*No explanation provided in source code.*

## Metrics
**Extension:** `.java`
**Size:** 17865 bytes
**Centrality Score:** 0.0002

## Imports (Dependencies)
- [[libreplan-business-src-main-java-org-libreplan-business-calendars-entities-CalendarAvailability.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-calendars-entities-ResourceCalendar.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-exceptions-InstanceNotFoundException.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-exceptions-MultipleInstancesException.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-common-exceptions-ValidationException.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-costcategories-entities-ResourcesCostCategoryAssignment.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-entities-CriterionSatisfaction.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-entities-CriterionType.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-entities-Machine.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-entities-Resource.java]]
- [[libreplan-business-src-main-java-org-libreplan-business-resources-entities-Worker.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-calendars-api-BaseCalendarDTO.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-calendars-impl-CalendarConverter.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-common-impl-DateConverter.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-common-impl-InstanceNotFoundRecoverableErrorException.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-costcategories-api-CostCategoryDTO.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-resources-api-CalendarAvailabilityDTO.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-resources-api-CriterionSatisfactionDTO.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-resources-api-MachineDTO.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-resources-api-ResourceCalendarDTO.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-resources-api-ResourceDTO.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-resources-api-ResourcesCostCategoryAssignmentDTO.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-resources-api-WorkerDTO.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-resources-criterion-api-CriterionDTO.java]]
- [[libreplan-webapp-src-main-java-org-libreplan-ws-resources-criterion-api-CriterionTypeDTO.java]]

## Imported By (Dependents)
- [[libreplan-webapp-src-test-java-org-libreplan-web-test-ws-resources-api-ResourceServiceTest.java]]