
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a command-line Hangman game using Python. In this assignment, you will practice strings, loops, conditionals, and basic game flow control.

## 📝 Tasks

### 🛠️	Build Core Hangman Loop

#### Description
Create the main game loop that selects a random word and lets the player guess one letter at a time until the word is solved or attempts run out.

#### Requirements
Completed program should:

- Randomly choose one word from a predefined Python list.
- Ask the player for a single letter guess during each turn.
- Reveal correct letters in their proper positions (for example: `_ a _ _ m a n`).
- Decrease remaining attempts only when the guessed letter is not in the word.
- End the game immediately when all letters are guessed or attempts reach 0.

### 🛠️	Display Results and Input Rules

#### Description
Improve the user experience by validating input and displaying clear win/lose messages at the end of the game.

#### Requirements
Completed program should:

- Reject invalid input (empty input, more than one character, numbers, or symbols) and prompt again.
- Handle repeated guesses without crashing and notify the player that the letter was already used.
- Show the current word progress and remaining attempts after each valid guess.
- Display a winning message when the player guesses the full word.
- Display a losing message and reveal the correct word when attempts are exhausted.
