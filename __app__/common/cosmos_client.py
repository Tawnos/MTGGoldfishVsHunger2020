from azure.cosmos import CosmosClient, PartitionKey, exceptions
from . import globals


class IDisposable(CosmosClient):
    """ A context manager to automatically close an object with a close method
    in a with statement. """

    def __init__(self, obj):
        self.obj = obj

    def __enter__(self):
        return self.obj  # bound to target

    def __exit__(self, exception_type, exception_val, trace):
        # extra cleanup in here
        self.obj = None


class Client:
    def __init__(self):
        self.cosmos_client = CosmosClient(globals.COSMOSDB_ENDPOINT, globals.COSMOSDB_API_KEY)
        self.db = self.cosmos_client.get_database_client(globals.DB_NAME)

        self.Users = self.db.get_container_client("Users")
        self.Votes = self.db.get_container_client("Votes")
        self.Donations = self.db.get_container_client("Donations")
        self.Goals = [
            {'amount': 1000, 'description': 'foo bar baz prize'},
            {'amount': 2000, 'description': 'foo bar baz prize'}
        ]

    def init_container(self, name, partitionId):
        try:
            return self.db.create_container(name, PartitionKey(path=partitionId))
        except exceptions.CosmosResourceExistsError:
            return self.db.get_container_client(name)

    # def upsert_item(container, doc_id):
    #     read_item = container.read_item(item=doc_id, partition_key=doc_id)
    #     read_item['subtotal'] = read_item['subtotal'] + 1
    #     response = container.upsert_item(body=read_item)


DB = Client()
