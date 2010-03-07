import re
from google.appengine.ext.webapp.mail_handlers import InboundMailHandler 
from rpc import Logger

class MailRouter(InboundMailHandler):
  routes = []
  
  def __init__(self):
    self.add_route(
      callback  = lambda m: Logger.log('Sender: %s\nTo: %s\nSubject: %s\nBody: %s' % (m.sender, m.to, m.subject, repr(unicode(m.body)))) # default route for debugging/testing
    )

  def receive(self, inbound_message):
    for route in self.routes:
      match = False
      for attr_name in route:
        if hasattr(inbound_message, attr_name):
          attr = getattr(inbound_message, attr_name)
          if route[attr_name] and not route[attr_name].match(attr):
            match = False
            break
          else:
            match = True

      if match:
        route['callback'](inbound_message)
        break

  def add_route(self, callback, to=None, sender=None, subject=None, body=None):
    route = {'callback': callback}
    if to:      route['to'] = re.compile(to)
    if sender:  route['sender'] = re.compile(sender)
    if subject: route['subject'] = re.compile(subject)
    if body:    route['body'] = re.compile(body)
    self.routes.append(route)