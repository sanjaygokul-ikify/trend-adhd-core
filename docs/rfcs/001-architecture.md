# Architecture RFC

## Key Components
- Cognitive Frame Manager (CFM)
- Threaded Reasoning Engines (TRE)
- Pruning Evaluator (EVAL)
- Synthesis Optimizer (SO)

## Data Flow

[User Query] -> CFM -> TREs -> EVAL -> SO -> Response


## Version Control
This RFC supersedes all earlier drafts about the tree-of-thought implementation. To evolve this architecture, create a new RFC using docs/rfcs/rfc_template.md