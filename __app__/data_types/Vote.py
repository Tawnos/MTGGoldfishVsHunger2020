from . import Toppings, DeckLink
import uuid

class Vote:
    def __init__(self, user_id, toppings, decks): 
        self.id = str(uuid.uuid4())
        self.user_id = user_id
        self.toppings = toppings
        self.decks = decks