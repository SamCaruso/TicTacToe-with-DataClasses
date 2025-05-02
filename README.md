<h1>TicTacToe-with-DataClasses</h1>

This is an interactive TicTacToe game that supports multiple players. It started as a learning project, and I updated it each time I learned new Python features. The initial version used **normal classes** (including inheritance and composition) and later I transitioned to **data classes**.

### <h2>Project Evolution</h2>
I originally envisioned the game as a single instance (with multiple rounds) that didn’t require creating multiple game instances. In the **SINGLE-GAME** version, you'll notice **class variables** instead of instance variables.

Later, I decided to allow for the creation of multiple Game objects and adapted the code accordingly in the **MULTIPLE-GAMES** version. Despite these architectural differences, the features of the game remain unchanged across both versions.

# Features
- 3 Game Modes:
  - Human vs Human
  - Human vs Computer (interactive choice of who goes first and with which symbol)
  - Computer vs Computer
- Score and round tracking
- Option to change players after each round, with scores and round counts updating accordingly
