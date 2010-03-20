import unittest
from StringIO import StringIO

from google.appengine.api.mail import EmailMessage
import webob
from google.appengine.ext import webapp

import handlers
from tests.messages import *

ROUTED = {'to': [], 'sender': [], 'unmatched': []}

def request(body):
  environ = {
    'wsgi.input': StringIO(body),
    'CONTENT_LENGTH': len(body),
  }

  if body.rfind('Content-Disposition: form-data;') > 0:
    parts = body.split('\r\n')
    environ['REQUEST_METHOD'] = 'POST'
    environ['CONTENT_TYPE']   = 'multipart/form-data; boundary=%s' % parts[0][2:]

  return webob.Request(environ)

class MessageRouter(handlers.MessageRouter):
  def __init__(self):
    self.add_route(
      name      = 'to exact',
      to        = 'prowl@mail-utils.appspotmail.com',
      callback  = lambda m: ROUTED['to'].append(m)
    )

    self.add_route(
      name      = 'sender domain',
      sender    = '.*@txt.voice.google.com',
      callback  = lambda m: ROUTED['sender'].append(m)
    )

    self.add_route(
      name      = 'unmatched',
      to        = '.*',
      callback  = lambda m: ROUTED['unmatched'].append(m)
    )

class TestMessageRouter(unittest.TestCase):
  def setUp(self):
    globals()['ROUTED'] = {'to': [], 'sender': [], 'unmatched': []} # reset router results
    self.message_router = MessageRouter()

  def test_gv_sms(self):
    self.message_router.receive(EmailMessage(to='prowl@mail-utils.appspotmail.com',))
    self.message_router.receive(EmailMessage(sender='noreply@txt.voice.google.com',))
    self.message_router.receive(EmailMessage(to='nobody@mail-utils.appspotmail.com',))
    self.assertEqual(1, len(ROUTED['to']))
    self.assertEqual(1, len(ROUTED['sender']))

  def test_email_payloads(self):
    self.message_router.request = request(email)
    self.message_router.post()
    self.message_router.request = request(email_no_subj)
    self.message_router.post()
    self.assertEqual(2, len(ROUTED['unmatched']))

    self.assert_(hasattr(ROUTED['unmatched'][1], 'to'))
    self.assert_(hasattr(ROUTED['unmatched'][1], 'sender'))
    self.assert_(hasattr(ROUTED['unmatched'][1], 'subject'))
    self.assert_(hasattr(ROUTED['unmatched'][1], 'body'))

  def test_xmpp_payloads(self):
    self.message_router.request = request(xmpp)
    self.message_router.post()
    self.message_router.request = request(xmpp_no_body)
    self.message_router.post()
    self.assertEqual(2, len(ROUTED['unmatched']))

    self.assert_(hasattr(ROUTED['unmatched'][1], 'to'))
    self.assert_(hasattr(ROUTED['unmatched'][1], 'sender'))
    self.assert_(hasattr(ROUTED['unmatched'][1], 'subject'))
    self.assert_(hasattr(ROUTED['unmatched'][1], 'body'))

if __name__ == '__main__':
  unittest.main()