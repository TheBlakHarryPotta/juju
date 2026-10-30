# Sales workflows: ideas and implementation status

**Implemented in the complete update:** One-Review Deal Package, Need Date Matchmaker and Repeat Business Memory. The proposal sections below preserve the reasoning behind those builds. See [COMPLETE-UPDATE.md](COMPLETE-UPDATE.md) and the feature guides for delivered behavior; other market-desk, tour-brief and conversion ideas remain future recommendations.

The new Tours, Networking, Prospect Pipeline and Weekly Sales Feed sections preserve a simple rule: a name, imported list or plan is not a completed sales call. Record actual dates and results when work happens. Completed tours and networking entries create one linked Activity Log record; edits update that record instead of adding it again. New prospects retain contact information, requested stay dates, contacted status and a next step. Saved reviewed calls and RFPs can create linked prospects without repeating their source activity in reports.

Weekly Sales Feed uses the selected legacy reporting week and hotel. It includes actual dated activities and inquiries plus clearly labeled prospect identification. Manual Send to weekly report uses stable source IDs and rejects records outside the selected week. Repeated sends do not add entries or activity counts. Planned/cancelled visits are excluded from actual work. Historical RFPs with no received date remain undated until the user verifies one.

Check duplicates compares normalized company/contact, email and phone. It identifies potential pairs; shared agency contacts and central numbers may legitimately belong to several companies. No automatic merge or deletion occurs. Exact source-row reimports skip already imported entries. This is separate from potential business-identity duplication across different files.

## Useful improvements to pilot next

- Before a site tour, generate a factual one-page brief from the prospect's existing notes: stated stay pattern, room mix, objections and the two questions still unanswered. Do not invent a budget or approval authority.
- After a completed tour, require one next step with an owner and date. Distinguish a promised proposal from a proposal actually sent.
- Use need dates from current approved revenue reports to shortlist companies with documented relevant stay patterns. Show the matching evidence and forecast date, then let the manager decide whom to contact.
- Build a recurring organizer list for tournaments, crew projects, training and associations using verified public information. Verify schedules and contact details before outreach; no private portal scraping or assumed relationships.
- Track outreach outcomes by cohort and actualized room nights. Show contact-to-tour and tour-to-proposal conversion separately from booked revenue. Do not claim causal revenue uplift without evidence.
- Add a reviewable call sheet that prioritizes due next steps, expiring agreements and source-backed account decline. Keep personal/sensitive information limited to approved work data.

For Pittsburgh prospecting, a future evidence-backed market desk could link official business directories, venue calendars, public project announcements and tourism information. These ideas do not assert that any specific event or company currently needs rooms. Dates, sources and licensing should be checked before importing or publishing prospect information.

## Chloe's next three build candidates

These are proposed additions, not features already delivered. They build on the current local app and do not require a live connection to Hilton portals. The order favors the manager's current single-property workflow; a second hotel can be added later.

### 1. Turn one conversation into one reviewed sales package

**Trigger:** You finish a call or drop in the entire inquiry, email or transcript.

**Concrete output:** One review screen proposes a linked prospect/contact, group opportunity, contract draft fields, next-step task and weekly-report source. It shows existing records alongside changes, asks whether to attach to an existing account, and flags missing dates, room allocations or approved rates. One approval saves the connected records under the same source identity. Nothing is sent or signed. A change receipt shows what was created or changed and allows a careful reversal of that batch.

**Why this is valuable:** A single conversation currently has several destinations. Connecting the same source once reduces repeated typing and keeps the proposal, follow-up and report from telling different stories. The practical test is whether a real inquiry can become a usable draft package in one review, without producing duplicate contacts or reported calls.

**Data and limits:** Requires the full reviewed transcript and a selected hotel. Missing facts remain blank. Legal clauses, taxes, concessions, final rates, signatures and nightly allocations require explicit approval. A source identity prevents another import or report sync from counting the same call again. It can run locally on the Mac; deterministic extraction can be the default, with optional local transcription rather than sending work data to a cloud model.

**Existing versus new:** Call Desk, reviewed field extraction, contract capture, linked prospects and report deduplication already provide parts of this. The new work is the single coordinated review, linking and reversible batch across those parts.

### 2. Match the hotel's need dates to the right prospect's stay pattern

**Trigger:** A newly reviewed PEP/GRO or other approved forecast export identifies dates the hotel wants to fill, and a prospect or previous group has a documented matching stay pattern.

**Concrete output:** A short list with an evidence card for each match: requested dates and nightly room counts, forecast source/as-of date, occupied nights covered, room-type constraints, missing information and one sensible next action. For a flexible prospect, show an alternative date pattern to review with the revenue manager. A follow-up draft refers to the client's stated needs rather than claiming inventory is held.

**Why this is valuable:** It connects the sales list to a particular commercial problem. The manager can spend time on leads that could fill the relevant nights instead of treating every prospect as equally urgent. Actualized results can later be compared with the original recommendation without claiming the app caused all revenue movement.

**Data and limits:** Needs dated, reviewed forecast exports and prospect stay dates or a verified recurring pattern. Lighthouse rate information and approved ProfitSword/revenue figures can provide context when their definitions and periods are known. A stale report must be visibly stale. Forecast capacity is not live sellable inventory, and price/availability still need confirmation in the approved systems. For dual sales later, show two independent property scenarios and avoid counting one opportunity twice; routing must respect each property's room types, restrictions and current source dates.

**Existing versus new:** The app already has need-date/displacement tools and prospect records. The new work is an explainable matching layer between them, with source freshness and explicit unknowns.

### 3. Build a repeat-business calendar from what actually happened

**Trigger:** A group departs, a project ends, or an agreement approaches its renewal window.

**Concrete output:** A reusable account/event brief with contracted versus actualized room nights, pickup by night, agreed rate and known concessions, organizer details, recorded service issues and next contact date. The calendar proposes a configurable rebooking reminder before the next planning cycle. When the organizer confirms new dates, it prepares a fresh opportunity using that confirmation, not last year's dates copied forward as fact.

**Why this is valuable:** It preserves the details that make a repeat conversation useful. The manager can contact an organizer with a factual account of the last stay and a specific unanswered question. It also makes a handoff to another sales manager or a second hotel more consistent without losing the originating property's history.

**Data and limits:** Needs authorized actualized production/pickup exports, the prior agreement and verified organizer/contact notes. Repeat timing is a reminder hypothesis until confirmed; an annual event may move, stop or change venue. Sensitive guest details do not belong in the sales brief. The local database and encrypted backup retain the history; no live PEP, OnQ, Lighthouse or ProfitSword connection is assumed.

**Existing versus new:** Account/group profiles and reporting exist. The new work is a dated closeout snapshot, an explicit actualized-versus-contracted comparison and the reminder-to-confirmed-new-opportunity workflow.

**Recommended next build:** Start with the single reviewed conversation package. It improves a daily task immediately and makes the other two ideas easier because prospects, stays, tasks and sources will already be linked consistently.
