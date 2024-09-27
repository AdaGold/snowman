import random
from  wonderwords import RandomWord
#https://pypi.org/project/wonderwords/

SNOWMAN_GRAPHIC = [
    '*   *   *  ',
    ' *   _ *   ',
    '   _[_]_ * ',
    '  * (")    ',
    '  \\( : )/ *',
    '* (_ : _)  ',
    '-----------'
]

SNOWMAN_WRONG_GUESSES = len(SNOWMAN_GRAPHIC)
SNOWMAN_MIN_WORD_LENGTH = 5
SNOWMAN_MAX_WORD_LENGTH = 8
SNOWMAN_MAX_WRONG_GUESSES = 7

def get_letter_from_user(snowman_word_dict, wrong_guesses_list):
    valid_input = False
    user_input_string = None
    while not valid_input:
        user_input_string = input("Guess a letter: ")
        if not user_input_string.isalpha():
            print("You must input a letter!")
        elif len(user_input_string) > 1:
            print("You can only input one letter at a time!")
        elif user_input_string in snowman_word_dict and snowman_word_dict[user_input_string]:
            print("You already guessed that letter and it's in the word!")
        elif user_input_string in wrong_guesses_list:
            print("You already guessed that letter and it's not in the word!")
        else:
            valid_input = True

    return user_input_string

def get_word_progress(snowman_word, snowman_word_dict):
    for letter in snowman_word:
        if not snowman_word_dict[letter]:
            return False
    return True

def build_word_dict(snowman_word):
    snowman_word_dict = {}
    for letter in snowman_word:
        snowman_word_dict[letter] = False
    return snowman_word_dict


def print_snowman(wrong_guesses_count):
    for i in range(SNOWMAN_WRONG_GUESSES - wrong_guesses_count, SNOWMAN_WRONG_GUESSES):
        print(SNOWMAN_GRAPHIC[i])

    
def print_word_progress_string(snowman_word, snowman_word_dict):
    output_string = ""
    for letter in snowman_word:
        if snowman_word_dict[letter]:
            output_string += letter
        else:
            output_string += "_"
        output_string += " "
    print(output_string)


def snowman(snowman_word):

    word_dict = build_word_dict(snowman_word) 
    wrong_guesses_list = []


    while len(wrong_guesses_list) < SNOWMAN_WRONG_GUESSES:
        user_input = get_letter_from_user(word_dict, wrong_guesses_list)
        
        if user_input in snowman_word:
            print("You guessed a letter that's in the word!")
            word_dict[user_input] = True 
        else:
            wrong_guesses_list.append(user_input)
            print(f"The letter {user_input} is not in the word")
        
        has_player_won = get_word_progress(snowman_word, word_dict)

        print_snowman(len(wrong_guesses_list))
        print(f"Wrong guesses: {wrong_guesses_list}")   

        print_word_progress_string(snowman_word, word_dict)

        if has_player_won:
            print("You win!")
            return
        
    print("Sorry, you lose!")
    print(f"The word was {snowman_word}.")