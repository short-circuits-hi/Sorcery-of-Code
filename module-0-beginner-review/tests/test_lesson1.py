#!/usr/bin/env python3
"""
Test file for module-0-beginner-review/lesson1/challenge.py
"""
import pytest
import sys
import os
from importlib.util import spec_from_file_location, module_from_spec

# Import the challenge solution
def import_challenge(module_path, lesson_name):
    challenge_path = os.path.join(module_path, lesson_name, "challenge.py")
    if not os.path.exists(challenge_path):
        return None
    
    spec = spec_from_file_location("challenge", challenge_path)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

challenge = import_challenge("module-0-beginner-review", "lesson1")

# Define the tests
def test_challenge_imported():
    """Test that the challenge module was imported correctly"""
    assert challenge is not None, "Could not import challenge.py"

def test_variables():
    """Test that the required variables are defined with correct values"""
    if hasattr(challenge, 'name'):
        assert isinstance(challenge.name, str), "name should be a string"
        assert len(challenge.name) > 0, "name should not be empty"
    
    if hasattr(challenge, 'level'):
        assert isinstance(challenge.level, int), "level should be an integer"
        assert challenge.level > 0, "level should be positive"

def test_functions():
    """Test that the required functions are defined and work correctly"""
    # Test celsius_to_fahrenheit function if it exists
    if hasattr(challenge, 'celsius_to_fahrenheit'):
        assert challenge.celsius_to_fahrenheit(0) == 32, "0°C should convert to 32°F"
        assert challenge.celsius_to_fahrenheit(100) == 212, "100°C should convert to 212°F"
        assert challenge.celsius_to_fahrenheit(25) == 77, "25°C should convert to 77°F"
    
    # Test is_even_or_odd function if it exists
    if hasattr(challenge, 'is_even_or_odd'):
        assert challenge.is_even_or_odd(2) == "even", "2 should be even"
        assert challenge.is_even_or_odd(7) == "odd", "7 should be odd"
        assert challenge.is_even_or_odd(0) == "even", "0 should be even"

# Run the tests
if __name__ == "__main__":
    pytest.main(["-v", __file__]) 