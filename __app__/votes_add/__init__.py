import azure.functions
from ..common.cosmos_client import DB
from ..data_types.Vote import Vote

def main(req: azure.functions.HttpRequest) -> str:
    req_body = req.get_json()

    user_id = req_body.get('user_id')
    toppings = req_body.get('toppings')
    decks = req_body.get('decks')

    vote = Vote(user_id, toppings, decks)
    DB.Votes.create_item(vote.__dict__)
    return {'RemainingVotes': {'Toppings': 2, 'Decks': 4}}
