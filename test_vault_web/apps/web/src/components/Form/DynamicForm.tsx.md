# DynamicForm.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/Form/DynamicForm.tsx`
- **Extension:** `.tsx`
- **Size:** 5508 bytes
- **Centrality Score:** 0.0051
- **In-Degree (Imported By):** 31
- **Out-Degree (Imports):** 6

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `FieldProps`
- `Control`
- `DefaultValues`
- `FieldValues`
- `Path`
- `SubmitHandler`
- `UseFormReturn`
- `DisabledBy`
- `BaseFormBuilderProps`
- `GenericFormElementProps`
- `DynamicFormProps`
- `DynamicFormFormInit`
- `DynamicForm`

## Imports (Dependencies)
- [[apps/web/src/components/Form/DynamicFormField.tsx.md|apps/web/src/components/Form/DynamicFormField.tsx]]
- [[apps/web/src/components/Form/FormWrapper.tsx.md|apps/web/src/components/Form/FormWrapper.tsx]]
- [[apps/web/src/components/Form/createZodResolver.ts.md|apps/web/src/components/Form/createZodResolver.ts]]
- [[apps/web/src/components/UI/Button.tsx.md|apps/web/src/components/UI/Button.tsx]]
- [[apps/web/src/components/UI/Typography/Heading.tsx.md|apps/web/src/components/UI/Typography/Heading.tsx]]
- [[apps/web/src/components/UI/Typography/Subtle.tsx.md|apps/web/src/components/UI/Typography/Subtle.tsx]]

## Imported By (Dependents)
- [[apps/web/src/components/Form/FormInput.tsx.md|apps/web/src/components/Form/FormInput.tsx]]
- [[apps/web/src/components/Form/FormMultiSelect.tsx.md|apps/web/src/components/Form/FormMultiSelect.tsx]]
- [[apps/web/src/components/Form/FormPasswordGenerator.tsx.md|apps/web/src/components/Form/FormPasswordGenerator.tsx]]
- [[apps/web/src/components/Form/FormSelect.tsx.md|apps/web/src/components/Form/FormSelect.tsx]]
- [[apps/web/src/components/Form/FormToggle.tsx.md|apps/web/src/components/Form/FormToggle.tsx]]
- [[apps/web/src/components/PageComponents/Channels/Channel.tsx.md|apps/web/src/components/PageComponents/Channels/Channel.tsx]]
- [[apps/web/src/components/PageComponents/ModuleConfig/AmbientLighting.tsx.md|apps/web/src/components/PageComponents/ModuleConfig/AmbientLighting.tsx]]
- [[apps/web/src/components/PageComponents/ModuleConfig/Audio.tsx.md|apps/web/src/components/PageComponents/ModuleConfig/Audio.tsx]]
- [[apps/web/src/components/PageComponents/ModuleConfig/CannedMessage.tsx.md|apps/web/src/components/PageComponents/ModuleConfig/CannedMessage.tsx]]
- [[apps/web/src/components/PageComponents/ModuleConfig/DetectionSensor.tsx.md|apps/web/src/components/PageComponents/ModuleConfig/DetectionSensor.tsx]]
- [[apps/web/src/components/PageComponents/ModuleConfig/ExternalNotification.tsx.md|apps/web/src/components/PageComponents/ModuleConfig/ExternalNotification.tsx]]
- [[apps/web/src/components/PageComponents/ModuleConfig/MQTT.tsx.md|apps/web/src/components/PageComponents/ModuleConfig/MQTT.tsx]]
- [[apps/web/src/components/PageComponents/ModuleConfig/NeighborInfo.tsx.md|apps/web/src/components/PageComponents/ModuleConfig/NeighborInfo.tsx]]
- [[apps/web/src/components/PageComponents/ModuleConfig/Paxcounter.tsx.md|apps/web/src/components/PageComponents/ModuleConfig/Paxcounter.tsx]]
- [[apps/web/src/components/PageComponents/ModuleConfig/RangeTest.tsx.md|apps/web/src/components/PageComponents/ModuleConfig/RangeTest.tsx]]
- [[apps/web/src/components/PageComponents/ModuleConfig/RemoteHardware.tsx.md|apps/web/src/components/PageComponents/ModuleConfig/RemoteHardware.tsx]]
- [[apps/web/src/components/PageComponents/ModuleConfig/Serial.tsx.md|apps/web/src/components/PageComponents/ModuleConfig/Serial.tsx]]
- [[apps/web/src/components/PageComponents/ModuleConfig/StatusMessage.tsx.md|apps/web/src/components/PageComponents/ModuleConfig/StatusMessage.tsx]]
- [[apps/web/src/components/PageComponents/ModuleConfig/StoreForward.tsx.md|apps/web/src/components/PageComponents/ModuleConfig/StoreForward.tsx]]
- [[apps/web/src/components/PageComponents/ModuleConfig/Tak.tsx.md|apps/web/src/components/PageComponents/ModuleConfig/Tak.tsx]]
- [[apps/web/src/components/PageComponents/ModuleConfig/Telemetry.tsx.md|apps/web/src/components/PageComponents/ModuleConfig/Telemetry.tsx]]
- [[apps/web/src/components/PageComponents/ModuleConfig/TrafficManagement.tsx.md|apps/web/src/components/PageComponents/ModuleConfig/TrafficManagement.tsx]]
- [[apps/web/src/components/PageComponents/Settings/Bluetooth.tsx.md|apps/web/src/components/PageComponents/Settings/Bluetooth.tsx]]
- [[apps/web/src/components/PageComponents/Settings/Device/index.tsx.md|apps/web/src/components/PageComponents/Settings/Device/index.tsx]]
- [[apps/web/src/components/PageComponents/Settings/Display.tsx.md|apps/web/src/components/PageComponents/Settings/Display.tsx]]
- [[apps/web/src/components/PageComponents/Settings/LoRa.tsx.md|apps/web/src/components/PageComponents/Settings/LoRa.tsx]]
- [[apps/web/src/components/PageComponents/Settings/Network/index.tsx.md|apps/web/src/components/PageComponents/Settings/Network/index.tsx]]
- [[apps/web/src/components/PageComponents/Settings/Position.tsx.md|apps/web/src/components/PageComponents/Settings/Position.tsx]]
- [[apps/web/src/components/PageComponents/Settings/Power.tsx.md|apps/web/src/components/PageComponents/Settings/Power.tsx]]
- [[apps/web/src/components/PageComponents/Settings/Security/Security.tsx.md|apps/web/src/components/PageComponents/Settings/Security/Security.tsx]]
- [[apps/web/src/components/PageComponents/Settings/User.tsx.md|apps/web/src/components/PageComponents/Settings/User.tsx]]

## Source Code Snippet
```tsx
import { createZodResolver } from "@components/Form/createZodResolver.ts";
import {
  DynamicFormField,
  type FieldProps,
} from "@components/Form/DynamicFormField.tsx";
import { FieldWrapper } from "@components/Form/FormWrapper.tsx";
import { Button } from "@components/UI/Button.tsx";
import { Heading } from "@components/UI/Typography/Heading.tsx";
import { Subtle } from "@components/UI/Typography/Subtle.tsx";
import { type ReactNode, useEffect } from "react";
import {
  type Control,
  type DefaultValues,
  type FieldValues,
  FormProvider,
  get,
  type Path,
  type SubmitHandler,
  type UseFormReturn,
  useForm,
...
```