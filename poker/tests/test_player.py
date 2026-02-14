from poker.player import *

import unittest

class TestPlayer(unittest.TestCase):
    def test_player_init(self):
        p1 = Player("Joe")
        p2 = Player("John")
        p3 = Player("Joe")
        self.assertEqual(p1, p3)
        self.assertNotEqual(p1, p2)