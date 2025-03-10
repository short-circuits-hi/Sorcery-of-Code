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
    modules = ["module-python", "module-ml", "module-ai-backend"]
    
    # Each module has 2 lessons for now
    lessons_per_module = {mod: 2 for mod in modules}
    
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

def unlock_lesson(module, lesson):
    """
    Unlocks a lesson by replacing LOCKED.md with the actual lesson content.
    
    Args:
        module (str): Module name
        lesson (str): Lesson name
    
    Returns:
        bool: True if successful, False otherwise
    """
    lesson_dir = Path(f"{module}/{lesson}")
    locked_file = lesson_dir / "LOCKED.md"
    
    if not locked_file.exists():
        print(f"No locked file found for {module}/{lesson}")
        return False
    
    # In a real implementation, this would decrypt or transform the locked file
    # For now, we'll simply create a placeholder
    lesson_file = lesson_dir / "lesson.md"
    
    with open(lesson_file, 'w') as f:
        f.write(f"""# {module.replace('-', ' ').title()} - {lesson.title()}

Congratulations on unlocking this lesson! This content was previously locked.

## Learning Objectives

- Objective 1
- Objective 2
- Objective 3

## Content

This is placeholder content for the unlocked lesson.

## Challenge

Check the challenge.py file for your next task.
""")
    
    print(f"Unlocked lesson: {module}/{lesson}")
    return True

def main():
    # This is a placeholder - in a real implementation, get these from the validation context
    current_module = "module-python"
    current_lesson = "lesson1"
    
    next_module, next_lesson = get_next_lesson(current_module, current_lesson)
    
    success = unlock_lesson(next_module, next_lesson)
    if success:
        print(f"Successfully unlocked {next_module}/{next_lesson}")
        return 0
    else:
        print(f"Failed to unlock {next_module}/{next_lesson}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
