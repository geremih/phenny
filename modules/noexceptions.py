#!/usr/bin/python3
"""
botfun.py - activities that bots do
author: mutantmonkey <mutantmonkey@mutantmonkey.in>
"""

def noexceptions(phenny, input):
   """Tells someone there aren't ever any exceptions"""
   #whouser = input.groups()[1]
   whouser = input.nick
   if not whouser:
      return phenny.say('NO EXCEPTIONS!')

   response = "NO EXCEPTIONS, %s!"
   phenny.say(response % whouser)

#noexceptions.commands = ['noexceptions']
#noexceptions.example = '.noexceptions firespeaker'
noexceptions.rule = r'.*(?i)(no exceptions).*$'
noexceptions.priority = 'low'

def harglebargle(phenny, input):
   """Tells someone hargle bargle (cf. http://nedroidcomics.livejournal.com/224029.html , http://quotes.firespeaker.org/?id=1415)"""
   whouser = input.groups()[1]
   if not whouser:
      return phenny.say('HARGLE BARGLE!')
   response = "HARGLE BARGLE, %s!"
   phenny.say(response % whouser)

harglebargle.commands = ['harglebargle']
harglebargle.example = '.harglebargle firespeaker'
harglebargle.priority = 'low'

if __name__ == '__main__':
   print(__doc__.strip())

def udmurt(phenny, input):
   """expresses joy over mention of Udmurt"""
   phenny.say("\o/ \o/ \o/ U D M U R T \o/ \o/ \o/")

udmurt.rule = r'.*(?i)(udmurt).*$'
udmurt.priority = 'low'
