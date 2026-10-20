# Benchmark V2 Pilot — Corpus coverage repair plan for v0.2

**Status:** DESIGN PROPOSAL ONLY — do not treat this as an approved data change.  
**Motivation:** The 2026-10-20 strict-evidence adjudication lowered six qrels from grade 2 to 1. The current `pilot-v0.1` corpus (12 queries, 24 synthetic documents) has **no fully relevant candidate** for three development queries.

## Exact uncovered needs

| Query | Requirements not fully supported by any existing candidate | Existing partial candidates |
|---|---|---|
| `SKQ01` | Rent skis **online** in Winterberg; the booking channel must be explicitly online | `SK01`, `SK02` (bookings, channel unspecified) |
| `PHQ01` | Book a physiotherapy appointment **online** in Innsbruck | `PH01`, `PH02` (appointment bookings, channel unspecified) |
| `TRQ01` | Book a **private car** on Oaxaca City → Puerto Escondido | `TR01`, `TR02` (private transfer, exact vehicle class unspecified) |

### Proposed synthetic new candidates (not generated or published yet)

Create fresh, versioned `pilot-v0.2` descriptions with new stable document IDs instead of changing the historical meaning of any v0.1 document:

- **SK09** — `Online-Skiverleih Winterberg — direkt online buchen`. Description must explicitly assert that **ski equipment rental in Winterberg can be booked online** in this synthetic page scenario.
- **PH09** — `Online-Terminbuchung Physiotherapie Innsbruck`. Description must explicitly assert **online physiotherapy appointment scheduling in Innsbruck**.
- **TR09** — `Private car booking: Oaxaca City → Puerto Escondido`. Description must explicitly assert **a bookable private car** (not a shared shuttle), with exact origin and destination.

All names, services and booking features would be explicitly **fictional test-page statements**, not claims about real local providers.

## Effect on pilot design — approval required

If these three pages are added as additional candidates, the V2 pilot corpus expands from **24 to 27 documents** and the qrel matrix from **288 to 324 query–document pairs** (`12 × 27`). The initial 24-document target was a **pilot design target**, not a reason to retain mislabeled documents. Alternative: replace three items in a clearly versioned corpus with explicit migration and new judgments, keeping 24 documents; the choice needs approval.

Whichever variant is selected:
1. Save the full `pilot-v0.1` snapshot and a versioned `pilot-v0.2`; do not overwrite history without trace.
2. Freeze exact candidate descriptions and document IDs before reviewing relevance labels; write no hidden facts into the scoring rubric.
3. Re-annotate/validate **every query–new-document pair**, including non-target queries, with `proposed_unreviewed` status until approved.
4. Check that all 12 queries have at least one **evidenced grade-2** candidate after adjudication.
5. Recheck grade distributions, corpus counts, split intent groups and multilingual equivalents.
6. Report the change in the README, changelog, and methods section before evaluating any model.
7. Keep all pilot scores exploratory: public access to test queries/labels undermines a future blinded test.

**Current stage:** The strict rule is adopted and six qrels were changed, but the pilot remains **not evaluation-ready**. The 260 proposed grade-0 judgments still need systematic review.
