import random
from typing import List
from .player import Deck, Player


class Board:
    """
    Represents the board of a card game.
    """

    def __init__(self) -> None:
        """
        Initializes the board with an empty list of players, turn count, active cards, and history cards.
        """
        self.players: List[Player] = []
        self.turn_count: int = 0
        self.active_cards: List[Cards] = []
        self.history_cards: List[Cards] = []

    def start_game(self) -> None:
        """
        Starts the game, fills the deck, distributes cards, and simulates turns until players have no cards left.
        """
        # Check if there are players to start the game
        if not self.players:
            print("No players to start the game.")
            return

        # Create a deck, fill it, and shuffle it
        deck = Deck()
        deck.fill_deck()
        deck.shuffle()

        # Distribute the cards to the players
        deck.distribute(self.players)

        # Main game loop
        while True:
            # Increment turn count
            self.turn_count += 1
            print(f"Turn {self.turn_count}")

            # Initialize a list to store cards played in this turn
            cards_played_this_turn = []

            # Each player plays one card
            for player in self.players:
                if not player.cards:
                    continue  # Skip players with no cards left

                card_played = player.play()
                self.active_cards.append(
                    (player.name, str(card_played))
                )  # Store player name and card as strings
                cards_played_this_turn.append(card_played)

                # Print the name of the player and the card they played
                print(f"{player.name} played: {card_played}")

            # Extend history_cards with cards played in this turn
            self.history_cards.extend(cards_played_this_turn)

            print("Number of Cards in History:", len(self.history_cards))

            # Check if all players have no cards left
            if all(not player.cards for player in self.players):
                print("Game Over")
                break
