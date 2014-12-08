"""
models.py

App Engine datastore models

"""


from google.appengine.ext import db
from google.appengine.ext import ndb

class UrlModel(ndb.Model):
    """Url Model"""  
    url = ndb.StringProperty(required=True)
    longUrl = ndb.StringProperty(required=True)
    urlHash = ndb.StringProperty(required=True)
    added_by = ndb.UserProperty()
    timestamp = ndb.DateTimeProperty(auto_now_add=True)
    

