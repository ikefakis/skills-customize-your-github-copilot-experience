# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build the classic word-guessing game in Python by combining strings, loops, conditionals, and random selection. Students will create an interactive game that reveals a hidden word one letter at a time while tracking incorrect guesses.

## 📝 Tasks

### 🛠️ Choose a Secret Word

#### Description
Create a predefined list of possible words and randomly select one word to use for each game.

#### Requirements
Completed program should:

- Include a list of at least five possible words.
- Randomly choose one word at the start of the game.
- Store the selected word so it can be checked against the player's guesses.

### 🛠️ Track Letter Guesses

#### Description
Build the main guessing loop that accepts one letter at a time and shows the player's current progress in an underscore format.

#### Requirements
Completed program should:

- Prompt the player to guess a letter.
- Display the secret word as underscores for unguessed letters and revealed letters for correct guesses.
- Prevent the game from crashing when the player enters repeated or invalid guesses.
- Show the letters the player has already guessed.

### 🛠️ Finish the Game

#### Description
Keep track of incorrect guesses and end the game when the player wins or runs out of attempts.

#### Requirements
Completed program should:

- Track the number of incorrect guesses remaining.
- End the game when the full word has been revealed or attempts reach zero.
- Display a win message when the player guesses the word correctly.
- Display a lose message that reveals the secret word when the player runs out of attempts.
