"""
views.py

URL route handlers

Note that any handler params must match the URL route params.
For example the *say_hello* handler, handling the URL route '/hello/<username>',
  must be passed *username* as the argument.

"""

from google.appengine.api import users
from google.appengine.runtime.apiproxy_errors import CapabilityDisabledError
from google.appengine.ext import ndb

from flask import render_template, flash, url_for, redirect, request, jsonify,Markup

from decorators import login_required, admin_required
from models import UrlModel
from application import app
import string,random, uuid



def hash_gen(size=6, chars=string.ascii_uppercase + \
                 string.digits+ "".join(str(uuid.uuid4()).split('-'))):
    return ''.join(random.choice(chars) for x in range(size))
    
@app.route('/')
@app.route('/index')
def index():
    return render_template("url_shortener.html")

@app.route('/create', methods=['GET'])
def create():
    longUrl = Markup(request.args.get('longUrl', False))
    if longUrl == None or longUrl == "":
       message = "Or try passing a url."
       return render_template('500.html',message=message), 500
    url_hash = hash_gen()
    shortUrl = request.url_root + url_hash
    data = {'url':shortUrl, 'hash':url_hash, 'longUrl':longUrl}
    results = {'status_code':200,'data':data,'status_txt':'OK'}
    jsonData = {'jsonResult':results}
    result = jsonData['jsonResult']
  
    url = UrlModel(
               url = shortUrl,
               longUrl = longUrl,
               urlHash = url_hash)
    ndb.Key(UrlModel, url_hash)
    try:
        url.put()
        flash(u'Data successfully saved.', 'success')
        return jsonify(result=result)
    except CapabilityDisabledError:
        flash(u'App Engine Datastore is currently in read-only mode.', 'failure')
        return jsonify(result=result)
    
@app.route('/<hashid>')
def short_url(hashid):
    try:
       qry = UrlModel.query(UrlModel.urlHash == hashid)
       qry1 = qry.get()
       result = qry1.longUrl
       return redirect(result,301)  
    except:
       return render_template('404.html'), 404
       

# Contrived admin-only view example
@app.route('/admin_only')
@admin_required
def admin_only():
    """This view requires an admin account"""
    return 'Super-seekrit admin page.'


# See http://code.google.com/appengine/docs/python/config/appconfig.html#Warming_Requests
@app.route('/_ah/warmup')
def warmup():
    """App Engine warmup handler
    See http://code.google.com/appengine/docs/python/config/appconfig.html#Warming_Requests

    """
    return ''

## Error handlers
# Handle 404 errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Handle 500 errors
@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

