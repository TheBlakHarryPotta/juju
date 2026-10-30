# Deal Package

Deal Package turns one reviewed conversation into connected sales records on the current device. It does not access Hilton portals, send messages, sign contracts or reserve live inventory.

## One combined review

Open Deal Package, paste/drop the entire transcript or inquiry, choose group contract or corporate agreement, and build one review. The existing local contract parser proposes company, event, contact information, dates, group/SRP code and room rows. Missing facts remain blank. Numeric date order and missing years stay unresolved unless the user explicitly supplies the relevant date choices.

Review the whole form. It creates a new prospect by default; selecting an existing prospect shows its current values next to the proposed values and requires explicit overwrite approval. Blank proposed fields preserve existing prospect information. No company/contact identity is guessed from similar names.

A group room block requires approved room type, rate and occupancy. Explicitly confirm a uniform count on every occupied night, or enter each night's count, including zero where appropriate. A total number of room nights is never distributed automatically. Unchecked room proposals stay outside the new contract. Without an approved block, the draft remains unallocated. Corporate rates are left for explicit review in Contract Maker.

Enter the planned next step and exact due date. The actual-call checkbox starts unchecked. Logging a completed call requires a valid completed date, explicit activity category and actual result. Importing an inquiry or drafting an opportunity never counts as a completed call by itself.

## What one approval saves

One revision-checked durable transaction creates or updates the explicitly selected prospect; creates a linked Prospect pipeline opportunity, a new unsigned Draft contract and a planned follow-up; and records one reporting source. It creates actual sales activity only with the completed-call confirmation. Otherwise the weekly source says that a deal package/opportunity was prepared. A planned follow-up remains separate from actual work.

New contract cutoff and hold dates remain blank unless reviewed. Source text does not change legal clauses, taxes, billing, signature or signing status. Contract Maker's template terms still need commercial/legal review before use. The group/SRP code is retained in the new contract; the separate SRP Vault is not changed outside the atomic transaction.

Approved nightly allocations are exposed to Need Date Matcher as reviewed requested nights, with source provenance. Mixed room types retain their identities; total-room matching does not prove that each type is available. Changing an existing prospect's dates without approving a new allocation invalidates its prior allocation review.

## Receipts and guarded undo

The receipt records affected records' before and after values, source metadata and time. It is included in normal encrypted backups. Reopening the app retains the receipt and links to the resulting sales drafts.

Undo is available only while affected records remain unchanged and no later work depends on newly created records. Unrelated hotel changes do not prevent undo and are preserved. Editing the linked opportunity or completing its task can block undo, because reversal must not overwrite subsequent work. The original source attachment remains local evidence after undo.

The full reviewed conversation is kept as a local text attachment with SHA-256 provenance. It stays outside printed contract clauses. Source retention occurs only after the user approves the package. If a later business-state commit fails, the original may remain as evidence, while none of the connected business records is published. The shared local attachment budget applies.

## Verification

The focused browser suite covers: inert review and one durable linked save; reload persistence; no completed activity without explicit confirmation; rejected future call dates; explicit room allocation; stale review rejection; simulated durable-save failure; successful undo with unrelated changes preserved; and rejection when a later linked record changed. Separate integration tests cover Call Desk handoff and the other innovation modules.

## Duplicate source safeguards

An exact original source ID already linked to completed activity cannot log another actual call through Deal Package. Keep the actual-call option unchecked to prepare new drafts without increasing completed activity counts, or review the original Activity Log entry.

The same conversation hash cannot create a second package while an applied package receipt for that hash exists in the same hotel. Open its existing records, or use guarded undo before rebuilding. An undone receipt permits a fresh review and rebuild. Edited conversations have a different hash and still require explicit prospect selection and complete review; the app does not guess that similar text represents the same business event.

## Pipeline room-type compatibility

The existing Pipeline editor supports King, Double Queen and explicit Run of House categories. A package fills that editor only when every reviewed room row has an exact supported identity. Uniform blocks populate the per-night counts; varying blocks populate the nightly grid. Its single group-rate field is the sourced weighted ADR when original room rows have different prices; the linked contract retains those exact prices.

Double/Double is not Double Queen. Suites, single Queens and other unsupported types are never silently converted to Queens or Run of House. If any row is unsupported, the entire legacy mix stays unallocated pending explicit room-type review. Full source room-night/revenue totals, exact reviewed room rows and requested nights remain retained. The Pipeline source selector uses Other unless an origin channel has been explicitly established; full original provenance stays in sourceRef.
