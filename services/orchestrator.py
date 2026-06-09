from typing import List
from packages.core import ReasoningEngine

class Orchestrator:
    def __init__(self):
        self.engine = ReasoningEngine(CognitiveFrame('default', 'default'))

    def run(self, prompt: str) -> List[str]:
        try:
            thoughts = self.engine.explore(prompt)
            thoughts = self.engine.prune(thoughts)
            result = self.engine.synthesize(thoughts)
            return [result]
        except Exception as e:
            logger.error(f'Error during thought synthesis: {e}')
            raise ReasoningError('Thought synthesis failed') from e