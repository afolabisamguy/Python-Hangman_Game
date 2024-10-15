# Python Hangman CLI Game

Welcome to the Hangman CLI Game! This is a command-line version of the classic word-guessing game where you try to guess a word one letter at a time. With each incorrect guess, a part of the ASCII art of a hangman is drawn. Once the hangman is fully drawn, the game is over, and you lose. You'll be prompted to play again if the game ends.

## Features

- **ASCII Art Hangman**: Visual representation of the hangman displayed with each wrong guess.
- **Word List**: A text file containing the words to guess.
- **Replayability**: After each game (win or lose), you'll be asked if you'd like to play again.

## How to Play

1. Run the main script from your command line.
2. The game will pick a random word from the word list.
3. Guess letters one at a time.
4. For each wrong guess, a part of the hangman will be drawn.
5. You win by guessing all the letters of the word before the hangman is fully drawn.
6. If you lose, you’ll be asked if you want to play again.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/hangman-cli.git
    ```

2. Navigate to the project directory:

    ```bash
    cd hangman-cli
    ```

3. Ensure you have Python installed. This game is written in Python 3.

## Usage

1. Run the game script:

    ```bash
    python main.py
    ```

2. Follow the on-screen instructions to play the game.

## Files

- **main.py**: The main game script that runs the game.
- **words.txt**: A text file containing a list of words used in the game.

## Example Game

```
Welcome to Hangman!
_ _ _ _ _  (Guess the word)

Guess a letter: e

You guessed wrong!
```

If you make 6 incorrect guesses, the hangman will be fully drawn, and you'll lose:

```
 ______
 |    |
 |    O
 |   /|\
 |   / \
 |
_|___

Game Over! The word was: python
Would you like to play again? (y/n):
```

## License

This project is licensed under the MIT License.
