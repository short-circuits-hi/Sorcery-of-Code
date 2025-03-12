#!/usr/bin/env python3
"""
Script to lock lessons in the repository by default.
This script should be run when setting up the repository.
"""
import os
import sys
import json
import shutil
from pathlib import Path

def get_module_structure():
    """
    Get the structure of modules and lessons in the repository.
    
    Returns:
        dict: Dictionary mapping modules to lists of lessons
    """
    structure = {
        "module-0-beginner-review": ["lesson1", "lesson2"],
        "module-python": ["lesson1", "lesson2"],
        "module-ml": ["lesson1", "lesson2"],
        "module-ai-backend": ["lesson1", "lesson2"]
    }
    return structure

def create_locked_file(module, lesson):
    """
    Create a LOCKED.md file for a lesson.
    
    Args:
        module (str): Module name
        lesson (str): Lesson name
    """
    lesson_dir = Path(f"{module}/{lesson}")
    locked_file = lesson_dir / "LOCKED.md"
    lesson_file = lesson_dir / "lesson.md"
    
    # If the lesson file exists, backup it as encrypted
    if lesson_file.exists():
        backup_dir = lesson_dir
        backup_file = backup_dir / "lesson.md.encrypted"
        
        # Ensure directory exists
        backup_dir.mkdir(parents=True, exist_ok=True)
        
        # Copy the lesson file to the backup
        shutil.copy(lesson_file, backup_file)
        
        # Output status
        print(f"Backed up {lesson_file} to {backup_file}")
    
    # Create the LOCKED.md file
    previous_lesson = ""
    lesson_num = int(lesson.replace("lesson", ""))
    
    if lesson_num > 1:
        previous_lesson = f"Module {module.split('-')[-1].title()}, Lesson {lesson_num - 1}"
    else:
        previous_module_idx = list(get_module_structure().keys()).index(module) - 1
        if previous_module_idx >= 0:
            previous_module = list(get_module_structure().keys())[previous_module_idx]
            previous_lesson = f"Module {previous_module.split('-')[-1].title()}, Lesson {len(get_module_structure()[previous_module])}"
    
    locked_message = f"""# 🔒 LESSON LOCKED 🔒

This lesson is currently locked. To unlock it:

1. Complete the challenges in {previous_lesson}
2. Submit your solution via a pull request
3. Wait for the automated tests to pass
4. Use the key you receive to unlock this lesson

Once unlocked, you'll find content about:
- Advanced concepts in {module.replace('-', ' ').title()}
- Practical examples and exercises
- Hands-on challenges to build your skills

Keep practicing, and you'll soon be ready to unlock this lesson!
"""
    
    with open(locked_file, 'w') as f:
        f.write(locked_message)
    
    # Remove the original lesson file if it exists
    if lesson_file.exists():
        os.remove(lesson_file)
    
    print(f"Created LOCKED.md for {module}/{lesson}")
    return True

def lock_all_lessons(first_lesson_unlocked=True):
    """
    Lock all lessons in the repository, except the first lesson if specified.
    
    Args:
        first_lesson_unlocked (bool): Whether to leave the first lesson unlocked
    """
    structure = get_module_structure()
    
    for module, lessons in structure.items():
        for i, lesson in enumerate(lessons):
            # Skip the first lesson of the first module if first_lesson_unlocked is True
            if first_lesson_unlocked and module == "module-0-beginner-review" and lesson == "lesson1":
                print(f"Skipping {module}/{lesson} as it should be unlocked by default")
                continue
            
            create_locked_file(module, lesson)

def main():
    """Main function to lock all lessons."""
    print("Locking all lessons...")
    lock_all_lessons(first_lesson_unlocked=True)
    print("Done!")
    return 0

if __name__ == "__main__":
    sys.exit(main()) 