# V2 Pilot — Relevance Annotation Guidelines
**Status: REVIEW DRAFT. No judgments have been human-validated.**

## Purpose
Test whether the 0–2 relevance rubric is usable for multilingual query-to-page retrieval, *before* collecting the proposed full V2 benchmark. The pilot contains **12 queries, 24 synthetic page-like documents and 288 draft judgments**. Real business/client information is excluded by design.

## Grading decision
- **2 — Fully relevant:** The page text clearly fulfills the explicit action/service, product, required location and route direction. A cross-language match is fully relevant when the need is met.
- **1 — Partially relevant:** The page is useful toward the task but misses a non-trivial requirement or does not offer the requested booking/action. Examples: a general overview vs a local reservation, or shared vs explicitly private transfer. Annotators should mark these as *borderline* for discussion.
- **0 — Not relevant:** The page belongs to another service, product, location, direction, or does not answer the informational need. Similar vocabulary alone is not sufficient.

## Specific edge cases to review
1. **SKQ01/SKQ02:** SK07 is grade 1 because it lists Winterberg as part of a national overview but cannot take a reservation. SK05 (snowboard) and SK06 (Mayrhofen) are grade 0.
2. **SKQ03:** SK03 is grade 2 despite being German-language: it clearly offers ski-edge repair in Winterberg. SK08 (lift tickets) is grade 0.
3. **PHQ03:** PH01/PH02 are grade 1 because they are general bookable physiotherapy services in Innsbruck but do not explicitly offer shoulder treatment. PH03 is grade 2. PH08 is a general Tyrol overview (grade 1).
4. **PHQ04:** PH05 is a focused Spanish explanation (grade 2); PH08 mentions manual therapy as part of a service overview (grade 1).
5. **TRQ01/TRQ02:** TR05 provides shared travel on the correct route (proposed grade 1), while the user explicitly requests private. TR06 and TR08 are informational only (grade 1). TR01/TR02 are full matches (grade 2).
6. **TRQ03:** TR03 is the sole full match for the **reverse route**, irrespective of its Spanish-language page.
7. **TRQ04:** TR04 is the only Airport → downtown booking. The direction and airport origin are essential.

## Annotation workflow
1. Read only the **query text** and the candidate's **title + description**. Do not read score outputs from any retrieval model.
2. Assign grade 0/1/2. Log whether information is insufficient or contradictory.
3. For each grade 1 or 2, include a short explanatory rationale; for grade 0 document the failing requirement when contested.
4. Review **all 288 pairs**; proposed initial judgments are **not** human-verified. A single reviewer can audit the pilot but should disclose that it is not independent double annotation.
5. Discuss borderline decisions and record adjudications in a changelog; update guidelines before changing many labels.
6. When ready, change judgment statuses to `reviewed` only after actual review and freeze the pilot files with a versioned commit. Do **not** treat current labels as frozen ground truth.
7. Verify query intent groups remain split together (cross-language paraphrases must not leak between development and test).

## Data ethics
All providers and page text in this pilot are fictional examples. Real place names are used only to test geographic intent. No customer data, medical records, availability assertions, prices, user addresses or private analytics are included.

## Modeling gate
Do not run, tune or publish pilot model leaderboards as validated benchmarks until labels and annotation guidelines have been reviewed and the intended retrieval text variant is frozen. Use test queries only after any development-stage decisions are fixed.

## What counts as a useful pilot outcome?
A verified, auditable judgment protocol and reproducible split—not a high retrieval score. Grade disagreements and ambiguous examples are valuable findings.
