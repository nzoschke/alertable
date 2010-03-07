import sys
sys.path.append('/Applications/GoogleAppEngineLauncher.app/Contents/Resources/GoogleAppEngine-default.bundle/Contents/Resources/google_appengine/')
sys.path.append('/Applications/GoogleAppEngineLauncher.app/Contents/Resources/GoogleAppEngine-default.bundle/Contents/Resources/google_appengine/lib/webob/')

import logging
import unittest

from google.appengine.api.mail import EmailMessage, InboundEmailMessage

from handlers import MailRouter
from rpc import Logger

class TestEmailMessage(object):
  def __init__(self, to='', sender='', subject='', body=''):
    self.to = to
    self.sender = sender
    self.subject = subject
    self.body = body

class TestMailRouter(unittest.TestCase):
  def setUp(self):
    logging.basicConfig(level=logging.DEBUG) # show all logging on STDOUT
    self.mail_router = MailRouter()

  def tearDown(self):
    pass

  def test_gv_sms(self):
    message = TestEmailMessage(sender='noreply@txt.voice.google.com',)
    self.mail_router.receive(message)

if __name__ == '__main__':
  unittest.main()