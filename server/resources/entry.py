from falcon_autocrud.resource import CollectionResource, SingleResource
from models import entry

class EntryCollectionResource(CollectionResource):
    methods = ['GET', 'POST']
    model = entry.Entry

class EntryResource(SingleResource):
    methods = ['DELETE', 'PATCH']
    model = entry.Entry
