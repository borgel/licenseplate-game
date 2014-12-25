#!/usr/bin/python

'''
asdasd

TODO add wordlength macro at top for configuration
'''

import pickle
import sys
from collections import defaultdict



USAGE = ''': [-c WORDLIST.txt to create the reference table from the wordlist] [XYZ 3 letter sequence to lookup]'''
PICKLE_FILE = "LicenseLookupTable.pickle"


# print all ordered 3 letter combos in this word
# run 3 indicies across the word until all reach the end
def letterCombos(word):
   a = 0
   b = a + 1
   c = b + 1
   while a < len(word):
      yield(word[a] + word[b] + word[c])

      c += 1
      if c == len(word):
         b += 1

         if b == len(word) - 1:
            a += 1

            if a == len(word) - 2:
               return

            b = a + 1

         c = b + 1


def computeDict(wordlist):
   # we want a dictionary of lists
   # somehow, if we make this a dict of sets it's SIGNIFICANTLY slower
   comboDict = defaultdict(list)

   print 'building table from ' + str(wordlist)
   wlist = open(wordlist, 'r')

   # for every line in the file, add it to the reference table (without newline)
   for w in wlist:
      # remove whitespace and newlines
      w = w.strip()

      # if the word is less than the shortest combo len, dont bother adding it
      if len(w) < 3:
         continue

      # iterate through all 3 letter combos in this word
      g = letterCombos(w)
      for combo in g:
         # FIXME TODO dont insert dupe words in the list. should they be sets?
         # or convert to set then to list?
         # or afterwards go through all lists and list(set()) them?
         comboDict[combo].append(w)

   wlist.close()

   # de-dupe each list of words
   for k in comboDict.keys():
      comboDict[k] = list(set(comboDict[k]))

   print 'Combo dictionary has a total of ' + str(len(comboDict)) + ' prefixes'

   # pickle out map to local dir
   f = open(PICKLE_FILE, 'w')
   pickle.dump(comboDict, f)
   f.close()

def doLookup(letters):
   print 'looking up words for ' + str(letters)

   # try to open our pickle file
   f = open(PICKLE_FILE, 'r')
   comboDict = pickle.load(f)
   f.close()

   for word in comboDict[letters]:
      print word

if len(sys.argv) < 2 or len(sys.argv) > 3:
   print str(sys.argv[0]) + USAGE
   exit(0)

if sys.argv[1] == '-c':
   computeDict(sys.argv[2])
   exit(0)

# else we got a 3 letter combo to lookup
letters = sys.argv[1]
if len(letters) != 3:
   print 'You can only look up 3 letter combinations!'
   exit(1)

doLookup(letters)
