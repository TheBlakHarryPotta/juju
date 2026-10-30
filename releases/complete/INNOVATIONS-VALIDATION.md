# Three innovations: integration and transaction validation

Validated October 30, 2026 using Node 24 and Linux Chromium. All new records, transcripts, contacts, forecasts and closeouts were synthetic. The private reference PDF and live Hilton systems were not used.

## Final result

The authoritative final full run completed **181 passed, 1 existing skip, 0 failed and 0 flaky cases**, from **182 cases in 21 files**, in **405.4 seconds**. Result: `test-results/innovations-authoritative/results.json`. This run includes the final planning-counter, source-selection, Pipeline compatibility and hotel-loading fixes and supersedes the earlier diagnostic runs. The one skip remains the retired v3 Claude-host screenshot tray; local extraction/OCR tests cover its replacement.

```sh
npm run build
SC_TEST_OUTPUT=test-results/innovations-authoritative npm test
```

A final check against the rebuilt production preview also passed **4/4 cases in 22.1 seconds**: encrypted restore/guarded undo, package-to-CSV forecast matching, actual closeout/reminder/new-cycle creation, and complete phone review with populated desktop/phone views. Result: `test-results/innovations-production-final/results.json`. These are four cases already included in the full suite, not additional unique tests. The six QA screenshots linked below were refreshed from this production run and visually inspected.

The new work adds **55 cases** to the prior 127-case catalog: 10 Deal Package cases, 15 Need Date model/import cases, 8 Repeat Business cases, 8 transaction cases, 8 connected integration cases, 3 Pipeline compatibility cases and 3 manual-source selection cases. These include domain assertions and actual browser workflows. Preliminary focused runs are diagnostic evidence, not extra unique cases added to the full result.

The production build transformed 336 modules. It succeeded with two advisories: the document-processing bundle exceeds Vite's chunk-size recommendation, and a dynamic import of intake cannot create a separate chunk while intake is also statically imported. Neither advisory is a build failure or a measured device-performance result.

## Connected journeys demonstrated

| Journey | Actual verification |
|---|---|
| Whole Call Desk conversation | The entire edited transcript opens one Deal Package review. Opening or canceling review creates no sales drafts. One approval saves the linked prospect, Prospect opportunity, unsigned Draft contract and planned task in exactly one durable snapshot revision. The original conversation remains local. |
| Room block and code | Ten King rooms on each of two explicit nights at $149 become 20 room nights and $2,980 proposed room revenue. The contract retains group code `00123` as text. Uniform nightly allocation and occupancy require explicit review; missing/tentative dates and alternative prices stay unresolved. This does not create a separate SRP Vault record automatically. |
| Actual contact versus preparation | A package without an explicitly confirmed call contributes a dated preparation highlight and zero completed calls. Explicit actual-call review produces one categorized call and one canonical reporting source. A previously logged Call Desk source cannot be counted again. An applied identical-conversation package cannot be replayed; safe undo permits rebuilding. |
| Reporting while viewing history | Creating a package with an older report week selected leaves that selected week unchanged. Its preparation highlight appears exactly once in its actual creation week, not the older week, and does not invent an actual call. |
| Forecast matching | The package's approved King allocation flows directly to Need Date Matchmaker. A real CSV supplies capacity 40 with forecast 20 and 25 on the two nights. All 20 requested room nights fit the entered soft-night headroom, producing 100%. No second manual copy of the nightly request is needed. |
| Forecast uncertainty | Missing nightly or room-type evidence, unreviewed requests, stale sources and other hotels do not become scored fits. Actual XLSX import retains sheet/hash/source-row evidence. Scores use reviewed forecast headroom, not live availability, a hold, approved pricing or a guarantee. |
| Outreach and actual follow-through | Matchmaker outreach stays an editable draft. Saving it makes one planned task and does not mark the prospect contacted. Repeat saves are blocked. The shared Follow-ups view rejects future “completed” dates; one actual result creates one dated follow-up activity. That later work prevents undoing its original package. |
| Actuals and repeat business | A past package with contracted 20 RN / $2,980 remains unchanged when the closeout records explicit actual 18 RN / $2,682 / $149 ADR. Source and as-of date are retained. Contracted production never autofills actuals. An explicit reminder becomes due in the app without logging a contact. |
| Fresh planning cycle | A new repeat opportunity requires newly confirmed future dates. Old quantities, rates, revenue, contract clauses and signatures are not copied. Reusing the same cycle name preserves one opportunity/prospect rather than creating another. New memories, cycles and receipts survive encrypted backup/restore and reload. |

## Pipeline and existing sales tools

The new records also pass actual editing checks in the older Pipeline UI. A known 10-King-per-night package shows its confirmed mix and $149 rate. Editing the rate to $159 updates 20 RN / $159 ADR / $3,180 stored revenue and transfers the current two-night counts/rate to the enhanced Deal Checker. A mixed King/Double-Double source preserves all 30 RN and both original room types in an explicit review editor; it is not partially mapped or mislabeled as Queen. A fresh repeat opportunity starts unallocated; after the user explicitly enters five King rooms over two nights at $149, its stored revenue becomes $1,490. Existing manual revenue overrides remain preserved. Moving either booking to Definite does not mark an unsigned contract Signed.

## Atomic save and guarded undo

The transaction tests verify durable state as well as the displayed state:

- A forced database write failure publishes no partial linked records or receipt, preserves the previous durable snapshot, releases the interface lock and permits a successful retry.
- Linked records and their receipt share one revision-checked snapshot. Stale review snapshots, foreign hotels/sources, forbidden settings changes and attempts to sign or modify signed contracts are rejected before publication.
- Undo finds records by ID, preserving unrelated later work and array insertions. A changed owned record rejects the entire undo; it does not delete the remaining linked records first.
- New historical work referencing an owned record blocks undo rather than leaving an orphan. This was checked both directly and with a real Repeat Business closeout linked to the package opportunity.
- Receipts survive page reload and authenticated encrypted backup/restore. Guarded undo still works afterward. Original source attachments remain as evidence when a package is undone or a business save fails.

## Defects caught and corrected before the final run

**Delayed hotel load could erase a committed package.** QA held an old hotel snapshot while a linked update committed in that hotel, then released the old load. The earlier code replaced the new live state, and an ordinary later save could lose the update durably. The regression reproduced this with synthetic data. The fix marks hotel loading as an active operation, blocks editing/linked updates during that interval and retains the existing generation guard for newer hotel-switch requests. The final race check accepts an explicit loading rejection or consistent preserved data; it never accepts silent loss.

**Existing call source could count twice.** Exact original source IDs/file IDs now prevent logging another actual call when a previously reviewed Call Desk source becomes a package. The user can leave actual-call logging off and explicitly link the existing prospect to create only the new drafts. Identical-conversation hashes also prevent replaying an already applied package.

**Generated plans were being counted as inquiries by an older rule.** Restoring the legacy source enum exposed those records to Pipeline’s ordinary inquiry counter. The final rule excludes only explicitly marked Deal Package and Repeat Business planning records. The focused UI test also creates a real ordinary inquiry with source Other and verifies it still counts once.

**Manual report sending could choose another record’s source.** Source lookup now requires the selected record’s canonical key or a real linked activity ID. Distinct prospect, package/call and derived-RFP cases verify the correct reporting source.

**Package highlight could be stranded in an old selected week.** Package-generated highlights now follow their actual preparation date, while ordinary manually scoped report highlights retain their existing rules.

Compatibility review also found that new UUID-based bookings bypassed old recalculation patterns, and that the older booking editor could not represent some approved room types. The shared compatibility fixes preserve unsupported types explicitly, keep current counts/revenue consistent, and stop booking status from silently signing a contract.

Other focused checks cover strict date validation, explicit actual-production coverage and duplicate planning-cycle identity. One early integration selector was corrected to reopen saved manual call notes from File Inbox, matching the application's existing guidance; Call Desk's list contains recordings. An earlier durable-state assertion compared the database to a different live baseline; it was strengthened to compare the full durable row before versus after rejected changes, including revision, with the preceding save settled. No guard was disabled to make a test pass.

## Visual evidence and practical limits

QA completed the entire package review at 390 px, then inspected all three populated views at desktop and phone sizes. Separate design review used the rebuilt production app. Screenshots contain only synthetic business information.

- [Deal Package desktop](screenshots/innovations-deal-package-desktop.png) / [phone](screenshots/innovations-deal-package-phone.png)
- [Need Dates desktop](screenshots/innovations-need-dates-desktop.png) / [phone](screenshots/innovations-need-dates-phone.png)
- [Repeat Business desktop](screenshots/innovations-repeat-business-desktop.png) / [phone](screenshots/innovations-repeat-business-phone.png)

Phone coverage is a 390 × 844 Chromium viewport, not physical iPhone/Safari certification. No M1 speed, battery, speech-recognition accuracy or live Hilton connectivity benchmark is claimed. Import review and source quality remain material to the results. No email, contract, inventory hold or external system update is sent automatically by these journeys.

Previous PDF, file extraction, OCR, offline, property isolation and sales calculation checks remain part of the full run. Existing test adaptation and the sole retired-host workflow skip are documented in [VALIDATION.md](VALIDATION.md).
