# Move To Another Computer Without Losing Work

## What To Transfer

Use `Genuity-Verify-TRANSFER-2026-10-01.zip` and its adjacent `.receipt.json` in the parent `karthik` folder. The ZIP contains the committed source, dependency locks, full Git history bundle, source PDFs, reference MVP, knowledge graphs, screenshot/performance evidence and a ready-to-preview static site.

Deliberately excluded: node_modules, Python virtual environments, machine-local build cache, runtime database, sessions and signing secrets. These are not portable source. Demo engineering data is reproducibly reseeded on backend startup. New-machine preview does not contain old server sessions or runtime experiment history.

## Open The Same Website Immediately

1. Extract the ZIP into a NEW directory. Never extract over your only working copy.
2. Install Node.js 24 LTS if it is not already installed. This prerequisite cannot be guaranteed to take one minute.
3. Inside the extracted `claude bro` folder, double-click OPEN-WEBSITE.cmd on Windows, or run `node tools/preview.mjs` on any supported OS.
4. Open http://127.0.0.1:5192. Keep the terminal open. No npm install, Python, API keys or internet service is required for this packaged preview.

The preview is a frozen snapshot. Editing source does not update it automatically. Use the development workflow below for code changes.

## Editable Frontend

From the extracted `claude bro` folder:

```powershell
npm.cmd --prefix site ci
npm.cmd --prefix site run dev -- --hostname 127.0.0.1 --port 5190
```

On macOS/Linux use `npm` instead of `npm.cmd`. Initial installation needs internet and can take several minutes. Use the lockfile; do not upgrade packages. Open http://127.0.0.1:5190. Tests and build commands are in README.md.

## Preserve Git History

The archive includes `Genuity-Verify-history.bundle` next to the project folder. A safe recovery into a separate folder is:

```powershell
git clone Genuity-Verify-history.bundle genuity-with-history
```

This creates a new checkout and does not overwrite `claude bro`. Work in the new checkout for incremental development with full history. The frozen preview remains available in the original extracted folder. The protected tag `genuity-preserved-2026-10-01` identifies the preserved application before transfer-helper additions.

To publish source later, create your own private remote and add/push it deliberately. No remote account or cloud project was configured. Do not push confidential PDFs/reference screenshots publicly without reviewing ownership and confidentiality.

## Backend And Console

The code remains in backend and web. Install Python 3.12 and uv, then run `uv sync --frozen`, `uv run pytest`, and `uv run uvicorn backend.api:create_app --factory --host 127.0.0.1 --port 8180` from the project root. In another terminal run `npm.cmd --prefix web ci` and `npm.cmd --prefix web run dev -- --host 127.0.0.1 --port 5180`. The console proxy already targets 8180.

Do not copy the old .venv or node_modules to another machine. Do not expose the development demo-auth server to the public internet. The backend is engineering software with open production-qualification gates, not a certified robot controller.

## Integrity And Recovery

The receipt gives the ZIP SHA256. On Windows: `Get-FileHash -Algorithm SHA256 -LiteralPath 'Genuity-Verify-TRANSFER-2026-10-01.zip'`. Compare it with the receipt. TRANSFER_MANIFEST.json inside the ZIP lists the source commit and SHA256/size for every packaged file. The packaging process verifies every ZIP entry and the Git bundle before issuing the receipt.

Keep one untouched ZIP and one working checkout. Before a model edits anything, have it read META_MUSE_START_HERE.md. No instruction file can guarantee a model's behavior, but the immutable copy, Git history and checksums provide a concrete recovery path if it makes a bad change.