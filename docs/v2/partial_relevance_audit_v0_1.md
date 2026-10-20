# Benchmark V2 pilot — Grade-1 relevance audit (v0.1)

**Status:** Independent *reasoning pass by the assistant only*; **not** a second-human annotation or validated ground truth.  
**Historical snapshot note (2026-10-20):** This report captures the **pre-adjudication** distribution of 14 proposed grade-1 labels. The user subsequently approved and we applied **PHQ01→PH08, PHQ02→PH08, and PHQ04→PH08: grade 1 → 0**. After the first correction, the dataset contained **11** proposed grade-1 pairs and five open HOLD cases. **Subsequent adjudication resolved all five HOLD cases provisionally**, with one additional change PHQ03→PH08 from grade 1 to grade 0. The **current dataset contains 10 grade-1 proposals**. See the [adjudication log](adjudication_log.md) for both chronological sets of decisions. The table below is intentionally preserved as the historical audit, not the latest grade distribution.

**Scope:** All 14 pairs currently assigned proposed grade **1** in `data/v2/pilot/qrels_draft.csv`.  
**Reference:** [Annotation guidelines](annotation_guidelines.md) and [pilot dataset](../../data/v2/pilot/README.md).  
**Change policy:** This file records recommendations **without changing any relevance grades, review statuses, query strings, document contents, or development/test splits**.

## Method

For each grade-1 pair, compare only the query text against the document **title and description** published in the pilot. Assess whether:
1. the page text concretely assists with the stated intent;
2. any explicit action, locality, service modality, product or direction is unmet;
3. the evidence supports meaningful partial relevance, or merely topical overlap.

Use three review outcomes:
- **KEEP-1 (provisional):** grade 1 is defensible on current visible text; still needs full annotation review;
- **HOLD:** the current evidence is too ambiguous for a confident 1/0 choice;
- **PROPOSE-0:** the current description fails to demonstrate useful partial satisfaction; prefer grade 0 subject to adjudication.

**Grade 1 never means successful task completion.** No inference about hidden booking functionality, location coverage or user willingness to relax hard constraints is permitted.

## All 14 reviewed pairs

| Pair | Query intent | Document evidence in the dataset | Grade now | Audit outcome | Diagnostic code / reasoning |
|---|---|---|---:|---|---|
| SKQ01 → SK07 | Rent skis online in Winterberg | General German ski-rental-location overview mentioning Winterberg; **no direct booking** | 1 | **HOLD** | `booking_unavailable`, possible `insufficient_evidence`: does it actually identify useful Winterberg rental options or only mention Winterberg? |
| SKQ02 → SK07 | Reserve rental skis in Winterberg (Spanish query) | Same overview, regardless of cross-language retrieval | 1 | **HOLD** | Same evidence gap as SKQ01; translations of equivalent intent should receive consistent labels |
| PHQ01 → PH08 | Book physiotherapy appointment in Innsbruck | Regional overview of treatments in Tyrol; **no concrete booking in Innsbruck** | 1 | **PROPOSE-0** | `booking_unavailable` / `insufficient_evidence`: neither the appointment action nor Innsbruck service is evidenced |
| PHQ02 → PH08 | Book physiotherapy appointment in Innsbruck (English query) | Same regional overview without specific Innsbruck booking | 1 | **PROPOSE-0** | Same missing booking and locality as PHQ01; cross-language equivalence must be treated consistently |
| PHQ03 → PH01 | Find physiotherapy for shoulder pain in Innsbruck | General bookable physiotherapy in Innsbruck; no shoulder specialty stated | 1 | **KEEP-1** | `specialization_unspecified` (proposed diagnostic code): city and treatment category fit; shoulder-specific suitability not shown |
| PHQ03 → PH02 | Find physiotherapy for shoulder pain in Innsbruck | English general bookable physiotherapy in Innsbruck; no shoulder specialty stated | 1 | **KEEP-1** | Same as PH01; do not infer shoulder treatment outcomes or specialist care |
| PHQ03 → PH08 | Find shoulder physiotherapy in Innsbruck | Regional overview mentions shoulders but does not identify a specific Innsbruck provider/booking | 1 | **HOLD** | `insufficient_evidence` / `location_unspecified`: may be relevant educationally but no clear Innsbruck treatment option |
| PHQ04 → PH08 | Explain what manual therapy is | Regional treatment overview **mentions** manual therapy but does not explain it | 1 | **PROPOSE-0** | `information_need_mismatch`: a passing mention is not an explanation |
| TRQ01 → TR05 | Book **private** Oaxaca City → Puerto Escondido transfer | Bookable **shared** shuttle in correct direction | 1 | **KEEP-1** | `service_modality_mismatch`: reasonable *alternative* under the exploratory rubric, but fails strict private-service requirement |
| TRQ01 → TR06 | Book private transfer on the specified route | General overview of ground travel choices on correct route, without booking; private service not specified | 1 | **HOLD** | `booking_unavailable`, possible `insufficient_evidence`: does the overview actually provide actionable private-transfer options? |
| TRQ01 → TR08 | Book private transfer on the specified route | Guide **specifically about private transfers** on correct route; no direct booking | 1 | **KEEP-1** | `booking_unavailable`: targeted information clearly helps but cannot fulfill booking |
| TRQ02 → TR05 | Book **private** transfer on same route (Spanish query) | Same **shared** shuttle in correct direction | 1 | **KEEP-1** | `service_modality_mismatch`: same rubric as TRQ01; user explicitly accepted the grade-1 fallback interpretation for TRQ01 |
| TRQ02 → TR06 | Book private transfer on specified route (Spanish query) | Same general travel overview without booking | 1 | **HOLD** | Same `booking_unavailable` and possible `insufficient_evidence` as TRQ01 |
| TRQ02 → TR08 | Book private transfer on specified route (Spanish query) | Same private-transfer guide, no booking | 1 | **KEEP-1** | `booking_unavailable`; same need and evidence as TRQ01 |

## Totals

| Audit outcome | Count | Meaning |
|---|---:|---|
| **KEEP-1** | **6** | Plausible partial assistance demonstrated in the document text |
| **HOLD** | **5** | Need to clarify usefulness or locality before deciding between 1 and 0 |
| **PROPOSE-0** | **3** | Existing description does not satisfy the pilot's evidence rule |
| **Total** | **14** | All existing grade-1 pairs reviewed in this pass |

**No rows have been relabeled.** All 288 grades remain in `qrels_draft.csv` with `review_status=proposed_unreviewed`; this report is a recommendation, not a dataset mutation.

## Methodological issues discovered

### 1. Semantic relatedness can masquerade as relevance
The PHQ04 → PH08 pair matches the *words* “manual therapy” but does not answer the “what is it?” question. Treating mere mention as partially relevant violates the documented need-satisfaction rubric.

### 2. Missing locality and missing booking action can compound
PHQ01/PHQ02 → PH08 fails to substantiate **both** booking in Innsbruck and a specific Innsbruck service. A regional overview of treatments should not automatically be considered an actionable booking alternative.

### 3. Cross-language pairs must be adjudicated together
SKQ01/SKQ02, PHQ01/PHQ02 and TRQ01/TRQ02 express equivalent needs in different languages. Their matched-document grades should be consistent unless language accessibility is explicitly defined as a user constraint. The pilot currently does not treat document-language matching as a hard relevance requirement.

### 4. The meaning of 'plausible alternative' needs boundaries
A shared shuttle on the correct route offers an actual booking but violates 'private'; a non-bookable travel overview may or may not help identify a private provider. They should not receive the same grade merely because both discuss the route. This ambiguity is a **research finding**, not a reason to retroactively tune descriptions to make a model look better.

### 5. Current failure-code schema is diagnostic only
`specialization_unspecified` and `location_unspecified` are **suggested additional codes**, not part of the approved diagnostic code list or dataset columns. Approve names and meanings in the annotation guide before structured capture. Do not add codes to the current CSV without separately approving a schema change.

## Next decision and proposed order of work

1. Confirm whether **title + description alone** must prove concrete assistance. Under that stricter evidence rule, PHQ01/PHQ02/PHQ04 → PH08 are recommended grade 0.
2. Review the **five HOLD pairs** on the *existing* source text, without rewriting the documents to manufacture support for a previous judgment. If text is insufficient, choose 0 or keep unresolved—not an assumed 1.
3. Record adjudications in a versioned change log; only then change approved `qrels_draft.csv` rows and statuses.
4. After resolving grade-1 ambiguity, audit a sample of grade-0 and grade-2 pairs. This pass does **not** verify the other **274 judgments**.
5. Do not run a benchmark leaderboard on unreviewed qrels or interpret its held-out test as blinded after public release.

## Human-review provenance

A user provisionally selected **SKQ01 → SK07 = 1** and **TRQ01 → TR05 = 1** in the learning session. These selections establish preferred exploratory rubric interpretations but are **not** independent, blinded double annotation. The SK07 choice remains conditional on whether the text supports actionable assistance; the TR05 choice assumes alternatives may count as partial relevance despite the explicit private requirement. All other outcomes in this audit are *assistant recommendations* and have not been independently checked.
