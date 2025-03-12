#!/usr/bin/env python3
"""
Script to validate a challenge solution and determine if it meets all requirements.
"""
import os
import sys
import json
import pytest
import importlib.util
from pathlib import Path

def validate_challenge(module, lesson):
    """
    Validates if a challenge solution is correct by running tests.
    
    Args:
        module (str): Module name
        lesson (str): Lesson name
    
    Returns:
        bool: True if the challenge is valid, False otherwise
    """
    print(f"Validating challenge: {module}/{lesson}")
    
    # Check if we have tests for this challenge
    test_file = Path(f"{module}/tests/test_{lesson}.py")
    challenge_file = Path(f"{module}/{lesson}/challenge.py")
    
    if not test_file.exists():
        print(f"No test file found for {module}/{lesson}")
        return False
    
    if not challenge_file.exists():
        print(f"No challenge file found for {module}/{lesson}")
        return False
    
    try:
        # Run pytest programmatically
        result = pytest.main([str(test_file), "-v"])
        
        # pytest.main returns 0 for success, non-zero for failures
        is_valid = result == 0
        
        if is_valid:
            print(f"✅ Challenge validation successful for {module}/{lesson}!")
        else:
            print(f"❌ Challenge validation failed for {module}/{lesson}. Please check your solution.")
        
        return is_valid
    except Exception as e:
        print(f"Error validating challenge: {e}")
        return False

def main():
    """Main function to validate a challenge based on GitHub Actions context."""
    # Get context from environment variables
    module = os.environ.get("MODULE", "module-0-beginner-review")
    lesson = os.environ.get("LESSON", "lesson1")
    
    print(f"Validating solution for {module}/{lesson}")
    
    result = validate_challenge(module, lesson)
    
    # Set the validation result as an environment variable for other steps
    with open(os.environ.get("GITHUB_ENV", ".env"), "a") as f:
        f.write(f"VALIDATION_SUCCESS={'true' if result else 'false'}\n")
    
    if result:
        return 0
    else:
        return 1

if __name__ == "__main__":
    sys.exit(main())
