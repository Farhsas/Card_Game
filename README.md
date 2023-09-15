# Card Game Simulator

This Python program simulates a simple card game with the following components:

- **Symbol**: Represents a symbol for a playing card, including color and icon.
- **Cards**: Represents a playing card with a symbol and a value.
- **Player**: Represents a player in a card game.
- **Deck**: Represents a deck of playing cards.
- **Board**: Represents the board of a card game.

## How to Use

1. Ensure you have Python installed on your system.

2. Clone this repository or copy the code to your local environment.

3. Run the game by executing the `main` script:
    ```bash
    python main.py
    ```

4. Enjoy the card game simulation!

## Components

### Symbol Class

- Represents a symbol for a playing card, including color (Red/Black) and icon (♥, ♦, ♣, ♠).
- Initializes with a random color and icon.

### Cards Class

- Represents a playing card with a symbol and a value (e.g., "A", "2", "3", ..., "K").
- Initializes with a random symbol and value.

### Player Class

- Represents a player in the card game.
- Initializes with a name, an empty list of cards, a turn count, and an empty history.
- Can play cards, and played cards are added to the history.

### Deck Class

- Represents a deck of playing cards.
- Initializes with an empty list of cards.
- Can fill the deck with a complete set of playing cards (52 cards), shuffle the cards, and distribute them to players evenly.

### Board Class

- Represents the board of the card game.
- Initializes with an empty list of players, turn count, active cards, and history cards.
- Can start the game, fill the deck, distribute cards, and simulate turns until players have no cards left.
