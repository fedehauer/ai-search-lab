# AI Search Lab — Benchmark V2 Pilot v0.2 (Synthetic / unreviewed)

**Status:** Draft data version for **annotation review**, not a validated ground truth and **not** an evaluation-ready leaderboard. No model runs have been performed on this dataset.

## What changed since v0.1?

- **3 new, fictional candidate pages** added: `SK09`, `PH09`, and `TR09`. Each explicitly documents a requirement that was unsupported by v0.1:
  - `SK09`: ski rental with **online reservation** in Winterberg;
  - `PH09`: physiotherapy appointment with **online scheduling** in Innsbruck;
  - `TR09`: **private car** booking Oaxaca City → Puerto Escondido.
- Existing **24 document texts**, **12 query texts**, all query intent-group and development/test assignments, and the **288 original query–document grades and rationales** are preserved unchanged.
- A **complete 36-row draft** was added: each of the 12 queries is graded against **each** new document (including unrelated and held-out test queries). New judgments are **AI-proposed, unreviewed**.
- Candidate corpus: **27 documents**; query set: **12**; fully enumerated qrels: **324 = 12 × 27**.
- Grade distribution: **289 grade-0 / 17 grade-1 / 18 grade-2**. Every query now has at least one *proposed* grade-2 candidate, but this is a structural/evidence check, **not** human validation.
- The pilot test labels are public; do not describe it as a permanently blinded test.

## Files

- `documents.jsonl` — 27 synthetic candidate pages, with original v0.1 IDs and texts intact.
- `queries.jsonl` — exact copy of the 12 v0.1 queries.
- `qrels_draft.csv` — 324 synthetic pair labels and brief reasons, all `proposed_unreviewed`.
- `splits.json` — inherited, unchanged group assignment plus v0.2 size/version metadata.
- `lineage.json` — version relationship, counts and change audit.
- `../../../scripts/validate_v2_pilot_v0_2.py` — Python standard-library validation, runnable locally or in Colab with the full GitHub repository checkout.

## Reproducibility and review

1. Run `python scripts/validate_v2_pilot_v0_2.py` from the repository root. The script checks counts, one pair per query and document, identical original records, inherited intent split, statuses, and at least one grade-2 candidate per query.
2. Evaluate grades by hand using [annotation guidelines](../../../docs/v2/annotation_guidelines.md), especially `PHQ03→PH09` (general physiotherapy without shoulder specialization, grade **1**) and whether new descriptions substantiate online booking/car class.
3. Inspect the [adjudication log](../../../docs/v2/adjudication_log.md) and [corpus repair proposal](../../../docs/v2/corpus_gap_plan_v0_2.md). This v0.2 file set is an implementation of the approved additive option.
4. Prioritize the **within-sector grade-0 audit**, and then all remaining rows, before declaring the qrels validated or scoring retrieval models.

**Safety / provenance:** Entirely synthetic fictional test pages; real place names only as geographic labels. No real provider availability, treatment outcome, personal data, or actual client/customer records are represented. Documentation and rationales are in English; query/page text remains multilingual as experimental data.
