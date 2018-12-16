from falcon_autocrud.auth import identify, authorize
from falcon_autocrud.resource import CollectionResource, SingleResource

from auth import Authenticate, Identify
from models import person

@identify(Identify)
@authorize(Authenticate)
class PersonCollectionResource(CollectionResource):
    allow_subresources = False
    methods = ['GET', 'POST']
    model = person.Person

@identify(Identify)
@authorize(Authenticate)
class PersonResource(SingleResource):
    allow_subresources = False
    methods = ['DELETE', 'PATCH']
    model = person.Person
