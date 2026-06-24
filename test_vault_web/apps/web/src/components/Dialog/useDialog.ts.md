# useDialog.ts

## Architecture Metrics
- **Path:** `apps/web/src/components/Dialog/useDialog.ts`
- **Extension:** `.ts`
- **Size:** 2730 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `DialogType`
- `BaseDialogConfig`
- `ConfirmDialogConfig`
- `AlertDialogConfig`
- `InfoDialogConfig`
- `CustomDialogConfig`
- `DialogConfig`
- `DialogState`
- `UseDialogReturn`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```ts
import { type ReactNode, useCallback, useState } from "react";
import type { useTranslation } from "react-i18next";

export type DialogType = "confirm" | "alert" | "info" | "custom";

export interface BaseDialogConfig {
  type: DialogType;
  title: string;
  description?: string;
  onConfirm?: () => void | Promise<void>;
  onCancel?: () => void;
  onClose?: () => void;
}

export interface ConfirmDialogConfig extends BaseDialogConfig {
  type: "confirm";
  confirmText?: string;
  cancelText?: string;
  variant?: "default" | "destructive";
  icon?: ReactNode;
...
```