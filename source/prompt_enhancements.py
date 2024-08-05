def option3_edit(input):
    """
    Minor edit to the user input for option 3.
    Args:
        input: str
    Returns:
        str
    """
    if input == "":
        return input
    else:
        return "The audience is " + input.lower()
    

def option4_edit(input):
    """
    Minor edit to the user input for option 4.
    Args:
        input: str
    Returns:
        str
    """
    if input == "":
        return input
    else:
        return "The tone is " + input.lower()
    

def option5_edit(input):
    """
    Minor edit to the user input for option 5.
    Args:
        input: str
    Returns:
        str
    """
    if input == "":
        return input
    else:
        return "The desired response length is " + input.lower()
    

def option6_edit(input):
    """
    Edit to the user input for option 6, making it readable for the LLM.
    Args:
        input: str
    Returns:
        str
    """
    if input == "No":
        return ""
    else:
        return "Showcase your steps to arrive at an answer"
    

def option7_edit(input):
    """
    Edit to the user input for option 7, making it readable for the LLM.
    Args:
        input: str
    Returns:
        str
    """
    if input == "No":
        return ""
    else:
        return "Include a source citations in your response"