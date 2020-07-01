from ..common import api_auth
import azure.functions
from ..common.cosmos_client import DB

def main(req: azure.functions.HttpRequest) -> str:
    total = DB.Donations.query_items(
        query="SELECT VALUE SUM(r.amount) FROM r"
    )
    return f"Total: {total}"
    