# Sales Command — complete local sales workflows

The three previously proposed innovations are implemented in this update: Deal Package, Need Date Matchmaker and Repeat Business Memory. The Pittsburgh themes, stadiums, local transcription, document tools and existing reports remain included.

## Start with a conversation

In Call Desk, open a recording/transcript or paste call notes, then choose **Build linked Deal Package**. You can also open **Deal Package** directly or choose it as the destination in **Import Station**.

Paste/drop the whole conversation and choose **Build one review**. Review the company/contact, stay dates, room allocation and rate together. Confirm whether a stated room count applies to every night, or enter the explicit nightly counts. Missing/uncertain facts stay unresolved. Choose a next step and its due date. Select an existing prospect only when you mean to update that record; replacement needs explicit approval.

The completed-call box starts off. Check it only for an actual completed call, then review its date, category and result. A previously logged source cannot count as another actual call, and an identical conversation with an applied package cannot create a duplicate package.

One approval saves the linked prospect, pipeline opportunity, unsigned contract draft, planned next step and report source. Contract terms, billing, taxes and signatures require their normal review; this action neither sends nor signs anything. Open **Follow-ups & History** to complete the planned task with the actual result/date. That completion enters Activity Log and the proper reporting week once.

Receipts show before/after changes. **Undo this update** reverses unchanged linked records while preserving unrelated work. Undo stops when those records were edited or later work depends on them. The original source and audit receipt remain available locally.

## Match requests to slower nights

Open **Need Date Matchmaker**, or send a forecast there from Import Station. Import a CSV/XLSX daily forecast, map the date, capacity, forecast rooms and optional room-type/minimum-rate columns, and explicitly review the source name and as-of date. Manual daily rows are available too.

Approved nightly requests from Deal Package are available without retyping. For other prospects, review their exact dates and nightly counts. A room-night total is not spread across nights automatically. Matching a typed request requires a matching room-type forecast; total hotel capacity alone does not confirm King/Queen availability.

The result shows requested nights, softer-night overlap, forecast headroom, pressure and missing information. Stale forecasts and incomplete requests stay unranked until reviewed. Edit/copy the outreach draft or create a planned follow-up. No contact is marked completed, no price is approved and no inventory is held. Forecast headroom is sourced planning context, not live PEP availability.

## Remember and re-earn past business

Open **Repeat Business Memory** and choose a past source group/contract or a manual historical closeout. Review the past stay and declared/contracted comparison, then enter actual production from a stayed-production report. An actual-production CSV can populate candidates; the review still requires the stay, totals, source and as-of date. Blank actuals remain unknown, not zero or the contracted amount.

Save the actualized-versus-declared comparison, organizer/business preferences, outcome and service follow-through. The reviewed closeout summary joins the weekly highlights without adding a completed call. Set the next planning window, lead time and reminder date. Due reminders appear while this app is open; this is not a background notification service.

When an organizer confirms new dates, choose **Re-earn this account**. Enter a new event/season name and confirmed arrival/checkout dates. This creates a fresh linked prospect/opportunity once per named cycle. Last year's room counts, rates, revenue, signatures and dates are not copied forward as confirmed facts.

## Import Station and next steps

Import Station now routes prospect lists, Lighthouse BT reports, conversations, forecasts and closeout CSVs into their appropriate review screens. File Inbox still retains other document formats; extraction support varies. **Follow-ups & History** brings planned tasks from all these tools together with their receipts.

Weekly Sales Report keeps its established Excel, email-text and Print/PDF exports. Dated completed work, clearly labeled draft preparation and reviewed closeout highlights use the same report data. Planned work does not inflate completed activity counts.

## Update the installed M1 app

1. Export an encrypted backup from the installed app's **Device & Backups**.
2. Stop its launcher with Control-C and close every Sales Command browser tab.
3. Extract this new ZIP into a separate folder.
4. Run **update-mac.command from the new folder**, then select the **old installed Sales-Command folder**.
5. Start **start-mac.command from the old installed folder**. Keep the same browser profile and `http://127.0.0.1:4173` address.
6. Open once with the local server running, close all app tabs, then reopen to activate the updated offline build.

The updater replaces the app build, retains a recovery copy, and preserves the existing transcription helper/model/token. Do not rerun speech setup just to apply this app update. Browser data remains at its existing origin. All new business data and receipts are included in encrypted backups.

Automated checks use synthetic inputs and Chromium. Review an actual authorized Lighthouse/production export against its source and inspect your final Safari PDFs before using them for work. These tools do not log into or write back to Hilton systems. New workflows use local rules and existing local parsing, without downloading another AI model or introducing a cloud AI provider.

See DEAL-PACKAGE.md, NEED-DATE-MATCHMAKER.md, REPEAT-BUSINESS.md and INNOVATIONS-VALIDATION.md for detailed behavior and verification.
