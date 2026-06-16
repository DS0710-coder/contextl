// types/user.ts
// User-related type definitions.

export interface UserData {
  id: string;
  name: string;
  email: string;
  avatarUrl?: string;
  role: "admin" | "user" | "viewer";
}
