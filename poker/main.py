from .poker_game import *

def main():
    p1 = Player("Jake")
    p2 = Player("Lainey")
    game = PokerGame(p1, p2)
    #ante up
    game.deal_player_cards()
    #bets?
    game.deal_flop()
    
    print(f"Jake's cards are: {p1.get_hole()}")
    print(f"Lainey's cards are: {p2.get_hole()}")

    game.deal_turn()
    game.deal_turn()
    print(p1.score_hand())

main()