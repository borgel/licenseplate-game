#!/usr/bin/python

'''
asdasd
'''


class LookupDictionary:
   # holds one node of our trie
   # Each trie of the trie is a node with a dict of 26 nodes
   class Node:
      def __init__(self, letter):
         self.letter = letter
         self.parent = None
         self.children = {}

      def addChild(self, child):
         child.parent = self
         self.children[child.letter] = child

   def __init__(self):
      # the root of the storage trie
      self.storageTrie = self.Node("");

      # the root of our cross trie. It is a trie of lists of Node pointers for a given letter
      self.crossTrie = {}

   def addWord(self, word):
      # TODO store in trie
      # TODO add a pointer to each letter node to the cross trie
      print "adding " + word
      # traverse the trie, adding each node manually? or can we recursively do that?

      curNode = self.storageTrie
      while len(word) > 0:
         print "word = " + str(word)
         # get the 0th letter to key off
         letter = word[0:1]

         # if that letter doesnt exist, do this
         if letter not in curNode.children:
            print '\tnot in'
            curNode.children[letter] = self.Node(letter)

         curNode = curNode.children[letter]
         word = word[1:]


   def findCombo(self, letters):
      # TODO do the lookup...
      print "finding " + str(list(letters)) + " starting with " + letters[-1:]


print 'starting'

# init the dictionary
licDict = LookupDictionary()

# mode 1, add to the dictionary
licDict.addWord("apple")
licDict.addWord("application")
licDict.addWord("ass")
licDict.addWord("berry")
licDict.addWord("pie")

# TODO traverse entire dict trie to see how it looks
print licDict.storageTrie.children
for n in licDict.storageTrie.children.values():
   print str(n) + str(n.letter)
   for nn in n.children.values():
      print "\t" + str(nn) + str(n.letter)

print "\n"
# mode 2, look for words with the triplet
licDict.findCombo("lig")
