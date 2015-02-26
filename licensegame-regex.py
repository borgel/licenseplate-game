#!/usr/bin/python

'''
asdasd
'''

import sys


USAGE = ''': [XYZ 3 letter sequence to lookup]'''

def doLookup(letters):
   print 'building table from the word list at ' + str(wordlist)
   wlist = open(wordlist, 'r')

   # for every line in the file, add it to the reference table (without newline)
   for w in wlist:
      # remove whitespace and newlines
      w = w.strip()

      #TODO FIXME run regex on w

   wlist.close()

if len(sys.argv) < 2 or len(sys.argv) > 3:
   print str(sys.argv[0]) + USAGE
   exit(0)

# else we got a 3 letter combo to lookup
letters = sys.argv[1]
if len(letters) != 3:
   print 'You can only look up 3 letter combinations!'
   exit(1)


#FIXME TODO build regex

doLookup(letters)

