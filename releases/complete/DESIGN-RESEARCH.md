# Pittsburgh site design research

Reviewed October 30, 2026. This work redesigns the whole Sales Command interface, including its shell, navigation, dashboard, cards, forms, tables, dialogs and mobile layouts. It is separate from the contract-document typography work.

## Research actually performed

I inspected the current app, its Aurora styles, the earlier desktop/mobile screenshots, navigation and workspace markup. I reread the cloud runtime/networking instructions, inspected the supported network policy file, and checked the current environment status before using the inherited proxy. The network was reported enforced and the environment running.

Public requests made through that proxy:

| URL | Observed result | What it supports |
|---|---|---|
| https://www.pinterest.com/search/pins/?q=pittsburgh%20dashboard%20design | Proxy tunnel HTTP 403 | Access was blocked; no pins or Pinterest designs were viewed. |
| https://dribbble.com/search/dashboard | Proxy tunnel HTTP 403 | Access was blocked; no current Dribbble designs were viewed. |
| https://www.awwwards.com/websites/dashboard/ | Proxy tunnel HTTP 403 | Access was blocked; no Awwwards examples were viewed. |
| https://linear.app/ | Proxy tunnel HTTP 403 | Access was blocked; no current Linear interface was inspected. |
| https://github.com/shadcn-ui/ui | HTTP 200 | Public project page for customizable accessible components; its current page title explicitly describes thoughtful defaults and extensible source. |
| https://github.com/radix-ui/primitives | HTTP 200 | Public project page for accessible UI primitives and design systems. |
| https://github.com/motiondivision/motion | HTTP 200 | Public project page for JavaScript/React animation tooling. |

The three GitHub projects' official README files were also read during the earlier design pass. Their MIT core licenses and the distinction between Motion core and paid extras were recorded there. This implementation uses authored CSS, SVG and browser animations; it does not install those component libraries merely for appearance.

These access results do not establish user reviews, a comparative survey of current paid design libraries, or visual inspection of blocked sites. No proxy bypass or network-policy widening was used.

## Art direction implemented

- **Steel City:** midnight steel, warm Pittsburgh gold, quiet neutral surfaces.
- **Three Rivers:** deep river blue with a pale teal current.
- **Foundry:** warm charcoal, copper and soft peach.
- **Sunday Morning:** warm paper, dark ink and restrained gold.

The bridge/skyline illustration is original inline SVG made for this app. Following the user's additional direction, its gold suspension silhouette is inspired by the Roberto Clemente Bridge; it is an authored illustration, not an exact historic or engineering model. It evokes the city's bridges, rivers and hills without copying a photograph, tourism asset, logo or third-party illustration. The illustrated scene and city coordinates communicate the chosen Pittsburgh theme; hotel records and property names still come from the actual workspace.

The redesign replaces the floating purple glass shell with a full-height navigation rail, clear grouped navigation, a calmer toolbar, a city-themed dashboard hero, four task shortcuts, consistent data cards and a distinct form/table system. Palette selection and motion preferences persist on this browser. Collapsible navigation groups retain their state, while the current section stays visible.

Motion uses subtle page entrances, button feedback, bridge drawing, flowing river curves and skyline reflections. Twelve staggered window groups slowly brighten and dim to evoke office lights; two small cars cross the deck at different speeds, and a small plane occasionally passes above the skyline. These are SVG shapes with CSS transforms and opacity, without a particle engine or animation library. A visible motion control, hidden-tab handling and the device's reduced-motion preference disable decorative motion. No external fonts, images or analytics are fetched by this design layer.

## Boundaries and verification

All new visual CSS is inside `@media screen` so contract and report print styling remains under the document stylesheets. The design module changes presentation and navigation controls; it does not rewrite calculations, rates, clauses, records, uploads or exports. The original hotel context remains visible.

Desktop/mobile screenshots, palette persistence, navigation, reduced-motion behavior, overflow, keyboard dialog behavior and PDF regression checks are performed separately by the main agent and Breakers. Their observed results should be used for readiness claims; this document does not predeclare those checks passed.

## Three Rivers stadium variant

The user's requested stadiums appear only in **Three Rivers**. The other three palettes keep their existing riverfront scene. Original SVG shapes depict a baseball ballpark with a diamond, bases, curved grandstands and floodlight towers, plus a separate football bowl with a marked field and goalposts. The scene is inspired by the riverfront relationship of PNC Park and Acrisure Stadium, without reproducing their logos, photographs, licensed artwork or exact architectural geometry.

The Clemente-inspired bridge, skyline, moving cars, occasional plane and river reflections remain. Stadium lights use a slow opacity cycle, without strobing or a particle engine, and follow the same motion-off, reduced-motion and hidden-tab controls. The Three Rivers phone layout fits the full illustrated view within its hero so both venues remain visible rather than cropping the right bank. The palette description mentions the stadiums to make this variant discoverable.
