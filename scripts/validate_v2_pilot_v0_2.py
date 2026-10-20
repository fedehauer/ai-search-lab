#!/usr/bin/env python3
"""Validate the synthetic AI Search Lab V2 pilot v0.2.

Run from any directory:
    python scripts/validate_v2_pilot_v0_2.py

No third-party dependencies. This verifies data integrity and evidence-coverage
proposals, NOT human agreement or benchmark validity.
"""
from __future__ import annotations

import csv
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OLD = ROOT / "data" / "v2" / "pilot"
NEW = ROOT / "data" / "v2" / "pilot_v0_2"
NEW_IDS = {"SK09", "PH09", "TR09"}
EXPECTED = {0: 289, 1: 17, 2: 18}
EXPECTED_GRADES = {
    ("SKQ01", "SK09"): 2,
    ("SKQ02", "SK09"): 2,
    ("PHQ01", "PH09"): 2,
    ("PHQ02", "PH09"): 2,
    ("PHQ03", "PH09"): 1,
    ("TRQ01", "TR09"): 2,
    ("TRQ02", "TR09"): 2,
}


def jsonl(path: Path) -> list[dict]:
    with path.open("r", encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def qrels(path: Path) -> list[dict]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    required = {"query_id", "document_id", "grade", "review_status", "rationale"}
    assert rows and set(rows[0]) == required, f"Unexpected qrels columns: {path}"
    for row in rows:
        assert row["grade"] in {"0", "1", "2"}, f"Invalid grade: {row}"
        row["grade"] = int(row["grade"])
    return rows


def validate() -> None:
    old_docs, new_docs = jsonl(OLD / "documents.jsonl"), jsonl(NEW / "documents.jsonl")
    old_queries, new_queries = jsonl(OLD / "queries.jsonl"), jsonl(NEW / "queries.jsonl")
    old_qrels, new_qrels = qrels(OLD / "qrels_draft.csv"), qrels(NEW / "qrels_draft.csv")
    old_splits, new_splits = read_json(OLD / "splits.json"), read_json(NEW / "splits.json")
    lineage = read_json(NEW / "lineage.json")

    assert (len(old_docs), len(old_queries), len(old_qrels)) == (24, 12, 288), (
        "Original pilot counts have changed"
    )
    assert (len(new_docs), len(new_queries), len(new_qrels)) == (27, 12, 324)
    assert old_docs == new_docs[:24], "Original 24 document entries were altered"
    assert old_queries == new_queries, "Original query entries were altered"
    assert set(x["document_id"] for x in new_docs[24:]) == NEW_IDS
    assert len({x["document_id"] for x in new_docs}) == 27
    assert len({x["query_id"] for x in new_queries}) == 12

    old_map = {(r["query_id"], r["document_id"]): r for r in old_qrels}
    new_map = {(r["query_id"], r["document_id"]): r for r in new_qrels}
    assert len(old_map) == 288 and len(new_map) == 324, "Duplicate qrel pair(s)"
    for key, original in old_map.items():
        assert new_map.get(key) == original, f"Existing qrel modified: {key}"

    keys = {
        (q["query_id"], doc["document_id"])
        for q in new_queries
        for doc in new_docs
    }
    assert set(new_map) == keys, "The 12 x 27 judgment matrix is incomplete"
    assert all(row["review_status"] == "proposed_unreviewed" for row in new_qrels)
    assert all(row["rationale"].strip() for row in new_qrels)
    actual_grades = Counter(row["grade"] for row in new_qrels)
    assert dict(actual_grades) == EXPECTED, (
        f"Unexpected grade counts: {dict(actual_grades)}"
    )
    for pair, expected in EXPECTED_GRADES.items():
        assert new_map[pair]["grade"] == expected, f"Incorrect grade for {pair}"

    for q in new_queries:
        assert any(
            new_map[(q["query_id"], d["document_id"])]["grade"] == 2
            for d in new_docs
        ), f"No proposed fully relevant document for {q['query_id']}"

    assert old_splits["assignments"] == new_splits["assignments"]
    assert old_splits["groups"] == new_splits["groups"]
    assert new_splits["version"] == "pilot-v0.2"
    assert (new_splits["docs_total"], new_splits["queries_total"]) == (27, 12)
    assert new_splits["expected_judgments"] == 324
    assignment_map = {x["query_id"]: x for x in new_splits["assignments"]}
    assert set(assignment_map) == {q["query_id"] for q in new_queries}
    assert Counter(q["split"] for q in new_queries) == {
        "development": 8,
        "test": 4,
    }
    groups = {}
    for q in new_queries:
        assert assignment_map[q["query_id"]]["split"] == q["split"]
        assert assignment_map[q["query_id"]]["intent_group_id"] == q["intent_group_id"]
        group = q["intent_group_id"]
        if group in groups:
            assert groups[group] == q["split"], f"Split leakage: {group}"
        groups[group] = q["split"]

    assert lineage["new_document_ids"] == ["SK09", "PH09", "TR09"]
    assert lineage["current_pairs"] == 324 and lineage["added_qrels_rows"] == 36
    assert lineage["preserved_qrels_rows"] == 288
    assert lineage["human_validation"] is False

    print("PASS — Synthetic V2 pilot v0.2 structural validation")
    print("27 documents x 12 queries = 324 complete, unreviewed judgments")
    print("Old pilot: 24 documents and 288 qrels preserved verbatim as records")
    print("New docs: SK09, PH09, TR09; all 36 new candidate pairs labeled")
    print("Grades: 0=289, 1=17, 2=18")
    print("All 12 queries have at least one PROPOSED grade-2 document")
    print("8 development / 4 test queries; no intent-group split leakage")
    print("WARNING: This does NOT establish validated human ground truth.")
    print("WARNING: Public pilot test queries/qrels are not blinded.")


if __name__ == "__main__":
    try:
        validate()
    except (AssertionError, ValueError, OSError, KeyError) as error:
        print(f"FAIL — {error}", file=sys.stderr)
        raise SystemExit(1)
