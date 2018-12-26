from falcon_autocrud.auth import authorize
from falcon_autocrud.resource import CollectionResource, SingleResource

from auth import AuthenticationChecker
from models import person

@authorize(AuthenticationChecker)
class PersonCollectionResource(CollectionResource):
    allow_subresources = False
    methods = ['GET', 'POST']
    model = person.Person

@authorize(AuthenticationChecker)
class PersonResource(SingleResource):
    allow_subresources = False
    methods = ['DELETE', 'PATCH']
    model = person.Person
