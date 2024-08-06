"""
Run tests to verify the prompt_enhancements module
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

from source.prompt_enhancements import option_3to5_edit, option_6_edit, option_7_edit





def test_option_3to5_edit():
    """
    Test the option_3to5_edit function
    """
    # Test case 1
    assert option_3to5_edit("", "") == ""
    # Test case 2
    assert option_3to5_edit("", "New York") == ""
    # Test case 3
    assert option_3to5_edit("New York City", "New York, ") == "New York, new york city"
    # Test case 4
    assert option_3to5_edit("NYC", "New York ") == "New York nyc"


def test_option_6_edit():
    """
    Test the option_6_edit function
    """
    # Test case 1
    assert option_6_edit("No") == ""
    # Test case 2
    assert option_6_edit("Yes") == "Showcase your steps to arrive at an answer"
    # Test case 3
    assert option_6_edit("") == ""


def test_option_7_edit():
    """
    Test the option_7_edit function
    """
    # Test case 1
    assert option_7_edit("No") == ""

    # Test case 2
    assert option_7_edit("Yes") == "Include a source citations in your response"

    # Test case 3
    assert option_7_edit("") == ""
