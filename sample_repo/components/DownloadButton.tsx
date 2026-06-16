// components/DownloadButton.tsx
// The actual download <button> element with icon and label.
interface DownloadButtonProps {
  onClick: () => void;
  disabled?: boolean;
}

export function DownloadButton({ onClick, disabled }: DownloadButtonProps) {
  return (
    <button
      className="download-btn"
      onClick={onClick}
      disabled={disabled}
      aria-label="Download file"
    >
      ⬇ Download
    </button>
  );
}
