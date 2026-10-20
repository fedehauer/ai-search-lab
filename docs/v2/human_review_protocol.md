# AI Search Lab — Human Relevance Review Protocol (Pilot v0.2)

**Status:** Review instructions, **not** evidence of completed human annotation.  
**Materials:** [Grade-masked review sheet](../../data/v2/pilot_v0_2/review_sheet_grade_masked.csv), [annotation guidelines](annotation_guidelines.md), and [pilot v0.2 dataset](../../data/v2/pilot_v0_2/README.md).  
**Scope:** 12 queries × 27 synthetic page-like documents = **324 unique judgments**. Queries include DE, ES and EN. Entirely synthetic material, no real patient/customer or private client data.

## 1. What exactly are we trying to determine?

For each user query and candidate page, decide **how well the *visible title and description* address the user's goal**, not how similar their words sound. This is a *retrieval relevance* exercise. It does not measure actual Google rankings, AI chatbot citations, or booked transactions.

### Grades (strict evidence rubric)

| Grade | Decision | Minimum evidence |
|---|---|---|
| **0** | Not relevant | Wrong action, service/product, essential city, direction, or the text is merely topical but does not meaningfully assist the user |
| **1** | Partially relevant | Provides **concrete useful guidance or a plausible alternative** for the specific task, but a stated requirement or completion path remains unmet; do not interpret as a successful booking |
| **2** | Fully relevant | The *title/description explicitly support all requested requirements*, including online booking if stated, route direction, city, private **car** if stated, and service/specialization if stated |

**Key distinction:** “Not evidenced” does **not** mean “does not exist.” When a page shows a general booking but does not say it is **online**, do not infer that it is online or grade it 2. Likewise, a “private transfer” does not explicitly prove a “private **car**” unless the text says so.

Do not penalize a German page just because the query is Spanish or English; evaluate the intended user need unless a query explicitly restricts language.

## 2. Review workflow

1. Make a personal copy of `review_sheet_grade_masked.csv` to edit locally (e.g., as a spreadsheet). **Do not fill, commit, or distribute contact details or sensitive personal information**.
2. Work from the `query_text`, `document_title` and `document_description` columns. The rows are deterministically shuffled (**seed 20261020**), with all **324** unique pairs represented. The sheet **hides all AI-proposed relevance grades**.
3. For each row, enter `reviewer_grade_0_1_2` as **0**, **1** or **2**. Enter `reviewer_rationale` explaining the matched or failed requirement; use only evidence in the given text. Enter one of `low`, `medium` or `high` in `confidence_low_medium_high`. `reviewer_code` is a nonidentifying code such as `R1`, never a person's email.
4. **Do not look at the existing `qrels_draft.csv` while assigning grades**. Do not view model rankings/similarity scores or assume unavailable facts. The reviewer may have prior access to this public project; the exercise is grade-masked, **not a truly blinded evaluation**.
5. Flag uncertain or ambiguous cases with `low` confidence and a written note. **Do not force an artificial grade-2 document for every query.** Finding uncovered needs is legitimate evidence of a dataset design problem.
6. Complete the first independent pass for **all 324 pairs**. A separate reviewer should grade at least **65 pairs** (approximately 20%), sampled across sectors, all languages, 0/1/2 candidate grades, and especially challenging 0-vs-1 or 1-vs-2 boundaries. Ideally both reviewers independently grade all 324; if not, describe the sampling strategy and limitations.
7. **Only after human grading**, join by `(query_id, document_id)` with the assistant-proposed qrels, generate a confusion matrix, calculate exact agreement, and optionally report weighted Cohen's kappa for pairs with two independent raters. If there is just one human and an AI-proposed starting set, **do not report this as independent two-human inter-annotator agreement**.
8. Resolve disagreements using a documented adjudication sheet, leaving old grades and reasons auditable. The final judge can be the original human reviewer when resources are limited, but must disclose the process.
9. Freeze an explicitly versioned set of human-reviewed qrels **only if all pairs are accounted for**, provenance is recorded, and the pilot corpus-coverage gate is honestly reported. Do not mark 324 records `reviewed` just because the assistant screened them.

## 3. Example decisions grounded in this pilot

| Query → page | Illustrative grade | Why |
|---|---:|---|
| `SKQ01 → SK09` | **2** | Ski rental in Winterberg with **explicit online booking** |
| `SKQ01 → SK01` | **1** | Ski rental bookings in Winterberg, but the *online* channel is not evidenced |
| `PHQ01 → PH03` | **1** | Innsbruck shoulder-physio information potentially helps discovery, but no demonstrated online appointment path |
| `TRQ01 → TR09` | **2** | Explicit bookable **private car** in correct Oaxaca City → Puerto Escondido direction |
| `TRQ03 → TR09` | **0** | Correct transport category but **opposite route direction** |
| `PHQ04 → PH08` | **0** | Mentions manual therapy without explaining what it is |

**These are training examples from the existing assistant-authored decisions, not evidence of an independent review.** For the truly grade-masked pass, avoid consulting these examples while grading the same rows; preferably have a reviewer unfamiliar with prior discussion perform the pass.

## 4. Suggested review blocks

To avoid 324 consecutive low-attention decisions, work in **batches of 27–54 pairs** (e.g., one to two query-equivalent batches), with breaks and retrospective ambiguity notes. The CSV is shuffled rather than sorted by query; that reduces answer-copying across near-duplicate queries but makes batch boundaries different.

Reviewers should not use any personal or sensitive patient details. Synthetic locations are geography labels only.

## 5. Acceptance gates before experiments

- **Structural gate:** `python scripts/validate_v2_pilot_v0_2.py` passes on the checked-out branch.
- **Judgment coverage:** 324/324 judgments from a real reviewer or a transparently documented lower-coverage pilot; no missing labels silently default to 0.
- **Quality gate:** disagreement examples adjudicated; any revised texts/queries must create a new version, not silently retrofit the source to a previous grade.
- **Relevance coverage:** each query should have at least one evidenced grade-2 document **for the intended benchmark design**; if not, fix corpus design *before* using it as a benchmark, without inflating labels.
- **Test integrity:** public pilot test qrels are not blinded. Results can demonstrate mechanics, but are **not** strong out-of-sample model-quality evidence. For robust comparisons, use a fresh test split and freeze the method before examining its labels.
- **Reproducibility/legal:** record dataset/script version and dependency pinning; settle software/dataset licenses before inviting reuse.

## 6. Deliverables after a review pass

Expected files, **not yet created as finished evaluation artifacts**:
- Anonymized completed review sheet with all assigned grades and reasons.
- Per-item discrepancy report between human grades and AI proposals, with disagreement counts by query/sector and grade.
- Adjudication decisions with evidence and reviewer provenance.
- Versioned, human-reviewed qrels and a concise limitations statement.

**Current truth:** No independent human relevance pass has been completed or claimed by this repository.
