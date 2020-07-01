import azure.functions
from ..common.cosmos_client import DB

def main(req: azure.functions.HttpRequest) -> str:
    DB.Votes.query_items(
        query="SELECT TOP 10 VALUE SUM(r.amount) FROM r",
        enable_cross_partition_query=True
    )
