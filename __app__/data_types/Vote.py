from . import Toppings, DeckLink
from typing import List, Tuple, Any
import uuid

class Vote:
    def __init__(self, user_id, toppings: List[Tuple[int, List[str]]], decks: List[Tuple[int,int]]): 
        self.id = str(uuid.uuid4())
        self.user_id = user_id
        self.toppings = toppings
        self.decks = decks