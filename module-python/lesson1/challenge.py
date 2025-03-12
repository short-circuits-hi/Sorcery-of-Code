#!/usr/bin/env python3
"""
Python Module - Lesson 1 Challenge

Complete the following functions to demonstrate your understanding of Python fundamentals.
Each function has a docstring with instructions and examples.

Run this file to test your solutions:
    python challenge.py

All tests must pass to earn your key!
"""

def reverse_string(text):
    """
    Reverse the input string.
    
    Example:
        reverse_string("hello") -> "olleh"
        reverse_string("Python") -> "nohtyP"
    
    Args:
        text (str): The string to reverse
        
    Returns:
        str: The reversed string
    """
    # TODO: Implement this function
    pass


def count_vowels(text):
    """
    Count the number of vowels (a, e, i, o, u) in the input string.
    Case insensitive.
    
    Example:
        count_vowels("hello") -> 2
        count_vowels("Python Programming") -> 4
    
    Args:
        text (str): The string to count vowels in
        
    Returns:
        int: The number of vowels
    """
    # TODO: Implement this function
    pass


def is_palindrome(text):
    """
    Check if the input string is a palindrome.
    A palindrome is a string that reads the same forwards and backwards,
    ignoring case, spaces, and punctuation.
    
    Example:
        is_palindrome("racecar") -> True
        is_palindrome("hello") -> False
        is_palindrome("A man, a plan, a canal: Panama") -> True
    
    Args:
        text (str): The string to check
        
    Returns:
        bool: True if the string is a palindrome, False otherwise
    """
    # TODO: Implement this function
    pass


def list_powers(n, power):
    """
    Create a list of the first n numbers raised to the given power.
    
    Example:
        list_powers(5, 2) -> [0, 1, 4, 9, 16]
        list_powers(3, 3) -> [0, 1, 8]
    
    Args:
        n (int): The number of elements in the list
        power (int): The power to raise each number to
        
    Returns:
        list: A list of integers
    """
    # TODO: Implement this function
    pass


def filter_strings_by_length(strings, min_length):
    """
    Filter a list of strings to include only those with length >= min_length.
    
    Example:
        filter_strings_by_length(["a", "ab", "abc", "abcd"], 3) -> ["abc", "abcd"]
        filter_strings_by_length(["hello", "hi", "hey"], 3) -> ["hello", "hey"]
    
    Args:
        strings (list): A list of strings
        min_length (int): The minimum length of strings to include
        
    Returns:
        list: A filtered list of strings
    """
    # TODO: Implement this function
    pass


# Test functions - DO NOT MODIFY
def test_function(func, inputs, expected_outputs):
    """Test a function with multiple inputs and expected outputs."""
    for i, (input_args, expected) in enumerate(zip(inputs, expected_outputs)):
        if isinstance(input_args, tuple):
            result = func(*input_args)
        else:
            result = func(input_args)
            
        assert result == expected, f"Test {i+1} failed: {func.__name__}({input_args}) returned {result}, expected {expected}"
    print(f"All tests passed for {func.__name__}!")

def run_tests():
    """Run all tests."""
    # Test reverse_string
    test_function(
        reverse_string,
        ["hello", "Python", "12345", ""],
        ["olleh", "nohtyP", "54321", ""]
    )
    
    # Test count_vowels
    test_function(
        count_vowels,
        ["hello", "Python Programming", "xyz", "AEIOUaeiou"],
        [2, 4, 0, 10]
    )
    
    # Test is_palindrome
    test_function(
        is_palindrome,
        ["racecar", "hello", "A man, a plan, a canal: Panama", "12321"],
        [True, False, True, True]
    )
    
    # Test list_powers
    test_function(
        list_powers,
        [(5, 2), (3, 3), (4, 1), (0, 5)],
        [[0, 1, 4, 9, 16], [0, 1, 8], [0, 1, 2, 3], []]
    )
    
    # Test filter_strings_by_length
    test_function(
        filter_strings_by_length,
        [
            (["a", "ab", "abc", "abcd"], 3),
            (["hello", "hi", "hey"], 3),
            (["one", "two", "three", "four", "five"], 4),
            ([], 1)
        ],
        [
            ["abc", "abcd"],
            ["hello", "hey"],
            ["three", "four", "five"],
            []
        ]
    )
    
    print("Congratulations! All challenges completed successfully!")

if __name__ == "__main__":
    try:
        run_tests()
    except AssertionError as e:
        print(f"Test failed: {e}")
        exit(1)
