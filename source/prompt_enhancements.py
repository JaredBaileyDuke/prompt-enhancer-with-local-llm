def option_3to5_edit(input, preceeding_text):
    """
    Minor edit to the user input for options 3-5.
    Args:
        input: str
        preceeding_text: str
    Returns:
        str
    """
    if input == "":
        return input
    else:
        return preceeding_text + input.lower()
    

def option_6_edit(input):
    """
    Edit to the user input for option 6, making it readable for the LLM.
    Args:
        input: str
    Returns:
        str
    """
    if input == "Yes":
        return "Showcase your steps to arrive at an answer"
    else:
        return ""
    

def option_7_edit(input):
    """
    Edit to the user input for option 7, making it readable for the LLM.
    Args:
        input: str
    Returns:
        str
    """
    if input == "Yes":
        return "Include a source citations in your response"
    else:
        return ""