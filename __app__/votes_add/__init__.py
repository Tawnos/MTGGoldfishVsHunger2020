import azure.functions as func
import http.client
import json
from ..common.cosmos_client import DB
from ..data_types.Vote import Vote

def main(req: func.HttpRequest) -> str:
    req_body = req.get_json()

    user_id = req_body.get('user_id')
    toppings = req_body.get('toppings')
    decks = req_body.get('decks')

    for toppingVote in toppings:
        if len(toppingVote["value"]) > 5:
            return func.HttpResponse(
                status_code=http.client.BAD_REQUEST, 
                body="No more than 5 toppings are allowed")
        
    #TODO: upsert the votes so that existing votes by the same user stay in the same voting document

    vote = Vote(user_id, toppings, decks)
    
    userVotes = DB.Votes.read_item(item=user_id, partition_key="/user_id")

    DB.Votes.create_item(vote.__dict__)

    voteJson = json.dumps(userVotes, default=lambda x: x.__dict__)
    return func.HttpResponse(
        status_code=http.client.CREATED, 
        body=voteJson)
