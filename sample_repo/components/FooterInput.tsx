// components/FooterInput.tsx
// Text input field used inside the footer for newsletter / subscription.
interface FooterInputProps {
  placeholder?: string;
  label?: string;
}

export function FooterInput({ placeholder, label }: FooterInputProps) {
  return (
    <div className="footer-input-wrapper">
      {label && <label>{label}</label>}
      <input
        type="text"
        className="footer-text-field"
        placeholder={placeholder ?? "Enter text…"}
        aria-label={label ?? "Footer input"}
      />
      <button className="footer-submit-btn">Submit</button>
    </div>
  );
}
