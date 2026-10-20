# Pilot v0.2 — Audit of 36 new query-document judgments

**Status:** One assistant-authored evidence audit of proposed, synthetic relevance judgments; **not** independent human annotation, validated ground truth, or model performance analysis.  
**Source:** `data/v2/pilot_v0_2/queries.jsonl`, `documents.jsonl` and `qrels_draft.csv`, using the published [strict explicit-evidence rubric](annotation_guidelines.md).  
**Reviewed corpus change:** Three extra synthetic documents (`SK09`, `PH09`, `TR09`) across all 12 queries.  
**Dataset edits:** **None.** All 324 qrels remain `proposed_unreviewed`.

## Summary

| Proposed grade | Pairs | Audit outcome |
|---|---:|---|
| 0 | **29** | KEEP-0 (provisional) |
| 1 | **1** | KEEP-1 (provisional) |
| 2 | **6** | KEEP-2 (provisional) |
| **Total** | **36** | No grade changes recommended in this pass |

The six grade-2 matches all have **explicit support** for the exact booking mode, location or route, and private **car** where required. The single grade-1 match `PHQ03→PH09` is a general physiotherapy booking in Innsbruck without explicit shoulder treatment. Thus a grade-2 label would incorrectly imply that a generic service can satisfy a shoulder-specific need.

## All 36 pairs

| Pair | Current grade | Audit recommendation | Explicit evidence / issue |
|---|---:|---|---|
| `SKQ01|SK09` | 2 | **KEEP-2** | Exact online ski rental in Winterberg, explicitly bookable on the page. |
| `SKQ01|PH09` | 0 | **KEEP-0** | The page is for a different service sector and provides no requested action, city-specific service, route, or explanation. |
| `SKQ01|TR09` | 0 | **KEEP-0** | The page is for a different service sector and provides no requested action, city-specific service, route, or explanation. |
| `SKQ02|SK09` | 2 | **KEEP-2** | Same Winterberg ski rental with direct online booking; query language does not constrain document language. |
| `SKQ02|PH09` | 0 | **KEEP-0** | The page is for a different service sector and provides no requested action, city-specific service, route, or explanation. |
| `SKQ02|TR09` | 0 | **KEEP-0** | The page is for a different service sector and provides no requested action, city-specific service, route, or explanation. |
| `SKQ03|SK09` | 0 | **KEEP-0** | Rental booking does not offer ski-edge repair. |
| `SKQ03|PH09` | 0 | **KEEP-0** | The page is for a different service sector and provides no requested action, city-specific service, route, or explanation. |
| `SKQ03|TR09` | 0 | **KEEP-0** | The page is for a different service sector and provides no requested action, city-specific service, route, or explanation. |
| `SKQ04|SK09` | 0 | **KEEP-0** | Rental booking does not sell new skis. |
| `SKQ04|PH09` | 0 | **KEEP-0** | The page is for a different service sector and provides no requested action, city-specific service, route, or explanation. |
| `SKQ04|TR09` | 0 | **KEEP-0** | The page is for a different service sector and provides no requested action, city-specific service, route, or explanation. |
| `PHQ01|SK09` | 0 | **KEEP-0** | The page is for a different service sector and provides no requested action, city-specific service, route, or explanation. |
| `PHQ01|PH09` | 2 | **KEEP-2** | Explicit online physiotherapy scheduling in Innsbruck. |
| `PHQ01|TR09` | 0 | **KEEP-0** | The page is for a different service sector and provides no requested action, city-specific service, route, or explanation. |
| `PHQ02|SK09` | 0 | **KEEP-0** | The page is for a different service sector and provides no requested action, city-specific service, route, or explanation. |
| `PHQ02|PH09` | 2 | **KEEP-2** | Physiotherapy booking in Innsbruck, with online scheduling explicitly available. |
| `PHQ02|TR09` | 0 | **KEEP-0** | The page is for a different service sector and provides no requested action, city-specific service, route, or explanation. |
| `PHQ03|SK09` | 0 | **KEEP-0** | The page is for a different service sector and provides no requested action, city-specific service, route, or explanation. |
| `PHQ03|PH09` | 1 | **KEEP-1** | Offers physiotherapy appointments in Innsbruck but explicitly does not identify shoulder-specific care; plausible general alternative only. |
| `PHQ03|TR09` | 0 | **KEEP-0** | The page is for a different service sector and provides no requested action, city-specific service, route, or explanation. |
| `PHQ04|SK09` | 0 | **KEEP-0** | The page is for a different service sector and provides no requested action, city-specific service, route, or explanation. |
| `PHQ04|PH09` | 0 | **KEEP-0** | Scheduling is not an explanation of manual therapy. |
| `PHQ04|TR09` | 0 | **KEEP-0** | The page is for a different service sector and provides no requested action, city-specific service, route, or explanation. |
| `TRQ01|SK09` | 0 | **KEEP-0** | The page is for a different service sector and provides no requested action, city-specific service, route, or explanation. |
| `TRQ01|PH09` | 0 | **KEEP-0** | The page is for a different service sector and provides no requested action, city-specific service, route, or explanation. |
| `TRQ01|TR09` | 2 | **KEEP-2** | Explicit private car reservation on the correct Oaxaca City → Puerto Escondido direction. |
| `TRQ02|SK09` | 0 | **KEEP-0** | The page is for a different service sector and provides no requested action, city-specific service, route, or explanation. |
| `TRQ02|PH09` | 0 | **KEEP-0** | The page is for a different service sector and provides no requested action, city-specific service, route, or explanation. |
| `TRQ02|TR09` | 2 | **KEEP-2** | Bookable private car, correct direction; matching page language is not required. |
| `TRQ03|SK09` | 0 | **KEEP-0** | The page is for a different service sector and provides no requested action, city-specific service, route, or explanation. |
| `TRQ03|PH09` | 0 | **KEEP-0** | The page is for a different service sector and provides no requested action, city-specific service, route, or explanation. |
| `TRQ03|TR09` | 0 | **KEEP-0** | Private car exists, but the route runs in the opposite direction. |
| `TRQ04|SK09` | 0 | **KEEP-0** | The page is for a different service sector and provides no requested action, city-specific service, route, or explanation. |
| `TRQ04|PH09` | 0 | **KEEP-0** | The page is for a different service sector and provides no requested action, city-specific service, route, or explanation. |
| `TRQ04|TR09` | 0 | **KEEP-0** | Oaxaca City departure does not meet Puerto Escondido Airport → downtown pickup. |

## Important QA findings

1. **Completeness:** All 12 queries have one row for each new candidate document, including no-match documents in other sectors. No unjudged pair is implicitly counted as grade 0.
2. **User need, not mere string overlap:** `SKQ03→SK09` is grade 0 despite Winterberg and skis being shared terms—repair is not rental. `TRQ03→TR09` is grade 0 despite being a private car service—the route is reversed.
3. **Multilingual equivalence:** SKQ01 (German) and SKQ02 (Spanish) both grade `SK09` as 2; likewise for Spanish and English queries referencing the same private route.
4. **Research design caution:** The three new pages were **constructed specifically to fill known relevance gaps** and contain explicit query terms, with an uneven “synthetic test page” description style relative to v0.1. Even if they are correctly graded, this is **not an unbiased test of real search behavior**. Do not use the pilot to claim a model outperforms another without a different, held-out benchmark.
5. **No independent adjudication:** This table does not mark labels as `reviewed`, does not constitute inter-annotator agreement, and does not change `qrels_draft.csv`.

**Next:** Examine the 73 same-domain grade-0 pairs using [the within-domain grade-0 audit](grade0_within_domain_audit_v0_2.md) and adjudicate any borderline pairs before a formal label freeze.
