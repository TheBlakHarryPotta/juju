# Group Deal Checker review and validation

Reviewed October 30, 2026. This change adds an explicit-input **operating-contribution** model. It does not assert Hilton policy, recognize unverified attrition collections, approve a quote or calculate net profit.

## What the existing calculator did

Source inspected: the legacy `gdDates`, `gdNight`, `gdCalc`, `gdNetPct`, `gdResult` and `ppToDeal` implementations in `index.html`. Existing records under `state.gd` are retained unchanged. The new checker uses `state.dealCheckV1`, scoped to the current hotel and included in the existing encrypted snapshot backup.

| Confirmed behavior | Concrete example / evidence | New behavior |
|---|---|---|
| `gdDates` silently stopped at 60 nights. | Arrival2030-01-01/departure2030-03-04 is62 occupied nights, but the loop condition `out.length <60` omitted the final two. | Every date must be present. Up to 90 nights are supported; longer stays are rejected explicitly and must be split. |
| Missing forecast defaulted to80% occupancy and could still produce “Yes”/“Take it.” | Capacity100, group10, BAR200, ask200, no forecast or cost estimate: `occ=80`, displacement0, and the comparison against the derived walk-away could approve the quote, while a warning acknowledged the missing forecast. | A missing nightly forecast or occupied-room cost blocks the financial analysis. No occupancy is invented. |
| Attrition was treated as protected collection in the expected-revenue calculation. | Quoted net room revenue10000, expected pickup50%, checked80% attrition: `pick=max(50,80)` produced 8000 before any actual collection evidence. | Sensitivities model occupied/paid rooms. Attrition/cancellation collections are excluded and terms require separate review. |
| Complimentary rooms were a fixed10-room step calculation. | A20-room peak gave `floor(20/10)=2` complimentary rooms, applied to each occupied night. This was a customization limit, not evidence of Hilton policy. | Exact complimentary rooms are entered for each night; no commission/comp/discount policy is supplied by the app. |
| The pricing model combined floor/CPOR and alternative gross ADR rather than a fully itemized contribution bridge. | `minNetRoom` blended displaced rooms at forecast ADR with nondisplaced rooms at the floor; `netAt` deducted commission/fees/rebates/upgrades, not a full occupied-room operating-cost schedule. | Group and alternative contribution both use separately entered direct costs. Every component is shown, with a separately labeled opportunity cost. |
| A single `other` amount could add revenue without separately showing its direct cost. | An entered 1000 ancillary sales value with 600 direct cost contributed1000 to that value, if the owner entered gross sales rather than already-net contribution. | Ancillary revenue and direct cost are separate; only their difference contributes. |
| Legacy minimum-stay/discount/attrition wording embedded negotiation heuristics. | The output could recommend a 3-night minimum,80% attrition or 21–30-day cutoff based on its profile. | The enhanced checker supplies no brand or owner policy. Optional minimum rate and cutoff come from the owner. |

These are traced code behaviors, not reports that a financial loss occurred. The original calculator remains in source to preserve existing data and compatibility, but normal navigation points at the enhanced checker. Pipeline imports preserve known dates/rate and source RN totals without guessing nightly allocations.

## Exact model

Room counts include comps. Departure is excluded from occupied nights. Monetary amounts must share one selected currency and exclude tax.

For each night:

```text
paid RN = total group rooms − complimentary rooms
occupied RN = paid RN + complimentary rooms
room revenue = paid RN × group rate
room commission = room revenue × group commission percentage
room selling fees = room revenue × group payment/selling percentage
rebates = paid RN × rebate per paid RN
occupied variable cost = occupied RN × group variable cost
occupied concession cost = occupied RN × concession cost per occupied RN

displaced RN = max(0, min(occupied RN, forecast WITHOUT group + occupied RN − capacity))
alternative margin per RN = alternative ADR × (1 − alternative selling %) − alternative variable cost
displaced contribution = displaced RN × max(0, alternative margin per RN)
```

Across the stay:

```text
ancillary contribution = ancillary revenue − direct ancillary cost
fixed costs = fixed concession cost + other incremental event costs

group operating contribution = room revenue − group commissions − selling fees
  − rebates − occupied variable costs − occupied concessions − fixed costs
  + ancillary contribution

incremental contribution = group operating contribution − displaced contribution

costs to cover = occupied variable costs + occupied concessions + rebates
  + fixed costs + displaced contribution − ancillary contribution

flat break-even rate = max(0, costs to cover ÷ (paid RN × retained room-revenue fraction))
flat target rate = max(0, (costs to cover + entered contribution target)
  ÷ (paid RN × retained room-revenue fraction))
```

The optional user-entered approved minimum is applied after the financial target rate. Financial floors round upward to the next cent. Full-precision intermediate arithmetic is retained; displayed dollar values round for readability. All-comps scenarios return no room-rate floor (`null`), not Infinity or a fabricated number.

The per-night floor excludes shared event costs and ancillary contribution, which are shown in the whole-stay calculation. A blended result therefore cannot conceal a negative peak-night contribution without a visible risk flag. Negative alternative margin is conservatively floored at zero so losing an unprofitable alternative is not credited as an extra benefit.

## Sensitivities and limits

- Quoted block:100% of the entered paid rooms, with explicit comps and costs.
- Lower paid pickup: editable paid-pickup percentage. The initial 80% is a labeled sensitivity example. Paid rooms and ancillary revenue scale together; comps, direct ancillary costs, fixed concessions and event costs remain committed. This may be conservative if actual costs are avoidable. Lower pickup can improve contribution when expensive displacement falls; the model does not falsely assume every lower-pickup case must be worse.
- Stronger alternative demand: editable additional occupancy points, capped at nightly capacity, and editable alternative ADR increase. Initial+10 points/+10% are sensitivity examples, not forecasts.

No actual forecast is imported automatically and no quoted result is treated as a guarantee. Alternative ADR and costs become required if any entered sensitivity displaces guests. A rate, cost or count is never substituted from an unrelated hotel. New capacity rows start from the selected hotel’s room-count setting and require adjustment for out-of-order/held rooms. Room-type/accessible-room allocation, actual live PEP inventory, contract enforceability, taxes, financing, overhead, ownership costs, ancillary channel commissions, service-charge allocation and unentered operating costs are outside this model. Include relevant costs in the entered amounts and obtain normal revenue/management approval.

The forecast must exclude the group. If the source already includes it, this model would double-count demand; that cannot be detected from a number alone. The owner must confirm the basis. There is no claim of connection to PEP, OnQ, Lighthouse or ProfitSword.

## Validation and independent known answer

Fixture: one occupied night;20 total group rooms,2 complimentary;150 rate;30 variable cost per occupied RN;5% group commission; all other group fees/costs and ancillary amounts explicitly0;100 capacity;90 forecast rooms without the group;200 alternative ADR;40 alternative variable cost;0 alternative selling cost.

```text
18 paid RN ×150 =2700 room revenue
commission =135
occupied variable cost =20 ×30 =600
group operating contribution =2700 −135 −600 =1965
10 displaced RN ×(200 −40) =1600 lost alternative contribution
incremental contribution =1965 −1600 =365
flat break-even =2200 ÷(18 ×0.95) =128.65497… =>128.66
```

The busy sensitivity caps forecast at 100 and increases alternative ADR to220. It displaces20 RN at180 margin:1965 −3600 =−1635 (floating-point tolerance applies in the test). That is why the fixture is labeled sensitive rather than universally attractive.

`tests/deal-checker.spec.js` covers:

1. The independent answer above and its busy-night sensitivity.
2. A two-night bridge with commissions, selling fees, rebates, variable concessions, fixed costs, ancillary costs and a contribution target.
3. Lower-pickup treatment of paid rooms, fixed comps and committed costs.
4. Nine combinations of comp/commission inputs: the upward-rounded target rate meets the target, while one cent less fails it.
5. Per-night rates and the equivalent flat floor.
6. No-displacement cases, including unused nights, without invented alternative data.
7. Alternative inputs required by stressed demand even if base displacement is zero.
8. All-comps, negative alternative margin, missing inputs, impossible capacity/comps,100% combined fees, malformed numbers, booleans/lists/objects and nonfinite values.
9. Strict calendar/date coverage and the 90-night bound.
10. Stale/historical dates, user-entered minimum-rate constraints and complete finite CSV scenario rows.

The model rejects malformed numeric values rather than coercing `false` or an empty list to an allegedly explicit zero. JSON, CSV and plain-text summaries can be exported only after current valid analysis. Editing any input visibly invalidates the prior analysis and disables export until recalculated. The CSV uses quoted cells and formula-prefix neutralization for strings. Drafts and up to 20 saved checks are retained per hotel; a backup remains necessary because browser storage can be cleared.

## Sources and verification boundaries

Primary implementation evidence: this repository’s existing `index.html` functions identified above, the new `src/deal-checker.js` formulas and the independent known-answer tests. Financial formulas in this report are derived explicitly, so no external hotel policy or unnamed “decision guide” is used as authority.

Further reading URLs are [STR’s glossary](https://str.com/data-insights/resources/glossary) for ADR/room metrics and [OpenStax cost-volume-profit / break-even](https://openstax.org/books/principles-managerial-accounting/pages/3-2-calculate-a-break-even-point-in-units-and-dollars). Both retrieval attempts returned proxy tunnel403 in this environment; their current contents were **not** consulted or verified. They are background references, not claimed evidence for Hilton policy, current costs or this particular calculation.
