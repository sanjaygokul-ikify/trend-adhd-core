import unittest
from cli.main import main
from packages.core import ReasoningEngine, Thought, CognitiveFrame

class TestPipeline(unittest.TestCase):
    def test_pipeline(self):
        # Arrange
        cognitive_frame = CognitiveFrame('test', 'test')
        engine = ReasoningEngine(cognitive_frame)
        # Act
        thoughts = engine.explore('test')
        thoughts = engine.prune(thoughts)
        result = engine.synthesize(thoughts)
        # Assert
        self.assertIsInstance(result, str)

if __name__ == '__main__':
    unittest.main()