# Module 0: Beginner Review - Lesson 2: Data Structures & Functions

Congratulations on unlocking this lesson! Now, let's explore Python's data structures and learn about functions.

## Learning Objectives
- Master Python's main collection types: lists, tuples, and dictionaries
- Understand how to manipulate and process collections of data
- Learn to define and use functions
- Practice working with data structures

## Python Collections

### Lists
Lists are ordered, mutable collections:

```python
# Creating lists
spells = ["Fireball", "Ice Lance", "Arcane Missiles"]
mixed_list = [1, "wizard", True, 3.14]

# Accessing elements
print(spells[0])           # Fireball
print(spells[-1])          # Arcane Missiles

# Modifying lists
spells.append("Frostbolt")  # Add to end
spells.insert(1, "Blink")   # Insert at index
removed = spells.pop()      # Remove and return last item
spells.remove("Fireball")   # Remove by value

# Slicing lists
first_two = spells[0:2]     # Get first two elements
reversed_list = spells[::-1]  # Reverse the list

# List operations
inventory = ["potion", "scroll"]
all_items = spells + inventory  # Concatenate lists
spell_count = len(spells)     # Get list length
```

### Tuples
Tuples are like immutable lists:

```python
# Creating tuples
coordinates = (10, 20)
single_item = (42,)  # Note the comma

# Accessing elements
x, y = coordinates   # Unpacking
print(x)             # 10

# Tuples are immutable
# coordinates[0] = 15  # This would raise an error
```

### Dictionaries
Dictionaries store key-value pairs:

```python
# Creating dictionaries
wizard = {
    "name": "Merlin",
    "level": 10,
    "spells": ["Fireball", "Teleport"],
    "health": 100
}

# Accessing values
print(wizard["name"])     # Merlin
print(wizard.get("mana", 0))  # 0 (default if key doesn't exist)

# Modifying dictionaries
wizard["mana"] = 50       # Add or update a key
wizard.update({"level": 11, "experience": 1000})  # Update multiple
del wizard["health"]      # Delete a key

# Dictionary operations
keys = wizard.keys()      # Get all keys
values = wizard.values()  # Get all values
items = wizard.items()    # Get all key-value pairs

# Checking for keys
if "spells" in wizard:
    print("Wizard knows spells!")
```

## Functions

Functions are reusable blocks of code:

```python
# Defining a function
def greet_wizard(name):
    """This function greets a wizard."""  # Docstring
    return f"Greetings, Wizard {name}!"

# Calling a function
message = greet_wizard("Gandalf")
print(message)  # Greetings, Wizard Gandalf!

# Default parameters
def cast_spell(spell_name, mana_cost=10):
    return f"Casting {spell_name} for {mana_cost} mana!"

print(cast_spell("Fireball"))     # Casting Fireball for 10 mana!
print(cast_spell("Lightning", 20))  # Casting Lightning for 20 mana!

# Multiple parameters and return values
def calculate_damage(base, multiplier, critical=False):
    damage = base * multiplier
    if critical:
        damage *= 2
    return damage, "critical" if critical else "normal"

damage, hit_type = calculate_damage(10, 1.5, True)
print(f"Dealt {damage} {hit_type} damage!")  # Dealt 30 critical damage!
```

## Mini-Puzzle Examples

**Puzzle 1**: Find the highest value in a list
```python
scores = [75, 92, 86, 45, 98]
highest = max(scores)
print(f"Highest score: {highest}")  # Highest score: 98
```

**Puzzle 2**: Count word occurrences in a list
```python
words = ["spell", "potion", "wizard", "spell", "magic", "potion", "spell"]
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(word_count)  # {'spell': 3, 'potion': 2, 'wizard': 1, 'magic': 1}
```

## Challenge

Open the `challenge.py` file to solve a series of puzzles focused on data structures and functions. These challenges will test your ability to work with Python collections and define useful functions.

## Next Steps

After completing this module's challenges, you'll be ready to move on to Module 1, where we'll dive into more advanced Python concepts and best practices! 