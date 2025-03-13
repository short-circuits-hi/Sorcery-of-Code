#!/usr/bin/env python3
"""
Script to award keys upon successful challenge completion and update the central leaderboard.
"""
import os
import sys
import json
import random
import string
from pathlib import Path
from datetime import datetime

# Import GitHub API library if available
try:
    from github import Github
    GITHUB_API_AVAILABLE = True
except ImportError:
    GITHUB_API_AVAILABLE = False
    print("Warning: PyGithub not installed. Central leaderboard updates will be skipped.")
    print("To install: pip install PyGithub")

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

def update_central_leaderboard(user, module, lesson, key, github_token):
    """
    Updates the central leaderboard in the main repository using GitHub API.
    
    Args:
        user (str): GitHub username
        module (str): Module name
        lesson (str): Lesson name
        key (str): Generated key
        github_token (str): GitHub token for authentication
    
    Returns:
        bool: True if successful, False otherwise
    """
    if not GITHUB_API_AVAILABLE:
        print("Skipping central leaderboard update: PyGithub not installed")
        return False
    
    if not github_token:
        print("Skipping central leaderboard update: No GitHub token provided")
        return False
    
    try:
        # Connect to GitHub
        g = Github(github_token)
        repo = g.get_repo("short-circuits-hi/Sorcery-of-Code")
        
        # Get the current leaderboard
        leaderboard_file = repo.get_contents("rewards/leaderboard.json")
        leaderboard_content = leaderboard_file.decoded_content.decode()
        leaderboard = json.loads(leaderboard_content)
        
        # Update the leaderboard with the user's progress
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
        
        # Add to latest updates
        if "latest_updates" not in leaderboard:
            leaderboard["latest_updates"] = []
            
        leaderboard["latest_updates"].insert(0, {
            "user": user,
            "module": module,
            "lesson": lesson,
            "timestamp": datetime.now().isoformat()
        })
        
        # Limit latest updates to 20 entries
        leaderboard["latest_updates"] = leaderboard["latest_updates"][:20]
        
        # Update badges based on progress
        badges = leaderboard["users"][user]["badges"]
        
        # Check if all lessons in a module are completed
        module_lessons = get_module_lessons(module)
        completed_lessons = [prog.split("/")[1] for prog in leaderboard["users"][user]["progress"] 
                            if prog.startswith(module)]
        
        badge_id = f"{module}_master"
        if (len(completed_lessons) == len(module_lessons) and 
            badge_id not in badges and
            badge_id in leaderboard.get("badges", {})):
            badges.append(badge_id)
            
            # Add a special update for badge awards
            leaderboard["latest_updates"].insert(0, {
                "user": user,
                "badge": badge_id,
                "badge_name": leaderboard["badges"][badge_id]["name"],
                "timestamp": datetime.now().isoformat()
            })
        
        # Commit the updated leaderboard
        repo.update_file(
            leaderboard_file.path,
            f"Update leaderboard for {user} - {module}/{lesson}",
            json.dumps(leaderboard, indent=2),
            leaderboard_file.sha
        )
        
        print(f"Central leaderboard updated for {user}")
        return True
    except Exception as e:
        print(f"Error updating central leaderboard: {e}")
        return False

def get_module_lessons(module):
    """Get the list of lessons for a module."""
    module_structure = {
        "module-0-beginner-review": ["lesson1", "lesson2"],
        "module-python": ["lesson1", "lesson2"],
        "module-ml": ["lesson1", "lesson2"],
        "module-ai-backend": ["lesson1", "lesson2"]
    }
    return module_structure.get(module, [])

def award_key(user, module, lesson):
    """
    Awards a key to a user for completing a challenge.
    Also updates both local and central leaderboards.
    
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
    
    # Update local leaderboard
    leaderboard_path = rewards_dir / "leaderboard.json"
    if leaderboard_path.exists():
        with open(leaderboard_path, 'r') as f:
            try:
                leaderboard = json.load(f)
            except json.JSONDecodeError:
                leaderboard = {"users": {}}
    else:
        leaderboard = {"users": {}}
    
    # Make sure required fields exist
    if "users" not in leaderboard:
        leaderboard["users"] = {}
    
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
    module_lessons = get_module_lessons(module)
    completed_lessons = [prog.split("/")[1] for prog in leaderboard["users"][user]["progress"] 
                        if prog.startswith(module)]
    
    if len(completed_lessons) == len(module_lessons) and f"{module}_master" not in badges:
        badges.append(f"{module}_master")
    
    # Save the updated local leaderboard
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
    
    # Create user progress file
    user_progress_dir = rewards_dir / "progress"
    user_progress_dir.mkdir(exist_ok=True)
    
    progress_file = user_progress_dir / f"{user}.json"
    
    progress_data = {}
    if progress_file.exists():
        with open(progress_file, 'r') as f:
            try:
                progress_data = json.load(f)
            except json.JSONDecodeError:
                progress_data = {}
    
    if 'unlocked_lessons' not in progress_data:
        progress_data['unlocked_lessons'] = []
    
    if progress_entry not in progress_data['unlocked_lessons']:
        progress_data['unlocked_lessons'].append(progress_entry)
    
    with open(progress_file, 'w') as f:
        json.dump(progress_data, f, indent=2)
    
    # Update central leaderboard using GitHub API
    github_token = os.environ.get("GH_TOKEN", os.environ.get("GITHUB_TOKEN"))
    if github_token:
        update_central_leaderboard(user, module, lesson, key, github_token)
    else:
        print("No GitHub token found. Skipping central leaderboard update.")
    
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
