from packages.core.engine import ReasoningEngine
from packages.core.types import Thought
from logging import getLogger

logger = getLogger(__name__)

class Executor:
    def __init__(self, reasoning_engine: ReasoningEngine):
        self.reasoning_engine = reasoning_engine

    def execute(self, prompt: str) -> str:
        thoughts = self.reasoning_engine.explore(prompt)
        pruned_thoughts = self.reasoning_engine.prune(thoughts)
        final_response = self.reasoning_engine.synthesize(pruned_thoughts)
        return final_response