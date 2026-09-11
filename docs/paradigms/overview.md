# Paradigm notes

Each note follows the same four beats: decision, structure, AI mapping, exact vs heuristic.

## 1. Linear programming

**Decision.** Continuous allocations under linear resource limits.

**Structure.**

```
min  c^T x
s.t. A x  <= b
```

The feasible set is a polyhedron. Optima sit at vertices when they exist.

**AI mapping.** Compressed sensing recoveries that stay linear. Multi object tracking as a network flow. Any stage that assigns a budget of tokens, compute, or bandwidth when the variables can stay continuous.

**Exact vs heuristic.** Simplex and interior point methods can return certificates. Large production systems often warm start or truncate. Do not call a truncated solve optimal.

## 2. Quadratic programming

**Decision.** Continuous choices whose cost includes interactions, not only linear terms.

**Structure.**

```
min  (1/2) x^T Q x + c^T x
s.t. A x  <= b
```

If Q is positive semidefinite the program is convex.

**AI mapping.** Locally linear embedding reconstruction weights. Kernel SVM duals. Model predictive control on learned dynamics. Portfolio style allocation of model capacity.

**Exact vs heuristic.** OSQP, Clarabel, and other first order solvers are the workhorses. Nonconvex Q needs a different honesty label.

## 3. Binary integer programming

**Decision.** Include or exclude. On or off. Route or skip.

**Structure.**

```
max  c^T x
s.t. A x  <= b
     x in {0,1}^n
```

**AI mapping.** RAG passage selection under a token budget. Mixture of Experts routing when each token picks a discrete expert set. Tool selection for an agent. Notification or alert dispatch.

**Exact vs heuristic.** Branch and bound can certify. Production RAG almost never solves the MIP to proven optimality at request time. Treat top k plus diversity rules as a heuristic unless you actually call a MIP solver.

## 4. Mixed integer programming

**Decision.** Some variables stay continuous, some must be integer. Precision, assignment, and resource limits live in one model.

**Structure.**

```
min  (1/2) x^T Q x + c^T x
s.t. A x  <= b
     x_I integer, x_C continuous
```

**AI mapping.** Decision trees as MIP encodings. Constrained retrieval. Mixed precision quantization. Keyframe selection. Clustering with discrete assignments and continuous centers.

**Exact vs heuristic.** MIP is the most common real decision hammer. It is also the easiest place to overclaim. Log the gap.

## 5. Binary quadratic programming

**Decision.** Binary choices that interact. Diversity, correlation, and pairwise repulsion belong here.

**Structure.**

```
max  x^T Q x + c^T x
     x in {0,1}^n
```

**AI mapping.** Diversity aware recommendation. QUBO style subset selection. Correlation clustering cousins.

**Exact vs heuristic.** Exact BQP is hard. QUBO heuristics, local search, and relaxations are the common path. Quantum annealer marketing is not a certificate.

## 6. Conic optimization

**Decision.** Continuous choices whose constraints live in a cone: second order, exponential, or other convex cones.

**Structure.** Second order cone form used in Group Lasso:

```
min  ||A x - b||_2
s.t. ||x_g||_2  <= t_g
```

**AI mapping.** Group feature selection. Robust norms. Control and robotics constraints that encode Euclidean budgets.

**Exact vs heuristic.** Interior point conic solvers are mature. The modeling layer (CVXPY, JuMP) matters as much as the solver.

## 7. Semidefinite programming

**Decision.** Optimize over positive semidefinite matrices.

**Structure.**

```
min  <C, X>
s.t. A(X) = b
     X  succeq  0
```

**AI mapping.** Sparse PCA. Some phase retrieval and kernel learning relaxations. Tight bounds for combinatorial problems.

**Exact vs heuristic.** SDP relaxations can be exact on special graphs and loose elsewhere. Rounding the matrix back to a discrete object is part of the algorithm, not a footnote.

## 8. Bilevel optimization

**Decision.** Choose an outer parameter that changes an inner training or planning problem.

**Structure.**

```
choose lambda
  theta*(lambda) = argmin_theta  TrainingLoss(theta, lambda)
  minimize ValidationLoss(theta*(lambda), lambda)
```

**AI mapping.** Hyperparameter optimization. Neural architecture search. Coreset selection. Diffusion schedule search. Some AI scientist plus simulator loops.

**Exact vs heuristic.** Implicit differentiation and unrolling are approximations of the lower level solution map. An LLM that proposes an objective and a simulator that fits parameters can resemble bilevel structure without being a smooth bilevel program.

## 9. Multiobjective optimization

**Decision.** Several losses or utilities that should not be smashed into one anonymous sum.

**Structure.** Find Pareto stationary points of (L1(theta), ..., LT(theta)).

**AI mapping.** Multi task learning. Accuracy vs latency vs energy vs safety.

**Exact vs heuristic.** Scalarization is a method, not the problem. If gradients conflict, name the conflict and report the front, not a single number.

## 10. Inverse optimization

**Decision.** Infer the objective that makes observed behavior optimal, or nearly optimal.

**Structure.** Observed action y is treated as the solution of

```
y ~ argmin_x  c(theta)^T x
```

Then recover theta.

**AI mapping.** Inverse reinforcement learning. Revealed preference. Recovering rewards from expert trajectories.

**Exact vs heuristic.** Identifiability is the central scientific issue. Many objectives explain the same behavior. Regularize the reward class or you will tell a story, not recover a law.

## 11. Distributionally robust optimization

**Decision.** Optimize against a neighborhood of plausible distributions, not only the empirical one.

**Structure.**

```
min_theta  max_{Q in U(P)}  E_Q[loss(theta; xi)]
```

**AI mapping.** Robust contrastive learning. Group shift. LLM preference alignment that must survive a changed user mix.

**Exact vs heuristic.** The uncertainty set is a modeling choice. A ball that is too large yields a conservative product. A ball that is too small is ordinary ERM in costume.

## 12. Submodular optimization

**Decision.** Build a set under diminishing returns.

**Structure.** Maximize f(S) subject to |S| <= k when f is monotone submodular. Greedy then has a 1 - 1/e guarantee under the standard assumptions.

**AI mapping.** Data subset selection. Document summarization. Active learning. KV cache eviction that is not static top k.

**Exact vs heuristic.** The greedy guarantee is real only when the set function is actually monotone submodular. Learned importance scores do not automatically inherit that proof.

## 13. Min max optimization

**Decision.** Two players, opposite objectives.

**Structure.**

```
min_G  max_D  V(D, G)
```

**AI mapping.** GANs. Some adversarial training loops. Robust control cousins.

**Exact vs heuristic.** The elegant saddle point lives in convex concave theory. Neural G vs neural D is usually a nonconvex nonconcave game. Classical global saddle guarantees do not transfer just because the loss looks like a GAN.
