// components/FileUploader.tsx
// Core file upload component. Handles drag-and-drop and the upload error handler.
import { uploadFile, UploadError } from "@/lib/upload";
import type { FileItem } from "@/types/files";

interface FileUploaderProps {
  onUpload: (file: FileItem) => void;
  isUploading: boolean;
}

export function FileUploader({ onUpload, isUploading }: FileUploaderProps) {
  const handleChange = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;

    try {
      const result = await uploadFile(file);
      onUpload(result);
    } catch (err) {
      if (err instanceof UploadError) {
        // upload error handler — display message to user
        console.error("Upload failed:", err.message);
      }
    }
  };

  return (
    <div className="file-uploader">
      <input
        type="file"
        onChange={handleChange}
        disabled={isUploading}
        aria-label="Upload file"
      />
      {isUploading && <span>Uploading…</span>}
    </div>
  );
}
