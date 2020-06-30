from . import Topping, DeckLink
from typing import List, Tuple, Any
import uuid

class Vote:
    def __init__(self, count: int, value: Any): 
        self.VoteId = uuid.uuid4()
        self.Count = count
        self.Value = value