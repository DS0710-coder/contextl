// app/layout.tsx — Root layout
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Sample App",
  description: "Repository Intelligence Engine sample repo",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
