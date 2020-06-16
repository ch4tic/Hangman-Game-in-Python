#!/usr/bin/python3

# Author: ch4tic - Eman Ćatić
# Github repository: https://github.com/ch4tic/Hangman-in-Python.git
# Date: 15.06.2020

# Importing some libraries/modules.
import time
import os
import sys
import random

# List of random words for the game.
words = ['giraffe', 'house', 'flat', 'dog', 'cat', 'elephant', 'computer', 'keyboard', 'deer', 'snake']

# Function that clears the screen
def clear():
    os.system('clear') # If the OS is Linux or MacOS.

# Function that prints a new line.
def new():
    print('\n')

# Function that appends a random word to a variable.
def random_word():
    global secretWord
    secretWord = random.choice(words)

# Function that introduces the user to the game.
def intro():
    clear() # Clearing the screen.
    welcomeString = 'Hangman Game'
    print('-' * len(welcomeString)) # Printing a nice banner :)
    print(welcomeString)
    print('-' * len(welcomeString)) # Printing a nice banner :)

# Function that runs the Hangman game, here the magic happens.
def hangman(secret):
    clear()
    intro()
    time.sleep(2)
    new()
    word_completion = '_' * len(secretWord) # Variable that tracks the word completion.
    tries =  len(secretWord) # Tries are equal to the len of the secretWord
    guesses = []  # All guessed letters are stored in this list.
    guessed = False # Did the user guess the word?

    # User is prompted for input while the tries are > than 0 and not guessed.
    while not guessed and tries > 0:
        guess = input('Guess a letter: ')
        # Checking if the user inputed a letter or not.
        if len(guess) == 1 and guess.isalpha():
            if guess not in secretWord:
                print('Guess not in word!')
                tries -= 1
                guesses.append(guess) # Appending the guess to the list of all guessed letters.
            elif guess in guesses:
                print('You already guessed that.')
            else:
                print('Good job kiddo!')
                guesses.append(guess)
                word_list = list(word_completion)
                indices = [i for i, letter in enumerate(secretWord) if letter == guess]
                for index in indices:
                    word_list[index] = guess
                word_completion = "".join(word_list)
                if "_" not in word_completion:
                    guessed = True
        else:
            print('Guess not valid!')

    # The user gets a nice message if he/she wins.
    if guessed == True:
        clear()
        print('You won!')
        time.sleep(1)
        print('Secret word: ' + str(secretWord))
        time.sleep(1)
    else:
        clear()
        print('Better luck next time!')
        time.sleep(1)
        print('The secret word was: ' + str(secretWord))
        time.sleep(1)

# This function is used for prompting the user for playing the game again.
def main():
    secretWord = random_word()
    hangman(secretWord)
    while input("Play Again? (Y/N) ").upper() == 'Y':
        secretWord = random_word() # Secret word is selected.
        hangman(secretWord) # If the user types Y the game starts.

# Initializing the main function at the start.
if __name__ == "__main__":
    main()
