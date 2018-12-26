from falcon_autocrud.auth import identify, authorize
from falcon_autocrud.resource import CollectionResource, SingleResource

from auth import AuthenticationChecker
from models import entry

@authorize(AuthenticationChecker)
class EntryCollectionResource(CollectionResource):
    methods = ['GET', 'POST']
    model = entry.Entry

@authorize(AuthenticationChecker)
class EntryResource(SingleResource):
    methods = ['DELETE', 'PATCH']
    model = entry.Entry
