import unittest
from google.appengine.api.mail import EmailMessage
from handlers import MailRouter

ROUTED = {'to': [], 'sender': []}

class MyMailRouter(MailRouter):
  def __init__(self):
    self.add_route(
      to        = 'prowl@mail-utils.appspotmail.com',
      callback  = lambda m: ROUTED['to'].append(m)
    )

    self.add_route(
      sender    = '.*@txt.voice.google.com',
      callback  = lambda m: ROUTED['sender'].append(m)
    )

class TestMailRouter(unittest.TestCase):
  def setUp(self):
    self.mail_router = MyMailRouter()

  def test_gv_sms(self):
    self.mail_router.receive(EmailMessage(to='prowl@mail-utils.appspotmail.com',))
    self.mail_router.receive(EmailMessage(sender='noreply@txt.voice.google.com',))
    self.assertEqual(1, len(ROUTED['to']))
    self.assertEqual(1, len(ROUTED['sender']))

if __name__ == '__main__':
  unittest.main()