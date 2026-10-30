# Need Date Matchmaker

Need Dates ranks reviewed prospect requests against a reviewed, dated forecast for the **current hotel only**. It answers which requests overlap the hotel’s softer forecast nights. It does not connect to live PEP inventory, hold rooms, promise room-type availability, set rates or estimate profits.

## Normal workflow

1. Add or import a prospect through Prospect Pipeline, or approve an explicit nightly allocation in a call package.
2. Open **Need Date Matchmaker** and load a forecast CSV, TSV, XLSX, XLSM or XLSB, or enter nightly rows manually.
3. Review the source name, report as-of date, fixed column mappings, room-type scope, capacity and forecast basis. Confirm that these prospects are not already included in the forecast.
4. Review a prospect’s full arrival/departure dates and requested rooms on **every** occupied night. An explicit 0 means no rooms requested that night; a blank means unknown.
5. Inspect ranked fit cards and the separate Needs Review list. Source dates, period, row references, requested rooms, capacity, forecast headroom and pressure are visible.
6. Open an editable local outreach draft, review it and save a **planned follow-up**. Nothing is sent; no completed activity or contacted status is created. Actual contact must be logged separately after it happens.

## Forecast schema and imports

Fixed destination fields:

| Field | Meaning |
|---|---|
| `date` | Full occupied-night date. Departure is excluded from a stay. |
| `capacity` | Explicit sellable total-room or room-type capacity, a whole number from 0 to 10,000. Adjust for out-of-order/held rooms as appropriate to the report basis. |
| `forecastRooms` | Forecast occupied rooms **without the prospects being evaluated**. Explicit0 is preserved. Must be between 0 and the reviewed capacity. Fractional expected values are accepted. |
| `roomType` | Optional room-type scope. Blank means a total-room row. A typed row is not a hotel total. |
| `approvedMinRate` | Optional source minimum-rate metadata. Stored as source evidence; it does not enter scoring or outreach and does not constitute a new approved quote. Currency and rate rules require separate confirmation. |

A committed forecast also retains its property ID, source name, as-of date, review time, actual source-row period, source-row references, source sheet and source file SHA-256 where a file was read. Manual revisions clear a prior file hash so edited numbers are not represented as the unchanged original file. Identical source/rows are reused instead of creating a new forecast revision solely from re-importing the same data.

The file itself is **not archived by this module**. Keep the original in File Inbox separately if needed. Reviewed rows and metadata are part of the hotel’s normal snapshot and encrypted backup.

Example header:

```csv
Date,Capacity,ForecastRooms,RoomType,ApprovedMinRate
```

The downloaded template contains the header only. It does not insert synthetic hotel inventory.

CSV/TSV/pasted tables reuse the bounded table parser. Spreadsheet files reuse the existing local workbook parser and sparse matrix conversion, with ZIP-directory and actual expanded-size validation before parsing. Forecast-specific header detection supports sheets with report-title rows. A sheet selector is provided for multi-sheet workbooks. Dates require ISO format, explicit MDY/DMY interpretation, or recognized Excel date serials. Review mappings are fixed fields; source headers are never executable object paths.

Limits: 5 MB source file, 1,000 forecast rows, existing shared table/cell/ZIP limits and at most 90 occupied nights per requested stay. Encrypted/unsupported formats are rejected. Macros, formulas and imported instructions are not executed by this feature. Unexpected spreadsheet structures require a clean CSV export rather than guessed fields.

## Request review and package integration

Original prospect records do not contain a reliable nightly room schedule. Total room nights, a month-only arrival or a contract with no linked review are **not** spread into invented nightly counts.

A manual review stores exact arrival/departure, per-night counts and optional room-type scope. It captures the prospect’s source stay and allocation fingerprint. If the prospect dates or source allocation later change, the manual review needs confirmation again.

An approved package can provide:

```js
prospect.requestedNights = [
  { date: 'YYYY-MM-DD', rooms: 12, roomType: 'King' }
];
prospect.requestedNightsReviewed = true;
prospect.requestedNightsReviewedAt = 'ISO timestamp';
prospect.requestedNightsSource = {
  kind: 'reviewed-package', id: 'package ID', name: 'source name', fileId: 'optional file ID'
};
prospect.requestedRoomType = 'King'; // optional single-type scope
```

Those counts are accepted only when the review flag is explicitly true and the full nightly schedule and stay dates validate. Date changes without newly approved allocation must reset that flag. `requestedRoomTypes` may list a mixed block whose nightly totals were explicitly approved; such aggregated counts match total-room forecasts only and receive a visible warning that the individual room-type capacities remain unverified.

An exact typed request requires an exact normalized typed forecast row for each relevant date. A total-room row cannot prove a King/Double Queen fit. Typed forecast rows are not summed to invent complete hotel coverage. Manual total-room scope remains a total-room analysis, with a warning if the source explicitly names a room type.

## Transparent score and ranking

For each requested night with rooms:

```text
forecast headroom = max(0, reviewed capacity − forecast rooms)
covered RN = min(requested rooms, forecast headroom)
pressure RN = max(0, requested rooms − forecast headroom)
forecast occupancy = forecast rooms / capacity × 100
soft covered RN = covered RN when occupancy ≤ the owner’s soft-night threshold
```

Across the stay:

```text
score = 100 × sum(soft covered RN) / total requested RN
```

The score is the **share of the request fitting soft-night forecast headroom**, not a probability, occupancy promise, chance of winning or profit estimate. Forecast headroom can be fractional because forecast demand can be fractional.

Requests without forecast pressure rank first. Within that category, larger useful soft-night RN rank first, then the score and account name. Requests with pressure are clearly flagged for revenue review. A request exceeding a reviewed night’s physical sellable capacity is unscored rather than presented as a fit.

Initial editable rules are 75% soft-night occupancy and a 7-day source freshness limit. These are triage examples, not Hilton, owner or management-company policy. An older source stops all ranking until a newer source is reviewed or the owner explicitly changes the freshness rule. Resaving a source does not change its as-of date or make it fresh automatically. Future as-of dates are rejected.

Full dates, explicit nightly counts, all required forecast rows and valid room-type scope are necessary for scoring. Missing rows are unknown, never zero. A stay that has started/passed remains unscored until its future dates are reviewed. Won, Lost and Do Not Contact prospects are excluded from new outreach matching. Other hotels’ source rows and prospects are not matched or written.

### Independent synthetic known answer

Request: 20 rooms on January 10 and 40 rooms on January 11, for 60 total requested RN. Both source capacities are 100. Forecasts are 50 and 80 rooms respectively. Soft threshold is 75%.

- January 10: 50 forecast headroom; 20 RN fit; occupancy 50%, so all 20 are soft covered RN.
- January 11: 20 headroom; 20 RN fit; 20 RN are above forecast headroom. Occupancy 80%, so none are soft covered RN.
- Totals: 40 forecast-covered RN, 20 soft covered RN, 20 pressure RN. Score 20 / 60 × 100 = 33.33%.

This is a labeled test fixture, not an actual forecast or availability claim. A smaller request fitting all forecast headroom ranks above it because the larger request has pressure that requires review.

## Local outreach and planned follow-ups

The generated template repeats only the reviewed request and asks the prospect to confirm dates, counts, room types and decision timing. It does not quote rates, confirm availability, reserve inventory or send email. The owner can edit the text before planning.

Saving a plan rechecks current property, request fingerprint, prospect status, forecast revision and freshness. A pending plan for the same prospect/request/forecast is not duplicated. The task retains the source name/as-of/period/hash, reviewed requested nights, threshold settings, fit metrics, editable outreach draft and review time. It is saved through `SC.commitPlannedTask`, in the planned-task collection. It does not call `SC.commitActivity` or mark a prospect contacted.

## Developer API

```js
import { initNeedDateMatchmaker } from './src/need-date-matchmaker.js';
initNeedDateMatchmaker({ SC });

SC.needDates.viewId; // 'needDates'
SC.needDates.evaluate(); // { ready, reason, forecast, ranked, unscored, candidates, ... }
SC.needDates.importForecast({ sourceName, asOf, reviewed: true, rows });
SC.needDates.reviewRequest(prospectId, { reviewed: true, arrive, depart, nights });
SC.needDates.receiveFile(file); // bounded local import preview, not automatic commit
SC.needDates.isBusy(); // include in active-job guard before restoring backups
```

Pure testable exports: `evaluateNeedDates`, `validateForecast`, `validateRequest`, `mapForecastTable`, `guessForecastMapping` and `needDateOutreach`.

State: `SC.state.needDateMatcher = { settings, forecast, overrides }`, within the current hotel snapshot. Import previews and open reviews are discarded on hotel change or restore. Async file reads use a captured property and generation; late results cannot replace another hotel’s review. Restore blocks new writes, and the root active-job guard prevents restore during file parsing.

## Verification and practical boundaries

Tests cover independent overlap math, rank order, missing dates/counts, partial coverage, editable freshness, future as-of, room-type totals/duplicates, zero inventory, capacity restrictions, terminal statuses, malformed numeric inputs, property isolation, changed source-request fingerprints, reviewed-package integration and inert fixed-field mapping. Browser tests exercise actual CSV mapping/commit, per-night review, planned-only follow-up, unchanged completed activity/contact status, stale-source behavior and hotel switching.

No external service was connected, no live inventory was inspected and no real company’s future travel demand was inferred. Profit, rate acceptance, decision probability, room holds, alternative hotels and automatic outbound messages are outside this feature. Use the Deal Checker and normal revenue/inventory approval for a quotation after needs and live options are confirmed.

Validation result: **15 tests passed** across the current source: 12 domain cases and 3 browser cases. The browser cases include actual CSV mapping/commit and planned-only follow-up, stale-source/hotel isolation, and a real XLSX with report-title rows retaining sheet/date/source-row/hash evidence. The distinction between package approval and manual count review is deliberate: approved native counts need no retyping, while unreviewed counts remain unscored. Cross-feature package/contract UI validation is handled by the integration suite.
