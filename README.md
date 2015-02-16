# countdown
Simple scripts for generating games from Countdown (Letters &amp; Numbers in Australia).

These are intended to be very simple scripts used for a niche purpose. Flexibility is sacrificed for simplicity, meaning that significant rule changes are intended to be implemented by changing the code rather than the parameters.

## Numbers

cd-numbers.py randomly generates six numbers to be combined together using addition, subtraction, multiplication or integer division to make a randomly generated three digit target, as per the rules on Countdown.

The user has a choice of the small/large number ratio. This is specified by entering the number of large numbers desired. The number of small numbers is then calculated by the fact that there must be six numbers.

Sample Usage:

(Yet to come)

## Letters

cd-letters.py randomly generates nine letters. The goal of the player is to find the largest word from the letters generated (using each generated letter at most once).

The user can choose the ratio of vowels to consonants, subject to the restrictions imposed by Countdown. The algorithm here works as specified on the Countdown wikipedia page, however it still does not produce results that seem as good as actual Countdown. A more refined algorithm would be required to achieve better results.

Sample Usage:

(Yet to come)
