# Examples

Start with `rag_knapsack.py`.

It is intentionally small. A model (here: hardcoded scores) proposes values. A binary program decides what to keep under a token budget, a cardinality cap, and a redundancy cut.

That is the documentation standard for future examples:

1. Name the decision.
2. Write the constraints in code.
3. Print the kept set, the resource use, and the objective.
4. Say whether the solver is exact or heuristic.
