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
        self.__cosmos_client = CosmosClient(globals.COSMOSDB_ENDPOINT, globals.COSMOSDB_API_KEY)
        self.__db = self.__cosmos_client.get_database_client(globals.DB_NAME)

        self.Votes = self.__db.get_container_client("Votes")
        self.Donations = self.__db.get_container_client("Donations")
        self.Goals = [
            {'amount': 5000, 'description': 'do a little dance'},
            {'amount': 10000, 'description': 'make a little love'},
            {'amount': 15000, 'description': 'get down tonight'},
            {'amount': 20000, 'description': 'get down tonight'}
        ]

    # def upsert_item(container, doc_id):
    #     read_item = container.read_item(item=doc_id, partition_key=doc_id)
    #     read_item['subtotal'] = read_item['subtotal'] + 1
    #     response = container.upsert_item(body=read_item)


DB = Client()
