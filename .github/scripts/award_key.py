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
from datetime import datetime

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
        lesson (str): The lesson name
    
    Returns:
        str: The generated key
    """
    key = generate_key()
    
    # Ensure the rewards directory exists
    rewards_dir = Path("rewards")
    rewards_dir.mkdir(exist_ok=True)
    
    # Update leaderboard
    leaderboard_path = rewards_dir / "leaderboard.json"
    if leaderboard_path.exists():
        with open(leaderboard_path, 'r') as f:
            try:
                leaderboard = json.load(f)
            except json.JSONDecodeError:
                leaderboard = {"users": {}}
    else:
        leaderboard = {"users": {}}
    
    if user not in leaderboard["users"]:
        leaderboard["users"][user] = {"keys": [], "badges": [], "progress": []}
    
    # Add key to user's record
    key_entry = {
        "module": module,
        "lesson": lesson,
        "key": key,
        "awarded_at": datetime.now().isoformat()
    }
    leaderboard["users"][user]["keys"].append(key_entry)
    
    # Update progress
    progress_entry = f"{module}/{lesson}"
    if progress_entry not in leaderboard["users"][user]["progress"]:
        leaderboard["users"][user]["progress"].append(progress_entry)
    
    # Award badges based on progress
    badges = leaderboard["users"][user]["badges"]
    
    # Module completion badges
    module_lessons = [dir_name for dir_name in os.listdir(module) if dir_name.startswith("lesson")]
    completed_lessons = [prog.split("/")[1] for prog in leaderboard["users"][user]["progress"] if prog.startswith(module)]
    
    if len(completed_lessons) == len(module_lessons) and f"{module}_master" not in badges:
        badges.append(f"{module}_master")
    
    # Save the updated leaderboard
    with open(leaderboard_path, 'w') as f:
        json.dump(leaderboard, f, indent=2)
    
    # Create a personal key file for the user
    user_keys_dir = rewards_dir / "keys"
    user_keys_dir.mkdir(exist_ok=True)
    
    user_key_file = user_keys_dir / f"{user}_{module}_{lesson}.txt"
    with open(user_key_file, 'w') as f:
        f.write(f"Key for {module}/{lesson}: {key}\n")
        f.write(f"Awarded to: {user}\n")
        f.write(f"Date: {datetime.now().isoformat()}\n")
    
    print(f"Key awarded to {user} for {module}/{lesson}: {key}")
    return key

def main():
    """Main function to award a key to a user based on GitHub Actions context."""
    # Get context from environment variables
    user = os.environ.get("GITHUB_ACTOR", os.environ.get("PR_USER", "unknown-user"))
    module = os.environ.get("MODULE", "module-0-beginner-review")
    lesson = os.environ.get("LESSON", "lesson1")
    
    print(f"Awarding key to {user} for completing {module}/{lesson}")
    key = award_key(user, module, lesson)
    
    # Set the key as an environment variable for other steps
    with open(os.environ.get("GITHUB_ENV", ".env"), "a") as f:
        f.write(f"USER_KEY={key}\n")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
