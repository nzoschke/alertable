import re

class Parser(object):
  # attr => regex map; if attr exists on message, named regex matches are merged into object
  regexes = {
    'to':       r'$(?P<to>)^',      # copy attr over unchanged
    'sender':   r'$(?P<sender>)^',
    'subject':  r'$(?P<subject>)^',
    'body':     r'$(?P<body>)^',
  }
  
  def __init__(self, inbound_message):
    for attr_name in self.regexes:
      attr = unicode(getattr(inbound_message, attr_name))
      setattr(self, attr_name, attr)

      p = re.compile(self.regexes[attr_name], re.S)
      match = p.match(attr)
      if not match:
        continue

      for name in match.groupdict():
        setattr(self, name, match.groupdict()[name].strip())

class GVSMS(Parser):
  regexes = {
    'body':     r'(From[^\n]+)?(?P<body>.*?)(\n\n--.*)?$',  # Strip off `From nobody...` and GV SMS signature if present
    'subject':  r'^(?P<subject>.*) \[',                     # Strip off [phone number]
  }

class GVVM(Parser):
  regexes = {
    'body':     r'.*Transcript: (?P<body>.*)Play',          # extract part between `Trascript:` and `Play message:`
    'subject':  r'^New (?P<subject>.*) at',                 # Strip off time
  }

  def __init__(self, inbound_message):
    super(GVVM, self).__init__(inbound_message)
    self.subject = self.subject[0].upper() + self.subject[1:] # capitalize first letter
