// components/Footer.tsx
// Site footer with text fields and links.
import { FooterInput } from "@/components/FooterInput";
import { FooterLinks } from "@/components/FooterLinks";

export function Footer() {
  return (
    <footer className="site-footer">
      <FooterInput placeholder="Subscribe to updates…" />
      <FooterLinks />
      <p className="footer-text">© 2024 Sample Corp. All rights reserved.</p>
    </footer>
  );
}
