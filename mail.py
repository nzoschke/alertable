from google.appengine.ext import webapp 
from google.appengine.ext.webapp.util import run_wsgi_app

from handlers import MailRouter
from rpc import Prowl, GoogleVoice, Logger
from parsers import GVSMS, GVVM

class MyMailRouter(MailRouter):
  def __init__(self):
    self.add_route(
      sender    = ".*txt.voice.google.com",
      subject   = ".*Karina",
      callback  = lambda m: Prowl.add(application='GV', event='New SMS')
    )

    self.add_route(
      sender    = ".*txt.voice.google.com",
      callback  = lambda m: Prowl.add(application='GV', event=GVSMS(m).subject, description=GVSMS(m).body)
    )

    self.add_route(
      sender    = ".*voice-noreply@google.com",
      callback  = lambda m: Prowl.add(application='GV', event=GVVM(m).subject, description=GVVM(m).body)
    )

    self.add_route(
      callback  = lambda m: Logger.log("Default Route :: %s -> %s: %s" % (m.sender, m.to, m.subject))
    )

if __name__ == '__main__':
  application = webapp.WSGIApplication([MyMailRouter.mapping()], debug=True)
  run_wsgi_app(application)