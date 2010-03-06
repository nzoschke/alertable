import re
from google.appengine.ext.webapp.mail_handlers import InboundMailHandler 
from rpc import Logger

class MailRouter(InboundMailHandler):
  routes = []
  
  def __init__(self):
    # default route for debugging/testing
    self.add_route(
      callback  = lambda m: Logger.log("%s -> %s: %s" % (m.sender, m.to, m.subject))
    )

  def receive(self, inbound_message):
    self.route(inbound_message)

  def add_route(self, callback, to=None, sender=None, subject=None, body=None):
    self.routes.append({
      'callback': callback,
      'to':       to and re.compile(to),
      'sender':   sender and re.compile(sender),
      'subject':  subject and re.compile(subject),
      'body':     body and re.compile(body)
    })

  def route(self, inbound_message):
    for route in self.routes:
      match = True
      for attr_name in ('to', 'sender', 'subject', 'body'):
        attr = getattr(inbound_message, attr_name)
        if route[attr_name] and not route[attr_name].match(attr):
          match = False
          break

      if match:
        route['callback'](inbound_message)
        break
