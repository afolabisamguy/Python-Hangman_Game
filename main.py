# Used this commented part to get the wordlist for the hangman game from a random source
# import requests
#
# sam = requests.get("https://pastebin.com/raw/RnDPnp9V")
#
# with open("hangman.txt", "w") as f:
#     for i in sam.text:
#         f.write(str(i))
#         print(i)

# Then used this next part to cut off the extra blank spaces between the words
# with open("hangman.txt", "r") as file:
#     lines = file.readlines()
# with open("hangman.txt", "w") as file:
#     for line in lines:
#         if line.strip() != '':
#             file.write(line)

import random
hangman_word = []
hangman_ascii = [
    """
    +---+
    |   |
        |
        |
        |
        |
  =========
""",
    """
    +---+
    |   |
    O   |
        |
        |
        |
  =========
""",
    """
    +---+
    |   |
    O   |
    |   |
        |
        |
  =========
""",
    """
    +---+
    |   |
    O   |
   /|   |
        |
        |
  =========
""",
    """
    +---+
    |   |
    O   |
   /|\  |
        |
        |
  =========
""",
    """
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
  =========
""",
    """
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
  =========
"""
]
with open("hangman.txt", "r") as file:
    for line in file:
        hangman_word.append(line.strip())

def hangman_game():
    print('Welcome to sam\'s hangman Game')
    print('You\'ll be given a random word, and you have to guess the letters in the word')
    print('if you guess wrong your hangman diagram will be updated and you\'ll lose if the diagram is compleete')
    print('You\'ll also have your incorrect guesses displayed to you to avoid undue repetitions')

    word = random.choice(hangman_word)
    dash = []
    counter = []
    count = 0
    correct_guesses = 0
    wrong_guess = []
    wrong_guesses = 0
    length = len(word)
    for i in range(length):
        dash.append('-')
    while correct_guesses != length:
        # print(word)
        print(*dash)
        print('Enter Your Guess: ')
        guess = input()
        if guess not in word:
            print('Sorry Your Guess Is Wrong')
            wrong_guess.append(guess)
            print(hangman_ascii[wrong_guesses])
            wrong_guesses += 1
            if wrong_guesses == len(hangman_ascii):
                print('You Lose')
                print(f'The Word is {word}')
                break
        else:
            if guess in dash:
                print('Sorry Your Guess Has Already Been Entered')
            else:
                for i in word:
                    if i == guess:
                        counter.append(count)
                        correct_guesses += 1
                    count += 1
                for i in counter:
                    dash[i] = guess
                count = 0
                counter.clear()
        print('Here are your Wrong guesses:', end=' ')
        print(*wrong_guess)
    if correct_guesses == length:
        print('You Correctly guessed the word.. Congratulations You Win')
        print(*dash)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    replay = True
    hangman_game()
    while replay:
        print('Do you want to play again? (y/n) ')
        answer = input()
        if answer == 'y':
            replay = True
            hangman_game()
        else:
            replay = False


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
