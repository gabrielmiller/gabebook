from falcon_autocrud.auth import identify, authorize
from falcon_autocrud.resource import CollectionResource, SingleResource

from auth import Authenticate, Identify
from models import entry

@identify(Identify)
@authorize(Authenticate)
class EntryCollectionResource(CollectionResource):
    methods = ['GET', 'POST']
    model = entry.Entry

@identify(Identify)
@authorize(Authenticate)
class EntryResource(SingleResource):
    methods = ['DELETE', 'PATCH']
    model = entry.Entry
