GAE Messaging Utils - Messaging (Email and XMPP) sending, receiving, routing and callbacks for Google App Engine
========================================================

git clone git://github.com/nzoschke/gae-message-utils.git

Create a `settings.py` file with your personal API tokens and routing rules:

    from handlers import MailRouter
    from parsers import GVSMS, GVVM
    from rpc import Prowl, GoogleVoice

    PROWL_API_KEY          = 'SECRET'
    GOOGLE_VOICE_BUTTON_ID = 'SECRET'

    class MailRouter(MailRouter):
      def __init__(self):
        # specific SMS sources sent to prowl with static sender and higher priority
        self.add_route(
          name      = 'Important SMS',
          sender    = '.*txt.voice.google.com',
          subject   = '.*ALERT', # from automatic pager system
          callback  = lambda m: Prowl.add(application='GV', event='New SMS Alert', priority=2)
        )
        
        # generic SMS prowl notifications with sender and message from SMS
        self.add_route(
          name      = 'SMS',
          sender    = '.*txt.voice.google.com',
          callback  = lambda m: Prowl.add(application='GV', event=GVSMS(m).subject, description=GVSMS(m).body)
        )
        
        # generic Voicemail prowl notifications with sender and transcription from VM
        self.add_route(
          name      = 'Voicemail',
          sender    = '.*voice-noreply@google.com',
          callback  = lambda m: Prowl.add(application='GV', event=GVVM(m).subject, description=GVVM(m).body)
        )
        
        # email notifications from Google Calendar connect a phone call
        self.add_route(
          name      = 'Stand Up Notification',
          sender    = '.*calendar-notification@google.com',
          body      = 'Stand Up',
          callback  = lambda m: GoogleVoice.connect('15551212')
        )
        
        super(MailRouter, self).__init__() # add default route
  