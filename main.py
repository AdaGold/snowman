import unittest

if __name__ == '__main__':
    # Get a random word 5-8 letters long
    user_input = ""
    while user_input != "p" and user_input != "t":
        user_input = input('Please enter p to play or t to test => ')
    
    if user_input == "p":    
        from game import snowman, SNOWMAN_MIN_WORD_LENGTH, SNOWMAN_MAX_WORD_LENGTH
        from wonderwords import RandomWord
        random_word_generator = RandomWord()        
        snowman_word = random_word_generator.word(word_min_length=SNOWMAN_MIN_WORD_LENGTH, word_max_length=SNOWMAN_MAX_WORD_LENGTH)

        snowman(snowman_word)
    else: 
      from game_test import *
      unittest.main(exit=False)