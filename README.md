# TicTacToe-with-DataClasses

Interactive TicTacToe game supporting multiple players. I used it as a learning project and updated it every time I learned new Python features. I started with NORMAL CLASSES (including inheritance and composition), then transitioned to DATA CLASSES.


I initially envisioned the game as a single one (still with multiple rounds) that does not require the possible creation of multiple instances of the game itself, so in the 'SINGLE-GAME' file you will see CLASS variables instead of INSTANCE ones.
I later decided to allow for the creation of multiple Game objects and I adjusted the code accordingly in the 'MULTIPLE-GAMES' file. 
In both versions the features of the game remain unchanged. 

# Features
-3 game modes:
 -Human vs Human
 -Human vs Computer (interactive choice of who goes first and with which symbol)
 -Computer vs Computer 
-Score and rounds tracking
-Option to change players after each round and the score and rounds change accordingly 
 


<h1>TicTacToe-with-DataClasses</h1>

This is an interactive TicTacToe game that supports multiple players. It started as a learning project, and I updated it each time I learned new Python features. The initial version used **normal classes** (including inheritance and composition), and later I transitioned to **data classes**.

### <h2>Project Evolution</h2>
I originally envisioned the game as a single instance (with multiple rounds) that didn’t require creating multiple game instances. In the **SINGLE-GAME** version, you'll notice **class variables** instead of instance variables.

Later, I decided to allow the creation of multiple Game objects and adapted the code for that in the **MULTIPLE-GAMES** version. Despite these architectural differences, the features of the game remain unchanged across both versions.

# Features
- 3 Game Modes:
  - Human vs Human
  - Human vs Computer (interactive choice of who goes first and which symbol to use)
  - Computer vs Computer
- Score and round tracking
- Option to change players after each round, with scores and round counts updating accordingly
