"""
Do Not Edit this file. You may and are encouraged to look at it for reference.
"""

import sys
if sys.version_info.major != 3:
    print('You must use Python 3.x version to run this unit test')
    sys.exit(1)

import unittest

import player

class TestPlayerPrintLetters(unittest.TestCase):
    def test001_exists(self):
        self.assertTrue('printLetters' in dir(player.Player),
            'Function "printLetters" is not defined, check your spelling')

    def test002_returnsString(self):
        from player import Player
        p = Player('Luke')
        letters = p.getLetters()
        self.assertEqual(len(letters), 7,
            "The player should start out with 7 letters, update the constructor to give the player 7 random letters")
        printletters = p.printLetters()
        self.assertTrue(isinstance(printletters, str), 'You should return a string')
        self.assertEqual(len(printletters), 13, 'Your string should have a space between each letter')

    def test003_returnsString(self):
        from player import Player
        p = Player('Luke')
        p.drawLetter()
        letters = p.getLetters()
        self.assertEqual(len(letters), 8,
            "The player should have 8 letters after being forced to draw an extra letter.")
        printletters = p.printLetters()
        self.assertTrue(isinstance(printletters, str), 'You should return a string')
        self.assertEqual(len(printletters), 15, 'Your string should have a space between each letter')

    def test004_returnsString(self):
        from player import Player
        from random import randint
        p = Player('Luke')
        r = randint(1, 10)
        for _ in range(r):
            p.drawLetter()
        letters = p.getLetters()
        self.assertEqual(len(letters), 7 + r,
            "The player should have %s letters after being forced to draw (%s) extra letter(s)." % (7+r, r))
        printletters = p.printLetters()
        self.assertTrue(isinstance(printletters, str), 'You should return a string')
        self.assertEqual(len(printletters), 13 + r * 2, 'Your string should have a space between each letter')

if __name__ == '__main__':
    unittest.main()
