import azure.functions
from ..common.cosmos_client import DB
from ..data_types.Vote import Vote

def main(req: azure.functions.HttpRequest) -> str:
    req_body = req.get_json()

    user_id = req_body.get('user_id')
    deck_id = req_body.get('deck_id')
