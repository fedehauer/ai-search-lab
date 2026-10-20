# Benchmark V2 pilot — Grade-0 audit triage (v0.1)

**Status:** Mechanical completeness and domain-consistency screen only. This is **NOT an independent annotation audit**, and no grade-0 qrel has been confirmed or changed as a result.  
**Input:** The current [qrels draft](../../data/v2/pilot/qrels_draft.csv), [queries](../../data/v2/pilot/queries.jsonl), and [documents](../../data/v2/pilot/documents.jsonl).  
**Purpose:** Prioritize human review of currently **260 proposed grade-0 pairs** under the [strict evidence rubric](annotation_guidelines.md).

## Verified structural counts (2026-10-20)

| Field | Count |
|---|---:|
| Queries | 12 |
| Candidate documents | 24 |
| Query-document pairs | 288 |
| Proposed grade 0 | **260** |
| Proposed grade 1 | 16 |
| Proposed grade 2 | 12 |
| Grade-0 pairs where query and document share a sector | **68** |
| Grade-0 pairs across different sectors | **192** |
| Nonzero-grade pairs across different sectors | **0** |
| Pairs with non-reviewed status | **288** |

The counts follow from the explicit domain tags: each of the three sectors has **4 queries × 8 candidate documents = 32 within-sector pairs**, or **96** total within-sector pairs. Of those 96, **28** are graded 1 or 2, leaving **68 within-sector grade-0 candidates**. The remaining **192** pairs are cross-sector and currently all grade 0.

### Important limitations
- **Sector mismatch is not automatically proof of irrelevance** for all possible datasets; a cross-domain document may sometimes satisfy a broad task. Every grade-0 pair still needs a documented relevance review.
- Mechanical field checks cannot establish whether nuanced cross-language synonyms or implicit services would make a within-sector document useful.
- The **pilot coverage gate is blocked**: `SKQ01`, `PHQ01`, and `TRQ01` currently lack an explicitly supported grade-2 candidate. See [corpus repair plan](corpus_gap_plan_v0_2.md).
- No retrieval model was used to decide relevance. We must not evaluate the pilot as ready or infer anything about real SEO rankings.

## Human audit order (proposed)

1. **68 within-sector grade-0 pairs first**: these are the highest-risk candidates for labeling mistakes such as service synonyms, partial task utility, local/route direction, and informational versus transactional need.
2. **192 cross-sector pairs**: review by query and business sector, using a repeatable relevance checklist; do not mark them reviewed just because tags differ.
3. Confirm that text-language differences did not cause a grade-0 decision where the service/action matches.
4. For every recommended change: record the original grade, proposed grade, exact supporting text, the requirement that matches or fails, and reviewer provenance in the adjudication log before editing qrels.
5. Keep reviewer labels `proposed_unreviewed` until actual review is complete, and freeze a new version only after pilot coverage and annotation gates pass.

## Illustrative within-sector grade-0 cases to examine

These examples are **audit prompts**, not newly approved changes:

| Query → document | Why review carefully |
|---|---|
| `SKQ01→SK05` | Same location but snowboard rental rather than **ski** rental; product mismatch likely justifies 0 |
| `SKQ01→SK06` | Correct rental category but **Mayrhofen** instead of Winterberg; geographic mismatch likely justifies 0 |
| `SKQ03→SK01` | Winterberg **rental** vs an explicit **ski-edge repair** need; service mismatch likely justifies 0 |
| `PHQ02→PH03` | Innsbruck and physiotherapy match, but PH03 offers shoulder-treatment information, not an explicit appointment; check whether the synthetic description provides actual help toward booking |
| `PHQ04→PH08` | Manual-therapy keyword is mentioned but the query seeks a **definition/explanation**; a mere mention is insufficient, consistent with earlier grade-0 adjudication |
| `TRQ03→TR01` | Private transfer on the **reverse direction**; direction is a hard requirement |
| `TRQ04→TR03` | Private Puerto Escondido → Oaxaca route is not **airport → downtown** pickup; origin and destination differ |
| `TRQ01→TR03` | Private travel service resembles query, but reverse origin/destination; cannot assume symmetry |

### Review output required before any grade-0 change

A separate grade-0 adjudication sheet should capture `query_id`, `document_id`, current grade, recommended grade, diagnostic failure code(s), exact quote from synthetic description, reviewer's identity/role, and whether review was independent. The current CSV does **not** have these fields, and the previous observations have not been inserted into any new labels.

**Next research checkpoint:** Resolve corpus coverage first or in parallel, then review the 68 within-sector grade-0 cases without looking at model rankings. Do not claim all 260 have been human-validated based on this triage.
