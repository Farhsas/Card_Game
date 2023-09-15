from utils.game import Board
from utils.player import Player, Deck
from utils.cards import Cards
from typing import List

if __name__ == "__main__":
    # Create players
    player1 = Player("Zian")
    player2 = Player("Nicolas")
    player3 = Player("Alexandre")

    # Create a board and add players to it
    board = Board()
    board.players.extend([player1, player2, player3])

    # Start the game
    board.start_game()
