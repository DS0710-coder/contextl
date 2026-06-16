// app/page.tsx — Root page for the sample repo
import { DownloadPanel } from "@/components/DownloadPanel";
import { UploadSection } from "@/components/UploadSection";
import { Footer } from "@/components/Footer";
import { fetchUserData } from "@/lib/api";

export default async function HomePage() {
  const user = await fetchUserData();
  return (
    <main>
      <h1>Welcome, {user.name}</h1>
      <UploadSection />
      <DownloadPanel />
      <Footer />
    </main>
  );
}
