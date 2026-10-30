# Sales Command: worker-by-worker change review

Prepared October 30, 2026. This distinguishes implemented changes from tested behavior and work that still needs real-world validation. The original user-supplied handoff files remain separate and unchanged; implementation is in this repository.

## Marcus: coordination, integration and delivery

- Preserved the existing Aurora app and business calculators rather than replacing it with a generic CRM.
- Established the Vite/npm build, pinned dependencies, local fonts/OCR/PDF assets, a narrow legacy adapter, installable/offline shell and reproducible asset generation.
- Connected transactional storage, feature workspaces, document intake and local transcription into one application.
- Added Device & Backups, blank-property creation, legacy attachment migration and encrypted backup/restore controls.
- Corrected offline cache matching after real offline tests found a Vary-header cache miss; blocked development-server access to private helper files after a test exposed an unprotected path, and rotated the test helper token.
- Built release ZIPs, verified checksums and GitHub downloads, and kept release delivery on a separate branch without changing master. Browser data, private tokens, models, virtual environments, test traces and uploaded reference PDFs are excluded from packages.
- For the current contract update: added the contract adapter, atomic field application, strict numeric/date/night validation, stale hotel/contract/data checks, signed-draft copying, approval invalidation, whole-transcript Call Desk transfer, local signature font mapping and export guards.
- Added the Mac app-only updater. It stages, verifies and replaces static app files, retains old app files for recovery, and preserves the existing local engine/model/token. It cannot modify or directly back up Safari's database, so export your encrypted backup first.

## Eliza: design and document presentation

Earlier release:
- Retained Aurora colors, glass surfaces, skyline, existing skins and dark/light settings.
- Fixed clipped mobile header controls and moved useful capture actions onto the first phone screen.
- Added Daily, Revenue, Documents and Presentation modes, presentation exit, keyboard/dialog focus behavior and reduced-motion support.
- Reviewed the new routes at a 390px viewport and captured synthetic desktop/mobile screenshots.

Current contract update:
- Inspected the supplied agreement as a visual reference.
- Built a courtesy agreement with navy headings, blue rules and section badges, pale two-column contacts, date grid, room/rate table, acceptance fields and repeated print headers/footers.
- Applied shared professional typography to standard group and corporate contracts without rewriting their existing clauses.
- Added an explicit layout picker and editable, property-specific courtesy terms. Courtesy is a separate agreement type that requires review, not a silent styling toggle for guaranteed groups.
- Preserved only your deliberate Hotel Sign action; no client signature is inferred or copied. Missing source-logo images are omitted cleanly.
- Used synthetic contacts in screenshots. The original PDF, client contact information and signature were not published.

## Aaron: repository research, installation and speech tools

- Inspected public repository documentation, licenses, maintenance evidence, security advisories and selected issue reports. His report distinguishes fetched evidence from unverified claims and blocked sources.
- Recommended focused libraries for local database, intake, PDF/Office processing, OCR, document generation and signatures instead of a large CRM replacement.
- Implemented bounded local intake, original retention, file hashes/deduplication, real PDF/DOCX/Excel/text extraction, local screenshot OCR, source review, voice-memo capture and manual transcript review.
- Added file/ZIP/pixel/page/time limits, actual archive-expansion validation, explicit coverage labels and safe attachment-only treatment for unsupported formats.
- Implemented the local speech companion, then replaced Python ML inference with official pinned whisper.cpp v1.9.5 for the M1 direction. Python now handles local HTTP/audio decoding only; the native CLI runs on demand.
- Built whisper.cpp on the cloud's Linux machine; created a Mac installer that enables Metal on Apple Silicon, pins the source commit, and verifies official model downloads.
- Verified fresh codec dependencies, actual audio decoding and checksum-failure cleanup. The cloud model download was blocked; no cloud end-to-end speech accuracy claim was made. The user subsequently reported successful installation and operation on the M1, which is user confirmation rather than our hardware benchmark.
- Aaron did not author the new contract parser or approve legal terms.

## Amad: security, persistence and integrity

- Reproduced and helped fix cross-hotel writes during asynchronous saves, executable model-generated field names, prototype-path handling, unsafe spreadsheet text exports, misleading saved status and stale deadline wording.
- Implemented transactional IndexedDB snapshots, stale-tab conflict protection, local migration, encrypted full-data backup and validated restore. Added restore/job interlocks, revision invalidation and recovery-copy retention.
- Found and corrected blank hotels inheriting sample property details and guarded legacy attachment operations against property switching and executable blob previews.
- Reworked the speech bridge around an argument-list native subprocess with local-only networking, Origin/Host/token checks, one-job handling, bounded audio/JSON/timeouts and no runtime model downloading.
- For contracts: reviewed property/target/fingerprint boundaries, actual-calendar dates, resolved cutoff/hold dates, nightly allocation, missing values vs zero, source provenance, review invalidation and uploaded-PDF privacy.
- Confirmed synthetic adapter probes for rejection/atomicity and checked that private PDF/client data did not enter public assets.
- Explicit boundary: the legacy manual editor is not a cryptographically immutable signed-document store. Bulk import/layout changes reject signed records; identity-verified signing remains outside this release.

## Chloe: sales workflows and whole-conversation filling

Earlier release:
- Reviewed every existing sales/revenue/report section and wrote a prioritized hotel-sales backlog.
- Built the property-scoped SRP vault, template/RFP library, document versioning, friendly merge inputs, genuine Word exports, production CSV import/history and Account Radar.
- Kept missing rows distinct from zero production; required comparable periods/coverage before trend claims; preserved source files and rejected duplicate imports.
- Added sourced follow-up plans that do not inflate completed activity. Explicit actual-outcome completion adds one activity.
- Built Signature Studio with local fonts, drawn/image marks, positioning/resizing and saved drafts, with its one-page/visual-signature limits clearly stated.

Current contract update:
- Implemented local whole-transcript parsing, full paste/text drop/file selection and a single review/apply screen.
- Extracts supported company/event/contact fields, stay/deadline dates, codes and room/rate proposals; retains the complete text locally as source evidence.
- Flags unclear years, numeric date order, corrected/conflicting facts, shorthand prices, room-night ambiguity and unsupported allocations. Two Queen Beds and Two Double Beds remain different products.
- Leaves existing filled fields unchecked unless replacement is explicitly selected. Room rows require explicit allocation/rate approval; one batch apply replaces only selected data.
- Prevents transcript-generated clauses, taxes, billing decisions, signatures or signing status. Signed contracts require a draft copy.
- This is deterministic local extraction, not an unrestricted AI model that understands every possible conversation. Review remains necessary.

## The Breakers: independent verification

Earlier release:
- Converted meaningful expectations into assertions and preserved transparent adaptations of the original scripts.
- Reported 40 app cases passed with one explicitly skipped obsolete host-only workflow; separately verified five security probes.
- Checked real local extraction/OCR, original downloads, explicit reviewed commits, storage reload/conflicts/backup recovery, SRP/Word/radar/signature workflows, mobile layout and actual offline reload/OCR.
- Nested calculation suites performed 720 reconciliation checks and 249 exploratory button clicks. These are not additional top-level Playwright cases.
- For native speech, 18 infrastructure tests passed using an explicitly synthetic CLI fixture, plus two relevant browser regressions. This validated the connection/security/codec contract, not speech recognition accuracy.

Current contract update:
- Added parser and browser tests covering one-shot capture, before/after review, explicit replacements/allocations, Call Desk transfer, malformed/conflicting values, signed copies, stale targets, provenance and courtesy export approval.
- Generated actual PDFs with synthetic data, checked final text and page bounds, and reviewed short and long contract layouts.
- Found test and implementation defects during review; each final passing claim is based on the corrected rerun, not an initial successful-looking log.
- Exact final counts, PDF measurements and remaining gaps are in CONTRACTS-VALIDATION.md.

## What this does not claim

No private Hilton API integration, automated PEP/OnQ/Lobby write-back, automatic device sync, public hosted deployment, employer approval, legal review or verified electronic-signature service is supplied. Automated browser/PDF tests run in Chromium, not physical Safari/Mac hardware. Inspect Safari's PDF preview before sending contracts. The M1 installer and app-only updater were syntax-checked here; their Mac UI behavior needs the user's actual machine. A successful dependency audit is a point-in-time check, not a guarantee against future vulnerabilities.

Before relying on reports for work, validate redacted real PEP/Lighthouse/ProfitSword exports and actual approved contract templates, then test encrypted backup recovery on the Mac. Large attachment collections remain subject to browser storage and backup size/memory limits.

## Final contract-update verification

The complete updated suite discovered 70 unique cases: **69 passed, one obsolete host-specific workflow explicitly skipped, zero failed and zero flaky**. All 29 newly added contract cases passed. After the last print-only CSS correction, five actual PDF cases were rerun against the rebuilt production app and all five passed; their white page margins were checked at the pixel level. These five are reruns, not five additional unique cases.

Measured synthetic PDFs: short courtesy agreement two pages; explicitly hotel-signed courtesy two pages; long courtesy three pages; long standard group five pages; long corporate agreement three pages. Text and bounds checks confirmed final clauses and signature sections were retained. Raster review found a dark-mode paper-margin issue that functional text tests missed; it was corrected and the production PDFs were retested.

The app-only updater's actual copy/verification/backup logic passed a temporary-folder fixture that retained a model and pairing-token fixture. Its macOS folder picker remains unexecuted here. No source customer PDF or client identifiers appear in shipped assets.
