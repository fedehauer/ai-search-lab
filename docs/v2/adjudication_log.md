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
