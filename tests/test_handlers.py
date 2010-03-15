import unittest
from google.appengine.api.mail import EmailMessage
import handlers

ROUTED = {'to': [], 'sender': []}

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

class TestMessageRouter(unittest.TestCase):
  def setUp(self):
    self.message_router = MessageRouter()

  def test_gv_sms(self):
    self.message_router.receive(EmailMessage(to='prowl@mail-utils.appspotmail.com',))
    self.message_router.receive(EmailMessage(sender='noreply@txt.voice.google.com',))
    self.message_router.receive(EmailMessage(to='nobody@mail-utils.appspotmail.com',))
    self.assertEqual(1, len(ROUTED['to']))
    self.assertEqual(1, len(ROUTED['sender']))

if __name__ == '__main__':
  unittest.main()