from ..common import api_auth
import azure.functions
from ..common.cosmos_client import DB

def main(req: azure.functions.HttpRequest) -> str:
    total = DB.Donations.query_items(
        query="SELECT VALUE SUM(r.amount) FROM r",
        enable_cross_partition_query=True
    )
    return f"Total: {total}"
    