# Pilot v0.2 — Audit of 73 within-domain grade-0 pairs

**Status:** Single assistant-authored, evidence-based preliminary audit. **NOT** independent human ground-truth verification.  
**Source:** `data/v2/pilot_v0_2/queries.jsonl`, `documents.jsonl` and `qrels_draft.csv`.  
**Method:** Compare each grade-0 query against the corresponding synthetic page's **title + description** under the [strict relevance guidelines](annotation_guidelines.md). Do not use model output or inferred hidden page functionality.  
**Dataset mutations:** None; all 324 pairs remain `proposed_unreviewed`.

## Findings

| Outcome | Count |
|---|---:|
| **KEEP-0**, provisionally supported by explicit service/product/locality/route mismatch | **71** |
| **HOLD**, potential partial relevance requiring a policy decision | **2** |
| **Total** same-domain grade-0 proposals inspected | **73** |

The two HOLD pairs are **PHQ01→PH03** and **PHQ02→PH03**. The candidate title and description offer information about *shoulder physiotherapy in Innsbruck*, but do not state an appointment booking mechanism. The queries request a *physiotherapy appointment in Innsbruck* (PHQ01 explicitly online). Under the rubric, one could defend grade **0** because no booking route is demonstrated, or grade **1** because a real, city-specific treatment page could help identify a suitable therapy service. We must decide whether this provides **meaningful help** or only topical/local overlap; do **not** silently raise the labels or rewrite the document to resolve the ambiguity. Neither can receive grade 2 under the adopted strict evidence criterion.

The other **71** appear consistent with grade 0 because of documented different service/condition/product, incorrect route direction or locality, or an informational page that does not answer the requested question. These are still **assistant recommendations**, not reviewer-confirmed ground truth.

## All 73 within-domain grade-0 pairs

### Ski (26 proposed grade-0 pairs)

| Pair | Reason code | Audit outcome | Rationale based on title + description |
|---|---|---|---|
| `SKQ01→SK03` | `service_type_mismatch` | **KEEP-0** | Repair rather than ski rental |
| `SKQ01→SK04` | `action_mismatch` | **KEEP-0** | Buying new skis rather than renting |
| `SKQ01→SK05` | `product_mismatch` | **KEEP-0** | Snowboard rental, explicitly not ski rental |
| `SKQ01→SK06` | `location_mismatch` | **KEEP-0** | Skis rented in Mayrhofen, not Winterberg |
| `SKQ01→SK08` | `service_type_mismatch` | **KEEP-0** | Lift tickets rather than equipment rental |
| `SKQ02→SK03` | `service_type_mismatch` | **KEEP-0** | Repair rather than ski rental |
| `SKQ02→SK04` | `action_mismatch` | **KEEP-0** | Buying new skis rather than renting |
| `SKQ02→SK05` | `product_mismatch` | **KEEP-0** | Snowboard rental, explicitly not ski rental |
| `SKQ02→SK06` | `location_mismatch` | **KEEP-0** | Skis rented in Mayrhofen, not Winterberg |
| `SKQ02→SK08` | `service_type_mismatch` | **KEEP-0** | Lift tickets rather than equipment rental |
| `SKQ03→SK01` | `service_type_mismatch` | **KEEP-0** | Ski rental information or booking does not describe ski repair or edge service |
| `SKQ03→SK02` | `service_type_mismatch` | **KEEP-0** | Ski rental information or booking does not describe ski repair or edge service |
| `SKQ03→SK04` | `service_type_mismatch` | **KEEP-0** | Retail purchase does not offer edge repair |
| `SKQ03→SK05` | `service_type_mismatch` | **KEEP-0** | Snowboard rental does not offer ski-edge repair |
| `SKQ03→SK06` | `service_type_mismatch` | **KEEP-0** | Ski rental information or booking does not describe ski repair or edge service |
| `SKQ03→SK07` | `service_type_mismatch` | **KEEP-0** | Ski rental information or booking does not describe ski repair or edge service |
| `SKQ03→SK08` | `service_type_mismatch` | **KEEP-0** | Lift ticket content does not provide repair |
| `SKQ04→SK01` | `action_mismatch` | **KEEP-0** | Rental is not buying new skis |
| `SKQ04→SK02` | `action_mismatch` | **KEEP-0** | Rental is not buying new skis |
| `SKQ04→SK03` | `action_mismatch` | **KEEP-0** | Repair is not new-ski purchase |
| `SKQ04→SK05` | `product_mismatch` | **KEEP-0** | Snowboard rental differs from purchasing skis |
| `SKQ04→SK06` | `action_mismatch` | **KEEP-0** | Rental is not buying new skis |
| `SKQ04→SK07` | `action_mismatch` | **KEEP-0** | Rental is not buying new skis |
| `SKQ04→SK08` | `service_type_mismatch` | **KEEP-0** | Lift pass is not ski retail |
| `SKQ03→SK09` | `service_type_mismatch` | **KEEP-0** | Ski rental information or booking does not describe ski repair or edge service |
| `SKQ04→SK09` | `action_mismatch` | **KEEP-0** | Rental is not buying new skis |

### Physiotherapy (25 proposed grade-0 pairs)

| Pair | Reason code | Audit outcome | Rationale based on title + description |
|---|---|---|---|
| `PHQ01→PH03` | `HOLD` | **HOLD** | Local shoulder-physiotherapy information might help find a local service, but no appointment or online booking is evidenced; relevance 0 vs 1 is genuinely disputable under the 'meaningful assistance' rule. |
| `PHQ01→PH04` | `information_need_mismatch` | **KEEP-0** | Back-exercise guide gives no route to a physio appointment |
| `PHQ01→PH05` | `information_need_mismatch` | **KEEP-0** | General manual-therapy explanation has no Innsbruck appointment options |
| `PHQ01→PH06` | `location_mismatch` | **KEEP-0** | Booking in Schwaz does not satisfy Innsbruck locality |
| `PHQ01→PH07` | `service_type_mismatch` | **KEEP-0** | Sports massage is explicitly not physiotherapy appointment booking |
| `PHQ01→PH08` | `location_and_booking_missing` | **KEEP-0** | Regional overview gives no concrete Innsbruck appointment booking; earlier adjudicated grade 0 |
| `PHQ02→PH03` | `HOLD` | **HOLD** | Local shoulder-physiotherapy information might help find a local service, but no appointment or online booking is evidenced; relevance 0 vs 1 is genuinely disputable under the 'meaningful assistance' rule. |
| `PHQ02→PH04` | `information_need_mismatch` | **KEEP-0** | Back-exercise guide gives no route to a physio appointment |
| `PHQ02→PH05` | `information_need_mismatch` | **KEEP-0** | General manual-therapy explanation has no Innsbruck appointment options |
| `PHQ02→PH06` | `location_mismatch` | **KEEP-0** | Booking in Schwaz does not satisfy Innsbruck locality |
| `PHQ02→PH07` | `service_type_mismatch` | **KEEP-0** | Sports massage is explicitly not physiotherapy appointment booking |
| `PHQ02→PH08` | `location_and_booking_missing` | **KEEP-0** | Regional overview gives no concrete Innsbruck appointment booking; earlier adjudicated grade 0 |
| `PHQ03→PH04` | `condition_mismatch` | **KEEP-0** | Back-exercise advice, not shoulder physiotherapy |
| `PHQ03→PH05` | `service_and_location_unspecified` | **KEEP-0** | Manual therapy explained generally; no Innsbruck shoulder-specific physio |
| `PHQ03→PH06` | `location_and_specialization_missing` | **KEEP-0** | Schwaz instead of Innsbruck; no shoulder treatment established |
| `PHQ03→PH07` | `service_type_mismatch` | **KEEP-0** | Sports massage, not shoulder physiotherapy |
| `PHQ03→PH08` | `location_unspecified` | **KEEP-0** | Tyrol regional shoulder mention does not identify an Innsbruck shoulder physio service; earlier adjudicated 0 |
| `PHQ04→PH01` | `information_need_mismatch` | **KEEP-0** | Physiotherapy appointment booking page does not explain manual therapy |
| `PHQ04→PH02` | `information_need_mismatch` | **KEEP-0** | Physiotherapy appointment booking page does not explain manual therapy |
| `PHQ04→PH03` | `information_need_mismatch` | **KEEP-0** | Shoulder treatment information is not an explanation of manual therapy |
| `PHQ04→PH04` | `information_need_mismatch` | **KEEP-0** | Back-exercise advice is unrelated to definition of manual therapy |
| `PHQ04→PH06` | `information_need_mismatch` | **KEEP-0** | Physiotherapy appointment booking page does not explain manual therapy |
| `PHQ04→PH07` | `service_type_mismatch` | **KEEP-0** | Sports massage service does not explain manual therapy |
| `PHQ04→PH08` | `mere_keyword_mention` | **KEEP-0** | Manual therapy mentioned but not defined or explained; already adjudicated 0 |
| `PHQ04→PH09` | `information_need_mismatch` | **KEEP-0** | Physiotherapy appointment booking page does not explain manual therapy |

### Transport (22 proposed grade-0 pairs)

| Pair | Reason code | Audit outcome | Rationale based on title + description |
|---|---|---|---|
| `TRQ01→TR03` | `route_direction_mismatch` | **KEEP-0** | Private transfer goes Puerto Escondido → Oaxaca City; wrong direction |
| `TRQ01→TR04` | `route_mismatch` | **KEEP-0** | Airport → city-center transfer is not Oaxaca City → Puerto Escondido |
| `TRQ01→TR07` | `origin_mismatch` | **KEEP-0** | Departs Huatulco, not Oaxaca City |
| `TRQ02→TR03` | `route_direction_mismatch` | **KEEP-0** | Private transfer goes Puerto Escondido → Oaxaca City; wrong direction |
| `TRQ02→TR04` | `route_mismatch` | **KEEP-0** | Airport → city-center transfer is not Oaxaca City → Puerto Escondido |
| `TRQ02→TR07` | `origin_mismatch` | **KEEP-0** | Departs Huatulco, not Oaxaca City |
| `TRQ03→TR01` | `route_direction_mismatch` | **KEEP-0** | Content covers Oaxaca City → Puerto Escondido; asked for the reverse route |
| `TRQ03→TR02` | `route_direction_mismatch` | **KEEP-0** | Content covers Oaxaca City → Puerto Escondido; asked for the reverse route |
| `TRQ03→TR04` | `route_mismatch` | **KEEP-0** | Airport → city-center pickup is not Puerto Escondido → Oaxaca City |
| `TRQ03→TR05` | `route_direction_mismatch` | **KEEP-0** | Content covers Oaxaca City → Puerto Escondido; asked for the reverse route |
| `TRQ03→TR06` | `route_direction_mismatch` | **KEEP-0** | Content covers Oaxaca City → Puerto Escondido; asked for the reverse route |
| `TRQ03→TR07` | `route_mismatch` | **KEEP-0** | Huatulco → Puerto Escondido is neither the right origin nor the right destination |
| `TRQ03→TR08` | `route_direction_mismatch` | **KEEP-0** | Content covers Oaxaca City → Puerto Escondido; asked for the reverse route |
| `TRQ04→TR01` | `route_mismatch` | **KEEP-0** | Oaxaca City → Puerto Escondido does not provide airport → downtown pickup |
| `TRQ04→TR02` | `route_mismatch` | **KEEP-0** | Oaxaca City → Puerto Escondido does not provide airport → downtown pickup |
| `TRQ04→TR03` | `route_mismatch` | **KEEP-0** | Puerto Escondido → Oaxaca City is not local airport → center pickup |
| `TRQ04→TR05` | `route_mismatch` | **KEEP-0** | Oaxaca City → Puerto Escondido does not provide airport → downtown pickup |
| `TRQ04→TR06` | `route_mismatch` | **KEEP-0** | Oaxaca City → Puerto Escondido does not provide airport → downtown pickup |
| `TRQ04→TR07` | `route_mismatch` | **KEEP-0** | Huatulco → Puerto Escondido is not airport → downtown pickup |
| `TRQ04→TR08` | `route_mismatch` | **KEEP-0** | Oaxaca City → Puerto Escondido does not provide airport → downtown pickup |
| `TRQ03→TR09` | `route_direction_mismatch` | **KEEP-0** | Content covers Oaxaca City → Puerto Escondido; asked for the reverse route |
| `TRQ04→TR09` | `route_mismatch` | **KEEP-0** | Oaxaca City → Puerto Escondido does not provide airport → downtown pickup |

## Research implications and work remaining

- **Do not conflate same domain with relevance.** An exact city match plus wrong action (repair vs rental, definition vs booking) is not enough for grade 1.
- **Do not automatically downgrade useful alternatives.** `PHQ01→PH03` and `PHQ02→PH03` require a consistent rule distinguishing actionable local-service information from a mere mention of therapy.
- **Cross-language sensitivity:** A German page can satisfy Spanish/English queries if the action and other constraints are evidenced; these grade-0 proposals are not based merely on language mismatches.
- **Within-domain audit coverage:** 73 pairs inspected with two holds; no new qrels changed. This review remains unblinded and assistant-authored.
- **Cross-domain grade-0 pairs:** **216** are outside the current within-domain review (12 queries × 18 off-domain candidates). They have not been individually adjudicated here; do not call them reviewed.
- **Full-label quality gate:** 324 labels remain proposed. Grade-0 triage cannot substitute for separate annotation by an independent human.
- **Design concern:** The three v0.2 pages were written to satisfy previously missing queries; because the new pages mirror the query vocabulary, a model's advantage could come from artificially easy retrieval. Test conclusions require a different, genuinely held-out dataset.

**Recommended next decision:** Resolve the two PHQ01/PHQ02 → PH03 borderline cases using one explicit, reproducible criterion. Record the user-approved decision in the adjudication log before any changes to qrels. Only afterward complete cross-domain review and consider a dataset freeze.
