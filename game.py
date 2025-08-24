SNOWMAN_MIN_WORD_LENGTH = 5
SNOWMAN_MAX_WORD_LENGTH = 8
SNOWMAN_MAX_WRONG_GUESSES = 7

SNOWMAN_GRAPHIC = [
    '*   *   *  ',
    ' *   _ *   ',
    '   _[_]_ * ',
    '  * (")    ',
    '  \\( : )/ *',
    '* (_ : _)  ',
    '-----------'
]


def snowman(snowman_word):
    print(f"random word: {snowman_word}")

    correct_letter_guess_statuses = build_letter_status_dict(snowman_word)
    wrong_guesses_list = []

    while len(wrong_guesses_list) < SNOWMAN_MAX_WRONG_GUESSES:
        user_input = get_letter_from_user(correct_letter_guess_statuses, wrong_guesses_list)

        if user_input in correct_letter_guess_statuses:                        
            print("You guessed a letter that's in the word!")
            correct_letter_guess_statuses[user_input] = True
        else:
            print(f"The letter {user_input} is not in the word")
            wrong_guesses_list.append(user_input)

        print_snowman_graphic(len(wrong_guesses_list))
        print_word_progress_string(snowman_word, correct_letter_guess_statuses)
        print(f"Wrong guesses: {wrong_guesses_list}")

        if is_word_guessed(snowman_word, correct_letter_guess_statuses):
            print("Congratulations, you win!")
            return
    
    print(f"Sorry, you lose! The word was {snowman_word}")


def print_snowman_graphic(wrong_guesses_count):
    for i in range(SNOWMAN_MAX_WRONG_GUESSES - wrong_guesses_count, SNOWMAN_MAX_WRONG_GUESSES):
        print(SNOWMAN_GRAPHIC[i])

def get_letter_from_user(correct_letter_guess_statuses, wrong_guesses_list):
    valid_input = False
    user_input_string = None

    while not valid_input:
        user_input_string = input("Guess a letter: ")
        if not user_input_string.isalpha():
            print("You must input a letter!")
        elif len(user_input_string) > 1:
            print("You can only input one letter at a time!")
        elif (user_input_string in correct_letter_guess_statuses       
                and correct_letter_guess_statuses[user_input_string]): 
            print("You already guessed that letter and it's in the word!")
        elif user_input_string in wrong_guesses_list:
            print("You already guessed that letter and it's not in the word!")
        else:
            valid_input = True

    return user_input_string
    

def build_letter_status_dict(snowman_word):
    letter_status_dict = {}
    for letter in snowman_word:
        letter_status_dict[letter] = False
    return  letter_status_dict
    

def print_word_progress_string(snowman_word, correct_letter_guess_statuses):
    progress_string = generate_word_progress_string(snowman_word, correct_letter_guess_statuses)
    print(progress_string)


def generate_word_progress_string(snowman_word, correct_letter_guess_statuses):
    output_string = ""
    is_not_first_letter = False

    for letter in snowman_word:
        if is_not_first_letter:
            output_string += " "

        if correct_letter_guess_statuses[letter]:
            output_string += letter
        else:
            output_string += "_"

        is_not_first_letter = True

    return output_string


def is_word_guessed(snowman_word, correct_letter_guess_statuses):
    for letter in snowman_word:
        if not correct_letter_guess_statuses[letter]:
            return False
    return True