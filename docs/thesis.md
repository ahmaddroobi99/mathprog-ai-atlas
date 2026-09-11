# Thesis

Machine learning predicts. Mathematical programming decides.

A trained model can emit a score, a probability, an embedding, a cost, or a utility. Those numbers are not yet an action. An action has to survive budgets, capacities, integrality, safety limits, competing objectives, and uncertainty.

```
real world
    |
    v
learned model
    |  scores, probabilities, embeddings, costs, utilities
    v
mathematical program
    |  objective, constraints, resources, assignments, uncertainty
    v
decision
    |
    v
real action
```

This atlas does not claim that every AI system is an LP or a MIP. It claims something narrower and more useful:

> Mathematical programming is the disciplined interface between learned predictions and constrained decisions.

## Why the interface matters

Two systems can look unrelated at the product layer and still share a decision structure.

| Product story | Decision structure |
| --- | --- |
| RAG context selection | multidimensional knapsack |
| Mixture of Experts routing | capacity constrained assignment |
| Test time compute | multiple choice knapsack |
| KV cache eviction | monotone submodular selection |
| Preference alignment under shift | distributionally robust optimization |
| Neural architecture search | bilevel program |
| GAN training | min max game |

Once the structure is named, the rest of the work gets easier. You can choose a solver class, a relaxation, a certificate, or an honest heuristic.

## Four error sources

Final decision quality is not the same thing as model quality.

```
final decision quality
          ^
          |
 +--------+--------+--------+
 |        |        |        |
prediction  candidate  solver  execution
error       loss       gap     drift
```

- **Prediction error.** The coefficients fed to the program are wrong.
- **Candidate loss.** Retrieval or proposal never offered the feasible optimum.
- **Solver gap.** The optimizer returned an approximate or timed out solution.
- **Execution drift.** The real system is not the model that was solved.

A perfect MIP cannot recover a document that retrieval never proposed. A greedy selector cannot inherit the certificate of branch and bound.

## Exact formulation and deployed algorithm

Keep these two layers separate in every note.

| Layer | What you get |
| --- | --- |
| Exact formulation | a model, a relaxation, sometimes a certificate |
| Deployed algorithm | pruning, greedy, local search, learned routing |

Both are useful. The failure mode is advertising the guarantee of the formulation while shipping the heuristic.

## Cross paradigm systems

Real systems do not stay in one box.

```
data
  -> learned coefficients (sometimes bilevel, DRO, or multiobjective)
  -> LP / QP / MIP / conic decision layer
  -> action
```

A robust training procedure can produce the costs. A MIP can consume those costs. An SDP can bound a relaxation. Duality can decompose an assignment. The atlas is a map of those joints, not a demand that one paradigm own the whole stack.
