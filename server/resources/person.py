from falcon_autocrud.resource import CollectionResource, SingleResource
from models import person

class PersonCollectionResource(CollectionResource):
    allow_subresources = False
    methods = ['GET', 'POST']
    model = person.Person

class PersonResource(SingleResource):
    allow_subresources = False
    methods = ['DELETE', 'PATCH']
    model = person.Person
