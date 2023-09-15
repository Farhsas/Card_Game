import random
from typing import List
from .cards import Cards


class Player:
    """
    Represents a player in a card game.
    """

    def __init__(self, name: str) -> None:
        """
        Initializes a player with an empty list of cards, a turn count of 0, no cards initially, and an empty history.
        """
        self.name: str = name
        self.cards: List[Cards] = []
        self.turn_count: int = 0
        self.number_of_cards: int = 0
        self.history: List[Cards] = []

    def __str__(self) -> str:
        """
        Returns a string representation of the player.
        """
        return f"Player has {self.number_of_cards} cards in his hand. His hand is {', '.join(str(card) for card in self.cards)} after {self.turn_count} turns."

    def play(self):
        """
        Randomly picks a card from the player's hand, adds it to the player's history, and returns the card.
        """
        if not self.cards:
            raise ValueError("No cards left to play")

        card_to_play = random.choice(self.cards)
        self.history.append(card_to_play)
        self.cards.remove(card_to_play)
        return card_to_play


class Deck:
    """
    Represents a deck of playing cards.
    """

    def __init__(self) -> None:
        """
        Initializes a deck with an empty list of cards.
        """
        self.cards: List[Cards] = []

    def fill_deck(self) -> None:
        """
        Fills the deck with a complete set of playing cards (52 cards).
        """
        symbols = ["♥", "♦", "♣", "♠"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

        for symbol in symbols:
            for value in values:
                card = Cards()
                card.color = "Red" if symbol in ["♥", "♦"] else "Black"
                card.icon = symbol
                card.value = value
                self.cards.append(card)

    def shuffle(self) -> None:
        """
        Shuffles the list of cards in the deck.
        """
        random.shuffle(self.cards)

    def distribute(self, players: List[Player]) -> None:
        """
        Distributes the cards evenly among the given list of players.
        """
        total_players = len(players)
        cards_per_player = len(self.cards) // total_players

        for player in players:
            for _ in range(cards_per_player):
                card = self.cards.pop()
                player.cards.append(card)
                player.number_of_cards += 1
