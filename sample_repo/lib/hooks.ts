// lib/hooks.ts
// Shared React hooks used across the app.
import { useState } from "react";
import { uploadFile } from "@/lib/upload";
import type { FileItem } from "@/types/files";

export function useUploadState() {
  const [isUploading, setIsUploading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleUpload = async (file: FileItem) => {
    setIsUploading(true);
    setError(null);
    try {
      // already uploaded by FileUploader; here we handle post-upload state
      setIsUploading(false);
    } catch (e: unknown) {
      setError((e as Error).message);
      setIsUploading(false);
    }
  };

  return { isUploading, error, handleUpload };
}

export function useDownloadState() {
  const [isDownloading, setIsDownloading] = useState(false);
  const [progress, setProgress] = useState(0);

  const startDownload = async (file?: FileItem) => {
    if (!file) return;
    setIsDownloading(true);
    setProgress(0);
    // Simulate download progress
    for (let i = 0; i <= 100; i += 10) {
      await new Promise((r) => setTimeout(r, 50));
      setProgress(i);
    }
    setIsDownloading(false);
  };

  return { isDownloading, progress, startDownload };
}
