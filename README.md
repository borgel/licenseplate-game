What?
=====
It plays the license plate game!

License plates are in the form #XYZ###. Where XYZ are letters and #'s are numbers.

The Game
--------
Find a word that uses the 3 letters in a given license plate, in order. Bonus points if they are sequential.

The Method
----------
1) 2 Tries

2) Precompute a hashmap of all every 3 letter combo => all words that contain that combo in that order.
26*26*26 = 17,576 entries
