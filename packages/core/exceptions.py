class ReasoningError(Exception):
    pass

class HypothesisExplorationError(ReasoningError):
    pass

class PruningError(ReasoningError):
    pass