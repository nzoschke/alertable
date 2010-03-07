import sys
sys.path.append('/Applications/GoogleAppEngineLauncher.app/Contents/Resources/GoogleAppEngine-default.bundle/Contents/Resources/google_appengine/')
sys.path.append('/Applications/GoogleAppEngineLauncher.app/Contents/Resources/GoogleAppEngine-default.bundle/Contents/Resources/google_appengine/lib/webob/')

import unittest
from tests.test_parsers import TestGVParsers
from tests.test_handlers import TestMailRouter

if __name__ == '__main__':
  unittest.main()
