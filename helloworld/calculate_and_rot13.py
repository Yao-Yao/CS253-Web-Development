import os
import webapp2

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)
    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)
    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))
        
class Calculate(Handler):
    def get(self):
        self.render('calculate.html')
        
    def post(self):
        self.write('<html><body>The result is:<pre>')
        self.write(eval(self.request.get('content')))
        self.write('</pre></body></html>')

class ROT13(Handler):
    def ROT(self, s):
        outstr = ''
        ch_rot13 = ''
        for ch in s:
            if ch.isalpha():
                if ch.islower():
                    ch_rot13 =  '%c' % (ord('a') + (ord(ch)-ord('a')+13)%26)
                else:
                    ch_rot13 =  '%c' % (ord('A') + (ord(ch)-ord('A')+13)%26)
            else:
                ch_rot13 = ch
            outstr += ch_rot13
        return outstr
    def get(self):
        self.render('rot13.html')

    def post(self):
        usr_text = self.request.get("text")
        rot13_text = self.ROT(usr_text)
        self.render('rot13.html', text=rot13_text)
