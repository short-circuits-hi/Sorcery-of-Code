#!/usr/bin/env python3
"""
Script to award keys upon successful challenge completion.
"""
import os
import sys
import json
import random
import string
from pathlib import Path

def generate_key():
    """
    Generates a unique key as a reward for completing a challenge.
    
    Returns:
        str: A unique key
    """
    # Generate a random key
    key_chars = string.ascii_letters + string.digits
    key = ''.join(random.choice(key_chars) for _ in range(16))
    return key

def award_key(user, module, lesson):
    """
    Awards a key to a user for completing a challenge.
    
    Args:
        user (str): The GitHub username of the user
        module (str): The module name
        lesson (str): The lesson number
    
    Returns:
        str: The generated key
    """
    key = generate_key()
    
    # Update leaderboard
    leaderboard_path = Path("rewards/leaderboard.json")
    if leaderboard_path.exists():
        with open(leaderboard_path, 'r') as f:
            leaderboard = json.load(f)
    else:
        leaderboard = {"users": {}}
    
    if user not in leaderboard["users"]:
        leaderboard["users"][user] = {"keys": [], "badges": []}
    
    leaderboard["users"][user]["keys"].append({
        "module": module,
        "lesson": lesson,
        "key": key
    })
    
    with open(leaderboard_path, 'w') as f:
        json.dump(leaderboard, f, indent=2)
    
    print(f"Key awarded to {user} for {module}/{lesson}: {key}")
    return key

def main():
    # This is a placeholder - in a real implementation, get these from the PR context
    user = os.environ.get("GITHUB_ACTOR", "test-user")
    module = "module-python"
    lesson = "lesson1"
    
    key = award_key(user, module, lesson)
    
    # In a real implementation, this key could be used to unlock the next lesson
    return 0

if __name__ == "__main__":
    sys.exit(main())
