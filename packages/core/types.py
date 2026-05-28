from dataclasses import dataclass
from typing import List

dataclass
class Thought:
    prompt: str
    cognitive_frame: 'CognitiveFrame'

    def __post_init__(self):
        self.children: List['Thought'] = []

@dataclass
class CognitiveFrame:
    name: str
    description: str