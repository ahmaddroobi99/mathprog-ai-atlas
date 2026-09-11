# Error budget

A decision pipeline has four places to lose quality. Write them down before you tune a solver.

```
candidate generation
        |
        v
   learned scores
        |
        v
     optimizer
        |
        v
     execution
```

| Source | Question | Typical failure |
| --- | --- | --- |
| Prediction error | Are the coefficients true enough? | A relevance model ranks the wrong passage first |
| Candidate loss | Did the generator even offer the optimum? | Retrieval never fetched the right document |
| Solver gap | How far is the returned point from the model optimum? | Time limit, greedy step, bad relaxation |
| Execution drift | Does the real system match the model? | Token counter differs from the constraint you wrote |

## How to report a result

Do not publish one number called accuracy for the whole stack. Report:

1. Recall of the candidate set.
2. Quality of the predicted coefficients on a held out slice.
3. Optimality gap of the solver, or an explicit heuristic with no gap.
4. Live metric after execution.

## Exact and heuristic

```
exact MIP
  branch and bound
  certificate
  gap -> 0

heuristic
  prune
  greedy
  local search
  fast
  no automatic certificate
```

Both belong in production. The documentation standard is to name which one you shipped.
