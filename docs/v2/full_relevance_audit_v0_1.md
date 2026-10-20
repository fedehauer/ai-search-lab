# Benchmark V2 pilot — Grade-2 relevance audit (v0.1)

**Status:** Evidence review by the assistant; **not a second independent human annotation, not a validated benchmark**.  
**Historical audit update (2026-10-20):** Following user approval of a strict explicit-evidence rule, all **six** HOLD pairs in this original grade-2 audit were downgraded **2 → 1** in `qrels_draft.csv`, and three queries (`SKQ01`, `PHQ01`, `TRQ01`) no longer have a fully relevant candidate. **The original table below is a pre-adjudication snapshot, not the current set of grade-2 labels.** See the [adjudication log](adjudication_log.md) and [current qrels](../../data/v2/pilot/qrels_draft.csv); current distribution is **260 / 16 / 12** for grades 0/1/2. The pilot does not yet pass its evaluation-ready gate.  

**Source:** Existing `data/v2/pilot/queries.jsonl`, `documents.jsonl`, `qrels_draft.csv`, plus the [annotation guidelines](annotation_guidelines.md).  
**Scope:** All **18** pairs labeled **2 (fully relevant)**. Read only synthetic query text and the candidate page title/description, **not model scores or model output**.  
**Dataset change:** None. This document reports provisional decisions; all **288** source judgments remain `proposed_unreviewed`.

## Summary

| Audit outcome | Pairs | Interpretation |
|---|---:|---|
| **KEEP-2 — provisional** | **12** | Direct evidence supports the requested service/action and essential location/route |
| **HOLD — evidence gap** | **6** | There is a potentially explicit constraint that the synthetic title/description does not settle |
| **PROPOSE-LOWER** | **0** | No unambiguous contradiction warranting immediate downgrade was found |
| **Total** | **18** | All grade-2 labels were examined |

**Key question:** Does a page *about reservations* prove an **online booking** mechanism, or only that bookings can be requested? Does “private transfer” necessarily meet “private **car** transfer”? We should not silently infer either from incomplete source text.

## Pair-by-pair audit

| Query → document | Query text | Evidence (synthetic document title + description) | Outcome | Diagnostic / reason |
|---|---|---|---|---|
| `SKQ01→SK01` | Wo kann ich Skier in Winterberg online mieten? | **Skiverleih Winterberg – Ski ausleihen** — Synthetic service page for ski rental bookings specifically in Winterberg. | **HOLD — evidence gap** | `online_booking_unspecified` — The document explicitly offers ski-rental bookings in Winterberg, but the described booking mechanism is not explicitly stated to be online. |
| `SKQ01→SK02` | Wo kann ich Skier in Winterberg online mieten? | **Alquiler de esquís en Winterberg** — Página sintética para reservar esquís de alquiler en Winterberg. | **HOLD — evidence gap** | `online_booking_unspecified` — The Spanish page offers rental reservations in Winterberg; an online booking mechanism is not explicitly stated. |
| `SKQ02→SK01` | ¿Dónde puedo reservar unos esquís de alquiler en Winterberg? | **Skiverleih Winterberg – Ski ausleihen** — Synthetic service page for ski rental bookings specifically in Winterberg. | **KEEP-2 — provisional** | Winterberg ski-rental booking; no online-only booking constraint in this query. |
| `SKQ02→SK02` | ¿Dónde puedo reservar unos esquís de alquiler en Winterberg? | **Alquiler de esquís en Winterberg** — Página sintética para reservar esquís de alquiler en Winterberg. | **KEEP-2 — provisional** | Winterberg ski rental and reservation explicitly match. |
| `SKQ03→SK03` | Where can I have my ski edges repaired in Winterberg? | **Skiservice Winterberg – Skireparatur** — Synthetische Serviceseite für Skireparatur und Kantenschliff in Winterberg. | **KEEP-2 — provisional** | Ski repair and edge work in Winterberg exactly address the request. |
| `SKQ04→SK04` | Where can I purchase new skis in Winterberg? | **Buy new skis in Winterberg** — Synthetic retail landing page for buying new skis in Winterberg. | **KEEP-2 — provisional** | Purchasing new skis in Winterberg is directly supported. |
| `PHQ01→PH01` | Online-Termin für Physiotherapie in Innsbruck vereinbaren | **Physiotherapie-Termin in Innsbruck buchen** — Synthetische Physiotherapie-Seite mit Terminbuchung in Innsbruck; keine Schulter-Spezialisierung erwähnt. | **HOLD — evidence gap** | `online_booking_unspecified` — An Innsbruck physiotherapy appointment can be booked, but online appointment scheduling is not explicitly asserted. |
| `PHQ01→PH02` | Online-Termin für Physiotherapie in Innsbruck vereinbaren | **Book physiotherapy in Innsbruck** — Synthetic physiotherapy appointment-booking landing page in Innsbruck; no shoulder specialty specified. | **HOLD — evidence gap** | `online_booking_unspecified` — The English appointment-booking landing page is relevant and city-specific, but online scheduling is not directly evidenced. |
| `PHQ02→PH01` | Find a physiotherapy appointment to book in Innsbruck | **Physiotherapie-Termin in Innsbruck buchen** — Synthetische Physiotherapie-Seite mit Terminbuchung in Innsbruck; keine Schulter-Spezialisierung erwähnt. | **KEEP-2 — provisional** | Bookable physiotherapy in Innsbruck, matching the city and appointment intent. |
| `PHQ02→PH02` | Find a physiotherapy appointment to book in Innsbruck | **Book physiotherapy in Innsbruck** — Synthetic physiotherapy appointment-booking landing page in Innsbruck; no shoulder specialty specified. | **KEEP-2 — provisional** | Direct physiotherapy appointment-booking page in Innsbruck. |
| `PHQ03→PH03` | Physiotherapy for shoulder pain in Innsbruck | **Schulterphysiotherapie in Innsbruck** — Synthetische Seite über Physiotherapie bei Schulterbeschwerden in Innsbruck; mit entsprechender Behandlungsinformation. | **KEEP-2 — provisional** | Shoulder physiotherapy for complaints in Innsbruck is explicitly supported. |
| `PHQ04→PH05` | ¿En qué consiste la terapia manual en fisioterapia? | **¿Qué es la terapia manual en fisioterapia?** — Guía sintética que explica la terapia manual, sus conceptos y su lugar en la fisioterapia. | **KEEP-2 — provisional** | Focused explanation of manual therapy meets the information need. |
| `TRQ01→TR01` | Book a private car transfer from Oaxaca City to Puerto Escondido | **Private transfer Oaxaca City → Puerto Escondido** — Synthetic booking page for a private one-way transfer from Oaxaca City to Puerto Escondido. | **HOLD — evidence gap** | `vehicle_type_unspecified` — A private, bookable transfer in the correct direction is offered, but a car rather than another private vehicle type is not explicitly specified. |
| `TRQ01→TR02` | Book a private car transfer from Oaxaca City to Puerto Escondido | **Reservar traslado privado Oaxaca capital → Puerto Escondido** — Página sintética de reserva privada en sentido Oaxaca capital hacia Puerto Escondido. | **HOLD — evidence gap** | `vehicle_type_unspecified` — The Spanish private-booking page covers the exact route but does not specify that the private transport is by car. |
| `TRQ02→TR01` | Quiero reservar un traslado privado de Oaxaca capital a Puerto Escondido | **Private transfer Oaxaca City → Puerto Escondido** — Synthetic booking page for a private one-way transfer from Oaxaca City to Puerto Escondido. | **KEEP-2 — provisional** | Private bookable transfer with correct origin and destination. |
| `TRQ02→TR02` | Quiero reservar un traslado privado de Oaxaca capital a Puerto Escondido | **Reservar traslado privado Oaxaca capital → Puerto Escondido** — Página sintética de reserva privada en sentido Oaxaca capital hacia Puerto Escondido. | **KEEP-2 — provisional** | Spanish private booking page with the exact direction. |
| `TRQ03→TR03` | Book a private ride from Puerto Escondido back to Oaxaca City | **Traslado privado Puerto Escondido → Oaxaca capital** — Página sintética de reserva en sentido Puerto Escondido hacia Oaxaca capital. | **KEEP-2 — provisional** | Bookable private reverse route Puerto Escondido to Oaxaca. |
| `TRQ04→TR04` | Reserve an airport pickup from Puerto Escondido Airport to downtown | **Traslado aeropuerto de Puerto Escondido → centro** — Página sintética para reservar recogida en el aeropuerto de Puerto Escondido con destino al centro. | **KEEP-2 — provisional** | Airport pickup from Puerto Escondido Airport to the city center; bookable. |

## Domain breakdown

| Domain | Grade-2 pairs | KEEP-2 provisional | HOLD |
|---|---:|---:|---:|
| ski | 6 | 4 | 2 |
| physiotherapy | 6 | 4 | 2 |
| transport | 6 | 4 | 2 |
| **Total** | **18** | **12** | **6** |

## Evidence gaps to adjudicate

### A. `online_booking_unspecified` (4 pairs)
- `SKQ01→SK01` and `SKQ01→SK02`: The query explicitly asks where to rent **online**. Both pages are described as supporting rental bookings in Winterberg, but do not explicitly specify a functional online reservation path.
- `PHQ01→PH01` and `PHQ01→PH02`: The query explicitly asks for an **online physiotherapy appointment**. Both support booking physiotherapy in Innsbruck, but the published descriptions do not specify the channel.

**Open methodology decision:** If a booking landing page is sufficient evidence of online reservability, write that assumption into the rubric and consistently apply it. If not, retain HOLD pending adjudication, and consider grade 1 where meaningful assistance but no online booking is established. The reviewer must not insert invented booking capabilities into source documents merely to defend an existing grade.

### B. `vehicle_type_unspecified` (2 pairs)
- `TRQ01→TR01` and `TRQ01→TR02`: The query requests a **private car transfer**. Both candidates offer **private transfers** on the correct route but do not expressly specify the vehicle class.

**Open methodology decision:** If “car transfer” is colloquial for private road transport, grade 2 is defensible. If the vehicle class is an explicit hard requirement, seek evidence or consider partial relevance. Record the interpretation *before* any model scoring.

### C. Multilingual equivalence
A page in a different language can satisfy the query's task under the pilot rubric. German, Spanish and English mismatches do **not**, by themselves, justify reducing grades unless the user explicitly requested a response language. Accessibility and ability to complete the action in a different language are separate research questions not yet modeled here.

### D. Held-out pilot limitation
This file discusses the openly published grade-2 pairs, including pilot test queries; therefore the current **public pilot test** cannot credibly serve as a permanently blinded evaluation. It is a methodology demonstration, not a basis for extrapolating model performance. A future test set must be fresh or have an explicitly fixed, pre-registered evaluation process.

## Recommended next steps

1. Agree a **single rule** for evidence of online booking and a **single rule** for the meaning of “private car”; test those rules across all 288 candidate judgments.
2. Record human adjudication for the six HOLD pairs; revise labels only with an explicit, versioned rationale. Do not change data to improve scores.
3. Perform a structured audit of the **260 grade-0 pairs**, initially looking for missed cross-language matches, service synonyms, alternative route directions and related services.
4. Reconfirm every query has at least one truly grade-2 candidate. If changing one grade leaves no full match, record that as a *dataset design issue*, not a reason to silently overrate another page.
5. After judgments are reviewed and frozen, run development experiments only. Test outcomes should be reported as exploratory if already public.

## Provenance
All examples are **synthetic**. This is one assistant-authored review pass. The 12 KEEP-2 decisions are **provisional**, the six HOLD decisions are **not downgraded or validated**, and the audit **does not alter labels, query content, documents or split assignments**.
