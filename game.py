SNOWMAN_MIN_WORD_LENGTH = 5
SNOWMAN_MAX_WORD_LENGTH = 8
SNOWMAN_MAX_WRONG_GUESSES = 7

SNOWMAN_1 = '*   *   *  '
SNOWMAN_2 = ' *   _ *   '
SNOWMAN_3 = '   _[_]_ * '
SNOWMAN_4 = '  * (")    '
SNOWMAN_5 = '  \\( : )/ *'
SNOWMAN_6 = '* (_ : _)  '
SNOWMAN_7 = '-----------'

def snowman(snowman_word):
    """Complete the snowman function
    replace "pass" below with your own code
    It should print 'Congratulations, you win!'
    If the player wins and, 
    'Sorry, you lose! The word was {snowman_word}' if the player loses
    """
    if not (SNOWMAN_MIN_WORD_LENGTH <= len(snowman_word) <= SNOWMAN_MAX_WORD_LENGTH):
        print("Invalid word length! The word must be between 5 and 8 characters.")
        return

    snowman_word_dict = {letter: False for letter in snowman_word}
    wrong_guesses_list = []
    num_wrong_guesses = 0 

    while num_wrong_guesses < SNOWMAN_MAX_WRONG_GUESSES:
        print_word_progress_string(snowman_word, snowman_word_dict)
        print_snowman_graphic(num_wrong_guesses)

        guessed_letter = get_letter_from_user(snowman_word_dict, wrong_guesses_list)

        if guessed_letter in snowman_word:
            snowman_word_dict[guessed_letter] = True

            if all(snowman_word_dict[letter] for letter in snowman_word):
                print_word_progress_string(snowman_word, snowman_word_dict)
                print("Congratulations, you win!")
                print_snowman_graphic(num_wrong_guesses)
                return
        else:
            if guessed_letter not in wrong_guesses_list:
                wrong_guesses_list.append(guessed_letter)
                num_wrong_guesses += 1
            else:
                print("You already guessed the letter and it's not in the word!")

    print(f"Sorry, you lose! The word was {snowman_word}.")  

def print_snowman_graphic(num_wrong_guesses):
    """This function prints out the appropriate snowman image 
    depending on the number of wrong guesses the player has made.
    """
    
    for i in range(1, num_wrong_guesses + 1):
        if(i == 1):
            print(SNOWMAN_1)
        if(i == 2):
            print(SNOWMAN_2)
        if(i == 3):
            print(SNOWMAN_3)
        if(i == 4):
            print(SNOWMAN_4)
        if(i == 5):
            print(SNOWMAN_5)
        if(i == 6):
            print(SNOWMAN_6)
        if(i == 7):
            print(SNOWMAN_7)

def get_letter_from_user(snowman_word_dict, wrong_guesses_list):
    """This function takes the snowman_word_dict and the list of characters 
    that have been guessed incorrectly (wrong_guesses_list) as input.
    It asks for input from the user of a single character until 
    a valid character is provided and then returns this character.
    """

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
    
def build_word_dict(snowman_word):
    """This function takes snowman_word as input and returns 
    a dictionary with a key-value pair for each letter in 
    snowman_word where the key is the letter and the value is `False`.
    """
    snowman_word_dict = {}
    for letter in snowman_word:
        snowman_word_dict[letter] = False
    return snowman_word_dict
    
def print_word_progress_string(snowman_word, snowman_word_dict):
    """
    This function takes the snowman_word and snowman_word_dict as input.
    It prints an output_string that shows the correct letter guess placements 
    as well as the placements for the letters yet to be guessed.
    """
    output_string = ""
    for letter in snowman_word:
        if snowman_word_dict[letter]:
            output_string += letter
        else:
            output_string += "_"
        output_string += " "
    print(output_string)

def get_word_progress(snowman_word, snowman_word_dict):
    """
    This function takes the snowman_word and snowman_word_dict as input.
    It returns True if all the letters of the word have been guessed, and False otherwise.
    """
    for letter in snowman_word:
        if not snowman_word_dict[letter]:
            return False
    return True