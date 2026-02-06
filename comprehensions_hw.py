# This file contains the first homework assignment, about lists, strings, and
# comprehensions.
# You must rename this file as comprehensions_hw.py for the tests and autograder.

def problem_1() -> str:
    '''
    Problem 1: Goal: Capitalize the zeroth letter of each word.
    '''
    initial_string: str = (
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
        "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
        "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi "
        "ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit "
        "in voluptate velit esse cillum dolore eu fugiat nulla pariatur. "
        "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia "
        "deserunt mollit anim id est laborum."
    )

    words = initial_string.split()
    capitalized_words = [word.capitalize() for word in words]
    string_with_each_word_captalized = " ".join(capitalized_words)

    return string_with_each_word_captalized


def problem_2() -> str:
    '''
    Problem 2: Goal: Get every-other letter of the last sentence
    '''
    initial_string: str = (
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod "
        "tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim "
        "veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea "
        "commodo consequat. Duis aute irure dolor in reprehenderit in voluptate "
        "velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat "
        "cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    )

    sentences = initial_string.split(".")
    last_sentence = sentences[-2].lstrip()
    even_letters_of_last_sentence = last_sentence[::2]

    return even_letters_of_last_sentence


def problem_3() -> dict:
    '''
    Problem 3: Goal: Create a dictionary whose keys are the characters of the
    sentence and values are their frequencies.
    '''
    initial_string: str = (
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod "
        "tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim "
        "veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea "
        "commodo consequat. Duis aute irure dolor in reprehenderit in voluptate "
        "velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat "
        "cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    )

    dict_of_letter_frequencies = {
        char: len([c for c in initial_string if c == char])
        for char in initial_string
    }

    return dict_of_letter_frequencies
