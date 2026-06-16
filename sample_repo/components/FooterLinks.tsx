// components/FooterLinks.tsx
// Navigation links rendered in the footer section.
const LINKS = [
  { label: "Privacy Policy", href: "/privacy" },
  { label: "Terms of Service", href: "/terms" },
  { label: "Contact", href: "/contact" },
];

export function FooterLinks() {
  return (
    <nav className="footer-links" aria-label="Footer navigation">
      <ul>
        {LINKS.map((link) => (
          <li key={link.href}>
            <a href={link.href}>{link.label}</a>
          </li>
        ))}
      </ul>
    </nav>
  );
}
