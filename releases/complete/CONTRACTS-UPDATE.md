# Professional contracts and whole-conversation filling

## What changed

Contract Maker now has shared professional typography, navy headings, blue rules, pale contact panels and clearer tables. Existing standard group and corporate agreements retain their wording. An explicitly selected **Courtesy room block · professional layout** follows the supplied reference's visual hierarchy with numbered sections, a stay-date grid, a room-rate table, repeated print headers/footers and an acceptance area. It uses text branding; the supplied PDF's logo, client information and signature were not copied into the release.

Courtesy is an alternate agreement with its own terms, not merely a cosmetic style. It is available only when the block is set to Courtesy (no attrition). Review its six required term sections for your property and confirm approval before exporting. Applicable taxes and governing law are not copied from another property. Changes to the contract or hotel details invalidate that approval until you check it again.

Your own explicit Hotel Sign action still appears in the new template. Client signature lines remain blank. This is a visual signature appearance, not certificate-backed or authenticated electronic signing.

## Fill a contract from a whole conversation

1. Open **Contract Maker** and open/create a group or corporate draft.
2. Paste the entire transcript or inquiry into **Fill a contract from the whole conversation**, or drag/drop plain text or a text file there.
3. Choose **Review all proposed fields**.
4. Review the proposals together. Existing filled fields need explicit replacement selection; room rows require explicit rate/count/nightly allocation confirmation. Missing years, ambiguous numeric dates and conflicting facts are left unresolved.
5. Select **Apply reviewed fields together**. The checked changes apply atomically to that draft. You do not copy each field separately.

From **Call Desk**, open the recording or notes review and choose **Use whole transcript in Contract Maker**. This transfers the complete current transcript. **Copy all / drag transcript** also copies the entire text for external paste/drag. If no draft is open, the complete text waits in Contract Maker while you create one. The contract draft type is your choice.

The local extractor supports company/event, contact details, arrival/checkout, explicit cutoff/hold dates, codes and room/rate proposals. Example:

```
Company: Example Field Services
Event: Summer Training
Contact: Morgan Lane
Email: morgan@example.test
Phone: 555-010-0199
Arrival: June 4, 2027
Departure: June 6, 2027
10 King rooms at $149 per night
8 double queen rooms at $159 per night
```

All fields are still reviewable. The room table is not allocated automatically: confirm that those counts apply every occupied night, or enter exact dates/counts. Total room nights alone do not prove a nightly block. “May 11–12” does not establish a year or whether May 12 is checkout, so it requires confirmation.

No transcript changes legal clauses, billing, taxes, signing status or signature marks. A signed contract must be duplicated into a draft. Changing the hotel, selected contract or underlying draft while review is open prevents applying stale changes. Original text is retained locally with a source hash/reference, outside printed clauses.

## Updating the installed Mac app

1. In your current app, export an encrypted backup from **Device & Backups**.
2. Stop the old launcher with Control-C in its Terminal window and close the app's browser tabs.
3. Download/extract the updated ZIP into a separate folder. Do not replace the existing installed folder in Finder.
4. In the NEW folder, run **update-mac.command** and choose your EXISTING installed Sales-Command folder when prompted.
5. Run **start-mac.command** from your original installed folder.
6. Open the app once while online, then close all Sales Command tabs and reopen it so the updated offline cache can activate.

The updater replaces only `dist`, verifies its copied files, and keeps a backup of the old app files. It does not remove/reinstall your speech engine, downloaded model, private pairing token or browser database. Keep using the same `http://127.0.0.1:4173` origin; changing hostname or port creates a separate browser workspace. The updater was functionally tested against temporary folders; its macOS folder-picker launcher was syntax-checked, not executed on a real Mac in this cloud.

## Validation limits

Read CONTRACTS-REVIEW.md and CONTRACTS-VALIDATION.md for exact test results. Automated PDF/browser checks use Chromium; Safari's print pagination or page-number support can differ. Inspect your PDF preview before sending an actual contract. Exact pixel matching, original PDF editing and automated legal approval are not included.

The updater uses two directory renames with rollback on ordinary errors. A power loss or forced termination between renames can leave the main dist folder missing; the prior app files remain under `.app-backups/<id>/dist` and can be copied back if the main dist is absent. This is an app-file recovery copy, not a replacement for the encrypted browser-data backup.
