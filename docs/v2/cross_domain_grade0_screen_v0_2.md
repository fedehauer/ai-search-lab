# Pilot v0.2 — Cross-domain grade-0 relevance screen

**Status:** Provisional assistant-run classification, **not independent human annotation**. All decisions below are source-consistent *KEEP-0 recommendations*, not validated ground truth. No model rankings were used.

## Source and method

Read the **12 synthetic query texts**, **27 synthetic page titles and descriptions**, and the **324 proposed qrels** in `data/v2/pilot_v0_2/`. Compare each query need (ski equipment; physiotherapy appointment/explanation; tourism transfer/airport pickup) against candidate page content outside its sector. The six sector-to-sector combinations all address fundamentally different services. This **does not assert that domain labels alone always prove irrelevance**; content and intent distinctions, not metadata alone, support this particular screen.

**Result:** Exactly **216 cross-sector pairs**, all already grade 0 and `proposed_unreviewed`. **No proposed change**. The remaining **71 within-sector grade-0** pairs were reviewed in the [historical 73-pair audit](grade0_within_domain_audit_v0_2.md); two prior HOLD cases were subsequently changed 0→1 with user approval.

## Six cross-sector combinations

| Query domain → candidate domain | Grade-0 pairs |
|---|---:|
| physiotherapy → ski | 36 |
| physiotherapy → transport | 36 |
| ski → physiotherapy | 36 |
| ski → transport | 36 |
| transport → physiotherapy | 36 |
| transport → ski | 36 |
| **Total** | **216** |

## Full pair inventory: 12 queries × 18 off-domain pages

| Query ID | Query sector | Pairs | Candidate document IDs (each remains proposed grade 0) |
|---|---|---:|---|
| `SKQ01` | ski | 18 | `PH01`, `PH02`, `PH03`, `PH04`, `PH05`, `PH06`, `PH07`, `PH08`, `TR01`, `TR02`, `TR03`, `TR04`, `TR05`, `TR06`, `TR07`, `TR08`, `PH09`, `TR09` |
| `SKQ02` | ski | 18 | `PH01`, `PH02`, `PH03`, `PH04`, `PH05`, `PH06`, `PH07`, `PH08`, `TR01`, `TR02`, `TR03`, `TR04`, `TR05`, `TR06`, `TR07`, `TR08`, `PH09`, `TR09` |
| `SKQ03` | ski | 18 | `PH01`, `PH02`, `PH03`, `PH04`, `PH05`, `PH06`, `PH07`, `PH08`, `TR01`, `TR02`, `TR03`, `TR04`, `TR05`, `TR06`, `TR07`, `TR08`, `PH09`, `TR09` |
| `SKQ04` | ski | 18 | `PH01`, `PH02`, `PH03`, `PH04`, `PH05`, `PH06`, `PH07`, `PH08`, `TR01`, `TR02`, `TR03`, `TR04`, `TR05`, `TR06`, `TR07`, `TR08`, `PH09`, `TR09` |
| `PHQ01` | physiotherapy | 18 | `SK01`, `SK02`, `SK03`, `SK04`, `SK05`, `SK06`, `SK07`, `SK08`, `TR01`, `TR02`, `TR03`, `TR04`, `TR05`, `TR06`, `TR07`, `TR08`, `SK09`, `TR09` |
| `PHQ02` | physiotherapy | 18 | `SK01`, `SK02`, `SK03`, `SK04`, `SK05`, `SK06`, `SK07`, `SK08`, `TR01`, `TR02`, `TR03`, `TR04`, `TR05`, `TR06`, `TR07`, `TR08`, `SK09`, `TR09` |
| `PHQ03` | physiotherapy | 18 | `SK01`, `SK02`, `SK03`, `SK04`, `SK05`, `SK06`, `SK07`, `SK08`, `TR01`, `TR02`, `TR03`, `TR04`, `TR05`, `TR06`, `TR07`, `TR08`, `SK09`, `TR09` |
| `PHQ04` | physiotherapy | 18 | `SK01`, `SK02`, `SK03`, `SK04`, `SK05`, `SK06`, `SK07`, `SK08`, `TR01`, `TR02`, `TR03`, `TR04`, `TR05`, `TR06`, `TR07`, `TR08`, `SK09`, `TR09` |
| `TRQ01` | transport | 18 | `SK01`, `SK02`, `SK03`, `SK04`, `SK05`, `SK06`, `SK07`, `SK08`, `PH01`, `PH02`, `PH03`, `PH04`, `PH05`, `PH06`, `PH07`, `PH08`, `SK09`, `PH09` |
| `TRQ02` | transport | 18 | `SK01`, `SK02`, `SK03`, `SK04`, `SK05`, `SK06`, `SK07`, `SK08`, `PH01`, `PH02`, `PH03`, `PH04`, `PH05`, `PH06`, `PH07`, `PH08`, `SK09`, `PH09` |
| `TRQ03` | transport | 18 | `SK01`, `SK02`, `SK03`, `SK04`, `SK05`, `SK06`, `SK07`, `SK08`, `PH01`, `PH02`, `PH03`, `PH04`, `PH05`, `PH06`, `PH07`, `PH08`, `SK09`, `PH09` |
| `TRQ04` | transport | 18 | `SK01`, `SK02`, `SK03`, `SK04`, `SK05`, `SK06`, `SK07`, `SK08`, `PH01`, `PH02`, `PH03`, `PH04`, `PH05`, `PH06`, `PH07`, `PH08`, `SK09`, `PH09` |

## Evidence-based outcome and limits

- Ski-rental, ski-repair or ski-purchase queries are not satisfied by physiotherapy pages or tourist transportation pages.
- Requests to book physiotherapy or understand manual therapy are not satisfied by ski equipment pages or transfer bookings.
- Requests to book an Oaxaca transfer or Puerto Escondido airport pickup are not satisfied by ski equipment pages or physiotherapy service pages.
- German, Spanish and English content was not rejected solely due to a language mismatch; this screen assesses user need.
- No label edits, query edits, document edits, split edits, model runs, statistical validity tests or independent annotation took place.
- All **324 qrels** remain unreviewed proposals; these 216 pairs were screened under a simple, reproducible cross-domain rule. Individual human reannotation is still required before claiming validated ground truth.
- Public test labels are not blinded; strong held-out model comparisons require a genuinely independent test dataset.

**After the user-approved PH03 corrections**, the current pilot has **287 grade-0 / 19 grade-1 / 18 grade-2** judgments; `287 = 216 cross-domain grade-0 + 71 within-domain grade-0`.

**Next quality gate:** Independent annotation (or explicit acknowledgment that the pilot is single-author exploratory), potential inter-annotator disagreement review, running the provided integrity validator, and a versioned dataset freeze prior to exploratory model runs.
