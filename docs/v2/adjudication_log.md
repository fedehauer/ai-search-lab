# Benchmark V2 pilot — Adjudication log

**Research status:** Pilot labels remain provisional; this log documents explicit human-approved changes made to an AI-proposed dataset. It is not evidence of independent or blinded annotation.

## 2026-10-20 — PH08 relevance reclassification

**Source audit:** [Partial relevance audit v0.1](partial_relevance_audit_v0_1.md)  
**Rubric:** [V2 annotation guidelines](annotation_guidelines.md)  
**Dataset:** [Pilot qrels draft](../../data/v2/pilot/qrels_draft.csv)  
**Applied commit:** [b2668109cbe760b54ca70225c72f071ad13b2246](https://github.com/fedehauer/ai-search-lab/commit/b2668109cbe760b54ca70225c72f071ad13b2246)

### Decision and authorization

The user approved the three **PROPOSE-0** cases from the assistant's grade-1 audit. The source was the existing synthetic `title + description` text, evaluated against explicit query requirements. No model rankings or performance scores were consulted as a reason for relabeling.

| Query | Document | Grade before | Grade after | Reason |
|---|---|---:|---:|---|
| **PHQ01** — Book physiotherapy appointment in Innsbruck (German) | PH08 — General regional treatment overview in Tyrol | 1 | **0** | Neither appointment-booking functionality nor a specific Innsbruck booking/service is supported by the page text. Merely belonging to the same therapeutic field is insufficient. |
| **PHQ02** — Book physiotherapy appointment in Innsbruck (English) | PH08 — Same general overview | 1 | **0** | Same intent and evidence as PHQ01; equivalent multilingual queries should receive consistent judgments. |
| **PHQ04** — What is manual therapy in physiotherapy? (Spanish) | PH08 — Regional treatment overview | 1 | **0** | The page only **mentions** manual therapy and does not explain what it is; mention alone fails the informational intent. |

### Exact dataset effects

- Exactly **3** existing grades changed, all from **1 → 0**. Their rationale strings were revised accordingly.
- Pair count stayed **288** (= 12 queries × 24 documents); no IDs, queries, document texts, splits, or grades in the other 285 pairs changed.
- Grade counts shifted from **256 / 14 / 18** to **259 / 11 / 18** for grades **0 / 1 / 2**.
- Existing `review_status=proposed_unreviewed` was **left unchanged for all 288 rows**. User authorization for these corrections is not an independent second-human assessment of a complete benchmark.
- The five previously flagged **HOLD** pairs were **not** reclassified. The six earlier **KEEP-1** recommendations likewise remain proposed.
- No V2 model performance claims were generated as part of this decision.

### Outstanding work

1. Resolve five HOLD cases: `SKQ01→SK07`, `SKQ02→SK07`, `PHQ03→PH08`, `TRQ01→TR06`, `TRQ02→TR06` using the rubric and only the existing title/description evidence.
2. Validate the remaining **285** proposed pair judgments (including grade 0 and grade 2) through a documented review process. This count includes the 11 remaining grade-1 pairs; resolving five HOLD cases is only part of the required work.
3. Document adjudications before any further label changes. Freeze a versioned benchmark only after all requirements and judgments have been audited.

---

## 2026-10-20 — Five previously ambiguous pilot cases

**Audit basis:** The five `HOLD` pairs in [Partial relevance audit v0.1](partial_relevance_audit_v0_1.md) were revisited using the *existing* title + description text and the established rule that a grade-1 document must supply specific useful assistance, but cannot be treated as accomplishing an explicit booking or service constraint. This continuation was user-authorized as a review task, **not independently annotated or blinded**.

| Query | Document | Before | After | Decision and evidence |
|---|---|---:|---:|---|
| SKQ01 | SK07 | 1 | **1** | Keep: a German national ski-rental locations overview explicitly includes **Winterberg**, the requested service and destination. It can assist discovery, but **has no direct online booking**. |
| SKQ02 | SK07 | 1 | **1** | Keep for consistency with the same intent expressed in Spanish; relevance does not require matching page language in this pilot. |
| PHQ03 | PH08 | 1 | **0** | Relabel: a Tyrol-wide treatment overview mentions shoulders, but does not evidence a **shoulder-physiotherapy option in Innsbruck**. This is insufficiently specific to the local service need. |
| TRQ01 | TR06 | 1 | **1** | Keep: an overview of ground-travel choices for the **exact Oaxaca City → Puerto Escondido direction** offers useful route-specific options, although **no private-transfer booking** is available. |
| TRQ02 | TR06 | 1 | **1** | Keep for the equivalent Spanish-language private-transfer query; same route-specific evidence, booking limitation and relevance policy. |

**Review distinction:** SK07 and TR06 are not grade 2: a rental booking/private-transfer booking is explicitly required but unavailable in their descriptions. Grade 1 represents *route/destination-specific exploratory utility*, not satisfaction of the user's strict action. PH08 is grade 0 because its text does not establish the requested **city-specific** treatment; mentioning a broad region and a related condition is insufficient.

**Change implemented:** Exactly one CSV row changed: `PHQ03,PH08` **1 → 0**, with a more precise rationale. [Commit bcbeb34257829f0a9315711ee9222e50cdc6c678](https://github.com/fedehauer/ai-search-lab/commit/bcbeb34257829f0a9315711ee9222e50cdc6c678).

**After this change:** All **288** qrels remain present, grades **260 / 10 / 18** for **0 / 1 / 2**, and **all statuses remain `proposed_unreviewed`**. The five HOLD decisions are now resolved **provisionally**; zero model-based evidence was used for any change. Pilot test-query judgments are public and openly adjudicated *before* V2 model runs; this pilot must not be advertised as a permanently blinded evaluation set.

**Remaining work:** Review the other **287** grade proposals systematically (including the four retained grade-1 decisions above); audit grade-0 and grade-2 labels; check whether the inclusion of cities/routes actually provides meaningful assistance, as opposed to mere name-dropping, using external human adjudicators if robust inter-annotator validity is a goal. The audit does not claim ground-truth validation, statistically independent labeling or downstream model superiority.

---

## 2026-10-20 — Strict evidence rule for six former grade-2 pairs

**Decision:** The user explicitly approved grading as fully relevant **only when the candidate title/description demonstrates every explicit query requirement**. Absence of evidence is not proof of service absence; it cannot establish full task satisfaction.

**Reference:** [Grade-2 audit](full_relevance_audit_v0_1.md) and [annotation guidelines](annotation_guidelines.md).  
**Implemented qrels commit:** [9cc674cf5c4f2d6a57a9083d4226a8e3c88f29a0](https://github.com/fedehauer/ai-search-lab/commit/9cc674cf5c4f2d6a57a9083d4226a8e3c88f29a0).

| Query | Candidate | Previous | New | Missing explicit evidence |
|---|---|---:|---:|---|
| SKQ01 — rent skis **online** in Winterberg | SK01 | 2 | **1** | Ski rental reservation is described, but **online reservation channel** is not |
| SKQ01 — same query | SK02 | 2 | **1** | Spanish rental booking page, but **online reservation channel** is not |
| PHQ01 — book physiotherapy **online** in Innsbruck | PH01 | 2 | **1** | Physio appointment booking is described, but **online scheduling** is not |
| PHQ01 — same query | PH02 | 2 | **1** | English booking page, but **online scheduling** is not |
| TRQ01 — book a private **car** transfer Oaxaca City → Puerto Escondido | TR01 | 2 | **1** | Correct private route/booking, but **car** vehicle class is not stated |
| TRQ01 — same query | TR02 | 2 | **1** | Correct private booking in Spanish, but **car** vehicle class is not stated |

**Only six existing rows changed**, and each had its rationale rewritten to distinguish `unspecified` from `unavailable`; every `review_status` remains `proposed_unreviewed`. Other **282** qrel rows, all 12 query strings, all 24 document descriptions, and development/test group allocations remain untouched.

### Data quality impact and evaluation blocker

- Total graded pairs still **288**.
- Grade distribution **260 / 16 / 12** for grades **0 / 1 / 2**, previously **260 / 10 / 18**.
- **SKQ01**, **PHQ01**, and **TRQ01** now have **no grade-2 candidate** in the published 24-document synthetic corpus.
- This violates the V2 pilot gate requiring one fully relevant candidate for every query. **Do not calculate/publish model performance as if the pilot passed validation.**
- The fix is a **separately versioned corpus design change**, with a new complete qrel pool and a fresh validation pass. Do not silently add capabilities to existing descriptions to preserve labels.
- Review of 260 grade-0 and remaining 16 grade-1 proposals is still needed. These six authorized changes are not evidence of full independent judgment validation.
