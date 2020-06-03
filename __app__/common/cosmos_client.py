import azure.cosmos.documents as documents
import azure.cosmos.cosmos_client as cosmos_client
from __app__.common import globals


# cosmos_client = dbClient.CosmosClient(globals.COSMOSDB_ENDPOINT, globals.COSMOSDB_API_KEY)

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

class CollectionManagement:
    database_link = 'dbs/' + globals.DB_NAME

    @staticmethod
    def find_Container(client, id):
        collections = list(client.QueryContainers(
            database_link,
            {
                "query": "SELECT * FROM r WHERE r.id=@id",
                "parameters": [
                    { "name":"@id", "value": id }
                ]
            }
        ))

        if len(collections) > 0:
            print('Collection with id \'{0}\' was found'.format(id))
        else:
            print('No collection with id \'{0}\' was found'. format(id))
        
    @staticmethod
    def create_Container(client, id):
        try:
            client.CreateContainer(database_link, {"id": id})
            print('Collection with id \'{0}\' created'.format(id))

        except errors.HTTPFailure as e:
            if e.status_code == 409:
               print('A collection with id \'{0}\' already exists'.format(id))
            else: 
                raise


        print("\n2.4 Create Collection - With Unique keys")

        try:
            coll = {"id": "collection_unique_keys", 'uniqueKeyPolicy': {'uniqueKeys': [{'paths': ['/field1/field2', '/field3']}]}}
            collection_options = { 'offerThroughput': 400 }
            collection = client.CreateContainer(database_link, coll, collection_options )
            unique_key_paths = collection['uniqueKeyPolicy']['uniqueKeys'][0]['paths']
            print('Collection with id \'{0}\' created'.format(collection['id']))
            print('Unique Key Paths - \'{0}\', \'{1}\''.format(unique_key_paths[0], unique_key_paths[1]))
            
        except errors.HTTPFailure as e:
            if e.status_code == 409:
               print('A collection with id \'{0}\' already exists'.format(collection['id']))
            else: 
                raise

        print("\n2.5 Create Collection - With Partition key")
        
        try:
            coll = {
                "id": "collection_partition_key",
                "partitionKey": {
                    "paths": [
                      "/field1"
                    ],
                    "kind": "Hash"
                }
            }

            collection = client.CreateContainer(database_link, coll)
            print('Collection with id \'{0}\' created'.format(collection['id']))
            print('Partition Key - \'{0}\''.format(collection['partitionKey']))
            
        except errors.CosmosError as e:
            if e.status_code == 409:
               print('A collection with id \'{0}\' already exists'.format(collection['id']))
            else: 
                raise

        print("\n2.6 Create Collection - With Partition key V2")

        try:
            coll = {
                "id": "collection_partition_key_v2",
                "partitionKey": {
                    "paths": [
                        "/field1"
                    ],
                    "kind": "Hash",
                    "version": 2
                }
            }

            collection = client.CreateContainer(database_link, coll)
            print('Collection with id \'{0}\' created'.format(collection['id']))
            print('Partition Key - \'{0}\''.format(collection['partitionKey']))

        except errors.CosmosError as e:
            if e.status_code == 409:
                print('A collection with id \'{0}\' already exists'.format(collection['id']))
            else:
                raise
                     
    @staticmethod
    def read_Container(client, id):
        print("\n4. Get a Collection by id")

        try:
            # All Azure Cosmos resources are addressable via a link
            # This link is constructed from a combination of resource hierachy and 
            # the resource id. 
            # Eg. The link for collection with an id of Bar in database Foo would be dbs/Foo/colls/Bar
            collection_link = database_link + '/colls/{0}'.format(id)

            collection = client.ReadContainer(collection_link)
            print('Collection with id \'{0}\' was found, it\'s _self is {1}'.format(collection['id'], collection['_self']))

        except errors.HTTPFailure as e:
            if e.status_code == 404:
               print('A collection with id \'{0}\' does not exist'.format(id))
            else: 
                raise
    
    @staticmethod
    def list_Containers(client):
        print('Collections:')
        
        collections = list(client.ReadContainers(database_link))
        
        if not collections:
            return

        for collection in collections:
            print(collection['id'])          
        
    @staticmethod
    def delete_Container(client, id):
        try:
           collection_link = database_link + '/colls/{0}'.format(id)
           client.DeleteContainer(collection_link)

           print('Collection with id \'{0}\' was deleted'.format(id))

        except errors.HTTPFailure as e:
            if e.status_code == 404:
               print('A collection with id \'{0}\' does not exist'.format(id))
            else: 
                raise
