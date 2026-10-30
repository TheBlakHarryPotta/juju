# Contract import and courtesy agreement review

Scope: the local whole-conversation parser/importer, contract adapter, and courtesy agreement renderer. Review used synthetic examples. All contract findings raised in this review have been addressed; the remaining boundaries below describe the scope of this application. The owner's private reference PDF was not copied into source, release assets, screenshots, or test fixtures.

## Confirmed protections

- The importer proposes fields in one review. Existing values are not selected for replacement automatically. Room rows require separate selection, explicit whole-table replacement approval, and an approved nightly rate and dated allocation.
- Applying a review checks the property, selected contract ID, exact original data JSON, and status. The adapter validates the complete candidate before mutating the contract. A property switch, target change, concurrent edit, signed status, or hotel signature flag prevents applying the old review.
- The supported field list excludes legal clauses, taxes, billing, signing state, contract status, and arbitrary object paths. Prototype-related keys are rejected recursively. Source strings are escaped in review and document rendering.
- The full conversation is retained as a local attachment, with a content hash and provenance reference. It is not automatically appended to printable contract clauses or notes. Source retention is property-scoped, deduplicated, and counted against the local attachment budget.
- Dates undergo an actual calendar round-trip check. Invalid days, departure before arrival, stays over the supported 120-night limit, negative/fractional room counts, missing rates masquerading as zero, and positive allocations on checkout day are rejected.
- Ambiguous numeric date order, missing years, contradictory statements, unclear rates, and room-night totals remain unresolved until explicitly reviewed. Omitted nights are not silently inferred from a total.
- A signed import target must first be copied to a separate unsigned draft. The original data is unchanged by that duplicate operation.
- Courtesy layout is a separate agreement, not a visual reskin of the standard group contract. The panel expressly explains that it has separately reviewed booking, billing, cancellation and other terms. It cannot be selected for a guaranteed/attrition block or corporate agreement. Export requires completed reviewed courtesy terms and a nonzero dated room allocation.
- The courtesy renderer does not assume Pennsylvania law, a tax percentage, or that a blank hotel's numeric tax defaults establish an approved tax policy. Optional governing-law text is rendered only when supplied. Client signature lines remain blank. A hotel signature appearance is included only after the user deliberately selects the contract's Hotel Sign action; no source signature is inferred or copied.

## Findings raised during review

| Finding and reproducible example | Resolution |
|---|---|
| `Company address: 123 Main Street` also proposed the company name `address: 123 Main Street`. `Contact phone` and `Contact title` similarly became contact-name suggestions. | Parser label precedence corrected. Re-executed examples now produce only the appropriate address, phone, or title field. |
| The adapter coerced missing room rates/counts (`null`, `false`, empty text) to zero. | Explicit numeric validation added before conversion. Synthetic adapter checks confirm a null rate is rejected without changing the contract. |
| Importer sent `sha256` and `transcriptFileId`, while the adapter initially discarded both. Pasted source history could not locate the retained text. | Source hash naming standardized; curated history now retains the transcript file ID and hash. Full raw source remains outside printed data. |
| A pending apply could complete after a new review opened. | Importer now binds the captured review identity through its asynchronous source-retention step. Adapter independently rechecks property/target/data/status at commit. |
| Approved governing-law text was accepted but not rendered. | Courtesy renderer now includes explicitly supplied governing-law text in its hotel-terms section. |
| Changing stay/company/deadline data after saving interpolated courtesy terms could leave `reviewed=true` while the saved wording still contained the old dates or company. | Fixed. Imported changes invalidate approval. An approval fingerprint also binds manually edited contract fields, hotel settings and sales identity. Executed synthetic checks confirm export is blocked after each change; custom text is preserved for explicit re-review. |
| A restored or earlier courtesy record could have `reviewed=true` without an approval fingerprint and bypass the fingerprint comparison. | Fixed. Missing fingerprints now invalidate approval. Executed the current adapter with a synthetic older record and confirmed its approval resets before it can be reused. |
| A relative hold can resolve after arrival: agreement dated Jan 1, seven-day hold, arrival Jan 2 resolves to Jan 8, even with no explicit `optionDate`. | Fixed. The adapter now validates resolved hold/cutoff dates and repeats validation on export. Executed the actual legacy date helpers with the adapter: the Jan 1 / seven-day hold / Jan 2 arrival case rejects atomically. |

## Checks executed by this reviewer

Executed the actual adapter source in an isolated JavaScript VM with synthetic contracts. Assertions passed for atomic rejection of forbidden signing/prototype fields; wrong property; wrong contract; stale target JSON; impossible calendar day; an excessive stay; a missing rate; an occupied checkout day; signed status; and an explicit hotel-signature flag. Assertions also passed for a new unsigned duplicate leaving its original payload unchanged, and for a permitted field change placing its source identifier/hash in history without copying an internal source sentinel into printable contract data.

Executed the actual parser with synthetic labeled input. Confirmed that an invalid February date remains unresolved; an explicit June 1–3 stay plus ten Kings at an explicit nightly rate yields the intended candidates; and the corrected company-address/contact-phone/contact-title labels no longer create spurious company/contact-name candidates.

Additional executed adapter checks confirmed that a restored or older approval without a fingerprint fails closed, that changing a group, hotel name or sales manager invalidates prior courtesy approval, that an imported event change resets approval, and that a proposed short stay with a relative hold after arrival is rejected without mutating the draft.

These checks are function-level evidence. Browser review, PDF pagination/export, visual comparison, and end-to-end selected-field application are recorded by the team's browser test results, not inferred from these fixtures.

## Remaining boundaries

The pre-existing manual contract editor still allows editing after a status is marked Signed and builds output using current hotel details. Import protection does not make the entire legacy editor immutable, provide recipient authentication, freeze an executed PDF, or create a cryptographic signature. Preserve the actual executed document separately. A displayed handwritten or cursive mark is a signature appearance.

This review does not approve contractual language for a hotel, jurisdiction, or management company. Property-specific terms require the user's authorized review. No private reference contract or identifiable client data is used as a release fixture; any bundled sample document must remain synthetic.

## App-only updater preservation review

Static review of `tools/update-app.py` confirms that it stages and verifies the incoming static `dist` files, retains the previous `dist` in `.app-backups`, and does not replace the installed speech engine, models, pairing token, or browser database. Root's updater fixture checks cover preservation and installation-rename rollback. The updater cannot directly back up Safari's database, so the user should export an encrypted backup before updating. The two directory renames are recoverable operations rather than a crash-proof filesystem transaction: if power is lost between them, the retained old app files may need to be restored from `.app-backups`. This does not remove the original engine, model, token, or browser data.
