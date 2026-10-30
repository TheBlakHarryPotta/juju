# Sales Command — Pittsburgh edition

This update changes the full application shell and adds local sales workflows. It preserves the existing contract maker, transcription helper, hotel workspaces and encrypted-backup workflow.

## Appearance

Use **Make it yours** in the sidebar or the palette button in the header. Choose Steel City (black/gold), Three Rivers (navy/teal with riverfront stadiums), Foundry (warm copper) or Sunday Morning (light). Three Rivers includes an original PNC Park-inspired ballpark and Acrisure-inspired football stadium; both fit the phone scene. Motion can be disabled; the device's Reduce Motion setting takes priority. The Pittsburgh illustration is original artwork inspired by the city's bridges and skyline, not an official branded asset.

## Your daily flow

1. Open **Import Station**. Choose **Prospect pipeline**, **Lighthouse → weekly BT Update**, or **File Inbox / Call Desk / Contract review** before adding the source.
2. Drop a CSV, TSV or XLSX table, or paste the entire table copied from Excel. Review the column mapping and source rows. Missing contact or stay details remain blank. Confirm the source's date order; the application does not guess two-digit years or ambiguous dates.
3. In **Prospect Pipeline**, record status, contact details, requested stay dates, next step and follow-up date. **Log actual contact** records completed work. Changing a status alone does not count a call.
4. In **Tours**, track inbound and outbound visits; in **Networking**, track introductions and events. Plans remain separate. Complete a meeting with its actual date/result to add one linked Activity Log entry. Editing that meeting updates its linked record.
5. Saved new RFPs and reviewed calls become source-linked prospects. Undated historical RFPs remain undated; an uploaded audio file alone never creates a completed call. Select Activity Log or RFP / lead when confirming the reviewed Call Desk draft, or choose Prospect pipeline explicitly.
6. Open **Weekly Sales Report**. Saved dated work feeds the established preview, Excel export, email text and Print/PDF. Completed contacts and prospect identification are labeled separately. Use record **Send to weekly report** buttons when needed. A section-wide fallback opens a summary/date review and adds a highlight without increasing activity counts. Repeat sends use stable source IDs.
7. **Check for duplicates** shows possible repeated sales records. Prospect checking also compares normalized email, phone and company/contact. Nothing is automatically merged or deleted. Reimporting an identical source row is skipped.

## Lighthouse: past week versus last year

Map Account / segment, current room nights and current room revenue. Optional current ADR is checked against revenue divided by room nights. Map last year's room nights and revenue when present. Confirm the exact seven-day source period, **Same week last year**, and the report ending date. No live Lighthouse login or direct connection is used.

The BT Update shows the account/segment, period, room nights, revenue, calculated ADR, and available comparison changes. Missing comparison data remains unavailable; absent accounts never become zero automatically. Total rows are excluded. Duplicate account rows require source cleanup rather than automatic summing across potentially overlapping segments. A reviewed correction can replace the same period, including a corrected mapping of the same original file.

The exact layout of your own Lighthouse export still needs verification against a sample. CSV, TSV and XLSX with a clear table header are supported here. PDF/Word/images use the existing local File Inbox extraction/OCR first; complex or partially extracted layouts need a complete tabular export before bulk import.

## Stronger Group Deal Checker

The main **Group Deal Checker** opens the enhanced model. Pipeline's check button transfers known group details; missing nightly allocations are left blank. Enter nightly rooms/comps, sellable inventory and forecast without the group, alternative ADR, actual costs, commissions, rebates and concessions. Explicitly enter zero when a cost does not apply.

The checker calculates room revenue, contribution after entered costs, displaced alternative contribution, break-even/target rate floors, night-level pressure and downside scenarios. Results are contribution estimates, not hotel net profit or automatic rate approval. Changed inputs require recalculation before export. Saved checks are local to the hotel and included in encrypted backups.

## Install this update without reinstalling transcription

1. In the old app, export an encrypted backup from **Device & Backups**.
2. Stop the old launcher with Control-C and close all Sales Command browser tabs.
3. Extract the new ZIP into a separate folder. Do not replace the installed folder in Finder.
4. Run `update-mac.command` from the **new** folder and choose the **old installed Sales-Command folder**.
5. Start `start-mac.command` from that old installed folder. Keep using `http://127.0.0.1:4173` in the same browser profile.
6. Open once while the app server is running, close every app tab, and reopen so the offline update can activate.

The app-only updater replaces `dist`, preserves the existing transcription model/helper/token, and retains the previous app build under `.app-backups`. Browser data stays in its existing origin. The macOS folder picker and Safari printing require a real Mac check; cloud automation uses Chromium. Review the final contract/report PDF before sending it to a client.
