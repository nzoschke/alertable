import logging
import re

from google.appengine.api import xmpp, mail
from google.appengine.ext import webapp

class XMPPMessage(xmpp.Message):
  """
  XMPP Message acts more like an EmailMessage
  """
  subject = ''

class MessageRouter(webapp.RequestHandler):
  routes = []

  def __init__(self):
    self.add_route(
      name      = 'log',
      to        = '.*',
      callback  = lambda m: logging.info('NO ROUTE\nSender: %s\nTo: %s\nSubject: %s\nBody: %s' % (m.sender, m.to, m.subject, repr(unicode(m.body)))) # default route for debugging/testing
    )

  def receive(self, inbound_message):
    for route in self.routes:
      logging.debug('Trying Route `%s`' % route['name'])
      match = False
      for attr_name in route:
        if not hasattr(inbound_message, attr_name):
          continue
        attr = unicode(getattr(inbound_message, attr_name))

        match = bool(route[attr_name].match(attr))
        logging.debug('self.%s: %s =~ %s => %s' % (attr_name, repr(attr), route[attr_name].pattern, match))
        if not match:
          break

      logging.debug('%s %s(inbound_message)' % (match and 'Calling' or 'Skipping', route['callback'].func_name))
      if match:
        route['callback'](inbound_message)
        return True

  def post(self):
    # assume Email message first
    inbound_message = mail.InboundEmailMessage(self.request.body)

    # prefer text body over html body
    bodies = [b.decode() for (c, b) in inbound_message.bodies('text/plain')] + [b.decode() for (c, b) in inbound_message.bodies('text/html')]
    if bodies:
      inbound_message.body = bodies[0]

    # if no sender, re-interpret as XMPP message
    if not hasattr(inbound_message, 'sender'):
      inbound_message = XMPPMessage(self.request.POST)
    self.receive(inbound_message)

  def add_route(self, callback, name=None, to=None, sender=None, subject=None, body=None):
    route = {'callback': callback}
    route['name'] = name or callback.func_name # only used for logging / debugging purposes
    if to:      route['to'] = re.compile(to)
    if sender:  route['sender'] = re.compile(sender)
    if subject: route['subject'] = re.compile(subject)
    if body:    route['body'] = re.compile(body)
    self.routes.append(route)