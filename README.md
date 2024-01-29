# Memory Game

## Description
This project implements the classic Memory game in Python, utilizing object-oriented programming. The game runs in the terminal and allows two players to compete against each other.

## Installation
1. Clone the repository.
   ```bash
   git clone https://github.com/your-username/Memory-Game.git

## Navigate to the project directory
cd Memory-Game

## Run the game
python Memory-Game.py

## Usage
1. Start the game by running the Memory-Game.py script.
2. Follow the instructions in the terminal to input player moves.
3. Players take turns flipping over two cards at a time.
4. If the cards match, the player keeps the pair and takes another turn.
5. If the cards do not match, they are turned face down again, and it is the next player's turn.
6. The game continues until all pairs are matched.
7. The game is won when all pairs of cards have been succesfully matched.

## Project Structure
1. `Memory-Game.py`: Contains the main function instantiating a game controller.
2. `GameController.py`: Class for managing the game, including players, the board, and scores.
3. `Player.py`: Class for information such as name, wins, pairs, and a message to provide feedback for any invalid move.
4. `Board.py`: Class for board information, including cells, guide, and functions for understanding the state of the board.
2. `README.md`: Project documentation.

## Dependencies
This project uses the following standard Python libraries:

* `os`: For interacting with the operating system and clearing the terminal.
* `sys`: For quit the game.
* `time`: For introducing pauses in the game execution.
* `random`: For shuffling the board.