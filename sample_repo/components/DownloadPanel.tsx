// components/DownloadPanel.tsx
// Panel containing the download button and progress indicator.
import { DownloadButton } from "@/components/DownloadButton";
import { useDownloadState } from "@/lib/hooks";
import type { FileItem } from "@/types/files";

interface DownloadPanelProps {
  file?: FileItem;
}

export function DownloadPanel({ file }: DownloadPanelProps) {
  const { isDownloading, progress, startDownload } = useDownloadState();

  return (
    <section className="download-panel">
      <h2>Download</h2>
      {isDownloading && <progress value={progress} max={100} />}
      <DownloadButton onClick={() => startDownload(file)} disabled={isDownloading} />
    </section>
  );
}
