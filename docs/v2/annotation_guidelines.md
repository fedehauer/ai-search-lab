# V2 Pilot — Relevance Annotation Guidelines
**Status: REVIEW DRAFT. No judgments have been human-validated.**

## Purpose
Test whether the 0–2 relevance rubric is usable for multilingual query-to-page retrieval, *before* collecting the proposed full V2 benchmark. The pilot contains **12 queries, 24 synthetic page-like documents and 288 draft judgments**. Real business/client information is excluded by design.

## Grading decision
- **2 — Fully relevant:** The page text clearly fulfills the explicit action/service, product, required location and route direction. A cross-language match is fully relevant when the need is met.
- **1 — Partially relevant:** The page provides **meaningful, evidence-supported assistance or a plausible alternative** toward the user's specific task, but fails to satisfy one or more explicit requirements. This is **not** successful task completion. Examples include an actionable destination-specific rental overview without direct booking, or a bookable shared shuttle where a private transfer was requested. Annotators must flag such cases as *borderline* and document the missing requirement. Mere topical overlap or location name-dropping is insufficient.
- **0 — Not relevant:** The page belongs to another service, product, location, direction, or does not answer the informational need. Similar vocabulary alone is not sufficient.

## Relevance vs. strict task satisfaction

**Two different judgments must not be conflated:**
- **Graded relevance (0/1/2):** Does the retrieved page help address the user's specific need, fully or partially?
- **Strict task satisfaction (yes/no):** Does the page demonstrably satisfy **every explicit constraint**, including booking ability, service modality and route direction? Grade 1 **never** implies strict task satisfaction. Grade 2 requires demonstrable satisfaction of all explicit requirements under the pilot's page-text evidence.

**Operational rule for grade 1:** The visible title + description must demonstrate a concrete connection to satisfying the query, beyond shared keywords. If they only mention the topic or location but offer no identifiable useful information, choose grade 0 or flag the case `insufficient_evidence` for adjudication. Never infer a booking flow, service availability or the user's willingness to compromise unless the synthetic text supports it.

**Requirements can be hard constraints:** For instance, `private` may be mandatory for a real traveler. A shared shuttle can be a plausible fallback in this *exploratory* relevance rubric, but a strict constraint-satisfaction interpretation would mark it as failing the task, and could justify grade 0 under a stricter annotation policy. Record such ambiguity before any change of rubric or relevance grades; do not silently recode the dataset.

### Suggested diagnostic failure codes (documentation only)

These codes explain *why* a candidate fails to achieve grade 2. They are **not yet columns in the pilot data**, and adding them to the guide does not modify any relevance judgments.

| Code | When to use | Example |
|---|---|---|
| `booking_unavailable` | Correct destination/service but no requested direct booking function | SKQ01 → SK07 (proposed grade 1) |
| `service_modality_mismatch` | Route/service is related but required service class differs | TRQ01 → TR05: shared instead of private (proposed grade 1) |
| `service_type_mismatch` | Wrong product or service | Ski rental query → snowboard rental page |
| `location_mismatch` | Service fits but required destination does not | Winterberg query → Mayrhofen-only rental |
| `route_direction_mismatch` | Origin/destination direction is reversed | Oaxaca → Puerto Escondido query → reverse-only transfer |
| `information_need_mismatch` | Content does not answer the informational question | Therapy explanation query → unrelated booking page |
| `insufficient_evidence` | The available title/description does not substantiate partial usefulness | Destination mentioned in passing without rental options |

**Review requirements:** (1) assess the exact query constraints; (2) inspect only title + description; (3) decide whether there is demonstrable meaningful assistance; (4) record the failed condition; (5) flag any judgment that depends on unstated flexibility or insufficient evidence. A second annotator or an adjudication pass should revisit borderline cases. The current 288 AI-proposed labels remain **unreviewed**.

## Specific edge cases to review
1. **SKQ01/SKQ02:** SK07 retains a **proposed, unreviewed grade 1** (`booking_unavailable`): it is a general ski-rental overview that includes Winterberg but cannot take an online reservation. **Validation question:** does its title + description demonstrate meaningful Winterberg rental guidance, or merely name-drop the destination? If only the latter, grade 0 is defensible; review the evidence before treating grade 1 as ground truth. SK05 (snowboard) and SK06 (Mayrhofen) are proposed grade 0.
2. **SKQ03:** SK03 is grade 2 despite being German-language: it clearly offers ski-edge repair in Winterberg. SK08 (lift tickets) is grade 0.
3. **PHQ03:** PH01/PH02 are grade 1 because they are general bookable physiotherapy services in Innsbruck but do not explicitly offer shoulder treatment. PH03 is grade 2. PH08 is a general Tyrol overview (grade 1).
4. **PHQ04:** PH05 is a focused Spanish explanation (grade 2); PH08 mentions manual therapy as part of a service overview (grade 1).
5. **TRQ01/TRQ02:** TR05 offers bookable shared travel on the correct route and retains **proposed, unreviewed grade 1** (`service_modality_mismatch`). It does **not** satisfy the explicitly requested private-service constraint. An annotator treating `private` as non-negotiable may argue for grade 0; log this interpretation rather than changing labels silently. TR06 and TR08 are informational alternatives (proposed grade 1). TR01/TR02 fully match the booking and modality (proposed grade 2).
6. **TRQ03:** TR03 is the sole full match for the **reverse route**, irrespective of its Spanish-language page.
7. **TRQ04:** TR04 is the only Airport → downtown booking. The direction and airport origin are essential.

## Annotation workflow
1. Read only the **query text** and the candidate's **title + description**. Do not read score outputs from any retrieval model.
2. Assign grade 0/1/2. Log whether information is insufficient or contradictory.
3. For each grade 1 or 2, include a short explanatory rationale; for grade 0 document the failing requirement when contested. For grade 1, explicitly record the unfulfilled requirement and a proposed failure code in the adjudication notes (the pilot CSV schema is unchanged).
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
