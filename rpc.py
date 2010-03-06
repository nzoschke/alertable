import httplib
import logging
import urllib

import settings

class Logger(object):
  messages = []
  
  @classmethod
  def log(cls, message):
    cls.messages.append(message)
    logging.info(message)
    
class Prowl(object):
  HOST = 'prowl.weks.net'
  
  @classmethod
  def add(cls, application, event, description=None, priority=0):
    """Send a notification using the Prowl API"""
    data = urllib.urlencode({
      'apikey': settings.PROWL_API_KEY, 
      'application': application, 
      'event': event,
      'description': description or '',
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