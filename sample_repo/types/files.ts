// types/files.ts
// Shared type definitions for file objects.

export interface FileItem {
  id: string;
  name: string;
  size: number;
  mimeType: string;
  url: string;
  uploadedAt: string;
}

export type FileStatus = "pending" | "uploading" | "complete" | "error";

export interface FileUploadState {
  file: FileItem | null;
  status: FileStatus;
  progress: number;
  errorMessage?: string;
}
