from ..common import api_auth
import azure.functions
from ..common.cosmos_client import DB
import json
import requests
import re

def get_deck_name(actual_url: str) -> Dict[str, str]:        
    response = requests.get(actual_url)
    if response.ok:
        deck_name = re.findall("<title>(.*)</title>", response.text)
        if deck_name:
            return {"name": deck_name[-1], "url": actual_url}
       
    return {"name": "Unknown Deck", "url": ""}

def main(req: azure.functions.HttpRequest) -> str:
    widget_url = "https://www.mtggoldfish.com/deck/"

    deck_url = req.route_params.get('deckURL')
    if deck_url:
        if deck_url.startswith(widget_url):
            return json.dumps(get_deck_name(deck_url))
        
        return "FAILED"
    
    # Query CosmoDB for top decks
    top_deck_ids = [2277093, 2277094, 2277095] 

    top_deck_names = [get_deck_name(widget_url + deck_id) for deck_id in top_deck_ids]

    return json.dumps(top_deck_names)