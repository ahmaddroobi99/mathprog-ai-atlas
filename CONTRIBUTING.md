# Contributing

This repository is a living atlas. The README is the teaching surface. Everything else exists so the README can stay short and accurate.

## What belongs here

- A new paradigm only if it changes how a decision is encoded.
- A new repository only if it is a solver, a modeling layer, a benchmark, or a clean application of one paradigm.
- A correction when a mapping overclaims exactness for a heuristic system.

## What does not belong here

- Generic awesome lists with no mapping to a decision structure.
- Vendor pitch pages with no formulation.
- Duplicate entries under a slightly different name.

## How to add a repository

1. Open `catalog/repositories.md`.
2. Add one row under the correct paradigm.
3. Required fields: name, url, role, why.
4. Keep the README table short. The catalog is the full list.

## How to add a note

Keep paradigm notes in `docs/paradigms/`. Each note should answer four questions:

1. What is being decided?
2. What is continuous, discrete, nested, robust, or adversarial?
3. Which AI system actually uses this structure?
4. Where does the exact formulation stop and the deployed heuristic begin?

## Voice

Write like a staff engineer teaching a colleague.

- Prefer short sentences.
- Name the decision, then the math.
- Do not claim a guarantee that the deployed system does not compute.
- Separate prediction error, candidate loss, solver gap, and execution drift.
