# Pittsburgh sales update: security and reliability review

Scope: destination-aware local prospect/report intake, property-scoped sales workflows, weekly-report integrity, and deal-checker integration. Review and assertions used synthetic businesses and reports. All concrete integration findings raised in this review were corrected. No critical implementation blocker remains from these checks.

This does not establish access to Hilton private systems, approval of hotel policy, or correctness against a real vendor export that has not been supplied and validated.

## Changes reviewed

- New data remains in the existing property snapshot/database tables, so normal encrypted backup and restore includes prospects, sales workflows, source attachments and BT imports.
- Commit APIs accept an expected property and reject a changed hotel before mutation. Imported fields cannot select an arbitrary property or generated record ID.
- Table headers map to fixed fields. Unknown headers such as `__proto__` or `propertyId` do not become object paths, metadata or executable code.
- Prospect names and notes are escaped as text in review and display. Prospect import does not mark contacts completed. Follow-up planning also does not create completed activity.
- Canonical source keys prevent an activity plus its derived prospect, an RFP plus its derived prospect, and a repeated report pin from becoming duplicate underlying work. Manual summaries/snapshots are labeled separately from actual contact counts.
- Lighthouse imports retain their source period, comparison label, source reference and explicit mapped values. Missing comparison values are not invented as zero. An exact repeat is a no-op; corrected values for an existing period require explicit replacement approval.
- CSV/TSV/text table imports read the original bytes. They do not mistake the File Inbox's intentionally truncated preview for the complete report. Partial non-text extraction is rejected as a complete table source.
- Import limits include file size, table length, row/column/cell bounds, validated Office archive limits and the shared attachment budget. Oversized originals are rejected before retention.
- Manual section highlights bind the property and report week around asynchronous hashing, keep review consent, and block restore while processing. A closed review cannot apply later.
- New deal-checker input paths allow known fields and explicit numeric values. Invalid types are rejected rather than silently treating a boolean or object as a financial zero. Results explain input assumptions and do not represent hotel quote approval.

## Findings corrected during integration

| Concrete issue | Correction and evidence |
|---|---|
| A caller-supplied planned-task `id` or `propertyId` could overwrite the generated envelope because the draft was spread last. | The bridge now builds a known-field payload and its own envelope. Browser assertion verifies either rejection or a generated ID in the active property; current implementation preserves the correct envelope. |
| Weekly-model RFP rows dropped their property field before the shared property filter, allowing a foreign synthetic RFP into the requested hotel's feed. | Foreign RFPs and foreign linked activities are excluded. The pure-model regression passes. |
| A saved call/RFP and its automatically derived prospect could produce two entries for the same underlying source. | Derived identification is omitted when its canonical actual call/RFP is present. Executed synthetic model assertions verify one entry for each source. |
| Re-importing the same BT file could return early even when the user changed mapping and explicitly approved a correction. | Exact no-op detection now includes the mapped rows, comparison and report end. UI test confirms changed mapping is blocked without replacement consent and updates the single existing period after approval. |
| A valid CSV larger than 200,000 characters could be parsed from the truncated Inbox preview, dropping later records. | Table intake now decodes original text bytes. A real browser import retained all 400 synthetic records while confirming that the separate Inbox preview was shorter than the original. |
| A pending text hash was not counted as a busy import job. | Text reads use a busy/finally guard, and restore checks specialized import/report busy states. Property checks repeat after hashing. |
| An older hotel switch could finish loading B after a newer switch to C, then apply B's snapshot under active hotel C. | Switch-generation and target guards now repeat across flush, legacy switching and snapshot loading. Browser regression delays B, completes C, releases B, and verifies both the active and durably saved C state remain C. |
| An optional RFP-to-prospect sidecar could throw after the main RFP had already been saved, encouraging duplicate retries. | Main RFP saving no longer throws from that sidecar step. Prospect synchronization occurs separately with error isolation. Reviewed in current bridge code. |
| A manually added summary could be counted in a feed tile labeled actual activity. | Summary/snapshot metrics are separate from actual inquiry/contact records; underlying completed-activity counters remain unchanged. |

## Executed tests

The final 12 unique cases in `tests/sales-security.spec.js` passed across one 10-case run and two focused single-case runs:

1. Caller-supplied planned-task property/ID cannot forge the saved envelope.
2. Planning creates no completed activity; repeating completion creates no second activity.
3. A file over 25 MB is rejected before retaining an original.
4. All six tested commit/completion APIs reject an obsolete expected property without changing active-hotel state.
5. The weekly model excludes foreign-property rows and deduplicates report pins.
6. Hostile headers map only to fixed prospect fields; source names/notes remain plain data.
7. Table/cell bounds and missing/fractional/ambiguous values are rejected; explicit numeric zero remains valid.
8. A hostile image-like company name renders literally, executes no handler, makes no external HTTP request, and is absent from a new hotel's prospect list. A stale-property import is rejected.
9. A corrected BT import requires replacement approval, replaces one period, and survives encrypted backup/restore together with a prospect and the generated weekly BT text.
10. A 400-row CSV is imported from its full original rather than the shorter Inbox preview.
11. During deferred manual-highlight hashing, restore is rejected and a property switch prevents the old highlight from being written into the new hotel.
12. A delayed older hotel load cannot overwrite the newer hotel's live or durable snapshot.

Additional direct assertions against the actual sales model confirm call/RFP-derived prospect deduplication and planned-tour exclusion. Static review also checked the new report/export provider wiring, source-period replacement, explicit source dates, escaped rendering, fixed-field inputs and device-local processing boundaries.

The first expanded browser run had a test-locator strictness error because existing sample RFP prospects added other headings. The selector was corrected to target the synthetic hostile name, and the corrected test passed. This was not an application XSS failure.

## Verification boundaries

These automated checks ran in Chromium with synthetic data. Phone viewport/workflow checks belong to The Breakers' separate results; they are not physical Safari/iPhone validation. Real Lighthouse/PEP/ProfitSword exports still require source-specific validation, including period definitions and any missing comparison columns. A label such as “same week last year” does not supply data absent from the file.

The hostile-import/local-only case intercepted foreign requests before they could leave the browser and observed none. This supports the tested import workflow; it is not a claim that every possible future action was network-audited. Local helper transcription, business websites and user-opened external links remain separate explicit operations.

Backup recovery was exercised for these new records at representative size. It does not establish that every possible maximum-size attachment collection fits browser memory. Keep a separately retained encrypted backup and validate recovery on the user's Mac before relying on the workspace for work records.
