import cgi
import webapp2

##from google.appengine.api import users

mainpage_html = '''
<html>
  <head>
    <title>user login</title>
  </head>

  <body>
    <form method="post">
      <p>
        user name: <input type="text" name="name" value="%(name)s">
        <span style="color:red">%(err_name)s</span>

      </p>
      <p>
        pwd1: <input type="text" name="pwd1" value="%(pwd1)s" class="red">
        <span style="color:red">%(err_pwd1)s</span>

      </p>
      <p>
        pwd2: <input type="text" name="pwd2" value="%(pwd2)s" class="red">
        <span style="color:red">%(err_pwd2)s</span>

      </p>
      <p>
        email: <input type="text" name="emailaddr" value="%(emailaddr)s" class="red">
        <span style="color:red">%(err_emailaddr)s</span>

      </p>
      <br>
      <input type="submit">
    </form>
  </body>

</html>
'''

def escape_html(s):
    for (i, o) in (('&', '&amp;'),
                   ('<', '&lt;'),
                   ('>', '&gt;'),
                   ('"', '&quot;')):
        s = s.replace(i, o)
    return s

def valid_name(name):
    for ch in name:
        if not ch.isalnum():
            return None
    return name        
   
def valid_pwd(pwd1):
    for ch in pwd1:
        if not ch.isalnum():
            return None
    return pwd1 

def valid_emailaddr(emailaddr):
    for ch in emailaddr:
        if not ch.isalnum() and ch != '@':
            return None
    index = emailaddr.find('@')
    if not emailaddr.count('@') == 1 or emailaddr[index+1:] == '' or emailaddr[:index] == '':
        return None
    return emailaddr
   
class MainPage(webapp2.RequestHandler):
    def get(self):
        #f=open('mainpage.html', 'r')
        self.response.out.write(mainpage_html % {'name':'',
                                                 'pwd1':'',
                                                 'pwd2':'',
                                                 'emailaddr':'',
                                                 'err_name':'',
                                                 'err_pwd1':'',
                                                 'err_pwd2':'',
                                                 'err_emailaddr':''})#f.read()
        #f.close()

    def post(self):
        usr_name = self.request.get("name")
        usr_pwd1 = self.request.get("pwd1")
        usr_pwd2 = self.request.get("pwd2")
        usr_emailaddr = self.request.get("emailaddr")
        err_name = ''
        err_pwd1 = ''
        err_pwd2 = ''
        err_emailaddr = ''

        if not valid_name(usr_name): err_name = 'invalid name'
        if not valid_pwd(usr_pwd1): err_pwd1 = 'invalid pwd'
        if not usr_pwd1 == usr_pwd2: err_pwd2 = 'password not same'
        if not valid_emailaddr(usr_emailaddr): err_emailaddr = 'invalid email address'

        if not err_name and not err_pwd1 and not err_pwd2 and not err_emailaddr:
            self.redirect('/thanks')
        else:
            self.response.out.write(mainpage_html % {'name':usr_name,
                                                     'pwd1':usr_pwd1,
                                                     'pwd2':usr_pwd2,
                                                     'emailaddr':usr_emailaddr,
                                                     'err_name':err_name,
                                                     'err_pwd1':err_pwd1,
                                                     'err_pwd2':err_pwd2,
                                                     'err_emailaddr':err_emailaddr})

class ThankPage(webapp2.RequestHandler):
    def get(self):
        #f=open('mainpage.html', 'r')
        self.response.out.write('thanks, you\'ve log in!')#f.read()
        #f.close()
        
app = webapp2.WSGIApplication([('/', MainPage),
                               ('/thanks', ThankPage)],
                              debug=True)

