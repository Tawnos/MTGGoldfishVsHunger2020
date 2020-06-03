import azure.cosmos.cosmos_client as cosmos_client
from __app__.common import globals

client = cosmos_client.CosmosClient(globals.COSMOSDB_ENDPOINT, globals.COSMOSDB_API_KEY)
db = client.CreateDatabase(globals.DB_NAME)
db.
