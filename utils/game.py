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
        if not self.players:
            print("No players to start the game.")
            return

        deck = Deck()
        deck.fill_deck()
        deck.shuffle()

        deck.distribute(self.players)

        while True:
            self.turn_count += 1
            print(f"Turn {self.turn_count}")

            cards_played_this_turn = []
            for player in self.players:
                if not player.cards:
                    continue

                card_played = player.play()
                self.active_cards.append((player.name, str(card_played)))
                cards_played_this_turn.append(card_played)

                print(f"{player.name} played: {card_played}")

            self.history_cards.extend(cards_played_this_turn)

            print("Number of Cards in History:", len(self.history_cards))

            if all(not player.cards for player in self.players):
                print("Game Over")
                break
