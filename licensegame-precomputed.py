#!/usr/bin/python

'''
asdasd

TODO add wordlength macro at top for configuration
'''

import sqlite3
import sys
from collections import defaultdict


USAGE = ''': [-c WORDLIST.txt to create the reference table from the wordlist] [XYZ 3 letter sequence to lookup]'''
STORAGE_FILE = "LicenseLookupTable.db"
SQL_TABLE_NAME = "words"
SQL_TABLE_CREATE = '''CREATE TABLE ''' + SQL_TABLE_NAME + ''' (tlc text, word text)'''

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
   print 'building table from the word list at ' + str(wordlist)
   wlist = open(wordlist, 'r')

   # truncate results DB
   f = open(STORAGE_FILE, 'w')
   f.truncate()
   f.close()

   # open connection to results DB to write results to
   conn = sqlite3.connect(STORAGE_FILE)
   c = conn.cursor()

   # create table
   c.execute(SQL_TABLE_CREATE)

   # for every line in the file, add it to the reference table (without newline)
   for w in wlist:
      # remove whitespace and newlines
      w = w.strip()

      kvs = set()

      # if the word is less than the shortest combo len, dont bother adding it
      if len(w) < 3:
         continue

      # iterate through all 3 letter combos in this word
      g = letterCombos(w)
      for combo in g:
         kvs.add((combo, w))

      # insert or replace combo:w in the DB
      #print 'adding: ' + str(kvs)
      c.executemany("INSERT OR REPLACE INTO " + SQL_TABLE_NAME + " VALUES(?,?)", kvs)

   wlist.close()

   #print 'Combo dictionary has a total of ' + str(len(comboDict)) + ' prefixes'

   conn.commit()
   conn.close()

def doLookup(letters):
   print 'looking up words for ' + str(letters)

   conn = sqlite3.connect(STORAGE_FILE)
   c = conn.cursor()

   # do an SQL lookup for all words with this prefix
   #for row in c.execute("SELECT * FROM " + SQL_TABLE_NAME + " WHERE tlc = '%s'" % letters):
   for row in c.execute("SELECT * FROM " + SQL_TABLE_NAME + " WHERE tlc = '%s' ORDER BY LENGTH(word)"  % letters):
      print row[1]

   conn.close()

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
