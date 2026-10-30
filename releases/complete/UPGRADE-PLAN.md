# Sales Command: Marcus’s upgrade decision report

Prepared October 30, 2026. Research and review of the supplied handoff, not implementation or deployment.

## Direction

Build a personal, local-first web application that preserves Sales Command’s Aurora identity and can add a second hotel without a redesign. A private web app provides a real address, navigation, saved workspaces, and mobile layouts. Add installation/offline support as a PWA. A website alone does not supply secure storage, transcription, or device synchronization.

The user selected: **just me initially, another hotel later; keep files and transcription local wherever practical**. No employer hosting or AI approval is assumed. No private Hilton integration is assumed.

The current `juju` repository has only a README and Git attributes. The working application is in the supplied ZIP. All 18 original archive files remain unchanged. The ZIP’s prior request for a narrow second-opinion review is context; the current request authorizes a broader improvement research pass.

## What to retain

Aurora purple/blue accents, glass panels, skyline artwork, report drill-downs, sales vocabulary, existing report parsers, activity-to-report workflows, multi-hotel selector, and review-before-save intake. Four skins and light/dark/automatic appearance already exist. Contract Maker already has a cursive-signature treatment. Screenshot and document imports already exist; their coverage and reliability need improvement.

## Fix before adding real work data

1. **Cross-property writes:** a cloud save can start for hotel A and read hotel B’s mutable state after an asynchronous wait. Isolated execution reproduced B data written under A document IDs. Snapshot property ID and payload together, use property-scoped revision checks, and test switching during saves.
2. **Imported-field code execution:** an AI-returned field key containing `x" onpointerover="alert(1)" z="` is inserted into `data-xf` without escaping. Browser testing confirms execution on pointerover. Use a strict allowed-field schema and safe DOM construction. Existing tests covering hostile field *values* do not cover this path.
3. **Misleading save state:** a local storage quota failure can say “Saved to cloud” merely because a cloud collection exists. Display committed persistence state, not configured capability. Provide recoverable backup and restore.
4. **Spreadsheet formula injection:** drill CSV output leaves a text value such as `=1+1` active. Write untrusted text as literal strings, preserve legitimate numeric columns, and verify Excel/LibreOffice behavior.
5. **PDF dependency:** the scanned-PDF path loads PDF.js 3.11.174, affected by the official 2024 advisory. Replace with a supported, patched version and matching worker; disable document scripting and enforce CSP. A newer official 2026 advisory also means “upgrade to any recent 5.x” is insufficient. Advisory presence is established; a malicious-PDF exploit was not executed in this review.
6. **Privacy wording:** the source claims guest names are never sent, but activity notes/contact fields enter AI context without the claimed redaction. Replace that claim with explicit, verified local/cloud processing boundaries and a preview of what leaves the device.

Detailed evidence and probes are in Amad’s and The Breakers’ reports. These are current defects; they have not been fixed by this research pass.

## Local-first architecture

- Keep the browser interface and current business calculations while introducing tested modules instead of extending more global function overrides.
- Store structured records transactionally in IndexedDB, with Dexie as a candidate wrapper. Use property IDs on every record and query. Keep file blobs separately from dashboard state, using IndexedDB or browser-supported OPFS after compatibility tests.
- Request persistent browser storage, but treat it as a convenience rather than a backup. Browser clearing, device loss, private browsing, and quotas remain relevant. Add versioned, encrypted export/restore with an actual recovery test and visible last-backup date.
- Bundle fonts, scripts, OCR workers, and models locally. Do not load document-processing code from third-party CDNs during daily use.
- Use browser OCR/document parsing first. Run desktop transcription through a local companion process, preferably whisper.cpp, when computer capacity allows. Bind any companion to loopback, validate Origin, and require scoped authorization; a random website must not be able to submit jobs to it.
- A phone cannot automatically use the local worker on a different computer. Phone options are short, tested on-device processing, saving a recording for later desktop processing, or a separately approved service. Browser/OS dictation is not automatically offline.
- Keep cloud sync optional. “Install on both devices” does not synchronize their local databases. Start with portable encrypted backup/restore; consider authenticated encrypted sync only if the user needs it.
- Protect a lost/shared device through OS sign-in, app lock where appropriate, minimal cached guest details, and deliberate export handling. Browser storage is not a guarantee of application-level encryption.

## GitHub shortlist and install decisions

These are researched candidates, not installed or compatibility-certified packages. Pin versions and validate actual redacted work samples during implementation. Full licensing, maintenance evidence, official advisories and issue-report caveats are in [Aaron’s report](aaron.md).

| Candidate | Intended role | Decision |
|---|---|---|
| [Uppy](https://github.com/transloadit/uppy), MIT | Shared drop/paste/upload UI | First wave; use local adapter, no hosted processing required |
| [Dexie](https://github.com/dexie/Dexie.js), Apache-2.0 | Transactional browser database | First wave; backups, encryption and sync are separate work |
| [PDF.js](https://github.com/mozilla/pdf.js), Apache-2.0 | PDF text and page rendering | First wave; supported version patched for relevant advisories, matching worker |
| [SheetJS CE](https://github.com/SheetJS/sheetjs), Apache-2.0 | Broad Excel/XLSB intake and spreadsheet output | Candidate pending current canonical distribution/version verification; GitHub points elsewhere |
| [Mammoth](https://github.com/mwilliamson/mammoth.js), BSD-2-Clause | DOCX text extraction | Prefer raw text; HTML is not sanitized by Mammoth |
| [DOMPurify](https://github.com/cure53/DOMPurify), retrieved LICENSE Apache-2.0 | Restricted HTML previews | Add if retaining HTML previews; still validate/escape field keys and URLs |
| [Tesseract.js](https://github.com/naptha/tesseract.js), Apache-2.0 | Local screenshot/scanned-page OCR | Evaluate on real samples; PDF pages must be rendered first |
| [Docxtemplater](https://github.com/open-xml-templating/docxtemplater), MIT/GPL choice for core | Fill existing approved Word templates | Prototype template fidelity; some image/advanced modules are paid |
| [docx](https://github.com/dolanmiu/docx), MIT | Generate new Word layouts | Alternative to template engine, not automatic preservation of arbitrary templates |
| [Signature Pad](https://github.com/szimek/signature_pad), MIT | Draw/save/place own signature | Complements licensed font marks; not a verified signing service |
| [whisper.cpp](https://github.com/ggml-org/whisper.cpp), MIT code | Local speech transcription | Preferred local candidate; benchmark hardware/models/accuracy before selecting |
| [ECharts](https://github.com/apache/echarts), Apache-2.0 | Interactive production charts | Optional; existing SVG charts may suffice initially |

Do not install both Word-generation options or both speech engines by default. [faster-whisper](https://github.com/SYSTRAN/faster-whisper) is a credible MIT local Python-worker alternative. ExcelJS and pdf-lib are deferred because the researched source histories show maintenance gaps; user issue reports are signals, not reproduced vulnerabilities. Documenso is an optional AGPL signing service with additional hosting/license work. Large CRMs would duplicate the existing hotel workflow.

For design, inspect [shadcn/ui](https://github.com/shadcn-ui/ui), [Radix](https://github.com/radix-ui/primitives) and [Motion](https://github.com/motiondivision/motion) as optional patterns/components, not three mandatory new dependencies. Existing app has no React build, so choosing React-only components entails a deliberate migration. Pinterest/Mobbin and several inspiration sites were blocked; Eliza’s report distinguishes inspected sources from proposed references.

## File intake and export contract

The correct promise is broad attachment support plus explicit extraction support. Never claim every file can be understood, previewed, or exported into every other format. Unknown binaries should stay attachments with a clear status, never be silently decoded as ordinary text or executed.

| Input | Planned behavior |
|---|---|
| PDF | Searchable preview, text extraction, OCR for scanned pages; show all processed/skipped pages |
| XLSX, CSV, TSV | Preview sheets/columns, map fields, verify totals, deduplicate imports |
| XLSB, XLS, XLSM | Dedicated compatibility tests using redacted real report samples; preserve macros only as inert attachments, never execute them |
| DOCX | Read text/fields; preserve the original; generate new documents from approved templates |
| DOC, MSG, unusual email containers | Explicit converter or attachment-only status until a supported adapter is validated |
| PNG, JPG, WebP and screenshots | Browser OCR plus an optional structured extraction step; highlight source evidence |
| HEIC/HEIF | Verify device decoder support; add a conversion path if needed |
| WAV, MP3, M4A, MP4, WebM | Audio extraction/transcription only after actual codec/size testing; original preserved |
| Other types | Policy-approved attachment storage; clear “extraction unavailable” state |

Every section should accept a contextual drop and offer **Attach only**, **Suggest fields**, or **Create record**. Review shows source file/page or audio timestamp, proposed values, uncertainty, duplicate warnings, target hotel, and changed totals. Nothing inferred silently becomes a contracted rate, date, signature, or saved business fact.

Start with DOCX, XLSX, CSV, PDF and JSON backup exports, plus original attachments and transcript TXT/VTT/SRT where supported. A PDF is a presentation artifact; a DOCX is editable; neither guarantees round-trip layout fidelity. Test actual work templates rather than promising arbitrary conversion.

## Section-by-section upgrades

| Existing section | Upgrade |
|---|---|
| Command Center | Today’s most valuable actions, production coverage/as-of date, at-risk account reasons, RFP deadlines and quick capture |
| Import Center | One inbox for files/screenshots/audio, resumable jobs, processing location labels, review, provenance and duplicate detection |
| Daily Checklist | Generate tasks from actual follow-ups, cutoff dates and missing reports; distinguish suggested routines from company requirements |
| Activity Log | Voice-assisted drafts, contact matching, next-action extraction, source timestamps, and a clear status for items still needing entry into Delphi |
| Pipeline | Stage history, expected room nights and net value, next step/owner, confidence and lost-business reason; preserve actual vs weighted projections |
| RFPs & Leads | Due-date queue, reusable property fact library, draft answers with evidence, and comparison against bid constraints |
| Accounts & Contacts | Company aliases, contact roles, linked stays/groups/calls, relationship timeline and source-backed outreach drafts |
| Group Deal Check | Night-by-night contribution scenarios, explicit assumptions, rate floors configured by the property, approval notes |
| Revenue Explorer | Source reconciliation, company/rate-code drill-down, import coverage, exportable views and saved comparisons |
| Revenue Meeting | Meeting brief built from current figures, exceptions, decision log, assigned actions and later outcome tracking |
| Sales Calendar | Combined deadlines, group cutoff/arrival, renewals, follow-ups and site tours; export calendar events |
| Displacement | Preserve existing model, expose costs/assumptions and sensitivity ranges, require complete demand inputs |
| Group Pace | Compare equivalent snapshots and stay periods; show pickup, wash and forecast separately with source dates |
| BT Accounts | Corporate production history, same-period comparisons, watchlist and recovery workflow |
| STR Report | Explain MPI/ARI/RGI with the actual reporting period, coverage and actions; avoid presenting correlation as cause |
| Rate Shop | Normalize room type, dates, taxes, breakfast, parking, refund terms and observation time; expire stale observations |
| Hayden’s Reports | Keep tested GRO/pickup/wash parsers; add versioned mappings and visible totals/reconciliation |
| Weekly Sales Report | Draft from recorded activity and verified production; show missing data and review before export |
| GM Owner Report | Concise executive view with actual/forecast/budget labels and linked source totals |
| Contract Maker | Versioned templates, safe merge fields, signature placement, PDF preview, approval history and final document lock |
| Action Plan | Link actions to accounts/opportunities and verified outcomes; separate estimated revenue from booked/realized revenue |
| Delphi Import | Mapping preview, repeat-import detection and reconciliation; do not imply two-way sync or completed Delphi entry |
| Bonus Tracker | Configurable plan versions, actual/potential distinction and import provenance; verify against the employer’s plan |
| Coach | Recommendations grounded in imported evidence and your property facts; no invented prospects, contact details or business claims |
| Settings & Data | Property setup, storage/backup health, processing permissions, export/restore and visible data retention controls |
| New: SRP & Group Vault | Search codes by group/company/hotel/stay dates; copy code, link confirmation source and track expiry/last verification |
| New: Templates & Bid Library | Contracts, RFP answers, proposals, rate letters, site-tour follow-ups and approved clauses, searchable by property and version |
| New: Call Desk | Start a memo, upload an existing recording or add notes; preview transcript and proposed account/activity/RFP fields |

Chloe’s companion report expands the workflows and acceptance criteria.

## Corporate account radar: useful evidence, not a guessed sales score

Keep dated production snapshots with account ID/aliases, hotel, stay period, room nights, room revenue, source report, import timestamp, cancellations and coverage. SRP codes are identifiers, not proof that two company names are the same account.

- **Declining production:** configurable starting rule of at least 20 baseline room nights, a decline of at least 25%, and at least 10 lost room nights across a comparable 28-day period. Display current/baseline RNs and revenue. Do not activate until coverage is complete. Align weekdays and use STLY or seasonal comparisons when available.
- **New to hotel records:** first observed in a sufficiently complete history, with a visible lookback window. Never relabel this as a newly founded business.
- **Reactivated:** returning production after a configurable inactive period; exclude missing-report gaps.
- **Opportunity:** recovering lost room nights might fill soft dates, but requires inventory, displacement and margin checks before proposing a rate.
- **Contact stale:** separate relationship age from production decline. No contact in 45 days does not prove lost room nights.

Each alert needs **Why this appeared**, **Show source rows**, **Assign next step**, and **Snooze/dismiss with reason**. Offer an outreach draft; sending remains the user’s action. Public prospect discovery should save the business/source/date and require verification of the decision maker. Do not invent direct emails or access private Hilton records.

## SRP, contracts, and signatures

The SRP vault should store hotel, code exactly as text (including leading zeroes), group/account, booking link if permitted, arrival/departure, cutoff, negotiated terms, source and last verification date. Permit the same code at different hotels or date ranges. Require verified entries before merging into a contract. Never store Hilton passwords here.

The template library should preserve originals and versioned approved clauses, support previews and merge-field validation, and show outstanding blanks before export. Drafting is not authority to approve rates, clauses or sign on someone else’s behalf.

Add a **My Signature** tray with a few locally bundled, licensed cursive fonts, a drawn signature and an uploaded transparent signature. Let the user drag their own signature onto designated fields, resize it, preview, and explicitly apply it. Applying a cursive image is not the same as an independently verifiable signing workflow. Reserve signed document hashes, consent/version audit records and recipient signing for a later dedicated signing integration if needed.

## Delivery order and acceptance gates

1. **Stabilize:** fix the reproduced defects; add regression tests; replace vulnerable parsing dependencies; verify backup/restore. Gate: malicious field keys, overlapping hotel saves and storage failures cannot silently corrupt or expose data.
2. **Personal local-first foundation:** preserve visual design, split modules, migrate sample/local data transactionally, add responsive PWA shell and local processing indicators. Gate: reopen and restore work offline; no silent external transmission.
3. **Highest-value sales tools:** SRP vault, template library and longitudinal account radar. Gate: importing the same report twice cannot double production, periods reconcile, and alerts explain their evidence.
4. **Capture and output:** unified contextual drop, complete-document handling, screenshot OCR, DOCX/XLSX/PDF exports and local voice draft workflow. Gate: representative sanitized work files and known-answer recordings produce reviewable accurate drafts.
5. **Optional expansion:** second-hotel migration, optional cross-device sync, approved live connectors and advanced signing. Gate: property isolation and actual authorization verified; no shared credentials or assumed private APIs.

Do not install whole CRMs, automation servers, and document suites merely because they are popular. Integrate a small number of libraries into the existing workflow; add a service only when a measured need justifies its administration and data access.

## Team and review record

Marcus coordinates decisions. Eliza reviewed design and mobile screenshots. Aaron researched public repositories, licenses, maintenance and issue reports. Amad traced security/backend risks and reproduced isolated failures. Chloe reviewed the sales workflows and differentiators. The Breakers ran existing suites and additional adversarial probes. Their reports are linked separately.

No application features were implemented, no files uploaded to an AI vendor, no Hilton-system access attempted, no outreach sent, and no production deployment performed. GitHub source research is not a benchmark of your files or a license/security approval for your employer. New dependencies should be pinned and audited when the implementation is selected.

## Validation and team deliverables

All nine supplied suites completed with exit code zero on unchanged handoff code, using system Chromium and adapted harness copies outside the handoff. The scripts are largely log-oriented; their successful exits are not equivalent to comprehensive assertions. Observed results include **720 reconciliation checks with zero failures** and **259 button clicks with no logged runtime errors**. Synthetic imports, expected displacement cases and mocked host workflows were exercised. New browser/function probes exposed defects beyond baseline coverage. No real transcription, Hilton integration, production data or live multi-device sync was validated.

- [Aaron: repository research, licenses and source evidence](aaron.md)
- [Eliza: design, mobile review and section-level UX](eliza.md)
- [Amad: security, backend and local-first architecture](amad.md)
- [Chloe: sales workflows, Account Radar rules and backlog](chloe.md)
- [The Breakers: executed suites, adversarial probes and limits](breakers.md)
- [Current desktop screenshot](eliza-desktop.png)
- [Current mobile screenshot](eliza-mobile.png)

No extra team members are needed for the next scoped build. A dedicated integration specialist would become useful only after approved vendor API documentation and access are available.
