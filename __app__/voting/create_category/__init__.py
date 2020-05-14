import azure.functions
import azure.cosmos.cosmos_client as cosmos_client
from __app__.common import globals

def main(req: azure.functions.HttpRequest) -> str:
    client = cosmos_client.CosmosClient(globals.COSMOSDB_ENDPOINT, globals.COSMOSDB_API_KEY)
    client.CreateContainer("test")
    