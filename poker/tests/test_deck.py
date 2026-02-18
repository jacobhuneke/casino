import unittest
from poker.deck import *

class TestDeck(unittest.TestCase):
    def test_deck_size(self):
        deck = Deck()
        self.assertEqual(52, deck.deck_size())

    def test_deck_init(self):
        deck = Deck()
        self.assertEqual("Ace of Clubs", deck.cards[0].__repr__())

    def test_remove_card(self):
        deck = Deck()
        card = Card(Rank.QUEEN, Suit.HEARTS)
        deck.remove_card(card)
        self.assertEqual(deck.deck_size(), 51)

    def test_remove_multiple_cards(self):
        deck = Deck()
        card1 = Card(Rank.QUEEN, Suit.HEARTS)
        card2 = Card(Rank.QUEEN, Suit.SPADES)
        card3 = Card(Rank.QUEEN, Suit.DIAMONDS)
        card4 = Card(Rank.QUEEN, Suit.CLUBS)
        deck.remove_card(card1)
        deck.remove_card(card2)
        deck.remove_card(card3)
        self.assertEqual(deck.deck_size(), 49)
        self.assertEqual(card4 in deck.cards, True)
        self.assertEqual(card1 in deck.cards, False)

    def test_shuffle(self):
        deck = Deck()
        card_list = deck.cards.copy()
        deck.shuffle_deck()
        self.assertNotEqual(card_list[0], deck.cards[0])
        
    def test_add_card(self):
        deck = Deck()
        card1 = Card(Rank.QUEEN, Suit.HEARTS)
        card2 = Card(Rank.QUEEN, Suit.SPADES)
        deck.remove_card(card1)
        deck.remove_card(card2)
        
        self.assertNotEqual(card1 in deck.cards, True)
        self.assertEqual(deck.deck_size(), 50)
        deck.add_card(card1)
        self.assertEqual(card1 in deck.cards, True)

    def test_add_same_card(self):
        deck = Deck()
        card1 = Card(Rank.QUEEN, Suit.HEARTS)
        with self.assertRaises(Exception):
            deck.add_card(card1)

    def test_get_card_empty_deck(self):
        deck = Deck()
        deck.cards = []
        with self.assertRaises(Exception):
            deck.deal_card()

if __name__ == "__main__":
    unittest.main()