# Casino

## Poker instructions
I had grand plans to code a whole casino with various games, money, and challenges, then converting it all to html to practice using guis and html.
Turns out this is a bit out of my scope, and will take me far more than the 40 hour max time I was to spend on this first project.
I might return to this project and complete it the way I initially dreamed eventually, but for now I'm content to wrap it up with just poker.

I made a two person poker game using pygame. You begin on a title screen, then go to an init screen where you can enter the names for two players.
A poker game is then initialized on the next screen once you hit enter. The two players are dealt their two cards. Whoever's turn it is has buttons to call, bet, or fold. When both players call the flop is dealt, then if both players call again the turn, and finally the river. 

Each player can choose to bet on any turn, and the ante of $.25 is automatically deducted from their cash
The players have three bet options based on the value of the current pot.

When a player folds, the other automatically wins the round and obtains the pot.
When a player wins, they obtain the pot. If a player wins and the other has less money than 0, you will be taken to the win screen,
which states who won and how much they are owed. You then have the option to play again or quit.

### Clone
```bash
git clone https://github.com/jacobhuneke/casino.git
cd casino
```

### Set up virtual environment
```bash
python3 -m venv .venv
```
mac/linux:
```bash
source .venv/bin/activate
```
windows:
```bash
.\.venv\Scripts\activate
```

```bash
pip install -r requirements.txt
```
### Run
```bash
chmod +x main.sh
./main.sh
```


