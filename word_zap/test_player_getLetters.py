"""
Do Not Edit this file. You may and are encouraged to look at it for reference.
"""

import sys
if sys.version_info.major != 3:
    print('You must use Python 3.x version to run this unit test')
    sys.exit(1)

import unittest

import player

class TestPlayerGetLetters(unittest.TestCase):
    def test001_getNameExists(self):
        self.assertTrue('getLetters' in dir(player.Player),
            'Function "getLetters" is not defined, check your spelling')

    def test002_getLettersReturnsList(self):
        from player import Player
        p = Player('Luke')
        letters = p.getLetters()
        self.assertTrue(isinstance(letters, list), "You should have returned a list")

if __name__ == '__main__':
    unittest.main()
