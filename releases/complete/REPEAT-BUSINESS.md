# Repeat Business Memory

Repeat Business Memory closes the gap between a past room block and a new sales conversation. It records reviewed production, business preferences, a chosen planning window and a local reminder. It does not treat a contract as proof that rooms were occupied.

## Use the feature

1. Open **Repeat Business Memory** and choose **Review a past-group closeout**. Link an existing group/opportunity or contract, or enter a manual historical closeout. Selected source records can prefill the declared comparison and business contact; actual production stays blank.
2. Enter the completed stay dates, actual report name and report as-of date. Supply actual room nights and/or actual room revenue. Blank means unknown; enter a zero only when the source explicitly reports zero. ADR is calculated from supplied actual revenue and room nights when both are known. An explicit source ADR is checked against those totals. ADR is undefined at zero actual room nights.
3. Optionally import an actual-production CSV. The original is retained in File Inbox and can be downloaded from the memory. Import Station can also send a CSV directly into a fresh closeout review. Importing populates candidates; it does not save a closeout until you complete the event, dates, source coverage and review confirmation.
4. Add the organizer's business contact, relevant service follow-through, business preferences and previous outcome. Keep guest rosters, payment data and sensitive guest notes out of these fields.
5. Save the reviewed closeout. The memory distinguishes actual room nights, room revenue and ADR from the declared/contracted comparison, with differences and pickup percentage where the necessary inputs exist.
6. Choose **Plan reminder**. Enter a planning window, lead days and an actual reminder date. **Suggest reminder from planning window** subtracts your chosen lead days; you decide whether to save that suggestion. Planning dates are not confirmed stay dates.
7. When the organizer confirms a new stay, choose **Create next-cycle prospect**. Enter a next event/season name and the new arrival and checkout dates, and explicitly confirm those dates. The app creates one linked Prospect opportunity and a not-contacted prospect atomically. It does not copy old room allocations, rates, revenue, legal terms or signatures.

The next event/season name identifies the cycle within that memory. Reusing the same name, including case/spacing differences, returns its existing opportunity rather than creating another. If dates change, review the existing opportunity. If a linked record was removed, restore/review that history before retrying rather than silently rebuilding a duplicate.

## Supported actual-production CSV

Use a CSV under 2 MB, with at most 366 nightly rows or one summary row. Review the source figures and use nonnegative, finite numbers.

Summary example:

```csv
Actual room nights,Actual room revenue,Actual ADR
80,12000,150
```

Nightly example:

```csv
Date,Room nights,Room revenue
2024-06-01,40,6000
2024-06-02,40,6000
```

A nightly import must include every occupied night of the completed stay, including explicit zero nights. Checkout is not occupied. Duplicate dates, outside-stay dates and nightly totals that disagree with the reviewed totals are rejected. Use a reviewed summary when a full daily breakdown is unavailable. A summary column named only `Rooms` is ambiguous; use `Actual room nights` for a stay total. In a dated nightly table, `Rooms` may describe that night's occupied room nights.

Revenue may remain unknown while actual room nights are known, or vice versa. The app preserves that distinction instead of manufacturing a zero or reconstructing revenue from an old quoted rate. Contracted comparison figures are optional. All displayed currency follows the existing USD convention; this feature does not convert currencies or reconcile mixed-currency sources. Use matching units and currency for actual and contracted comparisons.

## Reminders and weekly reports

The due queue is local and property-specific. A notice appears when the app opens/resumes or the section is opened with due reminders. There is no background notification service, automatic email or automatic call. Lead days are configurable from 0 to 730; the default 180 is an editable planning example, not a hotel policy.

A reviewed closeout contributes one dated highlight to the weekly report for the review date. It explicitly identifies the past stay, the actual/declared figures, variances and source as-of date. Unknown figures remain unknown. Editing the same memory updates its single summary; it does not create another call or completed activity. Business preferences and internal service notes are not automatically copied into that financial highlight.

Creating a new confirmed-date opportunity marks that reminder as linked to an opportunity. It does not mark the organizer contacted or imply that the new block is sold. Schedule another reminder explicitly when needed.

## Persistence and integrity

Data lives in `state.repeatBusiness` inside the existing property snapshot:

- `memories`: reviewed actuals, supplied nightly rows, declared comparisons, contact/work notes, source IDs, source hash/as-of and reminder choices.
- `cycles`: stable cycle name/key, confirmed new dates, memory ID, new opportunity ID and new prospect ID.
- `settings`: the chosen planning lead-days default.

Mutations use the shared revision-checked atomic transaction service. Creating a cycle updates the memory, opportunity, prospect and cycle link together. There are no partial business outputs after a failed durable commit. Original source attachments are retained independently as local evidence. Property changes, stale record edits, inaccessible foreign-property sources and malformed dates are rejected. Imported text is rendered as text, not executable HTML.

Central **Follow-ups & History** provides the transaction history and eligible Undo actions. Undo is guarded against later edits and external references; it must not erase a closeout or linked business history created after an earlier package. A closeout links to past business; it does not modify or sign that past contract.

Encrypted backup/restore includes the property snapshot and retained source attachments. Keep the backup separately. Purging an original from File Inbox does not erase the reviewed closeout numbers, but its source download and source-validated closeout editing may require restoring that original.

Limits are 500 retained closeouts and 1,000 cycle links per hotel, a completed closeout span of at most 366 nights, and a new opportunity span of at most 120 nights. Archive work with an encrypted backup before exceeding those limits. A new prospect's zero-valued pipeline placeholders mean **unquoted**, not an approved zero-dollar rate.

## Developer API

`initRepeatBusiness({ SC, db })` registers view `repeatBusiness` and exposes:

- `SC.repeatBusiness.closeout(input, { propertyId, memoryId?, baseJSON? })`
- `planReminder(memoryId, { date, windowStart?, windowEnd?, leadDays }, { propertyId, baseJSON? })`
- `createCycle(memoryId, { label, arrive, depart, confirmedNewDates: true, notes? }, { propertyId })`
- `receiveFile(file, { propertyId })`, which opens a review without committing actuals.
- `memories()`, `queue()`, `weeklyHighlights(range)` and `isBusy()`.

Pure exports support strict closeout, CSV, cycle and variance validation. Root initializes the transaction service first and includes `isBusy()` in the global restore interlock. The module does not wrap the old workspace busy flag, which would otherwise make its own atomic transaction reject itself.

## Validation

The final dedicated suite, `tests/repeat-business.spec.js`, completed **8 passed** in Chromium. It exercises:

- Missing actuals, false/fractional values, impossible or overlong dates, contradictory ADR, incomplete/outside-stay/repeated nightly rows and unreconciled totals.
- Declared source values prefilled while actual fields remain blank.
- Reviewed CSV original retention/download, actual-versus-contracted variance and a due local reminder without completed activity.
- Confirmed future dates, no reused historical dates, unquoted output, and an idempotent repeated planning cycle.
- Foreign-property record/source rejection and encrypted backup restoration.
- Escaped hostile text, duplicate closeout rejection and stale edit rejection.
- Import Station's uncommitted CSV handoff and filtered source choices.
- One dated weekly closeout summary, preserved unknown revenue and no fabricated actual call.

An early handoff test exposed an initializer guard attempting to read a source from an absent existing memory. That was corrected and the complete eight-case suite reran successfully. These are synthetic Chromium checks. Real stayed-production mappings, physical Safari/Mac behavior and employer-approved retention practices still need the user's work-context validation.
