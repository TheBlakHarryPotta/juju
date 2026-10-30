# Personal sales workspaces

These views add local tools alongside the existing Sales Command sections. They do not log in to PEP, OnQ, Hilton Lobby, Delphi or other portals, and do not automatically write back to them. Select the correct hotel before importing work. A second hotel has separate records and files. Use Device & Backups to export recovery copies; browser storage alone is not a backup.

## SRP & Group Code Vault

Add a code exactly as shown in the approved source, including leading zeros. Record code type, company/group, booking validity, source and restrictions. A verified entry requires a source reference and verification date. Mark verified today records your own verification, not a live PEP check. Expired dates are visibly labeled. Search spans codes, company, names and notes. Copy the code or full instructions deliberately; review before sharing an internal code externally.

Duplicate code/type/validity periods are rejected within the current hotel. Editing preserves the record identity. Deletion requires an explicit second click.

## Templates & RFP Library

Save approved contract, corporate agreement, proposal, RFP and reusable answer text. Original attachments of any type can be retained up to 25 MB. PDF originals preview locally; other unsupported originals download for their normal application. DOCX sources have their text and merge fields inspected locally. Text/Markdown attachments can populate the text editor.

Use `{{contact}}`, `{{hotel}}`, `{{arrival}}` or other simple named placeholders. Preview generates friendly inputs from those tags. All merge values are required. Export merged DOCX produces a genuine `.docx` file. An attached DOCX merges its original layout; exports from other attachment types use the saved text instead. Text edits do not rewrite an attached DOCX original. Missing merge values, malformed DOCX tags and oversized expanded documents produce errors rather than partially filled output.

Each save retains the previous text, attachment reference, source and metadata in version history. This is a local drafting tool, not a clause-approval service. Keep an approved source and review the exact file before use. Printing exports the merged text layout, not the attached DOCX layout; use the original document application when exact DOCX print fidelity is needed.

## Account Radar

1. Export an authorized account-production CSV with headers and a complete reporting period. Prepare aggregate account rows, not individual reservation detail. Read CSV and map the account, room-night and optional revenue columns.
2. Set the period dates, source report as-of date and actual stayed versus on-the-books basis. Mark complete only after checking report coverage. Blank numeric cells are rejected; explicit zero is accepted. Same exact normalized account labels are summed; different aliases are not guessed to be the same company.
3. Review the first five rows, mapping and row count, then save. Exact file hashes plus period/basis are checked transactionally for duplicates. Importing cumulative overlapping reports does not add them together: comparisons use only the selected snapshots.
4. Choose the current and earlier baseline imports. Confirm comparable seasonality, definitions and basis. Trend alerts require complete, equal-length, nonoverlapping periods of the same basis. For OTB, verify equal lead time yourself; the tool does not have nightly snapshots to prove it.

Default decline rule: at least 20 baseline RNs, a drop of at least 10 RNs and at least 25%. Growth requires at least 10 more RNs and at least 25%. Reactivated means an explicit zero baseline, positive current production and an earlier positive observation. No row in an import is **missing**, never zero. First observed means first in available imported records, not a newly founded business or newly won customer. Verify seasonal/project changes before outreach. Comparison CSV includes sources, periods and explanations.

## Signature Studio

Paste reviewed contract text or use a merged text template. Enter your own name and choose locally hosted Allura, Great Vibes or Caveat. Explicitly add a typed signature, draw your own mark, or upload your own PNG/JPEG signature image (2 MB maximum). Drag to place and drag the corner handle to resize. The handle also supports arrow keys. A local saved draft retains text and marks for that hotel; unsaved content is cleared when switching hotels.

The preview has a fixed US Letter width so printed coordinates match. On a phone, scroll the paper horizontally. This first release supports one-page composed contracts; shorten/split a long document before placing signatures. Print / save PDF uses the browser's print dialog and keeps marks in their placed positions. DOCX export retains text and typed signatures at the end, but omits drawn/uploaded marks. Uploaded PDF editing/signing is not supported.

A cursive or drawn mark is a visual appearance. This tool does not provide recipient authentication, a signing audit trail or cryptographic tamper evidence, and saving a draft does not certify a signed agreement. Use your organization's approved signing process when those capabilities are required. No mark is automatically applied to an imported/duplicated template.

## Implementation boundaries

All workspaces use property-scoped IndexedDB records through Dexie. Files are local Blobs with SHA-256 provenance. Source text and user values are escaped before rendering. Saved marks allow only bounded numeric positions, three permitted fonts and PNG/JPEG data URLs. Template histories preserve previous records; concurrent edits are rejected when another tab changed the stored version. File/production operations capture the active property before awaits. Imported content never executes as code and no cloud AI is called by these workspaces.

### Acting on an Account Radar signal

Each account row offers **Plan follow-up**. Review its current/baseline room nights, revenue where supplied, report periods and source evidence. Add a contact you have verified, choose a due date and edit the neutral outreach draft. The app does not guess why production changed, invent a contact, or send anything. Use the explicit copy action when ready. Download the actual current/baseline source CSV from the comparison controls when that original is available.

**Save follow-up plan** stores a property-specific plan outside Activity Log. It does not count as a completed call or inflate activity reports. Outstanding plans appear in Account Radar. After doing the work, choose **Log completed follow-up**, enter the actual result and completion date, then save. That explicit action creates one completed Activity Log entry; repeated completion of the same plan is rejected. Source production IDs, period context and file references travel with the plan and completed activity. Plans and their sources are included in the normal hotel-state backup.
