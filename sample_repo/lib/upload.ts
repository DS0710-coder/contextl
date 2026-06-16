// lib/upload.ts
// Upload utilities including UploadError class and uploadFile function.
import type { FileItem } from "@/types/files";

export class UploadError extends Error {
  constructor(message: string, public readonly statusCode?: number) {
    super(message);
    this.name = "UploadError";
  }
}

export async function uploadFile(file: File): Promise<FileItem> {
  const formData = new FormData();
  formData.append("file", file);

  const res = await fetch("/api/upload", {
    method: "POST",
    body: formData,
  });

  if (!res.ok) {
    const text = await res.text();
    throw new UploadError(`Upload failed: ${text}`, res.status);
  }

  return res.json();
}
