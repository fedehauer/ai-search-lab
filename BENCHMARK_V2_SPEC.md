# AI Search Lab — Benchmark V2 Specification

**Status:** PROPOSED — review required before generating datasets or running experiments  
**Pilot status update (2026-10-20):** The original 12-query/24-document **design target** was extended through a separately versioned **v0.2 pilot** with **27 synthetic documents and 324 proposed, unreviewed qrels** after six unsupported grade-2 relationships were adjudicated. Every query now has a *proposed* grade-2 candidate; the **human-validation and evaluation-readiness requirements remain unmet**. The public pilot test is not blinded. See [pilot v0.2](data/v2/pilot_v0_2/README.md) and [adjudication log](docs/v2/adjudication_log.md). This note updates the implementation status, not the proposed full V2 research target (60 queries / 80 documents).  
**Version:** 0.1 (design only)  
**Repository:** `fedehauer/ai-search-lab`  
**Language of technical documentation:** English  
**Experimental query languages:** German (DE), Spanish (ES), English (EN)

> This is a methodology proposal, **not** a completed study. The V2 dataset, relevance judgments, model runs, and performance results do not yet exist. Numbers below are design targets, not measured outcomes.

## 1. Research objective

Evaluate the quality of lexical, semantic, and hybrid retrieval methods when matching multilingual search queries to candidate page content under business-relevant intent and location constraints.

**Main research question:** Which retrieval approach ranks pages that *satisfy the user need*, rather than merely pages that share vocabulary or a broad topic, most effectively on the predeclared V2 benchmark?

**Scope:** query-to-document retrieval and ranking on a controlled dataset. This is **not** a study of Google rankings, SEO traffic impact, AI Overviews, or the internal retrieval/citation policies of commercial LLMs.

### Hypotheses (to test, not to assert)

- **H1 — Lexical/semantic:** Multilingual semantic retrieval may recover synonyms and cross-language matches that a simple word-based baseline misses.
- **H2 — Intent sensitivity:** Embedding similarity alone may over-rank pages with the right location/product but the wrong action (e.g., repair vs rent).
- **H3 — Hybrid retrieval:** Combining lexical and semantic rankings may improve ranking quality, but need not outperform either system.
- **H4 — Context:** Query language, locality, and field length (title vs title + description) may meaningfully affect retrieval.

## 2. Proposed dataset

| Component | Planned size | Notes |
|---|---:|---|
| Queries | 60 | 20 per domain; DE, ES, EN; natural language distribution |
| Candidate documents | 80 | 30 ski, 25 physiotherapy, 25 transport |
| Query-document pairs | 4,800 | Full candidate pool: 60 × 80 |
| Development queries | 40 | Used to examine errors and select methods |
| Held-out test queries | 20 | Used only after methods/configurations are frozen |
| Relevance grades | 0, 1, 2 | See section 4 |

**Domains (synthetic, not real client datasets):**

1. **Ski rental / alpine services** — rent vs buy vs repair, ski vs snowboard, lift passes, destination matches (e.g., Winterberg, Mayrhofen, Zell am See).
2. **Local physiotherapy** — appointment vs treatment explanation, treatment type, local area/city, availability claims only when explicitly present in a synthetic document.
3. **Tourist transfers** — origin/destination direction, route, shared/private transport, information vs booking intent (e.g., Oaxaca and Puerto Escondido).

Document entries are invented page-like titles and short descriptions. Geographic names can be real, but **pages, providers, prices, schedules, availability, patient information, and testimonials must not imply factual claims about real businesses**. Do not include confidential client exports, personal data, private dashboards, proprietary analytics, or unpublished company records.

**Planned content fields:** `document_id`, `title`, `description`, `language`, `domain`, `synthetic=true`, `generation_version`. The retrieval text is **only** the visible `title` or `title + description`, per run; metadata such as intent, locations, and relevance judgments is **not** a model input.

**Planned query fields:** `query_id`, `text`, `language`, `domain`, `intent_group_id`, `split` and provenance metadata. Explicit candidate documents must exist for every query, including at least one fully relevant document.

### Distribution / coverage checklist

- Exactly **20 queries per domain**; total **60**.
- German, Spanish, and English all represented meaningfully; final counts and the reason for natural, domain-specific language distributions documented *before* scoring.
- At least **10 deliberate cross-language retrieval cases** distributed across development and test.
- Include hard negatives: correct location but wrong service, correct service but wrong location, changed booking direction, neighboring services, same topic but wrong intent, compound words and synonyms.
- Include a mix of navigational, informational, local commercial and transactional intents, with explicit testable interpretations.
- Avoid testing on exact duplicates of V1's six queries; V1 is an educational reference only.

## 3. Data split and leakage controls

**Planned domain allocation:**

| Domain | Development | Test | Total |
|---|---:|---:|---:|
| Ski | 14 | 6 | 20 |
| Physiotherapy | 13 | 7 | 20 |
| Transport | 13 | 7 | 20 |
| **Total** | **40** | **20** | **60** |

The same **80 candidate documents** form the retrieval corpus for both query splits. Do **not** randomly split near-duplicate queries across the two splits.

- Assign stable `intent_group_id` identifiers for equivalence classes such as the same service, route/direction and destination; keep each group entirely in development **or** test.
- Ensure any paraphrases or translations expressing essentially the same user need remain in the same split.
- Balance domains and, where feasible, query languages across splits, checking imbalance before lock.
- **Freeze** documents, queries, judgments and split manifest *before* the final test.
- Select algorithms, RRF parameters, preprocessing and title/description variant on the **development** split only.
- Run the held-out test **once for the frozen configuration**. If later adjusted using observed test errors, label further results exploratory and create a new test set.
- Report any exceptions, duplicates, changed labels or document edits in a changelog.

**Public-release caveat:** Once test judgments are published openly, this test is no longer blinded for future versions. Record a dated freeze and create a fresh holdout for subsequent work.

## 4. Relevance annotation protocol

Use **graded, need-satisfaction judgments**, not just semantic topical relatedness.

| Grade | Meaning | Example for “rent skis in Winterberg” |
|---|---|---|
| **2 — Fully relevant** | Directly meets the requested action/service and required location/route/direction | Ski rental landing page for Winterberg |
| **1 — Partially relevant** | Plausibly helps, but misses a requirement or is too general to fully satisfy it | General Germany ski rental overview with no Winterberg-specific service |
| **0 — Not relevant** | Wrong task, product, location or route, or only superficial topical overlap | Ski repair in Winterberg, ski rental in another city |

**Decision rules:**

- Evaluate from the **searcher's perspective**. A page advertising “we sell skis” may satisfy a query seeking to buy; “verkaufen” is **not automatically** a negative.
- For local intent, a correct service in the wrong town is normally grade 0 unless the query explicitly allows a wider radius and the synthetic page supports it.
- For transfers, **direction matters**: Oaxaca → Puerto Escondido is not automatically equivalent to the reverse route.
- Do not infer opening hours, availability, actual prices, medical treatment outcomes, or booking capability absent from the content.
- Judge the page based only on the specified retrieval text and a written query-intent rubric, not the model ranking.
- Record ambiguity explicitly; a guideline update must precede any systematic relabeling.

**Judgment completeness:** 60 × 80 = **4,800 grades** for a fully judged benchmark. Missing judgments are **missing**, not grade 0. No final Recall or nDCG claims until the relevant judged pool is complete. Full manual review is substantial, so conduct a **pilot** before scaling.

**Quality assurance (proposed):** Independently second-judge at least **20% of pairs** (960/4,800) with intentional oversampling of borderline grades 0 vs 1 and 1 vs 2. Measure agreement (e.g., weighted Cohen’s kappa when appropriate), discuss disagreements, and maintain an adjudication log. If only one annotator is available, clearly disclose this limitation and use a structured re-review rather than claiming independent agreement.

## 5. Pilot gate — no full dataset until reviewed

Build a smaller **12-query / 24-document** pilot first (up to **288 pair judgments**), covering all three domains, all three languages, at least two cross-language cases, and hard negatives.

Pilot acceptance criteria:
- Every query has a written intended need and at least one grade-2 candidate.
- Annotation guidelines allow someone else to repeat a judgment; directional/local intent edge cases are resolved.
- Query group splitting has **no cross-split near-duplicates**.
- Evaluation script treats **missing labels as errors**, not non-relevant.
- Data provenance and privacy review are complete.
- Only after approval, expand to 60 queries / 80 documents; the pilot is not a substitute for the final held-out test.

## 6. Retrieval systems and experiment controls

**V1 reference implementations:**
- TF-IDF (token word unigrams/bigrams).
- `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`.
- Equal-weight Reciprocal Rank Fusion (`k=60`) of lexical and semantic ranks.

**V2 candidate additions (subject to development-only selection):**
- **BM25**, with documented tokenizer and German/Spanish normalization decisions.
- One **multilingual retrieval-specialized embedding model** with documented model card, size, license and maximum input length.
- Optional **reranker** after candidate retrieval; report its cost/latency separately.

**Fair comparison requirements:**
- Identical query corpus, 80 candidates, qrels and evaluation code.
- Same retrieval text variant across systems per declared comparison.
- Record exact Python/library versions, model identifiers **and immutable model revisions**, tokenizer options, random seeds where applicable and CPU/GPU settings.
- TF-IDF/BM25 vocabularies/statistics fitted on the document corpus, not relevance labels.
- RRF is based on ranks, not sums of uncalibrated similarity scores; specify `k`, candidate cutoffs, tie handling and any weights.
- Treat the default `k=60` from V1 as a **reference**, not a universally optimal constant.
- Record runtime and memory/latency where practical; models are not presumed better because they are larger.

## 7. Evaluation metrics

**Primary ranking metric:**
- **nDCG@5** with gains from grades 0/1/2: recognizes partially relevant pages and ranking position.

**Secondary diagnostics (grade 2 treated as relevant):**
- **Recall@3** and **Recall@5**.
- **MRR@3** (rank of first fully relevant document, capped at 3).
- **Hit@1** (fully relevant document at rank 1).
- Optional **Precision@3**, always interpreted with the number of grade-2 candidates per query.

**Sensitivity analysis:** Repeat binary metrics with `grade >= 1` and label these separately; never silently change the definition of relevance.

**Reporting:**
- Macro-average metrics across queries; include numerator/denominator and query counts.
- Breakdown by domain, query language and cross-language vs same-language cases.
- Side-by-side query examples, ranks, grade labels and failure taxonomies.
- Include run settings, costs/latency and uncertainty. With only 20 held-out queries, do **not** make sweeping or statistically confident superiority claims.

## 8. Planned repo artifacts (none generated by this specification)

```text
docs/v2/annotation_guidelines.md    # grading rubric + examples + disagreements
data/v2/documents.jsonl             # synthetic documents + provenance
data/v2/queries.jsonl               # queries and intent groups
data/v2/qrels.csv                   # complete human-reviewed graded judgments
data/v2/splits.json                 # immutable dev/test assignments
notebooks/benchmark_v2.ipynb        # evaluation notebook
results/v2/                     # per-query metrics, config, and summary
```

A script should validate IDs, 60/80 counts, completeness of all qrels, grade range, group leakage, and duplicate/query translation consistency **before** evaluating models.

**License:** V1 currently has no software license. Decide a repository software license and any **separate dataset license** explicitly before third-party reuse; model weights remain governed by their own licenses.

## 9. Milestones and review gates

| Stage | Deliverable | Pass condition |
|---|---|---|
| **M0 — Design** | This specification | Reviewed; unresolved decisions closed |
| **M1 — Pilot** | 12 queries, 24 pages and judged pairs | Annotation rubric, provenance and split logic validated |
| **M2 — Dataset V2** | 60 queries, 80 docs, qrels + split manifest | Complete labels, checked leakage, frozen test |
| **M3 — Baselines** | TF-IDF, MiniLM, BM25 on development | Reproducible settings and error analysis |
| **M4 — New methods** | Embeddings, RRF and optional reranker | Development-only selection, recorded compute costs |
| **M5 — Final evaluation** | One frozen held-out test run | Honest reporting with limitations |
| **M6 — Publication** | GitHub report; optional Hugging Face demo | Source, reproduction steps, appropriate permissions |

## 10. Decisions requested before moving to M1

1. **Use of data:** Confirm only synthetic, non-client content for V2, with no private data or customer identities.
2. **Scope:** Approve the 3-domain mix (ski, physiotherapy, tourist transport) rather than focusing the first serious benchmark on a single sector.
3. **Annotation resources:** Decide whether full human review of 4,800 pairs is realistic; if not, reduce the design rather than report incomplete qrels as complete.
4. **Licensing:** Decide the software and dataset licensing policy before a reusable public dataset release.
5. **Publication:** Approve pilot results for public disclosure only after their methodological limitations are documented.

**Next action after review:** Create the 12-query/24-document pilot with English annotations and multilingual *query content*. Do not run or publish a V2 leaderboard before the evaluation protocol is approved.
