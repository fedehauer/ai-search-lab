# AI Search Lab — Benchmark V1

**An exploratory, reproducible learning exercise in multilingual Information Retrieval for SEO.**  
Created as an applied Information Retrieval exercise by Federico Hauer.

> **Research status: educational / exploratory.** Not a production search engine, a Google ranking study, or a measurement of ChatGPT retrieval behavior.

## Research question

Given multilingual SEO queries and candidate page titles, how do three retrieval approaches compare?

1. **TF-IDF** — token-based lexical similarity with 1–2 word n-grams.
2. **MiniLM** — `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` sentence embeddings.
3. **Hybrid RRF** — equal-weight reciprocal rank fusion (`k=60`) of the two ranked lists.

## Dataset

- **6** synthetic queries (German and Spanish).
- **11** synthetic page titles (German and Spanish).
- **66** query–document comparisons.
- Human-assigned **binary relevance labels** provided in `data/benchmark_v1.json`.

A relevant result in this exercise is one that satisfies the specified service/action and destination under the author-defined labels. These labels are assumptions for teaching, not a validated production ground truth.

## Results from the original Colab run

| System | Macro Recall@3 | Mean Hit@1 | MRR@3 |
|---|---:|---:|---:|
| TF-IDF | 66.67% | 83.33% | 83.33% |
| MiniLM | 83.33% | 83.33% | 88.89% |
| Hybrid RRF | 83.33% | 83.33% | 91.67% |

The MRR gain for Hybrid RRF came from a **single query**: the relevant repair page moved from rank 3 (MiniLM) to rank 2 (Hybrid RRF). No method placed the repair page first. These numbers cannot establish broad superiority of any method.

`results/v1_per_query.csv` and `results/v1_summary.csv` preserve the **actual notebook outputs** supplied in the original run, not newly inferred scores.

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/fedehauer/ai-search-lab/blob/main/notebooks/AI_Search_Lab_Benchmark_V1_English.ipynb)

## Run in Google Colab

1. Download or open `notebooks/AI_Search_Lab_Benchmark_V1_English.ipynb` in [Google Colab](https://colab.research.google.com/).
2. Go to **Runtime → Run all** (CPU runtime is sufficient).
3. The first code cell installs `sentence-transformers` and `scikit-learn` in the Colab environment.
4. Subsequent cells download MiniLM from Hugging Face, evaluate all three systems, and print per-system metrics.
5. The last code cell saves a `benchmark_v1_results.csv` in Colab's temporary environment. Download it if you want to retain the new run.

**Cost:** No paid Hugging Face Inference Providers are used. Colab's free compute is subject to resource limits and availability.

**Dependencies:** `requirements.txt` lists the top-level dependencies. The original environment's exact package versions were not captured; the organized notebook now prints the installed versions. Exact reproduction across environments requires pinning these versions and model revision.

## Project structure

```text
ai-search-lab/
├── notebooks/
│   └── AI_Search_Lab_Benchmark_V1_English.ipynb
├── data/
│   └── benchmark_v1.json
├── results/
│   ├── v1_per_query.csv
│   └── v1_summary.csv
├── requirements.txt
├── .gitignore
└── README.md
```

## Methodological limitations

- Six invented queries and eleven invented page titles are not a representative SEO dataset.
- Ground truth is binary and author-defined; real pages may require graded relevance judgments.
- Precision@3 is capped when fewer than three relevant documents exist.
- TF-IDF is a basic lexical baseline, not an optimized BM25 or language-specific retrieval system.
- Zero-score lexical ties are resolved by document ID for deterministic ranking.
- RRF `k=60` and equal weights were not tuned on a separate development set.
- The notebook runs MiniLM on CPU; exact scores can vary with library/model versions.
- The study says **nothing direct about Google rankings, AI Overview selection, or citation behavior of commercial chatbots**.

## Next steps

This repository preserves the first learning stage. Before making stronger claims or deploying a real product:

1. Review all relevance judgments and document the annotation criteria.
2. Build **Benchmark V2** with a broader, authorized dataset.
3. Separate development queries from the final evaluation set.
4. Pin package versions, model revision, and runtime configuration.
5. Compare stronger lexical baselines (e.g., BM25), other embedding models, and rerankers.

**License note:** No software license has been assigned to this project yet; choose one before inviting third-party reuse. The underlying model's license is separate.


**Language policy:** Documentation, comments, variable names, and outputs are in English. The German and Spanish query/title strings are preserved as experimental data.