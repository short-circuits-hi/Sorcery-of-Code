#!/usr/bin/env python3
"""
Module 0: Beginner Review - Lesson 1 Challenge

Complete the following puzzles to test your understanding of Python basics.
Each puzzle has instructions and a function shell for you to complete.

Run this file to test your solutions:
    python challenge.py

All tests must pass to earn your key!
"""

def spell_mixer(first_half, second_half):
    """
    Puzzle 1: String Concatenation
    Combine two spell parts to create a complete spell.
    
    Example:
        spell_mixer("Fire", "ball") -> "Fireball"
        spell_mixer("Frost", "bolt") -> "Frostbolt"
    
    Args:
        first_half (str): First part of the spell
        second_half (str): Second part of the spell
        
    Returns:
        str: Complete spell name
    """
    # TODO: Complete this function
    pass


def potion_strength(ingredients, multiplier):
    """
    Puzzle 2: Basic Math Operations
    Calculate the potion strength by multiplying the sum of ingredient values
    
    Example:
        potion_strength([2, 3, 5], 2) -> 20
        potion_strength([1, 1, 1, 1], 3) -> 12
    
    Args:
        ingredients (list): List of ingredient potency values
        multiplier (int): Strength multiplier
        
    Returns:
        int: Total potion strength
    """
    # TODO: Complete this function
    pass


def can_cast_spell(mana_available, mana_cost):
    """
    Puzzle 3: Conditional Logic
    Determine if a spell can be cast based on available mana
    
    Example:
        can_cast_spell(50, 30) -> True
        can_cast_spell(20, 30) -> False
    
    Args:
        mana_available (int): Mana points the wizard has
        mana_cost (int): Mana points required to cast the spell
        
    Returns:
        bool: True if spell can be cast, False otherwise
    """
    # TODO: Complete this function
    pass


def spell_chant(word, times):
    """
    Puzzle 4: Loops and String Repetition
    Create a spell chant by repeating a word a specified number of times
    
    Example:
        spell_chant("Abra", 3) -> "Abra Abra Abra"
        spell_chant("Hocus", 2) -> "Hocus Hocus"
    
    Args:
        word (str): Word to repeat
        times (int): Number of times to repeat
        
    Returns:
        str: Spell chant with words separated by spaces (no trailing space)
    """
    # TODO: Complete this function
    pass


def temperature_converter(temp_value, conversion_direction):
    """
    Puzzle 5: Calculations and Conditionals
    Convert temperature between Celsius and Fahrenheit
    
    Celsius to Fahrenheit: (Celsius * 9/5) + 32
    Fahrenheit to Celsius: (Fahrenheit - 32) * 5/9
    
    Example:
        temperature_converter(100, "C to F") -> 212.0
        temperature_converter(32, "F to C") -> 0.0
    
    Args:
        temp_value (float): Temperature value to convert
        conversion_direction (str): Either "C to F" or "F to C"
        
    Returns:
        float: Converted temperature value
    """
    # TODO: Complete this function
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
    print(f"✅ All tests passed for {func.__name__}!")

def run_tests():
    """Run all tests."""
    # Test spell_mixer
    test_function(
        spell_mixer,
        [("Fire", "ball"), ("Frost", "bolt"), ("Shadow", "step"), ("", "magic")],
        ["Fireball", "Frostbolt", "Shadowstep", "magic"]
    )
    
    # Test potion_strength
    test_function(
        potion_strength,
        [([2, 3, 5], 2), ([1, 1, 1, 1], 3), ([10], 5), ([], 10)],
        [20, 12, 50, 0]
    )
    
    # Test can_cast_spell
    test_function(
        can_cast_spell,
        [(50, 30), (20, 30), (100, 100), (0, 1)],
        [True, False, True, False]
    )
    
    # Test spell_chant
    test_function(
        spell_chant,
        [("Abra", 3), ("Hocus", 2), ("Magic", 1), ("Spell", 0)],
        ["Abra Abra Abra", "Hocus Hocus", "Magic", ""]
    )
    
    # Test temperature_converter
    test_function(
        temperature_converter,
        [(100, "C to F"), (32, "F to C"), (0, "C to F"), (0, "F to C")],
        [212.0, 0.0, 32.0, -17.77777777777778]
    )
    
    print("🎉 Congratulations! You've solved all the puzzles in Module 0, Lesson 1! 🎉")

if __name__ == "__main__":
    try:
        run_tests()
    except AssertionError as e:
        print(f"❌ Test failed: {e}")
        exit(1) 