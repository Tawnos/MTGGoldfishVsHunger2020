import azure.functions as func
import json
from MTGGoldFishVsHunger.common import cosmos_client

def main(req: func.HttpRequest) -> func.HttpResponse:
    
    return func.HttpResponse(
        body = json.dumps(cosmos_client.DB.Goals),
        mimetype="application/json",
        charset="utf-8"
    )

        # [
        #     {'amount':1000, 'description': 'foo bar baz prize'}, 
        #     {'amount':2000, 'description': 'foo bar baz prize'}
        # ]