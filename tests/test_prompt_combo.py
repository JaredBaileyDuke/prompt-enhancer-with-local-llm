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
    assert prompt_combo("Where you are from", "New York", "NYC") == \
        "Where you are from. Your response should have the following attributes: " + \
        "New York. NYC"
    # Test case 2
    assert prompt_combo("What you are doing", "Working", "Studying", "Playing") == \
        "What you are doing. Your response should have the following attributes: " + \
        "Working. Studying. Playing"
    # Test case 3
    assert prompt_combo("What you are eating", "Pizza") == \
        "What you are eating. Your response should have the following attributes: " + \
        "Pizza"
    # Test case 4
    assert prompt_combo("What you are drinking") == \
        "What you are drinking. Your response should have the following attributes: "
