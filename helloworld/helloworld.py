##import webapp2
##
##class MainPage(webapp2.RequestHandler):
##  def get(self):
##      self.response.headers['Content-Type'] = 'text/plain'
##      self.response.write('Hello, Udacity!')
##
##app = webapp2.WSGIApplication([('/', MainPage)],
##                              debug=True)

##import cgi
##import webapp2
##
##from google.appengine.api import users
##
##class MainPage(webapp2.RequestHandler):
##    def get(self):
##        f=open('page.html', 'r')
##        self.response.out.write(f.read())
##        f.close()

##def escape_html(s):
##    for (i, o) in (('&', '&amp;'),
##                   ('<', '&lt;'),
##                   ('>', '&gt;'),
##                   ('"', '&quot;')):
##        s = s.replace(i, o)
##    return s

import os
import webapp2
import jinja2
from google.appengine.ext import db
##from google.appengine.api import users
from userlogin import *
from calculate_and_rot13 import *

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)
    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)
    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))
            
class AsciiChan(Handler):
    def render_page(self):
        arts = db.GqlQuery('SELECT * FROM Art ORDER BY created DESC')
        self.render('ascii_chan.html', arts=arts)
    def get(self):
        self.render_page()
    def post(self):
        clear = self.request.get('clear')
        if clear == 'on':
            arts_del = db.GqlQuery('SELECT * FROM Art')
            db.delete(arts_del)
            
        self.redirect('/asciichan')

class AsciiChanHandler(Handler):
    def get(self, art_id):
        #arts = db.GqlQuery('SELECT * FROM Art ORDER BY created DESC')
        a = Art.get_by_id(int(art_id))
        self.render('ascii_chan_sub.html', arts=[a])
        
class SubmitHandler(Handler):
    def get(self):
        self.render('submit.html', title='', art='', error='')
    def post(self):
        title = self.request.get('title')
        art = self.request.get('art')
        title = title.strip()
        if title and art:
            a = Art(title=title, art=art)
            a.put()
            self.redirect('/asciichan/'+str(a.key().id()))
        else:
            error = 'both non-empty title and art needed!'
            self.render('submit.html', title=title, art=art, error=error)
        
class Art(db.Model):
    title = db.StringProperty(required = True)
    art = db.TextProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)
    
class MainPage(Handler):
    def get(self):
        self.render('mainpage.html')


        
app = webapp2.WSGIApplication([('/', MainPage),
                               ('/calculate', Calculate),
                               ('/rot13', ROT13),
                               ('/asciichan', AsciiChan),
                               ('/asciichan/(\d+)', AsciiChanHandler),
                               ('/submit', SubmitHandler),
                               ('/userlogin', UserloginPage),
                               ('/thanks', ThanksPage)],
                              debug=True)


