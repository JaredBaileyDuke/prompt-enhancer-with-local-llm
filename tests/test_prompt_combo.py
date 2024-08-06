"""
Run tests to verify the prompt_combo module
"""

# Imports
import sys
import os

# Get the current file's directory
current_dir = os.path.dirname(os.path.abspath(__file__))
# Get the parent directory
parent_dir = os.path.dirname(current_dir)
# Add the grandparent directory to the system path
sys.path.append(parent_dir)

# disable pylint from having issues with importing from a sibling folder
# pylint: disable=C0413
# pylint: disable=E0401
from source.prompt_combo import prompt_combo



# Define the test functions
def test_prompt_combo():
    """
    Test the prompt_combo function
    """
    # Test case 1
    assert prompt_combo("Where you are from", "New York", "New York City", "NYC") == (
        "Where you are from. Your response should have the following attributes: "
        "New York. New York City. NYC"
        )
    
    # Test case 2
    assert prompt_combo("What you are doing", "Working", "Studying", "Playing") == (
        "What you are doing. Your response should have the following attributes: "
        "Working. Studying. Playing"
        )
    
    # Test case 3
    assert prompt_combo("What you are eating", "Pizza", "Burger", "Salad") == \
        "What you are eating. Your response should have the following attributes: Pizza. Burger. \
            Salad"
    
    # Test case 4
    assert prompt_combo("What you are drinking", "Water", "Soda", "Juice") == \
        "What you are drinking. Your response should have the following attributes: Water. Soda. \
            Juice"
    
    # Test case 5
    assert prompt_combo("What you are wearing", "Shirt", "Pants", "Shoes") == \
        "What you are wearing. Your response should have the following attributes: Shirt. Pants. \
            Shoes"
    
    # Test case 6
    assert prompt_combo("What you are watching", "Movie", "TV Show", "Documentary") == \
        "What you are watching. Your response should have the following attributes: Movie. \
            TV Show. Documentary"
    
    # Test case 7
    assert prompt_combo("What you are reading", "Book", "Magazine", "Newspaper") == \
        "What you are reading. Your response should have the following attributes: Book. \
            Magazine. Newspaper"
    
    # Test case 8
    assert prompt_combo("What you are listening to", "Music", "Podcast", "Audiobook") == \
        "What you are listening to. Your response should have the following attributes: Music. \
            Podcast. Audiobook"
    
    # Test case 9
    assert prompt_combo("What you are playing", "Game", "Sport", "Instrument") == \
        "What you are playing. Your response should have the following attributes: Game. Sport. \
            Instrument"
    
    # Test case 10
    assert prompt_combo("What you are learning", "Language", "Skill", "Subject") == \
        "What you are learning. Your response should have the following attributes: Language. \
            Skill. Subject"
