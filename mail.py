import logging
from google.appengine.ext import webapp 
from google.appengine.ext.webapp.util import run_wsgi_app

try:
  from settings import MailRouter
except ImportError, e:
  logging.warning(e)
  from handlers import MailRouter

if __name__ == '__main__':
  application = webapp.WSGIApplication([MailRouter.mapping()], debug=True)
  run_wsgi_app(application)