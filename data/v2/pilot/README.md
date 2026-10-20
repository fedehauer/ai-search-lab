# AI Search Lab — V2 Pilot (Review Draft)

**Status:** Synthetic candidate data and **proposed, unreviewed relevance judgments**. No new model results, no validated evaluation, no customer data.

- **12** queries (4 ski, 4 physiotherapy, 4 tourist transport)
- **24** invented page-like documents (8 per sector)
- **288** query-document grade proposals, in the full **0/1/2** rubric
- **8** development queries, **4** reserved test queries; paraphrase/translation intent groups do not cross splits
- Query languages: **{"de":2,"es":3,"en":7}**
- Candidate corpus shared by both splits; no labels should be fed into retrieval models.

## Files
- `documents.jsonl`: fictional page titles, descriptions and language metadata
- `queries.jsonl`: multilingual queries, intent-group IDs and suggested split
- `qrels_draft.csv`: complete 288-row **AI-proposed** relevance annotations, **not yet reviewed**
- `splits.json`: auditable query-group assignments
- `../../../../docs/v2/annotation_guidelines.md`: human review instructions and disputed edge cases

## Review gate

**Do not present these judgments as validated ground truth.** First review the borderline examples and then the complete pair judgments using the published annotation rules. If requirements or grades change, version the data, update the rationale and rerun the leakage/completeness checks. Refrain from reporting scores on the held-out split until the design is frozen.

Reference specification: [BENCHMARK_V2_SPEC.md](../../../BENCHMARK_V2_SPEC.md).
