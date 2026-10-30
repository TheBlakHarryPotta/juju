# Pittsburgh workspace validation

Validated October 30, 2026 in Linux Chromium using synthetic records and the application's labeled sample workspace. Before screenshots were captured before integration. No private reference PDF or client contacts were copied into fixtures or preview assets.

## Release evidence

| Run | Actual result |
|---|---|
| Full application regression | **119 passed, 1 existing skip, 0 failures, 0 flaky**, from 120 cases, in **251.4 seconds** |
| Latest affected intake, sales, security and design checks | **49 passed**, no skips/failures/flaky cases, in **91.5 seconds** |
| Rebuilt production checks on port 4173 | **5 passed**, no skips/failures/flaky cases, in **27.5 seconds** |
| Marcus’s final async-toolbar production check | **5 passed**, no skips/failures/flaky cases, in **17.9 seconds** |

The full run preceded the last explicit Call Desk activity-category and linked-prospect deduplication correction. The affected run then verified that final source, including two additional regressions. The production run verified the rebuilt result, final presentation styling, clean screenshots, motion, Call Desk categorization and offline OCR. Marcus then fixed the report/duplicate toolbar being replaced by asynchronously rendered SRP, Template and Radar views. His final rebuilt-production check verified those controls, reviewed manual-highlight deduplication, motion/reduced motion, actual courtesy PDF white paper and offline OCR. Its result is `test-results/pittsburgh-async-production/results.json`. Counts overlap and must not be added together as unique cases. The current test catalog contains 127 cases; the only skip is the retired v3 Claude-host screenshot tray, replaced by local intake/OCR.

Commands:

```sh
SC_TEST_OUTPUT=test-results/pittsburgh-final npm test
SC_SKIP_SERVERS=1 SC_TEST_OUTPUT=test-results/pittsburgh-affected-final npx playwright test tests/intake.spec.js tests/sales-import.spec.js tests/sales-logic.spec.js tests/sales-security.spec.js tests/sales-workflows.spec.js tests/pittsburgh-design.spec.js
SC_SKIP_SERVERS=1 SC_TEST_URL=http://127.0.0.1:4173 SC_TEST_OUTPUT=test-results/pittsburgh-production-final npx playwright test tests/workspaces.spec.js tests/pittsburgh-design.spec.js tests/offline.spec.js -g 'workspace modes|each Pittsburgh palette|Three Rivers actually|reviewed Call Desk prospecting|production PWA'
```

A fresh final production build succeeded with 326 transformed modules. Vite's existing advisory about the large document-processing JavaScript chunk remains. The full run also executed 720 nested invariant checks with zero failures and 218 exploratory clicks without reported runtime errors; these are not additional Playwright cases.

## What was demonstrated

- Four palettes persist after reload without changing the active property, accounts or activity records: Steel City, Three Rivers, Foundry and Sunday Morning.
- Motion settings persist. Cars in both directions, aircraft, window lights, river current and reflections have advancing animation clocks over a real 1.2-second interval; river transforms change. System reduced motion stops those animations. This is behavior evidence, not a battery, frame-rate or M1 benchmark.
- Actual phone menu taps navigate ten routes, including new sales workspaces, Import Station and Deal Review. The document stays 390 px wide with no page runtime errors. Desktop Presentation reclaims the full 1440 px content width and has a working exit.
- An actual CSV is retained and mapped for review before prospects are created. Phone leading zeros survive; missing contact and stay details remain blank. Imported leads remain New and do not inflate completed calls. Exact source reimport is skipped.
- An actual Lighthouse CSV excludes its Total row, preserves 20 room nights, $2,980 revenue, $149 ADR and comparison 25 room nights, then supplies the weekly report and email text with a 20% decline.
- Reviewing a Call Desk transcript as an RFP creates its New prospect without inventing a completed call. Reviewing an actual prospecting call creates exactly one categorized activity and one linked Contacted prospect; repeated renders and reload preserve those identities and one weekly call count.
- Planned visits stay separate from completed work. Completing and editing Tours/Networking updates one linked activity. Manual section highlights require a reviewed actual date; canceling saves nothing, repeated sends retain one highlight and do not add another completed call. Duplicate review lists possible matches without deleting source records.
- Deal Review independently reconciles 20 occupied rooms including 2 complimentary rooms: 18 paid × $150 = $2,700 room revenue; $135 commission and $600 variable cost yield $1,965 group contribution. Ten displaced rooms at $160 alternative contribution cost $1,600, leaving **$365 incremental contribution** and a **$128.66** flat break-even rate. The stronger-demand scenario yields approximately **−$1,635**. The actual downloaded JSON contains those values. Editing costs blocks stale exports until recalculation.
- Security checks cover foreign-property sources, delayed hotel-switch races, hostile headers/names, report deduplication, complete CSV source reading, reviewed BT corrections and encrypted backup recovery of the new sales records. See [PITTSBURGH-SECURITY-REVIEW.md](PITTSBURGH-SECURITY-REVIEW.md).
- Existing contract PDF, file extraction, signatures, templates, radar and persistence regressions passed. The final production app reloads offline and performs real local screenshot OCR without external HTTP requests.

## Defects caught during review

The old body backdrop blocked real phone taps above the app stacking context. Moving it below the sidebar fixed the actual navigation regression. A subsequent SVG sizing correction temporarily hid the desktop skyline; its wrapper sizing was fixed, and the test now requires a visible illustration with meaningful dimensions. No forced clicks replaced the phone interaction.

The final Call Desk correction added an explicit reviewed activity category and used the linked activity ID to prevent a second prospect during automatic synchronization. Dedicated actual-UI and source-identity tests passed after that fix.

Two early deal-test assumptions were corrected: the scenario identifier is `demand`, and floating-point values require numerical tolerance. The manual dialog close selector was scoped to its form because the existing accessibility enhancement names close controls “Close dialog.” These were test corrections, not weakened application guards.

## Visual evidence

All eight final palette screenshots were generated from the rebuilt production app, cleared of transient toasts/hover effects, and personally inspected by QA. Marcus independently reviewed the palette designs and phone rendering.

- Before: [desktop](screenshots/pittsburgh-before-desktop-viewport.png), [phone](screenshots/pittsburgh-before-phone-viewport.png).
- After: [Steel desktop](screenshots/pittsburgh-steel-desktop.png), [Steel phone](screenshots/pittsburgh-steel-phone.png); [River desktop](screenshots/pittsburgh-river-desktop.png), [River phone](screenshots/pittsburgh-river-phone.png); [Foundry desktop](screenshots/pittsburgh-copper-desktop.png), [Foundry phone](screenshots/pittsburgh-copper-phone.png); [Daylight desktop](screenshots/pittsburgh-daylight-desktop.png), [Daylight phone](screenshots/pittsburgh-daylight-phone.png).
- Actual eight-second motion preview: [animated GIF](screenshots/pittsburgh-river-animation.gif), [H.264 MP4](screenshots/pittsburgh-river-animation.mp4). The GIF has 80 frames at 10 fps; the MP4 is 600 × 294, H.264/yuv420p. Both are cropped from a real browser recording of the original SVG scene in a synthetic hotel. QA inspected decoded frames at the beginning and seven seconds, visibly confirming changed aircraft/car positions and river details.
- Synthetic feature views: [prospects](screenshots/pittsburgh-feature-prospects.png), [tours](screenshots/pittsburgh-feature-tours.png), [networking](screenshots/pittsburgh-feature-networking.png), [source review](screenshots/pittsburgh-feature-import-review.png), [column mapping](screenshots/pittsburgh-feature-import-mapping.png), [deal results](screenshots/pittsburgh-feature-deal-results.png), [weekly feed](screenshots/pittsburgh-feature-weekly-feed.png).

## Limits

Browser automation ran in Chromium; the phone check is a viewport simulation, not a physical-device or Safari certification. These tests demonstrate local behavior with synthetic inputs, not Hilton connectivity, source-report completeness, speech-recognition accuracy, approved hotel rates or profitability from unverified assumptions. Imported figures and commercial terms still require the user's review.

## Three Rivers stadium variant

After the stadium-only visual update, **all 16 affected design/stadium cases passed** in 66.1 seconds against the rebuilt production app, followed by **one passing actual courtesy PDF case** in 3.3 seconds. Both stadiums are visible only in River, persist through reload, fit the desktop and phone hero, and respect reduced motion. QA independently inspected the final desktop/phone images. River previews and the actual eight-second animated GIF/H.264 MP4 were refreshed. See [PITTSBURGH-STADIUMS-VALIDATION.md](PITTSBURGH-STADIUMS-VALIDATION.md) for commands and exact scope. The unrelated full sales suite was not repeated solely for this visual change.
