// lib/api.ts
// Client-side API helpers for fetching data from the backend.
import type { UserData } from "@/types/user";
import type { FileItem } from "@/types/files";

const BASE_URL = process.env.NEXT_PUBLIC_API_URL ?? "";

export async function fetchUserData(): Promise<UserData> {
  const res = await fetch(`${BASE_URL}/api/user`);
  if (!res.ok) throw new Error("Failed to fetch user data");
  return res.json();
}

export async function fetchFiles(): Promise<FileItem[]> {
  const res = await fetch(`${BASE_URL}/api/files`);
  if (!res.ok) throw new Error("Failed to fetch files");
  return res.json();
}
