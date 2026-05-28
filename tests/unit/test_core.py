import unittest
from packages.core import Thought, CognitiveFrame, ReasoningEngine

class TestCore(unittest.TestCase):
    def test_thought(self):
        cognitive_frame = CognitiveFrame('test', 'test')
        thought = Thought('test', cognitive_frame)
        self.assertEqual(thought.prompt, 'test')
        self.assertEqual(thought.cognitive_frame, cognitive_frame)

    def test_reasoning_engine(self):
        cognitive_frame = CognitiveFrame('test', 'test')
        engine = ReasoningEngine(cognitive_frame)
        thoughts = engine.explore('test')
        self.assertIsInstance(thoughts, list)
        self.assertIsInstance(thoughts[0], Thought)

if __name__ == '__main__':
    unittest.main()