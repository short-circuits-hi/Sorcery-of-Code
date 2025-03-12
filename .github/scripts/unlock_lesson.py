#!/usr/bin/env python3
"""
Script to unlock the next lesson after a challenge is completed.
"""
import os
import sys
import json
import shutil
from pathlib import Path

def get_next_lesson(current_module, current_lesson):
    """
    Determines the next lesson based on the current module and lesson.
    
    Args:
        current_module (str): Current module
        current_lesson (str): Current lesson
    
    Returns:
        tuple: (next_module, next_lesson)
    """
    # Module progression order
    modules = ["module-0-beginner-review", "module-python", "module-ml", "module-ai-backend"]
    
    # Lessons per module
    lessons_per_module = {
        "module-0-beginner-review": 2,
        "module-python": 2,
        "module-ml": 2,
        "module-ai-backend": 2
    }
    
    # Parse the current lesson number
    current_lesson_num = int(current_lesson.replace("lesson", ""))
    
    # Check if there's another lesson in the same module
    if current_lesson_num < lessons_per_module[current_module]:
        return current_module, f"lesson{current_lesson_num + 1}"
    
    # Move to the next module
    try:
        current_module_index = modules.index(current_module)
        if current_module_index < len(modules) - 1:
            next_module = modules[current_module_index + 1]
            return next_module, "lesson1"
    except ValueError:
        pass
    
    # If we're at the end, return the current module/lesson
    return current_module, current_lesson

def unlock_lesson(module, lesson, user_id):
    """
    Unlocks a lesson by removing the LOCKED.md and generating/revealing the actual lesson content.
    
    Args:
        module (str): Module name
        lesson (str): Lesson name
        user_id (str): GitHub username of the user
    
    Returns:
        bool: True if successful, False otherwise
    """
    base_dir = Path(".")
    lesson_dir = base_dir / module / lesson
    locked_file = lesson_dir / "LOCKED.md"
    hidden_lesson_file = lesson_dir / "lesson.md.encrypted"
    lesson_file = lesson_dir / "lesson.md"
    
    if not locked_file.exists():
        print(f"No locked file found for {module}/{lesson}")
        return False
    
    # Record the unlock in the user's progress file
    user_progress_dir = base_dir / "rewards" / "progress"
    user_progress_dir.mkdir(parents=True, exist_ok=True)
    
    progress_file = user_progress_dir / f"{user_id}.json"
    
    progress_data = {}
    if progress_file.exists():
        with open(progress_file, 'r') as f:
            try:
                progress_data = json.load(f)
            except json.JSONDecodeError:
                progress_data = {}
    
    if 'unlocked_lessons' not in progress_data:
        progress_data['unlocked_lessons'] = []
    
    lesson_key = f"{module}/{lesson}"
    if lesson_key not in progress_data['unlocked_lessons']:
        progress_data['unlocked_lessons'].append(lesson_key)
    
    with open(progress_file, 'w') as f:
        json.dump(progress_data, f, indent=2)
    
    print(f"Recorded unlock in user progress: {user_id} - {module}/{lesson}")
    
    # For this implementation, we'll create a PR that reveals the lesson.md file for this specific user
    # In a real implementation with server-side control, we would have different logic
    
    # Create a new branch for the user's unlock
    branch_name = f"unlock-{user_id}-{module}-{lesson}"
    os.system(f"git checkout -b {branch_name}")
    
    # Create/reveal the lesson file
    if hidden_lesson_file.exists():
        # Copy the encrypted file to the normal location
        shutil.copy(hidden_lesson_file, lesson_file)
    else:
        # If no pre-made content exists, create a basic lesson file
        with open(lesson_file, 'w') as f:
            f.write(f"""# {module.replace('-', ' ').title()} - {lesson.title()}

Congratulations on unlocking this lesson! 

## Learning Objectives

- Objective 1
- Objective 2
- Objective 3

## Content

This lesson content was unlocked based on your completion of the previous challenge.

## Challenge

Check the challenge.py file for your next task.
""")
    
    # Commit and push the changes
    os.system(f"git add {lesson_file}")
    os.system(f"git commit -m 'Unlock {module}/{lesson} for user {user_id}'")
    os.system(f"git push origin {branch_name}")
    
    # Create a PR that's just for this user
    # In a real implementation, this would be handled by a server or GitHub App
    # that can create PRs programmatically
    
    print(f"Unlocked lesson: {module}/{lesson} for user {user_id}")
    return True

def main():
    # Get context from environment variables
    user_id = os.environ.get("GITHUB_ACTOR", "unknown-user")
    
    # Parse PR details to determine which module/lesson was completed
    # This is simplified - in a real implementation, you'd extract this from the PR context
    pr_title = os.environ.get("PR_TITLE", "")
    
    # Default fallback if we can't determine from the PR
    current_module = "module-0-beginner-review"
    current_lesson = "lesson1"
    
    # Try to extract module/lesson from PR title
    # Example PR title: "Solution for module-python/lesson1"
    if "solution for " in pr_title.lower():
        path_part = pr_title.lower().split("solution for ")[1].strip()
        parts = path_part.split("/")
        if len(parts) == 2:
            current_module, current_lesson = parts
    
    next_module, next_lesson = get_next_lesson(current_module, current_lesson)
    
    success = unlock_lesson(next_module, next_lesson, user_id)
    if success:
        print(f"Successfully unlocked {next_module}/{next_lesson} for {user_id}")
        return 0
    else:
        print(f"Failed to unlock {next_module}/{next_lesson}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
