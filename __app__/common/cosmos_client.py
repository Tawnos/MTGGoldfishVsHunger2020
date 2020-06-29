import azure.cosmos.documents as documents
import azure.cosmos.cosmos_client as dbClient
from __app__.common import globals



class IDisposable(cosmos_client.CosmosClient):
    """ A context manager to automatically close an object with a close method
    in a with statement. """

    def __init__(self, obj):
        self.obj = obj

    def __enter__(self):
        return self.obj # bound to target

    def __exit__(self, exception_type, exception_val, trace):
        # extra cleanup in here
        self.obj = None

class Users:
    def __init(self, client: dbClient):
        self.container = client.get_container_client("Users")

    def get(id):
        collections = list(client.QueryContainers(
            database_link,
            {
                "query": "SELECT * FROM r WHERE r.id=@id",
                "parameters": [
                    { "name":"@id", "value": id }
                ]
            }
        ))

class Donations:
    def __init(self, client: dbClient)
        self.container = client.get_container_client("Donations")

class Votes:
    def __init(self, client: dbClient)
        self.container = client.get_container_client("Votes")


class Client:
    database_link = 'dbs/' + globals.DB_NAME

    def __init__(self, database_link):
        self.cosmos_client = dbClient.CosmosClient(globals.COSMOSDB_ENDPOINT, globals.COSMOSDB_API_KEY)
        self.database_link = database_link

    def upsert_item(container, doc_id):
        read_item = container.read_item(item=doc_id, partition_key=doc_id)
        read_item['subtotal'] = read_item['subtotal'] + 1
        response = container.upsert_item(body=read_item)
