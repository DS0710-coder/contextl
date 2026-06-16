// components/UploadSection.tsx
// Handles file upload UI and delegates to FileUploader.
import { FileUploader } from "@/components/FileUploader";
import { useUploadState } from "@/lib/hooks";

export function UploadSection() {
  const { isUploading, error, handleUpload } = useUploadState();

  return (
    <section className="upload-section">
      <h2>Upload a File</h2>
      {error && <p className="error">{error}</p>}
      <FileUploader onUpload={handleUpload} isUploading={isUploading} />
    </section>
  );
}
