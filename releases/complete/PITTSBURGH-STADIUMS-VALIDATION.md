# Three Rivers stadium variant validation

Validated October 30, 2026 against the rebuilt production app on local port 4173 using Linux Chromium. QA modified tests, documentation and preview artifacts; the designer supplied the application artwork/styles.

## Results

- **16 passed, 0 skipped, 0 failed, 0 flaky**, in **66.1 seconds**: the 12 existing Pittsburgh design/integration cases plus four independent stadium cases.
- **1 actual contract PDF case passed**, in **3.3 seconds**, against the same production build.
- Fresh production build succeeded with 326 modules. Only the existing large-chunk advisory remained.

```sh
SC_SKIP_SERVERS=1 SC_TEST_URL=http://127.0.0.1:4173 SC_TEST_OUTPUT=test-results/pittsburgh-stadiums-final npx playwright test tests/pittsburgh-design.spec.js tests/pittsburgh-stadiums.spec.js
SC_SKIP_SERVERS=1 SC_TEST_URL=http://127.0.0.1:4173 SC_TEST_OUTPUT=test-results/pittsburgh-stadiums-print npx playwright test tests/contracts.spec.js -g 'courtesy document renders synthetic'
```

The initial anchored PDF title filter matched no tests; the corrected substring filter executed and passed the actual case above. No application failure was observed. The broad sales suite was not rerun solely for this visual change. These are overlapping targeted checks, not additional full-suite totals. The current catalog contains 127 cases in 14 files.

## Independent checks

Both the ballpark and football stadium render visibly only in Three Rivers. They remain hidden in Steel City, Foundry and Sunday Morning. The skyline and bridge remain visible across palettes. Reload preserves the River selection without changing active-property, account or activity data.

At desktop 1440 × 1000 and phone 390 × 844, both landmark bounds remain inside the hero and viewport, with no horizontal page overflow or reported page error. QA independently opened the resulting screenshots: the ballpark diamond, seating and lights and the football field/stadium are recognizable; neither landmark is cut off on the phone.

With normal motion enabled, the stadium lighting animation clocks advance by more than 900 ms over a real 1.2-second interval. System reduced motion removes those animations. Existing cars, aircraft, river and window-motion checks also pass. This does not establish physical-device performance or battery use.

The actual courtesy contract PDF still has its expected readable text, two Letter pages, white paper margins and words within page bounds. Stadium artwork remains outside that printed document.

## Review assets

- [Desktop stadium scene](screenshots/pittsburgh-stadiums-desktop.png)
- [Phone stadium scene](screenshots/pittsburgh-stadiums-phone.png)
- Existing River desktop/phone preview files were refreshed to the same variant.
- [Actual eight-second animated scene](screenshots/pittsburgh-river-animation.gif) and [H.264 MP4](screenshots/pittsburgh-river-animation.mp4) are refreshed from a browser recording with a synthetic hotel. The GIF was verified as 80 frames / 8,000 ms, approximately 2.15 MB. The MP4 is eight seconds, 600 × 294, H.264/yuv420p. QA inspected decoded frames at zero and seven seconds: both stadiums remain visible while aircraft, cars and river details change. No private client document or original reference PDF is included.

The scene is original stylized SVG artwork, not a measured map or architectural model. Browser verification is Chromium; the phone viewport is not a physical-device or Safari certification.
