"""
This module contains functions that prepare the user input for the LLM.
"""

def option_3to5_edit(option_input, preceeding_text):
    """
    Minor edit to the user input for options 3-5.
    Args:
        input: str
        preceeding_text: str
    Returns:
        str
    """
    if option_input == "":
        return option_input
    return preceeding_text + option_input.lower()
    

def option_6_edit(option_input):
    """
    Edit to the user input for option 6, making it readable for the LLM.
    Args:
        input: str
    Returns:
        str
    """
    if option_input == "Yes":
        return "Showcase your steps to arrive at an answer"
    return ""
    

def option_7_edit(option_input):
    """
    Edit to the user input for option 7, making it readable for the LLM.
    Args:
        input: str
    Returns:
        str
    """
    if option_input == "Yes":
        return "Include a source citations in your response"
    return ""
