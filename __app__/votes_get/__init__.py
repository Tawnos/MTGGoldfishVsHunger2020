import azure.functions as func
import json
from ..common.cosmos_client import DB
import logging

def set_default(obj):
    if isinstance(obj, set):
        return list(obj)
    return obj.__dict__

def main(req: func.HttpRequest) -> str:

    toppings = DB.Votes.query_items(
        query='SELECT SUM(t["count"]) AS count, t["value"] AS toppings FROM v JOIN t in v.toppings GROUP BY t["value"]',
        enable_cross_partition_query=True
    )

    logging.info(toppings)
    logging.info(f"Zach {toppings}")

    decks = DB.Votes.query_items(
        query='SELECT SUM(d["count"]) AS count, d["value"] AS toppings FROM v JOIN d in v.decks GROUP BY d["value"]',
        enable_cross_partition_query=True
    )

    return json.dumps({"toppings": toppings, "decks": decks.to_json()})
