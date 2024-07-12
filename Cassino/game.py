from dataclasses import dataclass, field
from typing import List

@dataclass
class Game:
    slots: List[List[str]] = field(default_factory = [])

    def desenhar(self):
        print(self.slots)
        
