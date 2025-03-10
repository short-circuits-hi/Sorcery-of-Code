# Module 0: Beginner Review - Lesson 1: Python Fundamentals

Welcome to the beginning of your magical journey! This quick review will refresh your Python basics before we dive deeper.

## Learning Objectives
- Understand Python variables and basic data types
- Master simple operations and string manipulation
- Learn to use control structures (if statements and loops)
- Practice with mini-puzzles

## Python Variables and Data Types

In Python, variables are created when you assign a value:

```python
# Variable assignment
name = "Apprentice"  # String
level = 1            # Integer
power = 98.6         # Float
is_wizard = True     # Boolean

# Python figures out the type automatically
print(type(name))    # <class 'str'>
print(type(level))   # <class 'int'>
```

### Strings
Magical incantations (strings) can be manipulated:

```python
spell = "Lumos"
print(spell.upper())      # LUMOS
print(len(spell))         # 5
print(spell[0])           # L
print(spell[-1])          # s
print(spell + " Maxima")  # Lumos Maxima
```

### Numbers
Perform arithmetical operations:

```python
# Basic operations
potion_strength = 10 + 5   # Addition: 15
mana_left = 100 - 30       # Subtraction: 70
damage = 5 * 4             # Multiplication: 20
spell_shares = 100 / 4     # Division: 25.0 (returns float)
spell_slots = 10 // 3      # Integer division: 3
mana_remainder = 10 % 3    # Modulo: 1
power_level = 2 ** 3       # Exponentiation: 8
```

## Control Structures

### Conditional Statements
Make decisions based on conditions:

```python
mana = 50

if mana >= 100:
    print("Cast powerful spell!")
elif mana >= 50:
    print("Cast medium spell!")
else:
    print("Not enough mana, use a minor spell.")
```

### Loops
Repeat actions with loops:

```python
# For loop with range
for i in range(5):  # 0, 1, 2, 3, 4
    print(f"Casting spell attempt {i+1}")

# While loop
countdown = 3
while countdown > 0:
    print(f"{countdown}...")
    countdown -= 1
print("Spell activated!")

# Loop through a collection
spells = ["Fireball", "Frostbolt", "Arcane Missile"]
for spell in spells:
    print(f"Learned: {spell}")
```

## Mini-Puzzle Examples

**Puzzle 1**: Convert temperature from Celsius to Fahrenheit
```python
# Formula: (Celsius * 9/5) + 32
celsius = 25
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C is {fahrenheit}°F")  # 25°C is 77.0°F
```

**Puzzle 2**: Check if a number is even or odd
```python
number = 7
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")  # 7 is odd
```

## Challenge

Open the `challenge.py` file to solve a series of beginner-level puzzles that test your understanding of Python basics. Complete all puzzles correctly to unlock the next lesson!

## Next Steps

After completing this lesson's challenges, you'll receive a key to unlock Lesson 2, where we'll cover lists, dictionaries, and basic functions. 