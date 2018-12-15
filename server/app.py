import falcon
import os

from falcon_autocrud.middleware import Middleware
from sqlalchemy import create_engine

from resources import entry, person

app = falcon.API(
    middleware=[Middleware()]
)

db = create_engine('sqlite:///' + os.getenv('GB_APP_ROOT') + '/' + os.getenv('GB_DB_PATH'), echo=True)

app.add_route('/entry', entry.EntryCollectionResource(db))
app.add_route('/entry/{id}', entry.EntryResource(db))
app.add_route('/person', person.PersonCollectionResource(db))
app.add_route('/person/{id}', person.PersonResource(db))
