import base64
import httplib
import logging
import urllib
import settings

class Prowl(object):
  HOST = 'prowl.weks.net'
  
  @classmethod
  def add(cls, application, event, description='', priority=0):
    """Send a notification using the Prowl API"""
    data = urllib.urlencode({
      'apikey': settings.PROWL_API_KEY, 
      'application': application, 
      'event': event,
      'description': description,
      'priority': priority, 
    })

    headers = {
      'Content-type': 'application/x-www-form-urlencoded',
      'User-Agent': 'httplib',
    }

    conn = httplib.HTTPSConnection(cls.HOST)
    conn.request('POST', '/publicapi/add', data, headers)
    response = conn.getresponse()
    data = response.read()

    return ('success' in data)

class GoogleVoice(object):
  HOST = 'clients4.google.com'
  PATH = '/voice/embed/webButtonConnect'
  
  @classmethod
  def connect(cls, caller_number):
    """Connect a phone call using a Google Voice Widget"""
    data = urllib.urlencode({
      'buttonId': settings.GOOGLE_VOICE_BUTTON_ID,
      'callerNumber': caller_number,
      'showCallerNumber': 1,
      'name': 'h'
    })

    headers = {
      'Content-type': 'application/x-www-form-urlencoded',
      'User-Agent': 'httplib',
    }

    conn = httplib.HTTPSConnection(cls.HOST)
    conn.request('POST', cls.PATH, data, headers)
    response = conn.getresponse()
    data = response.read()

    return ('ok=true' in data)

class Campfire(object):
  HOST = 'campfirenow.com'
  
  @classmethod
  def speak(cls, subdomain, room_id, body):
    data = '<message><body>%s</body></message>' % body
    
    headers = {
      'Content-type': 'application/xml',
      'Authorization': "Basic " + base64.b64encode(settings.CAMPFIRE_API_TOKEN + ':x')
    }
    
    host = '%s.%s' % (subdomain, cls.HOST)
    path = '/room/%s/speak.xml' % room_id
    conn = httplib.HTTPSConnection(host)
    conn.request('POST', path, data, headers)
    response = conn.getresponse()
    data = response.read()
    
    return ('message' in data)
