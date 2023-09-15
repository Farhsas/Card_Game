import random
from typing import List


class Symbol:
    """
    Represents a symbol for a playing card, including color and icon.
    """

    def __init__(self) -> None:
        """
        Initializes a Symbol with a random color and icon.
        """
        self.icon: str = random.choice(["♥", "♦", "♣", "♠"])
        self.color: str = "Red" if self.icon in ["♥", "♦"] else "Black"

    def __str__(self) -> str:
        """
        Returns a string representation of the symbol.
        """
        return f"The symbol is {self.color} {self.icon}"


class Cards(Symbol):
    """
    Represents a playing card with a symbol and a value.
    """

    def __init__(self) -> None:
        """
        Initializes a Card with a random symbol and value.
        """
        super().__init__()
        self.value: str = random.choice(
            ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        )

    def __str__(self) -> str:
        """
        Returns a string representation of the card.
        """
        return f"{self.value} {self.icon}"
