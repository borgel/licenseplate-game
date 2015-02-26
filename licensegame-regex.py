#!/usr/bin/python

'''
asdasd
'''

import sys
import re

USAGE = ''': [XYZ 3 letter sequence to lookup]'''

def doLookup(letters):
   print 'regexing from the word list at ' + str(wordlist)
   wlist = open(wordlist, 'r')

   reg = re.compile('.*?' + letters[0] + '.*?' + letters[1] + '.*?' + letters[2] + '.*?')

   # for every line in the file, add it to the reference table (without newline)
   for w in wlist:
      # remove whitespace and newlines
      w = w.strip()

      found = reg.search(w)
      if found != None:
         #print found.span()
         #print found.group()
         print w

   wlist.close()

if len(sys.argv) < 2 or len(sys.argv) > 3:
   print str(sys.argv[0]) + USAGE
   exit(0)

# else we got a 3 letter combo to lookup
letters = sys.argv[2]
wordlist = sys.argv[1]
if len(letters) != 3:
   print 'You can only look up 3 letter combinations!'
   exit(1)

doLookup(letters)

