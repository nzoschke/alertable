from google.appengine.ext import webapp 
from google.appengine.ext.webapp.util import run_wsgi_app

from handlers import MailRouter
from rpc import Prowl, GoogleVoice, Logger
from parsers import GVSMS, GVVM

if __name__ == '__main__':
  application = webapp.WSGIApplication([MailRouter.mapping()], debug=True)
  run_wsgi_app(application)