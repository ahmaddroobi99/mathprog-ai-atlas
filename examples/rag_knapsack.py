"""RAG passage selection as a binary knapsack.

This is the smallest honest example of the atlas thesis.
A retriever emits relevance scores. The program decides which
passages to keep under a token budget and a cardinality cap.

Install:
    pip install pulp

The solver here is exact for tiny n. Production RAG is usually a
heuristic with the same shape.
"""

from __future__ import annotations

from dataclasses import dataclass

try:
    import pulp
except ImportError as exc:  # pragma: no cover
    raise SystemExit("Install pulp: pip install pulp") from exc


@dataclass(frozen=True)
class Passage:
    name: str
    relevance: float
    tokens: int
    redundant_with: tuple[str, ...] = ()


PASSAGES = [
    Passage("intro_def", relevance=0.91, tokens=180),
    Passage("proof_sketch", relevance=0.84, tokens=260),
    Passage("same_proof_copy", relevance=0.82, tokens=240, redundant_with=("proof_sketch",)),
    Passage("application_rag", relevance=0.88, tokens=150),
    Passage("application_moe", relevance=0.80, tokens=140),
    Passage("limitations", relevance=0.70, tokens=120),
    Passage("unrelated_bio", relevance=0.22, tokens=200),
]


def select(passages: list[Passage], token_budget: int = 500, max_keep: int = 3) -> list[str]:
    model = pulp.LpProblem("rag_select", pulp.LpMaximize)
    choose = {p.name: pulp.LpVariable(p.name, cat="Binary") for p in passages}

    model += pulp.lpSum(p.relevance * choose[p.name] for p in passages)
    model += pulp.lpSum(p.tokens * choose[p.name] for p in passages) <= token_budget
    model += pulp.lpSum(choose[p.name] for p in passages) <= max_keep

    names = {p.name: p for p in passages}
    for p in passages:
        for other in p.redundant_with:
            if other in names:
                model += choose[p.name] + choose[other] <= 1

    model.solve(pulp.PULP_CBC_CMD(msg=False))
    return [p.name for p in passages if choose[p.name].value() == 1]


if __name__ == "__main__":
    kept = select(PASSAGES)
    print("kept:", ", ".join(kept))
    print("tokens:", sum(p.tokens for p in PASSAGES if p.name in kept))
    print("value:", sum(p.relevance for p in PASSAGES if p.name in kept))
