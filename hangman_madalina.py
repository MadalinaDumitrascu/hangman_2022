import sys
import random
from ascii import hangman

def display_start_menu():
    print("Welcome to the Hangman!!!")
    difficulty = input("Please choose level of difficulty. Easy, Hard or Quit:  ").lower()
    if difficulty == "quit": 
        print("Buh-Bye!") 
        sys.exit() 
    return difficulty

def get_level():
    difficulty = display_start_menu()
    if difficulty == "easy":
        return difficulty
    elif difficulty == "hard":    
        return difficulty
    else: 
        difficulty = display_start_menu()   
     
def read_words(file):
    lines = open(file, 'r').readlines()
    word_list = [line.split(" | ")[1].replace("\n", "") for line in lines]
    return word_list

def get_words_level_difficulty():
    file = 'countries-and-capitals.txt'
    word_list = read_words(file)
    easy = []
    hard = []
    for w in word_list:
        if len(w) > 7:
            w = hard.append(w)
        else:
            w = easy.append(w) 
    return easy, hard

def get_word(difficulty):
    easy, hard = get_words_level_difficulty()
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
    

def display_ascii_art(lives):
    hang = hangman[::-1]
    print(hang[lives])


def is_won(word):
    return not "_" in word 
    
def display_ask_for_letter():
    letter = input(" Please provide a letter: ").lower()
    if letter == 'quit':
        print("Bye")
        sys.exit()
    return letter


def get_letter():
    letter = display_ask_for_letter()
    while not all([y.isalpha() for y in letter]):
        letter = display_ask_for_letter()
    return letter 
           

def is_letter_in_word(letter, word):
    return letter in word.lower()
    

def search_replace_letter(letter, word, guess):
    guesslist = list(guess)
    for pos, char in enumerate(word.lower()):
        if char == letter:
            guesslist[pos] = letter 
    return "".join(guesslist)             


def main(): 
    difficulty = get_level()
    lives = set_lives(difficulty)
    word = get_word(difficulty)
    word_list = word.split(" ") # pt numele formate din mai multe cuvinte, scapi de spatiul liber si sa nu se numere la _
    guess = " ".join([len(x) * "_" for x in word_list])
    tried_letters = set()
  
    while True:
        display_word(guess, tried_letters)
        letter = get_letter()
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
                print(f"the word was: {word}") 
                break   


if __name__ == '__main__':
    main()