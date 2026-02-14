import unittest
from poker.deck import *

class TestDeck(unittest.TestCase):
    def test_deck_size(self):
        deck = Deck()
        self.assertEqual(52, deck.deck_size())

    def test_deck_init(self):
        deck = Deck()
        deck_str = "Rank.TWO of Suit.DIAMONDS, Rank.THREE of Suit.DIAMONDS, Rank.FOUR of Suit.DIAMONDS, Rank.FIVE of Suit.DIAMONDS, Rank.SIX of Suit.DIAMONDS, Rank.SEVEN of Suit.DIAMONDS, Rank.EIGHT of Suit.DIAMONDS, Rank.NINE of Suit.DIAMONDS, Rank.TEN of Suit.DIAMONDS, Rank.JACK of Suit.DIAMONDS, Rank.QUEEN of Suit.DIAMONDS, Rank.KING of Suit.DIAMONDS, Rank.ACE of Suit.DIAMONDS, Rank.TWO of Suit.CLUBS, Rank.THREE of Suit.CLUBS, Rank.FOUR of Suit.CLUBS, Rank.FIVE of Suit.CLUBS, Rank.SIX of Suit.CLUBS, Rank.SEVEN of Suit.CLUBS, Rank.EIGHT of Suit.CLUBS, Rank.NINE of Suit.CLUBS, Rank.TEN of Suit.CLUBS, Rank.JACK of Suit.CLUBS, Rank.QUEEN of Suit.CLUBS, Rank.KING of Suit.CLUBS, Rank.ACE of Suit.CLUBS, Rank.TWO of Suit.HEARTS, Rank.THREE of Suit.HEARTS, Rank.FOUR of Suit.HEARTS, Rank.FIVE of Suit.HEARTS, Rank.SIX of Suit.HEARTS, Rank.SEVEN of Suit.HEARTS, Rank.EIGHT of Suit.HEARTS, Rank.NINE of Suit.HEARTS, Rank.TEN of Suit.HEARTS, Rank.JACK of Suit.HEARTS, Rank.QUEEN of Suit.HEARTS, Rank.KING of Suit.HEARTS, Rank.ACE of Suit.HEARTS, Rank.TWO of Suit.SPADES, Rank.THREE of Suit.SPADES, Rank.FOUR of Suit.SPADES, Rank.FIVE of Suit.SPADES, Rank.SIX of Suit.SPADES, Rank.SEVEN of Suit.SPADES, Rank.EIGHT of Suit.SPADES, Rank.NINE of Suit.SPADES, Rank.TEN of Suit.SPADES, Rank.JACK of Suit.SPADES, Rank.QUEEN of Suit.SPADES, Rank.KING of Suit.SPADES, Rank.ACE of Suit.SPADES"
        self.assertEqual(deck_str, deck.__repr__())

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