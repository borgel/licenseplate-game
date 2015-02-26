#!/usr/bin/env python

# uhh, make this not shit

import webapp2
import re

USAGE_MSG = '''
asd
'''

GITHUB_DICT = 'https://raw.githubusercontent.com/borgel/licenseplate-game/master/wordlist-nodupes-ascii.txt'

# do the actual game or whatever
class QueryHandler(webapp2.RequestHandler):
   def get(self, pattern):
      if(len(pattern) != 3):
         self.response.write("query wasn't 3 chars")
         return

      self.response.write("Searching for places with the ordered pattern: " + str(pattern))
      self.response.write("<br>")

      reg = re.compile('.*?' + pattern[0] + '.*?' + pattern[1] + '.*?' + pattern[2] + '.*?')

      # open file
      # for w in file
      # w = w.strip()
      # found = reg.search(w)
      # if found != None:
      #    #print found.span()
      #    #print found.group()
      #    print w
      wlist = open('dictionaries/dict.txt')

      hits = 0

      # for every line in the file, add it to the reference table (without newline)
      for w in wlist:
         # remove whitespace and newlines
         w = w.strip()

         found = reg.search(w)
         if found != None:
            self.response.write(w + '<br>')
            hits = hits + 1

      wlist.close()

      self.response.write('<br>')
      self.response.write('Found ' + str(hits) + ' matching words')
      self.response.write('<br>')

class MainHandler(webapp2.RequestHandler):
    def get(self):
       # TODO make this print a form to fill out to execute the search
        self.response.write(USAGE_MSG)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/search/(.*)', QueryHandler)
], debug=True)
