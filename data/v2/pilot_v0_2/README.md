# AI Search Lab — Benchmark V2 Pilot v0.2 (Synthetic / unreviewed)

**Status:** Draft data version for **annotation review**, not a validated ground truth and **not** an evaluation-ready leaderboard. No model runs have been performed on this dataset.

## What changed since v0.1?

- **3 new, fictional candidate pages** added: `SK09`, `PH09`, and `TR09`. Each explicitly documents a requirement that was unsupported by v0.1:
  - `SK09`: ski rental with **online reservation** in Winterberg;
  - `PH09`: physiotherapy appointment with **online scheduling** in Innsbruck;
  - `TR09`: **private car** booking Oaxaca City → Puerto Escondido.
- Existing **24 document texts**, **12 query texts**, all query intent-group and development/test assignments, and the **288 inherited query–document rows** were copied from v0.1, then **two** v0.2 PH03 labels were changed 0→1 with user approval. The other **286 inherited qrels** remain identical.
- A **complete 36-row draft** was added: each of the 12 queries is graded against **each** new document (including unrelated and held-out test queries). New judgments are **AI-proposed, unreviewed**.
- Candidate corpus: **27 documents**; query set: **12**; fully enumerated qrels: **324 = 12 × 27**.
- Current grade distribution: **287 grade-0 / 19 grade-1 / 18 grade-2**. Every query now has at least one *proposed* grade-2 candidate, but this is a structural/evidence check, **not** human validation.
- The pilot test labels are public; do not describe it as a permanently blinded test.

## Files

- `documents.jsonl` — 27 synthetic candidate pages, with original v0.1 IDs and texts intact.
- `queries.jsonl` — exact copy of the 12 v0.1 queries.
- `qrels_draft.csv` — 324 synthetic pair labels and brief reasons, all `proposed_unreviewed`.
- `splits.json` — inherited, unchanged group assignment plus v0.2 size/version metadata.
- `lineage.json` — version relationship, counts and change audit.
- `../../../scripts/validate_v2_pilot_v0_2.py` — Python standard-library validation, runnable locally or in Colab with the full GitHub repository checkout.

## GitHub Actions execution (2026-10-20)

**PASS — structural validation actually executed** in [GitHub Actions run #39454935795](https://github.com/fedehauer/ai-search-lab/actions/runs/39454935795). The Python script verified 27 documents, 12 queries, 324 pairs, grades 287/19/18, preserved v0.1 source records, exactly two authorized inherited qrel changes, and development/test group consistency.

This validates **data integrity only**, not whether the proposed relevance labels are correct.

## Human review resources

- [Human review protocol](../../../docs/v2/human_review_protocol.md): graded rubric, review workflow, independent annotation criteria, adjudication and freeze rules.
- [Grade-masked CSV sheet](review_sheet_grade_masked.csv): all 324 pairs in shuffled order, no proposed relevance grades, and blank human judgment/reason/confidence/reviewer fields.
- The sheet is a **template**, not completed human annotation. Every qrel remains `proposed_unreviewed`.

## Reproducibility and review

1. Run `python scripts/validate_v2_pilot_v0_2.py` from the repository root. The script checks counts, one pair per query and document, identical original document/query records, two explicitly approved inherited-qrel modifications, inherited intent split, statuses, and at least one grade-2 candidate per query.
2. Evaluate grades by hand using [annotation guidelines](../../../docs/v2/annotation_guidelines.md), especially `PHQ03→PH09` (general physiotherapy without shoulder specialization, grade **1**) and whether new descriptions substantiate online booking/car class.
3. Inspect the [adjudication log](../../../docs/v2/adjudication_log.md) and [corpus repair proposal](../../../docs/v2/corpus_gap_plan_v0_2.md). This v0.2 file set is an implementation of the approved additive option.
4. Read the [within-sector audit](../../../docs/v2/grade0_within_domain_audit_v0_2.md), including the later user-approved PH03 decision, and the [cross-sector screen](../../../docs/v2/cross_domain_grade0_screen_v0_2.md). The 71 within-sector and 216 cross-sector grade-0 labels are still **assistant-only provisional judgments**, not independent human validation.

**Safety / provenance:** Entirely synthetic fictional test pages; real place names only as geographic labels. No real provider availability, treatment outcome, personal data, or actual client/customer records are represented. Documentation and rationales are in English; query/page text remains multilingual as experimental data.
