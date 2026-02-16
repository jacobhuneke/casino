from poker.player import *
from poker.poker_game import *
import unittest

class TestPlayer(unittest.TestCase):
    def test_player_init(self):
        p1 = Player("Joe")
        p2 = Player("John")
        p3 = Player("Joe")
        self.assertEqual(p1, p3)
        self.assertNotEqual(p1, p2)
    
    def test_hole_no_cards(self):
        p1 = Player("Joe")
        self.assertEqual(p1.get_hole(), [])
    
    def test_hole_with_cards(self):
        deck = Deck()
        p1 = Player("Joe")
        deck.shuffle_deck()
        p1.add_card(deck.deal_card())
        p1.add_card(deck.deal_card())
        with self.assertRaises(Exception):
            p1.add_card(deck.deal_card())

    def test_get_hand_rank(self):
        p1 = Player("Jake")
        self.assertEqual(p1.get_hand_rank(), PokerRank.HIGH_CARD)

    def test_score_combo(self):
        p1 = Player("Jake")
        p2 = Player("Lainey")
        game = PokerGame(p1, p2)
        game.deal_player_cards()
        game.deal_flop()
        #print(p1.score_hand())
    
    def test_flush(self):
        c1 = Card(Rank.ACE, Suit.CLUBS)
        c2 = Card(Rank.EIGHT, Suit.CLUBS)
        c3 = Card(Rank.FIVE, Suit.CLUBS)
        c4 = Card(Rank.JACK, Suit.CLUBS)
        c5 = Card(Rank.QUEEN, Suit.CLUBS)
        combo = [c1, c2, c3, c4, c5]
        self.assertEqual(score_combo(combo), PokerRank.FLUSH)

    def test_no_flush(self):
        c1 = Card(Rank.ACE, Suit.CLUBS)
        c2 = Card(Rank.EIGHT, Suit.CLUBS)
        c3 = Card(Rank.FIVE, Suit.CLUBS)
        c4 = Card(Rank.JACK, Suit.DIAMONDS)
        c5 = Card(Rank.QUEEN, Suit.CLUBS)
        combo = [c1, c2, c3, c4, c5]
        self.assertNotEqual(score_combo(combo), PokerRank.FLUSH)

    def test_straight_flush_low_ace(self):
        c1 = Card(Rank.ACE, Suit.CLUBS)
        c2 = Card(Rank.TWO, Suit.CLUBS)
        c3 = Card(Rank.FIVE, Suit.CLUBS)
        c4 = Card(Rank.FOUR, Suit.CLUBS)
        c5 = Card(Rank.THREE, Suit.CLUBS)
        combo = [c1, c2, c3, c4, c5]
        self.assertEqual(score_combo(combo), PokerRank.STRAIGHT_FLUSH)
    
    def test_straight_low_ace(self):
        c1 = Card(Rank.ACE, Suit.CLUBS)
        c2 = Card(Rank.TWO, Suit.CLUBS)
        c3 = Card(Rank.FIVE, Suit.CLUBS)
        c4 = Card(Rank.FOUR, Suit.CLUBS)
        c5 = Card(Rank.THREE, Suit.HEARTS)
        combo = [c1, c2, c3, c4, c5]
        self.assertEqual(score_combo(combo), PokerRank.STRAIGHT)

    def test_straight_middle(self):
        c1 = Card(Rank.SEVEN, Suit.CLUBS)
        c2 = Card(Rank.EIGHT, Suit.DIAMONDS)
        c3 = Card(Rank.FIVE, Suit.CLUBS)
        c4 = Card(Rank.FOUR, Suit.CLUBS)
        c5 = Card(Rank.SIX, Suit.HEARTS)
        combo = [c1, c2, c3, c4, c5]
        self.assertEqual(score_combo(combo), PokerRank.STRAIGHT)

    def test_straight_high(self):
        c1 = Card(Rank.ACE, Suit.CLUBS)
        c2 = Card(Rank.JACK, Suit.DIAMONDS)
        c3 = Card(Rank.TEN, Suit.CLUBS)
        c4 = Card(Rank.KING, Suit.CLUBS)
        c5 = Card(Rank.QUEEN, Suit.HEARTS)
        combo = [c1, c2, c3, c4, c5]
        self.assertEqual(score_combo(combo), PokerRank.STRAIGHT)

    def test_straight_high_nroyal(self):
        c1 = Card(Rank.ACE, Suit.CLUBS)
        c2 = Card(Rank.JACK, Suit.DIAMONDS)
        c3 = Card(Rank.TEN, Suit.CLUBS)
        c4 = Card(Rank.KING, Suit.CLUBS)
        c5 = Card(Rank.QUEEN, Suit.HEARTS)
        combo = [c1, c2, c3, c4, c5]
        self.assertNotEqual(score_combo(combo), PokerRank.ROYAL_FLUSH)

    def test_royal_flush(self):
        c1 = Card(Rank.ACE, Suit.CLUBS)
        c2 = Card(Rank.JACK, Suit.CLUBS)
        c3 = Card(Rank.TEN, Suit.CLUBS)
        c4 = Card(Rank.KING, Suit.CLUBS)
        c5 = Card(Rank.QUEEN, Suit.CLUBS)
        combo = [c1, c2, c3, c4, c5]
        self.assertEqual(score_combo(combo), PokerRank.ROYAL_FLUSH)

    def test_full_house(self):
        c1 = Card(Rank.TEN, Suit.CLUBS)
        c2 = Card(Rank.TEN, Suit.DIAMONDS)
        c3 = Card(Rank.TEN, Suit.SPADES)
        c4 = Card(Rank.THREE, Suit.CLUBS)
        c5 = Card(Rank.THREE, Suit.HEARTS)
        combo = [c1, c2, c3, c4, c5]
        self.assertEqual(score_combo(combo), PokerRank.FULL_HOUSE)
    
    def test_three_ofa_kind(self):
        c1 = Card(Rank.TEN, Suit.CLUBS)
        c2 = Card(Rank.TEN, Suit.DIAMONDS)
        c3 = Card(Rank.TEN, Suit.SPADES)
        c4 = Card(Rank.FOUR, Suit.CLUBS)
        c5 = Card(Rank.THREE, Suit.HEARTS)
        combo = [c1, c2, c3, c4, c5]
        self.assertEqual(score_combo(combo), PokerRank.THREE_OF_A_KIND)
    
    def test_two_pair(self):
        c1 = Card(Rank.TEN, Suit.CLUBS)
        c2 = Card(Rank.TEN, Suit.DIAMONDS)
        c3 = Card(Rank.NINE, Suit.SPADES)
        c4 = Card(Rank.THREE, Suit.CLUBS)
        c5 = Card(Rank.THREE, Suit.HEARTS)
        combo = [c1, c2, c3, c4, c5]
        self.assertEqual(score_combo(combo), PokerRank.TWO_PAIR)

    def test_one_pair(self):
        c1 = Card(Rank.EIGHT, Suit.CLUBS)
        c2 = Card(Rank.TEN, Suit.DIAMONDS)
        c3 = Card(Rank.SEVEN, Suit.SPADES)
        c4 = Card(Rank.THREE, Suit.CLUBS)
        c5 = Card(Rank.THREE, Suit.HEARTS)
        combo = [c1, c2, c3, c4, c5]
        self.assertEqual(score_combo(combo), PokerRank.ONE_PAIR)

    def test_high_card(self):
        c1 = Card(Rank.EIGHT, Suit.CLUBS)
        c2 = Card(Rank.TEN, Suit.DIAMONDS)
        c3 = Card(Rank.SEVEN, Suit.SPADES)
        c4 = Card(Rank.THREE, Suit.CLUBS)
        c5 = Card(Rank.TWO, Suit.HEARTS)
        combo = [c1, c2, c3, c4, c5]
        self.assertEqual(score_combo(combo), PokerRank.HIGH_CARD)

    def test_four_ofa_kind(self):
        c1 = Card(Rank.TEN, Suit.CLUBS)
        c2 = Card(Rank.TEN, Suit.DIAMONDS)
        c3 = Card(Rank.TEN, Suit.SPADES)
        c4 = Card(Rank.FOUR, Suit.CLUBS)
        c5 = Card(Rank.TEN, Suit.HEARTS)
        combo = [c1, c2, c3, c4, c5]
        self.assertEqual(score_combo(combo), PokerRank.FOUR_OF_A_KIND)