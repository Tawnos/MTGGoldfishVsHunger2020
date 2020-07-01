from azure.cosmos import cosmos_client, PartitionKey
from ..common import globals

client = cosmos_client.CosmosClient(globals.COSMOSDB_ENDPOINT, globals.COSMOSDB_API_KEY)
db = client.create_database(globals.DB_NAME)

db.create_container(id="Votes", partition_key=PartitionKey(path='/user_id', kind='Hash'))
db.create_container(id="Donations", partition_key=PartitionKey(path='/user_id', kind='Hash'))
