#!/usr/bin/env python3
"""
Module 0: Beginner Review - Lesson 2 Challenge

Complete the following puzzles to test your understanding of Python data structures and functions.
Each puzzle has instructions and a function shell for you to complete.

Run this file to test your solutions:
    python challenge.py

All tests must pass to earn your key!
"""

def spell_inventory(spells):
    """
    Puzzle 1: List Operations
    Count the number of spells in the inventory and categorize them.
    
    Example:
        spell_inventory(["Fireball", "Ice Lance", "Fireball", "Arcane Missiles"])
        -> {"count": 4, "unique": 3}
    
    Args:
        spells (list): List of spell names
        
    Returns:
        dict: Dictionary with total count and number of unique spells
    """
    # TODO: Complete this function
    pass


def merge_potions(potion1, potion2):
    """
    Puzzle 2: Dictionary Manipulation
    Merge two potion dictionaries. If both dictionaries have the same ingredient key,
    add their values. Return a new dictionary with all ingredients.
    
    Example:
        merge_potions({"mandrake": 2, "toadstool": 1}, {"mandrake": 1, "dragonscale": 3})
        -> {"mandrake": 3, "toadstool": 1, "dragonscale": 3}
    
    Args:
        potion1 (dict): First potion with ingredient names as keys and amounts as values
        potion2 (dict): Second potion with ingredient names as keys and amounts as values
        
    Returns:
        dict: Merged potion dictionary
    """
    # TODO: Complete this function
    pass


def find_highest_score(score_records):
    """
    Puzzle 3: List of Tuples Processing
    Find the player with the highest score from a list of (name, score) tuples.
    
    Example:
        find_highest_score([("Merlin", 95), ("Gandalf", 86), ("Dumbledore", 98), ("Radagast", 74)])
        -> ("Dumbledore", 98)
    
    Args:
        score_records (list): List of (name, score) tuples
        
    Returns:
        tuple: The (name, score) tuple with the highest score
    """
    # TODO: Complete this function
    pass


def format_spellbook(spells):
    """
    Puzzle 4: List and String Manipulation
    Format a spellbook table from a list of spell dictionaries.
    Each spell has a name, element, and power_level.
    
    Example:
        format_spellbook([
            {"name": "Fireball", "element": "Fire", "power_level": 7},
            {"name": "Ice Shard", "element": "Ice", "power_level": 5}
        ])
        -> "NAME      | ELEMENT   | POWER\n--------------------------\nFireball  | Fire      | 7\nIce Shard | Ice       | 5"
    
    Args:
        spells (list): List of spell dictionaries
        
    Returns:
        str: Formatted spellbook table as a string
    """
    # TODO: Complete this function
    pass


def create_spell_function(element):
    """
    Puzzle 5: Function Factory
    Create a spell casting function for a specific element.
    The returned function should take a spell name and power level,
    and return a formatted spell casting message.
    
    Example usage:
        cast_fire = create_spell_function("fire")
        cast_fire("Inferno", 8) -> "Casting fire spell: INFERNO with power 8!"
        
        cast_ice = create_spell_function("ice")
        cast_ice("Blizzard", 6) -> "Casting ice spell: BLIZZARD with power 6!"
    
    Args:
        element (str): Element type for the spell (fire, ice, etc.)
        
    Returns:
        function: A spell casting function specific to the element
    """
    # TODO: Complete this function
    pass


# Test functions - DO NOT MODIFY
def test_function(func, inputs, expected_outputs):
    """Test a function with multiple inputs and expected outputs."""
    for i, (input_args, expected) in enumerate(zip(inputs, expected_outputs)):
        if isinstance(input_args, tuple):
            result = func(*input_args)
        else:
            result = func(input_args)
            
        assert result == expected, f"Test {i+1} failed: {func.__name__}({input_args}) returned {result}, expected {expected}"
    print(f"✅ All tests passed for {func.__name__}!")

def run_tests():
    """Run all tests."""
    # Test spell_inventory
    test_function(
        spell_inventory,
        [
            ["Fireball", "Ice Lance", "Fireball", "Arcane Missiles"],
            ["Lightning Bolt", "Lightning Bolt", "Lightning Bolt"],
            ["Polymorph"],
            []
        ],
        [
            {"count": 4, "unique": 3},
            {"count": 3, "unique": 1},
            {"count": 1, "unique": 1},
            {"count": 0, "unique": 0}
        ]
    )
    
    # Test merge_potions
    test_function(
        merge_potions,
        [
            ({"mandrake": 2, "toadstool": 1}, {"mandrake": 1, "dragonscale": 3}),
            ({"wolfsbane": 3}, {"moonstone": 2}),
            ({}, {"lavender": 1, "mint": 2}),
            ({"ginger": 1, "honey": 2}, {})
        ],
        [
            {"mandrake": 3, "toadstool": 1, "dragonscale": 3},
            {"wolfsbane": 3, "moonstone": 2},
            {"lavender": 1, "mint": 2},
            {"ginger": 1, "honey": 2}
        ]
    )
    
    # Test find_highest_score
    test_function(
        find_highest_score,
        [
            [("Merlin", 95), ("Gandalf", 86), ("Dumbledore", 98), ("Radagast", 74)],
            [("Harry", 85), ("Ron", 78), ("Hermione", 100)],
            [("Solo Player", 50)]
        ],
        [
            ("Dumbledore", 98),
            ("Hermione", 100),
            ("Solo Player", 50)
        ]
    )
    
    # Test format_spellbook
    test_function(
        format_spellbook,
        [
            [
                {"name": "Fireball", "element": "Fire", "power_level": 7},
                {"name": "Ice Shard", "element": "Ice", "power_level": 5}
            ],
            [
                {"name": "Lightning", "element": "Storm", "power_level": 9},
                {"name": "Earthquake", "element": "Earth", "power_level": 8},
                {"name": "Tornado", "element": "Air", "power_level": 7}
            ]
        ],
        [
            "NAME      | ELEMENT   | POWER\n--------------------------\nFireball  | Fire      | 7\nIce Shard | Ice       | 5",
            "NAME      | ELEMENT   | POWER\n--------------------------\nLightning | Storm     | 9\nEarthquake| Earth     | 8\nTornado   | Air       | 7"
        ]
    )
    
    # Test create_spell_function
    cast_fire = create_spell_function("fire")
    cast_ice = create_spell_function("ice")
    
    assert cast_fire("Inferno", 8) == "Casting fire spell: INFERNO with power 8!"
    assert cast_fire("Ember", 3) == "Casting fire spell: EMBER with power 3!"
    assert cast_ice("Blizzard", 6) == "Casting ice spell: BLIZZARD with power 6!"
    assert cast_ice("Frost Nova", 4) == "Casting ice spell: FROST NOVA with power 4!"
    
    print("✅ All tests passed for create_spell_function!")
    
    print("🎉 Congratulations! You've solved all the puzzles in Module 0, Lesson 2! 🎉")
    print("You're now ready to move on to Module 1 and continue your journey to become a coding wizard!")

if __name__ == "__main__":
    try:
        run_tests()
    except AssertionError as e:
        print(f"❌ Test failed: {e}")
        exit(1) 