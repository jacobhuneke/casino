from poker.poker_game import *

def main():
    p1 = Player("Jake")
    p2 = Player("Lainey")
    game = PokerGame(p1, p2)
    #ante up
    game.deal_player_cards()
    #bets?
    game.deal_flop()
    
    print(f"Jake's cards are: {p1.get_hole()}")
    print(f"Lainey's cards are: {p2.get_hole()}\n")

   
    #game.deal_turn()
    print(f"The cards on the board are: {game.flop}")
    print(f"Jake has a {p1.score_hand().value[1]}, {p1.best_hand}")
    print(f"Lainey has a {p2.score_hand().value[1]}, {p2.best_hand}\n")
    game.deal_turn()
    print(f"The cards on the board are: {game.flop}")
    print(f"Jake has a {p1.score_hand().value[1]}, {p1.best_hand}")
    print(f"Lainey has a {p2.score_hand().value[1]}, {p2.best_hand}\n")
    game.deal_turn()
    print(f"The cards on the board are: {game.flop}")
    print(f"Jake has a {p1.score_hand().value[1]}, {p1.best_hand}")
    print(f"Lainey has a {p2.score_hand().value[1]}, {p2.best_hand}")

    winner = get_winner(p1, p2)
    if winner != None:
        print(f"The winner is: {winner.name}, with a {winner.hand_rank.value[1]}")
    else:
        print(f"There was a Tie! Both players win")
main()