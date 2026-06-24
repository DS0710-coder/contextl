# github.ts

## Architecture Metrics
- **Path:** `apps/web/src/core/utils/github.ts`
- **Extension:** `.ts`
- **Size:** 2108 bytes
- **Centrality Score:** 0.0010
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `RepoIdentifier`
- `GithubIssueUrlOptions`
- `ValidatedOptions`
- `validateOptions`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[apps/web/src/components/UI/ErrorPage.tsx.md|apps/web/src/components/UI/ErrorPage.tsx]]

## Source Code Snippet
```ts
interface RepoIdentifier {
  user: string;
  repo: string;
}

interface GithubIssueUrlOptions extends Partial<RepoIdentifier> {
  repoUrl?: string;
  body?: string;
  title?: string;
  labels?: string[];
  template?: string;
  assignee?: string;
  projects?: string[];
  logs?: string;
  version?: number;
}

type ValidatedOptions = {
  repoUrl: string;
} & Omit<GithubIssueUrlOptions, "repoUrl" | "user" | "repo">;
...
```