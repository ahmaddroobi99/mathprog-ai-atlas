# Repository catalog

Ten repositories per paradigm. The list is a starting atlas, not a ranking of quality. Prefer the modeling layer when you are writing a formulation. Prefer the solver when you need a certificate or a speed path.

Role tags:

- `solver` computes a solution
- `modeling` writes the program
- `application` is an AI system that uses the structure
- `benchmark` measures formulations or solvers
- `notes` teaches the math

## Linear programming

| Repository | Role | Why it is here |
| --- | --- | --- |
| [google/or-tools](https://github.com/google/or-tools) | solver | Production LP and MIP with routing and assignment examples |
| [ERGO-Code/HiGHS](https://github.com/ERGO-Code/HiGHS) | solver | Open simplex and interior point engine used across SciPy and modeling layers |
| [coin-or/pulp](https://github.com/coin-or/pulp) | modeling | Smallest honest way to write an LP in Python |
| [cvxpy/cvxpy](https://github.com/cvxpy/cvxpy) | modeling | Disciplined convex modeling that lowers to LP when the program is linear |
| [Pyomo/pyomo](https://github.com/Pyomo/pyomo) | modeling | Algebraic modeling for structured LPs and beyond |
| [jump-dev/JuMP.jl](https://github.com/jump-dev/JuMP.jl) | modeling | Fast modeling language with first class LP solvers |
| [scipy/scipy](https://github.com/scipy/scipy) | solver | scipy.optimize.linprog is the default scientific Python entry point |
| [coin-or/Clp](https://github.com/coin-or/Clp) | solver | Classic COIN-OR LP engine |
| [jckantor/ND-Pyomo-Cookbook](https://github.com/jckantor/ND-Pyomo-Cookbook) | notes | Teaching examples that stay close to formulations |
| [Pyomo/pyomo-gallery](https://github.com/Pyomo/pyomo-gallery) | notes | Compact LP and MIP patterns |

## Quadratic programming

| Repository | Role | Why it is here |
| --- | --- | --- |
| [osqp/osqp](https://github.com/osqp/osqp) | solver | Operator splitting QP used in control and learning |
| [qpsolvers/qpsolvers](https://github.com/qpsolvers/qpsolvers) | modeling | One Python API over many QP backends |
| [osqp/osqp-python](https://github.com/osqp/osqp-python) | solver | Direct Python interface |
| [cvxpy/cvxpy](https://github.com/cvxpy/cvxpy) | modeling | Convex QP with constraints written as math |
| [Simple-Robotics/proxsuite](https://github.com/Simple-Robotics/proxsuite) | solver | ProxQP for robotics and MPC style QPs |
| [coin-or/qpOASES](https://github.com/coin-or/qpOASES) | solver | Active set QP with a long control history |
| [liuq/QuadProgpp](https://github.com/liuq/QuadProgpp) | solver | Goldfarb Idnani dense QP |
| [google/osqp-cpp](https://github.com/google/osqp-cpp) | solver | C++ wrapper used in systems code |
| [gbionics/osqp-eigen](https://github.com/gbionics/osqp-eigen) | solver | Eigen facing QP in robot stacks |
| [osqp/osqp_benchmarks](https://github.com/osqp/osqp_benchmarks) | benchmark | Compare QP engines on shared problems |

## Binary integer programming

| Repository | Role | Why it is here |
| --- | --- | --- |
| [google/or-tools](https://github.com/google/or-tools) | solver | CP-SAT and MIP for binary assignment |
| [coin-or/Cbc](https://github.com/coin-or/Cbc) | solver | Open branch and cut |
| [scipopt/scip](https://github.com/scipopt/scip) | solver | Exact MIP with plugins |
| [Pyomo/pyomo](https://github.com/Pyomo/pyomo) | modeling | Binary variables as first class objects |
| [coin-or/pulp](https://github.com/coin-or/pulp) | modeling | Binary knapsacks without ceremony |
| [JWally/jsLPSolver](https://github.com/JWally/jsLPSolver) | solver | Browser side LP and ILP for small demos |
| [ANL-CEEESA/MIPLearn](https://github.com/ANL-CEEESA/MIPLearn) | application | Learning to solve MIP instances |
| [ds4dm/ecole](https://github.com/ds4dm/ecole) | application | RL gym for exact MIP solvers |
| [ds4dm/learn2branch](https://github.com/ds4dm/learn2branch) | application | Learned branching inside exact solvers |
| [OptimizationExpert/Pyomo](https://github.com/OptimizationExpert/Pyomo) | notes | Worked discrete models you can read in an afternoon |

## Mixed integer programming

| Repository | Role | Why it is here |
| --- | --- | --- |
| [google/or-tools](https://github.com/google/or-tools) | solver | The default open MIP path for product engineers |
| [ERGO-Code/HiGHS](https://github.com/ERGO-Code/HiGHS) | solver | Open MIP that SciPy already ships |
| [scipopt/PySCIPOpt](https://github.com/scipopt/PySCIPOpt) | modeling | Python access to SCIP |
| [Pyomo/pyomo](https://github.com/Pyomo/pyomo) | modeling | Mixed discrete and continuous models |
| [jump-dev/JuMP.jl](https://github.com/jump-dev/JuMP.jl) | modeling | MIP at research speed |
| [coin-or/Cbc](https://github.com/coin-or/Cbc) | solver | Branch and cut workhorse |
| [ANL-CEEESA/MIPLearn](https://github.com/ANL-CEEESA/MIPLearn) | application | Learned MIP branching and warm starts |
| [ds4dm/ecole](https://github.com/ds4dm/ecole) | benchmark | Standard environment for ML inside MIP |
| [ds4dm/learn2branch](https://github.com/ds4dm/learn2branch) | application | Learning branch variable selection |
| [OptimizationExpert/Pyomo](https://github.com/OptimizationExpert/Pyomo) | notes | Supply chain MIP casebook |

## Binary quadratic programming

| Repository | Role | Why it is here |
| --- | --- | --- |
| [dwavesystems/dwave-ocean-sdk](https://github.com/dwavesystems/dwave-ocean-sdk) | modeling | QUBO tooling, classical and annealer backends |
| [dwavesystems/dimod](https://github.com/dwavesystems/dimod) | modeling | Shared binary quadratic model API |
| [dwavesystems/qbsolv](https://github.com/dwavesystems/qbsolv) | solver | Decomposing QUBO heuristic |
| [recruit-communications/pyqubo](https://github.com/recruit-communications/pyqubo) | modeling | Write QUBO from Python expressions |
| [tamuhey/awesome-qubo](https://github.com/tamuhey/awesome-qubo) | notes | Map of QUBO applications |
| [OpenJij/OpenJij](https://github.com/OpenJij/OpenJij) | solver | Open Ising and QUBO heuristics |
| [dwavesystems/dwave-system](https://github.com/dwavesystems/dwave-system) | modeling | Sampler layer over QUBO models |
| [dwavesystems/dwave-hybrid](https://github.com/dwavesystems/dwave-hybrid) | solver | Classical hybrid decomposition for large QUBO |
| [lanl-ansi/Juniper.jl](https://github.com/lanl-ansi/Juniper.jl) | solver | Nonlinear branch and bound neighbor of discrete quadratic models |
| [qiskit-community/qiskit-optimization](https://github.com/qiskit-community/qiskit-optimization) | modeling | QUBO and binary quadratic modeling in Qiskit |

Treat annealer repos as formulation tools. They do not turn BQP into an easy problem.

## Conic optimization

| Repository | Role | Why it is here |
| --- | --- | --- |
| [cvxpy/cvxpy](https://github.com/cvxpy/cvxpy) | modeling | SOCP and other cones with a readable DSL |
| [cvxgrp/scs](https://github.com/cvxgrp/scs) | solver | Splitting conic solver |
| [oxfordcontrol/Clarabel.rs](https://github.com/oxfordcontrol/Clarabel.rs) | solver | Modern interior point conic solver |
| [embotech/ecos](https://github.com/embotech/ecos) | solver | Embedded SOCP |
| [jump-dev/Convex.jl](https://github.com/jump-dev/Convex.jl) | modeling | Julia disciplined convex layer |
| [cvxopt/cvxopt](https://github.com/cvxopt/cvxopt) | solver | Classic Python convex and conic stack |
| [oxfordcontrol/COSMO.jl](https://github.com/oxfordcontrol/COSMO.jl) | solver | ADMM conic solver |
| [cvxpy/cvxpylayers](https://github.com/cvxpy/cvxpylayers) | application | Differentiable convex layers, including cones |
| [cvxgrp/cvxpygen](https://github.com/cvxgrp/cvxpygen) | application | Generated C solvers from CVXPY models |
| [cvxpy/cvxkerb](https://github.com/cvxpy/cvxkerb) | application | Landing rocket demo of constrained convex control |

## Semidefinite programming

| Repository | Role | Why it is here |
| --- | --- | --- |
| [cvxpy/cvxpy](https://github.com/cvxpy/cvxpy) | modeling | SDP as X >> 0 |
| [cvxgrp/scs](https://github.com/cvxgrp/scs) | solver | First order SDP at useful scale |
| [jump-dev/SumOfSquares.jl](https://github.com/jump-dev/SumOfSquares.jl) | modeling | Polynomial and SDP relaxations |
| [oxfordcontrol/Clarabel.rs](https://github.com/oxfordcontrol/Clarabel.rs) | solver | SDP capable interior point |
| [coin-or/Csdp](https://github.com/coin-or/Csdp) | solver | Classic primal dual SDP |
| [sqlp/sdpt3](https://github.com/sqlp/sdpt3) | solver | Reference interior point SDP |
| [scikit-learn/scikit-learn](https://github.com/scikit-learn/scikit-learn) | application | SparsePCA as the deployed cousin of the SDP story |
| [jump-dev/Hypatia.jl](https://github.com/jump-dev/Hypatia.jl) | solver | Advanced conic interior point including SDP |
| [cvxgrp/scs-python](https://github.com/cvxgrp/scs-python) | solver | Python interface to SCS for SDP experiments |
| [MOSEK/Mosek.jl](https://github.com/MOSEK/Mosek.jl) | solver | Commercial SDP quality, Julia interface |

## Bilevel optimization

| Repository | Role | Why it is here |
| --- | --- | --- |
| [facebookresearch/higher](https://github.com/facebookresearch/higher) | application | Differentiable inner optimizers |
| [quark0/darts](https://github.com/quark0/darts) | application | Original DARTS code, the standard continuous NAS bilevel |
| [microsoft/nni](https://github.com/microsoft/nni) | application | NAS and HPO platform |
| [optuna/optuna](https://github.com/optuna/optuna) | application | Practical outer loop over inner training |
| [cvxpy/cvxpylayers](https://github.com/cvxpy/cvxpylayers) | application | Implicit differentiation through convex inner problems |
| [locuslab/optnet](https://github.com/locuslab/optnet) | application | QP inner problems as network layers |
| [D-X-Y/Awesome-NAS](https://github.com/D-X-Y/Awesome-NAS) | notes | Map of architecture search as outer and inner programs |
| [awslabs/syne-tune](https://github.com/awslabs/syne-tune) | application | Distributed outer loop over inner training jobs |
| [microsoft/archai](https://github.com/microsoft/archai) | application | Research platform for architecture search |
| [ray-project/ray](https://github.com/ray-project/ray) | application | Tune as an outer loop over inner training |

## Multiobjective optimization

| Repository | Role | Why it is here |
| --- | --- | --- |
| [anyoptimization/pymoo](https://github.com/anyoptimization/pymoo) | solver | NSGA-II, NSGA-III, and the standard Python front |
| [Project-Platypus/Platypus](https://github.com/Project-Platypus/Platypus) | solver | Compact multiobjective algorithms |
| [DEAP/deap](https://github.com/DEAP/deap) | solver | Evolutionary multiobjective primitives |
| [jMetal/jMetalPy](https://github.com/jMetal/jMetalPy) | solver | Classic algorithm library |
| [optuna/optuna](https://github.com/optuna/optuna) | application | Multiobjective HPO |
| [facebookresearch/fairseq](https://github.com/facebookresearch/fairseq) | application | Multi task training patterns in sequence models |
| [Cranial-XIX/CAGrad](https://github.com/Cranial-XIX/CAGrad) | application | Conflicting gradients in multi task learning |
| [median-research-group/LibMTL](https://github.com/median-research-group/LibMTL) | application | Multi task learning benchmark library |
| [intel/neural-compressor](https://github.com/intel/neural-compressor) | application | Accuracy versus latency tradeoffs in deployed models |
| [automl/multi-objective-nas](https://github.com/automl) | notes | Multiobjective architecture search neighbor |

## Inverse optimization

| Repository | Role | Why it is here |
| --- | --- | --- |
| [HumanCompatibleAI/imitation](https://github.com/HumanCompatibleAI/imitation) | application | Modern IRL and imitation algorithms |
| [yrlu/irl-imitation](https://github.com/yrlu/irl-imitation) | application | MaxEnt and LP IRL implementations |
| [Farama-Foundation/Minari](https://github.com/Farama-Foundation/Minari) | benchmark | Offline expert datasets for inverse problems |
| [Farama-Foundation/Gymnasium](https://github.com/Farama-Foundation/Gymnasium) | benchmark | Standard environments for recovered rewards |
| [DLR-RM/stable-baselines3](https://github.com/DLR-RM/stable-baselines3) | application | Forward RL after a reward is inferred |
| [XanderJC/scalable-birl](https://github.com/XanderJC/scalable-birl) | application | Bayesian IRL |
| [ran-weii/cleanil](https://github.com/ran-weii/cleanil) | application | Clean imitation and IRL implementations |
| [ahq1993/inverse_rl](https://github.com/ahq1993/inverse_rl) | application | Variational inverse RL |
| [gemst1/IRL](https://github.com/gemst1/IRL) | notes | Survey style code index |
| [justinjfu/inverse_rl](https://github.com/justinjfu/inverse_rl) | application | Classic adversarial IRL code family |

## Distributionally robust optimization

| Repository | Role | Why it is here |
| --- | --- | --- |
| [namkoong-lab/dro](https://github.com/namkoong-lab/dro) | modeling | DRO methods on CVXPY and PyTorch |
| [kohpangwei/group_DRO](https://github.com/kohpangwei/group_DRO) | application | Group shift robust networks |
| [p-lambda/wilds](https://github.com/p-lambda/wilds) | benchmark | In the wild distribution shift benchmark |
| [Iyengar-Lab/E2E-DRO](https://github.com/Iyengar-Lab/E2E-DRO) | application | End to end DRO with learned models |
| [pmichel31415/P-DRO](https://github.com/pmichel31415/P-DRO) | application | Parametric likelihood ratio DRO |
| [MadryLab/robustness](https://github.com/MadryLab/robustness) | application | Robust training reference |
| [LongPham7/Distributionally-Robust-Optimization](https://github.com/LongPham7/Distributionally-Robust-Optimization) | application | DRO for deep nets |
| [brain-lab-research/ALSO](https://github.com/brain-lab-research/ALSO) | application | DRO aligned with practical deep learning |
| [Prinway/Distributionally-Robust-Optimization-Notes](https://github.com/Prinway/Distributionally-Robust-Optimization-Notes) | notes | Compact DRO notes |
| [facebookresearch/wilds](https://github.com/p-lambda/wilds) | benchmark | Keep WILDS as the shift benchmark even when mirrored |

## Submodular optimization

| Repository | Role | Why it is here |
| --- | --- | --- |
| [jmschrei/apricot](https://github.com/jmschrei/apricot) | solver | Submodular selection for data subsets |
| [decile-team/submodlib](https://github.com/decile-team/submodlib) | solver | Rich submodular function library |
| [huggingface/transformers](https://github.com/huggingface/transformers) | application | KV cache implementations to rewrite as set selection |
| [Dao-AILab/flash-attention](https://github.com/Dao-AILab/flash-attention) | application | Attention kernels whose cache policy can be treated as a set function |
| [microsoft/DeepSpeed](https://github.com/microsoft/DeepSpeed) | application | Inference cache and token dropping cousins |
| [NVIDIA/TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM) | application | Production KV cache eviction to compare against greedy submodular |
| [snorkel-team/snorkel](https://github.com/snorkel-team/snorkel) | application | Data selection neighbor |
| [modAL-python/modAL](https://github.com/modAL-python/modAL) | application | Active learning as iterative set building |
| [google-research/google-research](https://github.com/google-research/google-research) | application | Search the tree for summarization and facility location |
| [stanfordnlp/CoreNLP](https://github.com/stanfordnlp/CoreNLP) | notes | Classic summarization neighbor; use apricot for the set function |

## Min max optimization

| Repository | Role | Why it is here |
| --- | --- | --- |
| [eriklindernoren/PyTorch-GAN](https://github.com/eriklindernoren/PyTorch-GAN) | application | Catalog of GAN objectives |
| [junyanz/pytorch-CycleGAN-and-pix2pix](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix) | application | Paired and unpaired adversarial translation |
| [NVlabs/stylegan2](https://github.com/NVlabs/stylegan2) | application | High quality generator discriminator game |
| [NVlabs/stylegan3](https://github.com/NVlabs/stylegan3) | application | Later StyleGAN game |
| [goodfeli/adversarial](https://github.com/goodfeli/adversarial) | notes | Early adversarial training code family |
| [POSTECH-CVLab/PyTorch-StudioGAN](https://github.com/POSTECH-CVLab/PyTorch-StudioGAN) | benchmark | Many GAN recipes, one library |
| [ajbrock/BigGAN-PyTorch](https://github.com/ajbrock/BigGAN-PyTorch) | application | Class conditional GAN |
| [lucidrains/stylegan2-pytorch](https://github.com/lucidrains/stylegan2-pytorch) | application | Minimal StyleGAN2 |
| [MadryLab/mnist_challenge](https://github.com/MadryLab/mnist_challenge) | application | Robust optimization as a min max attack defense game |
| [locuslab/robust-overfitting](https://github.com/locuslab/robust-overfitting) | application | Adversarial training dynamics |

## Shared modeling layer

These cut across paradigms. Pin them at the top of any new experiment.

| Repository | Why |
| --- | --- |
| [cvxpy/cvxpy](https://github.com/cvxpy/cvxpy) | Write convex programs the way you write math |
| [google/or-tools](https://github.com/google/or-tools) | Discrete decisions in production |
| [Pyomo/pyomo](https://github.com/Pyomo/pyomo) | Structured programs larger than a notebook |
| [jump-dev/JuMP.jl](https://github.com/jump-dev/JuMP.jl) | Research grade modeling |
| [SciML/Optimization.jl](https://github.com/SciML/Optimization.jl) | One Julia interface over many solver classes |
| [cvxpy/cvxpylayers](https://github.com/cvxpy/cvxpylayers) | Differentiable optimization inside a net |
