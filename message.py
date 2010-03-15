import logging
from google.appengine.ext import webapp 
from google.appengine.ext.webapp.util import run_wsgi_app

try:
  from settings import MessageRouter
except ImportError, e:
  logging.warning(e)
  from handlers import MessageRouter

if __name__ == '__main__':
  application = webapp.WSGIApplication([
    ('/_ah/mail/.+', MessageRouter),
    ('/_ah/xmpp/message/chat/', MessageRouter),
  ], debug=True)
  run_wsgi_app(application)