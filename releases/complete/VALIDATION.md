# Validation

Validated October 30, 2026 in the managed cloud environment using Node 24 and system Chromium. All data used by QA was synthetic or supplied sample data.

## Final release result

`SC_TEST_OUTPUT=test-results/innovations-authoritative npm test` completed with **181 passed, 1 explicitly skipped, 0 failed and 0 flaky tests**, from **182 discovered cases in 21 files**, in **405.4 seconds**. This is the authoritative full run after the transaction, planning-counter, manual-source selection and Pipeline compatibility fixes. It supersedes earlier diagnostic runs and includes all current innovations. Focused runs overlap this total and are not added as unique tests. The final rebuilt production preview additionally passed four overlapping connected-workflow checks in 22.1 seconds, including encrypted recovery/undo, forecast matching, closeout/repeat planning and the complete phone review. Result: `test-results/innovations-production-final/results.json`.

The configuration starts/reuses the development server on port 5173 and a production build preview on port 4173. Set `CHROMIUM_PATH` if system Chromium is installed elsewhere.

Earlier review also ran `node tests/amad-security-probes.cjs`, which completed **5 passing function-level security/integrity probes**. These five are separate from the Playwright case count.

| Area | Evidence |
|---|---|
| Existing hotel calculations | Adapted handoff suites preserve parser, displacement, entity-profile and drill-down behavior. The invariant suite executes **720 explicit reconciliation checks with zero failures**. Expected displacement cases match. The exploratory button suite executes **218 clicks with no reported runtime errors**. These nested checks are not additional Playwright cases. |
| Local persistence | Edits survive reload; capture snapshots retain the original property when a caller switches hotels before flush; stale tabs cannot overwrite newer durable edits. A new hotel stays blank when visiting Plans and Contracts. |
| Atomic linked updates | One durable revision saves linked records and a receipt. Failed writes publish no partial business records. Undo preserves unrelated edits and stops for changed or referenced records; receipts survive reload and encrypted restore. Pending hotel loads block linked mutation rather than replacing newer saved state. |
| Recovery | Encrypted backup restores records and an original Blob attachment. Wrong passphrases leave current data unchanged. Restore refuses to run while processing is active. Simulated localStorage and database quota failures show an error rather than claiming cloud success. |
| Security regressions | Malicious extracted field names cannot create executing attributes; prototype paths are rejected; a cloud push retains its original property snapshot through asynchronous waits. Spreadsheet formula-like text is neutralized. Ordinary, raw-query, encoded and `/@fs/` pairing-credential requests return HTTP 403. |
| Actual file processing | Real TXT, CSV, DOCX, XLSX and text-based PDF fixtures extract locally. Leading-zero codes survive. Original bytes remain stored and can be downloaded. A raster screenshot runs through real local Tesseract OCR, recognizes the test text and produces confidence above 50%. |
| Intake boundaries | Extraction does not change sales records until explicit review confirmation. Reviewed account and manual call-note drafts commit correctly. Drag/drop preserves section context; hostile HTML remains an inert attachment. Repeated files deduplicate within a hotel; files over the configured limit are rejected. |
| Sales workspaces | SRP create/edit/search/verify/delete preserves leading zeros. Templates retain history and export an actual merged DOCX whose document XML contains the expected values. Account production imports aggregate duplicate account rows and reject duplicate uploads. Radar withholds trend claims for incomplete or incomparable periods and distinguishes missing data from explicit zero. |
| New connected workflows | Whole Call Desk text creates one reviewed Deal Package. Approved King nights match a typed dated forecast without recopying. Repeat Business keeps 18 actual RN separate from 20 contracted RN, schedules local reminders, and creates a fresh confirmed-date opportunity once. Pipeline rate/count edits and unsupported bed types remain consistent; Definite never silently signs a contract. |
| Follow-up workflow | Saving a sourced Account Radar follow-up plan does not increase completed activity. Recording an actual outcome later adds exactly one activity; repeating completion is rejected. |
| Signature appearance | Typed marks can be placed, resized, removed and saved as a local draft. This tests a printable appearance, not authenticated electronic signing. |
| UI | New workspaces fit a 390px viewport without horizontal page overflow. Workspace modes navigate correctly and Presentation has an exit. Legacy dialogs contain keyboard focus and close with Escape. Eliza separately reviewed desktop/mobile screenshots in `docs/screenshots`. |
| Offline production app | A fresh browser installs the production service worker, goes offline, reloads successfully, preserves the saved manager setting and performs actual screenshot OCR while offline. No external HTTP requests were observed in that test. |

## Transparent handoff adaptations

Eight legacy suite scripts execute through assertion-based wrappers. Their browser executable and URL are adapted for this environment, and host-capability scenarios use in-memory mocks with explicit test-only opt-in. These mocks do not establish live Claude or cloud authorization.

The one skipped case is the old **v3 Claude-host screenshot tray** workflow, which has been replaced by local File Inbox and OCR. The real local extraction/OCR tests exercise its replacement. The v4 adaptation retains and asserts legacy goal logging and pasted BT-production behavior; its retired file-input/Claude-modal steps are replaced by the real intake, production-import and review tests. No passing claim is made for the retired interfaces.

The original handoff ZIP and its tests were not modified. Adapted copies are under `tests/legacy/`.

## Installation and build evidence

Marcus separately verified a clean `npm ci` in `/tmp/sales-command-install-check`, using copied manifest, lockfile and asset setup script. Installation completed with 94 packages and generated the local OCR/PDF assets through postinstall. The application checkout's installed dependencies were left intact. The final production build transformed 336 modules and completed successfully with an advisory bundle-size warning and an ineffective dynamic-import advisory for intake, which is also imported statically. A full dependency audit reported zero vulnerabilities at the time checked; this does not replace continuing dependency maintenance.

## Limits

- Automated browser coverage is Chromium in this environment. The responsive check is not a physical-device, Safari, screen-reader or full accessibility certification.
- No confidential Hilton data or live PEP, OnQ, Lobby, Lighthouse or ProfitSword connection was used. The tests establish local import behavior, not permission or write-back access to those systems.
- Actual microphone recording and recorded-call transcription accuracy were not validated end to end. Manual transcript review works. The local speech helper and its model remain a separately configured component; model-download access was blocked in this environment. No speech-recognition success is claimed.
- Supported-file fixtures and explicit size guards were tested; this is not proof that every format, corrupted document or malicious archive is handled perfectly. Unsupported files remain attachment-only, within configured limits.
- The app remains local-first. A test of local durable saves and encrypted recovery does not establish cross-device cloud synchronization, centralized organizational authentication or a deployed production service.
- Signature appearance and DOCX output do not establish recipient identity, certificate-backed signing, or legal enforceability.

Test reports, traces and intermediate failures are generated under ignored `test-results/` and are not release source. The authoritative final full-suite result is `test-results/innovations-authoritative/results.json` in the validation workspace.

## Contract workflow update

The full application run includes 29 contract parser/browser cases. After the final print-only CSS correction, all five actual PDF cases also passed against the rebuilt production app, including white paper margins, page bounds and explicit hotel-only signatures. See [CONTRACTS-VALIDATION.md](CONTRACTS-VALIDATION.md) for exact coverage, page counts and synthetic review samples.

## Pittsburgh sales and design update

Four persistent palettes, real scene motion/reduced-motion behavior, actual phone menu taps, reviewed prospect/Lighthouse imports, Tours/Networking, report identity guards and Deal Review now have integration coverage. The last Call Desk fix correctly classifies a reviewed call and preserves one linked Contacted prospect through render/reload. See [PITTSBURGH-VALIDATION.md](PITTSBURGH-VALIDATION.md) for exact run boundaries, independent arithmetic and final visual evidence.

## River stadium visual update

The later Three Rivers stadium variant passed **16 targeted production design/stadium cases** plus **one actual courtesy PDF check**. Other palettes hide the stadiums; both fit the phone hero and lighting stops for reduced motion. The existing River screenshots and eight-second GIF/MP4 previews were refreshed. See [PITTSBURGH-STADIUMS-VALIDATION.md](PITTSBURGH-STADIUMS-VALIDATION.md). These overlap earlier checks and do not represent another complete sales-suite run.

## Three innovations and shared workflow compatibility

The final full run includes 55 cases added since the 127-case stadium catalog: Deal Package, Need Date Matchmaker, Repeat Business Memory, guarded transactions, connected UI journeys, Pipeline compatibility and exact manual-report source selection. See [INNOVATIONS-VALIDATION.md](INNOVATIONS-VALIDATION.md) for independent arithmetic, failure/undo scenarios, defects corrected and synthetic desktop/phone evidence.
