import sys
import random
hangman = [
'''

  +---+
  |   |
      |
      |
      |
      |
=========''', 


'''
  +---+
  |   |
  O   |
      |
      |
      |
========= ''', 

''' 
 +---+
  |   |
  O   |
  |   |
      |
      |
=========''', 

  
'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', 
'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', 
'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', 
'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


def get_level():
    print("Welcome to the Hangman!!!")
    difficulty = input("Please choose level of difficulty. Easy, Hard or Quit:  ").lower()
    if difficulty == "quit": 
        print("Buh-Bye!") 
        sys.exit() 
    elif difficulty == "easy":
        return difficulty
    elif difficulty == "hard":    
        return difficulty
    else: 
        difficulty = get_level()   
     

def generate_word(difficulty): 
    lines = open('countries-and-capitals.txt', 'r').readlines()
    word_list = [line.split(" | ")[1].replace("\n", "") for line in lines]
    easy = []
    hard = []
    for w in word_list:
        if len(w) > 7:
            w = hard.append(w)
        else:
            w = easy.append(w) 
    if difficulty == 'easy':
        word = random.choice(easy)
    elif difficulty == 'hard':
        word = random.choice(hard)
    return word                   
    
def set_lives(difficulty):
    if difficulty == 'easy':
        lives = 7
    elif difficulty == 'hard':
        lives = 3
    return lives


def display_word(word, tried_letters):
    print(word)
    print([y for y in tried_letters])     
    

hang = hangman[::-1]

def display_ascii_art(lives):
    print(hang[lives])


def is_won(word):
    return not "_" in word 
    

def ask_for_letter():
    letter = input(" Please provide a letter: ").lower()
    while not all([y.isalpha() for y in letter]):
        letter = input(" Please provide a letter: ").lower()
    if letter == 'quit':
        print("Bye")
        sys.exit()
    return letter 
           


def is_letter_in_word(letter, word):
    return letter in word.lower()
    


def search_replace_letter(letter, word, guess):
    guessList = list(guess)
    for pos, char in enumerate(word.lower()):
        if char == letter:
            guessList[pos] = letter 
    return "".join(guessList)             


def main():

    difficulty = get_level()
    lives = set_lives(difficulty)
    word = generate_word(difficulty)
    word_list = word.split(" ") # pt numele formate din mai multe cuvinte, scapi de spatiul liber si sa nu se numere la _
    guess = " ".join([len(x) * "_" for x in word_list])
    tried_letters = set()
  
    while True:
        display_word(guess, tried_letters)
        letter = ask_for_letter()
        tried_letters.add(letter)
        if is_letter_in_word(letter, word):
            guess = search_replace_letter(letter, word, guess)
            if is_won(guess):
                print("You won! Buh-bye")
                break
        else:
            lives = lives - 1
            display_ascii_art(lives)
            if lives == 0:
                print("game over. no more lives") 
                break   

main()