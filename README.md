What?
=====
It plays the license plate game!

Modern California license plates are in the form #XYZ###. Where XYZ are letters and #'s are numbers.

The Game
--------
Find a word that uses the 3 letters in a given license plate, in order. Bonus points if they are sequential.

Usage
=====
1) Precomputed:
   - Generation:
   - Usage:

2) Tries: Do this... eventually...

Word List Format
================
TODO

The Method
----------
1) 2 Tries

2) Precompute a hashmap of all every 3 letter combo => all words that contain that combo in that order.
26*26*26 = 17,576 entries. Each combo is then a constant O(1) lookup.

Resources
=========
- Dictionary sourced from [http://wordlist.aspell.net/]. They provide a tarball with many more resources then we care about. To generate my test word list, all the files in final/ with the prefix 'american' were concatenated together. There's no reason more couldn't have been used.

To do this, I used this one-liner:
    find .|grep -v 'proper-names\|abbreviations'|xargs cat |strings|LC_ALL=C tr '[:upper:]' '[:lower:]'|LC_ALL=C sort|LC_ALL=C uniq - > all-nodupes.txt

This cats together all the files whose name doesn't include the two grepped-for strings, lowercasing them, removing any words with unicode, and de-duping. The nasty LC_ALL=c was to get (all those binaries) to parse unicode weirdness.

Using the 2014.11.17 tarball, I got a total of 643,417 words in 6.5MB. I'm sure there are still some dupes, but whatever. Good enough for now.


