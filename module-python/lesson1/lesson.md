# Python Module - Lesson 1: Python Fundamentals Review

Welcome to the first lesson of the Sorcery of Code Python module! Let's start by refreshing our Python fundamentals.

## Learning Objectives

- Review Python basic syntax and data types
- Understand control structures and loops
- Master list comprehensions and dictionary operations
- Practice solving small coding challenges

## Python Basics Review

### Data Types
Python has several built-in data types:
- Numbers (int, float, complex)
- Strings
- Lists
- Tuples
- Dictionaries
- Sets

### Control Structures
```python
# If statements
x = 10
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")

# For loops
for i in range(5):
    print(i)  # Prints 0, 1, 2, 3, 4

# While loops
count = 0
while count < 5:
    print(count)
    count += 1
```

### List Comprehensions
```python
# Generate a list of squares
squares = [x**2 for x in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Filter even numbers
even_numbers = [x for x in range(20) if x % 2 == 0]
print(even_numbers)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```

## Challenge

Now it's your turn! Open the `challenge.py` file to complete the exercises. Once you've solved all the challenges, submit a pull request to earn your first key!

## Next Steps

After completing this lesson's challenge, you'll receive a key to unlock Lesson 2, where we'll dive deeper into intermediate Python concepts.
