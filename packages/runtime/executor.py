from packages.core.engine import ReasoningEngine
from packages.core.types import Thought
from logging import getLogger

logger = getLogger(__name__)

class Executor:
    def __init__(self, reasoning_engine: ReasoningEngine):
        self.reasoning_engine = reasoning_engine

    def execute(self, prompt: str, timeout: float = 30.0) -> str:
        import signal
        import threading
        try:
            # Create a timer to raise a timeout exception after the specified time
            def timeout_handler(signum, frame):
                raise TimeoutError('Timeout occurred during thought synthesis')
            signal.signal(signal.SIGALRM, timeout_handler)
            signal.alarm(int(timeout))
            thoughts = self.reasoning_engine.explore(prompt)
            pruned_thoughts = self.reasoning_engine.prune(thoughts)
            final_response = self.reasoning_engine.synthesize(pruned_thoughts)
            signal.alarm(0)  # Disable the alarm
            return final_response
        except TimeoutError as e:
            logger.error(f'Timeout during thought synthesis: {e}')
            raise ReasoningError('Thought synthesis timed out') from e
        except Exception as e:
            logger.error(f'Error during thought synthesis: {e}')
            raise ReasoningError('Thought synthesis failed') from e