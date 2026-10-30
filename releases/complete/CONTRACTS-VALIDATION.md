# Contract capture and PDF validation

Validated October 30, 2026 on synthetic data in Chromium. The user's reference PDF and its private client details were not copied into fixtures, samples or public assets.

## Final results

- Full application suite: **69 passed, 1 explicitly skipped, 0 failures and 0 flaky tests**, from 70 discovered cases, in 216 seconds. This includes **29 new contract cases**: 9 parser cases and 20 browser cases.
- After a print-only correction for dark-theme paper margins and legacy table-border overrides, **all 5 real PDF cases passed again against the rebuilt production app on port 4173**, in 18 seconds. These are repeated checks of five existing cases, not five additional unique tests.
- Existing calculation evidence remains 720 reconciliation checks with zero failures and 249 exploratory button clicks without reported runtime errors. These nested checks are not additional Playwright cases.

Commands:

```sh
SC_TEST_OUTPUT=test-results/contracts-final npm test
SC_TEST_URL=http://127.0.0.1:4173 SC_TEST_OUTPUT=test-results/contracts-print-production npx playwright test tests/contracts.spec.js -g 'actual PDF|multi-page PDF|long courtesy|courtesy PDF renders'
```

## What was demonstrated

| Area | Verified behavior |
|---|---|
| Whole conversation | A labeled transcript and a mixed spoken/labeled transcript supply organization, event, contact, phone, email, address, dates, group code and two room proposals in one review. Paste, plain-text drag/drop and the Call Desk whole-transcript button work without copying individual fields. |
| Review boundary | Opening or canceling review does not mutate the contract. One confirmed batch fills an initially empty header and room table. Existing values need explicit selection. Source text is retained locally rather than inserted as legal clauses. |
| Uncertainty | Missing years and ambiguous numeric date order stay unresolved until the user chooses explicitly. Conflicting company names and alternative prices are flagged. Currency thousands are preserved; oversized tokens and count substrings are not truncated into different commitments. Double-bed and queen-bed types remain distinct. |
| Rooms | A synthetic block of 10 King and 15 two-double-bed rooms at $149 for one occupied night produces 25 room nights and $3,725 in the calculator. Quantities are not spread across nights without explicit uniform allocation or exact nightly input. Room-night totals are not treated as per-night rooms. |
| Contract integrity | Import cannot change signature, status, taxes, billing or legal clauses. Forbidden/prototype fields and invalid room dates are rejected atomically. Changing hotels, contracts, signing state or the reviewed snapshot rejects the old apply. Newer manual changes survive rejection. |
| Signed documents | Signed contracts require a draft copy. Explicit hotel signing renders only the hotel mark/date; group signature/date stay blank. No mark is inferred from a transcript. |
| Courtesy approval | Export is blocked until all six property-specific terms are reviewed. Imported or manual party changes invalidate approval while preserving the terms' text. |
| Untrusted input | Hostile HTML remains inert text. Source instructions cannot mutate prototypes or mark a contract signed. |
| Standard contracts | Long standard group and corporate PDFs retain their existing legal wording, custom end-of-terms sentinel, cancellation/availability or force-majeure content, and final acceptance. Rendering does not mutate contract state. |

## Actual browser PDF checks

The tests generate PDFs with Chromium `page.pdf()`, extract text with `pdftotext`, count pages with `pdfinfo`, and check all extracted word bounds against Letter page dimensions. Rasterized PDF corner pixels must be white even when the app uses its dark theme. Page screenshots were also visually reviewed.

| Synthetic document | Actual Letter pages |
|---|---:|
| Courtesy agreement, 25 rooms, one night | 2 |
| Same courtesy agreement with explicit hotel signature | 2 |
| Long courtesy agreement with an unbroken organization name and extra terms | 3 |
| Long standard group contract | 5 |
| Long corporate agreement | 3 |

The short courtesy output has repeated headers/footer details and page numbers. Long documents keep final terms and acceptance, without words exceeding the physical page bounds.

Reviewable synthetic samples:

- [Two-page courtesy PDF](samples/synthetic-courtesy-agreement.pdf)
- [Actual PDF page 1](samples/synthetic-courtesy-page-1.png)
- [Actual PDF page 2](samples/synthetic-courtesy-page-2.png)

These samples use a fictional QA hotel, fictional organization, reserved example phone numbers and `.test` email addresses. The six short terms are synthetic QA text, not property-approved commercial or legal language.

## Qualifications

The parser is deterministic local extraction, not a guarantee of complete or correct understanding of an arbitrary recording. Explicit review and property approval remain required. The tests use synthetic text and known readable documents; they do not establish real call-transcription accuracy, integration with Hilton systems, legal enforceability or authentication of an electronic signature.

The only skipped case remains the retired v3 Claude-host screenshot tray, replaced by the tested local File Inbox/OCR workflow. No new contract case was skipped. The stale-tab regression setup now completes deferred startup mirrors and establishes explicit revision ordering before testing rejection; it does not disable the conflict check or change application persistence logic.

The print-only patch was followed by the five relevant production PDF checks. The unrelated application suite was not repeated again solely for that CSS correction.
