from . import Topping, DeckLink
from typing import List, Tuple, Any

class Vote:
    def __init__(self, count: int, value: Any): 
        self.Count = count
        self.Value = value