import unittest

from parsers import Parser, GVSMS, GVVM
from tests.messages import sms1, sms2, vm

class TestGVParsers(unittest.TestCase):
  def test_sms_parser(self):
    self.assertEqual("What time is the show?\nI - can't remember", GVSMS(sms1).body)
    self.assertEqual("SMS from Mr. Ed", GVSMS(sms1).subject)
    self.assertEqual("Ok I will see you at 8", GVSMS(sms2).body)

  def test_vm_parser(self):
    self.assertEqual("Call me back. Bye.", GVVM(vm).body)
    self.assertEqual("Voicemail from Mr Wizard", GVVM(vm).subject)

if __name__ == '__main__':
  unittest.main()