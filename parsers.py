import logging
import re
import pdb

class Parser(object):
  regexes = {
    'body':     '$^',
    'subject':  '$^',
  }
  
  def __init__(self, inbound_message):
    for attr_name in ('to', 'sender', 'subject', 'body'):
      # parse field, and set to match if applicable
      attr = unicode(getattr(inbound_message, attr_name))
      setattr(self, attr_name, attr)
      #print "self.%s = %s" % (attr_name, attr)
      
      if self.regexes.has_key(attr_name):
        p = re.compile(self.regexes[attr_name], re.S)
        match = p.match(attr)
        if not match:
          continue

        for name in match.groupdict():
          setattr(self, name, match.groupdict()[name].strip())
          #print "self.%s = %s" % (name, match.groupdict()[name].strip())

class GVSMS(Parser):
  regexes = {
    'body':     r'(From[^\n]+)?(?P<body>.*?)(\n\n--.*)?$', # Strip off `From nobody...` and GV SMS signature if present
    'subject':  r'^(?P<subject>.*) \[',
  }

class GVVM(Parser):
  regexes = {
    'body':     '.*Transcript: (?P<body>.*)Play',  # extract part between Trascript: and Play message: text
    'subject':  r'^New (?P<subject>.*) at',
  }
  
  def __init__(self, inbound_message):
    super(GVVM, self).__init__(inbound_message)
    self.subject = self.subject[0].upper() + self.subject[1:] # capitalize first letter
