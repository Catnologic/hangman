# HANGMAN feb-july 2020

HANGMAN_PHOTOS = {"picture 1":
    """    x-------x
    |
    |
    |
    |
    |""",

    "picture 2":
    """    x-------x
    |       |
    |       0
    |
    |
    |""",

    "picture 3":
   """    x-------x
    |       |
    |       0
    |       |
    |
    |""",

    "picture 4":
    """    x-------x
    |       |
    |       0
    |      /|
    |
    |""",

    "picture 5":
    """    x-------x
    |       |
    |       0
    |      /|\\
    |
    |""",

    "picture 6":
    """    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |""",

    "picture 7":
    """    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |"""}


WIN = """
 __          _______ _   _ 
 \ \        / /_   _| \ | |
  \ \  /\  / /  | | |  \| |
   \ \/  \/ /   | | | . ` |
    \  /\  /   _| |_| |\  |
     \/  \/   |_____|_| \_|
                           
"""

LOSE = """
  _      ____   _____ ______ 
 | |    / __ \ / ____|  ____|
 | |   | |  | | (___ | |__   
 | |   | |  | |\___ \|  __|  
 | |___| |__| |____) | |____ 
 |______\____/|_____/|______|
                             
"""


def welcome_screen():
    """"Prints game's name and the number of tries at the start of the game
    :return: None
    """

    HANGMAN_ASCII_ART = """
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/
                     
"""
    num_of_tries = 6
    print(HANGMAN_ASCII_ART, num_of_tries)


def user_path_input():
    """Verifies the existence of a working file path
    :return: file path containing list of words
    :rtype: str
    """

    import os.path
    user_input = ""
    while not os.path.exists(user_input):
        user_input = input("Enter file path: ")
        if not os.path.exists(user_input):
            print("This file doesn't exist.")
    return user_input


def check_if_number_is_decimal():
    """Checks whether the input is made up of numbers only
    :return: a number
    :rtype: int
    """

    user_number_input = ""
    while not user_number_input.isdecimal():
        user_number_input = input("Enter a number: ")
        if not user_number_input.isdecimal():
            print("You must type numbers Only.")
    return int(user_number_input)


def choose_word(file_path, index):
    """Receives a file path and a number indicating the location of chosen word
    :param file_path: file path
    :param index: index number
    :type file_path: str
    :type index: int
    :return: word in location of the index number
    :rtype: str
    """

    open_file = open(file_path, "r")
    read_content = open_file.read()
    split_content = read_content.split(" ")
    different_words = list(set(split_content))
    chosen_word = different_words[index % len(different_words)]
    return chosen_word


def hangman(secret_word, max_tries, num_of_tries):
    """Controls the gameplay - asking for a letter until number of failed attempts is reached
    :param secret_word: word to guess
    :param max_tries: number of allowed tries
    :param num_of_tries: number of actual tries
    :type secret_word: str
    :type max_tries: int
    :type num_of_tries: int
    :return: None
    """

    num_of_tries = 0
    old_letters_guessed = []
    while num_of_tries < max_tries:
        letter_guessed = input("Guess a letter: ")
        is_input_valid = check_valid_input(letter_guessed, old_letters_guessed)
        if not is_input_valid:
            continue
        elif is_input_valid:
            is_correct = try_update_letter_guessed(letter_guessed, old_letters_guessed, secret_word)
            if not is_correct:
                num_of_tries += 1
                print(" :( ")
                hangman_pics(num_of_tries)
                show_hidden_word(secret_word, old_letters_guessed)
                continue
            elif is_correct:
                check_winner = check_win(secret_word, old_letters_guessed)
                if not check_winner:
                    show_hidden_word(secret_word, old_letters_guessed)
                elif check_winner:
                    print(WIN)
                    show_hidden_word(secret_word, old_letters_guessed)
                    return
    print(LOSE)
    print(secret_word)


def check_valid_input(letter_guessed, old_letters_guessed):
    """Checks whether letter guessed is ONE letter from the abc
    :param letter_guessed: letter
    :param old_letters_guessed: list of previously guessed letters
    :type letter_guessed: str
    :type old_letters_guessed: list
    :return: whether letter guessed is valid or not
    :rtype: bool
    """

    if not len(letter_guessed) == 1 or \
            not letter_guessed.isalpha() or \
            letter_guessed in old_letters_guessed:
        print("X")
        print(old_letters_guessed)
        return False
    else:
        return True


def try_update_letter_guessed(letter_guessed, old_letters_guessed, secret_word):
    """Checks whether or not the input letter is in the secret word
    :param letter_guessed: letter
    :param old_letters_guessed: list of previously guessed letters
    :param secret_word: word to guess
    :type letter_guessed: str
    :type old_letters_guessed: list
    :type secret_word: str
    :return: if the letter is in the secret word or not
    :rtype: bool
    """

    letter_guessed = letter_guessed.lower()
    old_letters_guessed.append(letter_guessed)
    old_letters_guessed = sorted(old_letters_guessed)
    old_letters_guessed = str(" -> ".join(old_letters_guessed))
    if letter_guessed in secret_word:
        return True
    else:
        print(old_letters_guessed)
        return False


def hangman_pics(num_of_tries):
    """Prints out the hangmanp progression every failed guess
    :param num_of_tries: global variable, indicates how many incorrect guesses the player can make
    :type num_of_tries: int
    :return: None
    """

    print(HANGMAN_PHOTOS["picture " + str(num_of_tries + 1)])


def check_win(secret_word, old_letters_guessed):
    """Checks whether all of the secret word's letters were guessed
    :param secret_word: word to guess
    :param old_letters_guessed: list of previously guessed letters
    :type secret_word: str
    :type old_letters_guessed: list
    :return: whether all the word's letters were guessed or not
    :rtype: bool
    """

    for letter in secret_word:
        letter = letter.lower()
        if letter not in old_letters_guessed:
            return False
    return True


def show_hidden_word(secret_word, old_letters_guessed):
    """Prints out the secret word with an underscore for undisclosed letters
    :param secret_word: word to guess
    :param old_letters_guessed: list of previously guessed letters
    :type secret word: str
    :type old_letters_guessed: list
    :return: None
    """

    show_user = ""
    for letter in secret_word:
        if letter in old_letters_guessed:
            show_user += letter + " "
        else:
            show_user += "_ "
    print(show_user)


def main():
    welcome_screen()
    file_path = user_path_input()
    index = check_if_number_is_decimal()
    secret_word = choose_word(file_path, index)
    print("Let's start!")
    print(HANGMAN_PHOTOS["picture 1"])
    MAX_TRIES = 6
    num_of_tries = 0
    hangman(secret_word, MAX_TRIES, num_of_tries)

if __name__ == "__main__":
  main()