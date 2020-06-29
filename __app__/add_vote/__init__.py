import azure.functions
from ..common.cosmos_client import DB

def main(req: azure.functions.HttpRequest) -> str:
    req_body = req.get_json()

    DB.Votes.create_item(body=req_body)
    return {'RemainingVotes': {'Toppings': 2, 'Decks': 4}}
