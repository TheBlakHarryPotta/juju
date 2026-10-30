# Design for the three sales innovations

The Deal Package, Need-Date Matchmaker and Repeat Business workspaces use the existing Pittsburgh design system. This update adds workflow styling; it does not replace the four palettes, stadium scene, river movement, bridge traffic or aircraft.

## Design decisions

- Each workspace opens with its purpose and the next useful action. Headings stay in sales language; technical storage and parsing details belong in supporting help or source evidence.
- Forms use the same input shapes, contrast tokens and spacing in Steel City, Three Rivers, Foundry and Sunday Morning.
- Original information and proposed actions remain visually distinct. Source evidence has a quiet accent border and readable expandable text, rather than appearing as a confirmed result.
- Suggestions, plans, missing information and saved results use written status labels. Color adds emphasis but does not carry the meaning by itself.
- A package receipt has a clear saved-result treatment. It should say what changed, link to the resulting records and explain any available undo limitations. Styling never implies an action succeeded before the underlying operation finishes.
- Need-date opportunities should show the date range, available source evidence and an editable next action together. Missing hotel inventory is not styled as a verified available room block.
- Repeat-business reminders stay distinct from completed activity. Review and planned dates should be visible before any action to create or complete work.
- Long account names, source filenames, copied text and evidence wrap within their cards. Wide comparison tables scroll within their own region.

## Phone and accessibility

Two-column layouts become one column on phones. Inputs use a 16px font to avoid automatic phone zoom, action buttons have a 44px minimum target, and evidence summaries remain keyboard-operable native details controls. Existing focus styles and modal focus handling remain in place. No new decorative animations are needed during review; the existing reduced-motion preference also covers these workspaces.

## Scope and verification

The design implementation is `src/innovation-design.css`, loaded after the existing styles. Every rule is limited to screen media, so existing contract/report PDF presentation remains under the document stylesheets. Business calculations, imports, identity, record creation, duplicate checks and undo behavior are owned by the feature modules and their tests.

The shared selectors are `.innovation-page`, `.innovation-hero`, `.innovation-grid`, `.innovation-card`, `.innovation-field`, `.innovation-evidence`, `.innovation-actions`, `.innovation-status` and optional receipt/table helpers. Feature-specific hooks include `.deal-package-receipt`, `.deal-package-room` and the Repeat Business forms/queue.

The actual integrated markup and populated synthetic desktop/phone views were inspected on the rebuilt production app. A separate disposable browser context created a package through the real review form, supplied a reviewed dated forecast and nightly request, saved a reviewed past-group closeout and reminder, and displayed the linked Follow-ups & History workspace. That context was closed after capture.

All four views had a document width of 390px at a 390px viewport, with no observed page errors. The receipt's before/after details were opened and visually checked. The populated matcher presents its ranked opportunities before setup controls; the report utility remains available after each innovation workspace. The single closeout card uses the available width instead of leaving an empty second column.

Production captures are in `docs/screenshots/innovations-eliza-production-*.png`: desktop and phone images for Deal Package, Need Dates, Repeat Business and Follow-ups, plus an opened package-receipt image. All example people, organizations, forecasts and production figures are synthetic.

These observations verify presentation and the exercised fixture, not the entire application's business logic. Breakers' independent regression results are reported in the main validation documentation. No performance claim for a particular Mac model is inferred from the browser captures.
