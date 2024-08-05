# have prompt and a variable number of arguments
# return a string that is the prompt followed by the arguments separated by a period and a space
def prompt_combo(prompt, *args):
    """
    Combines a prompt and a variable number of arguments into a single string.
    Args:
        prompt: string
        args: strings
    Returns:
        string
    """
    return prompt + ". Your response should have the following attributes: " + ". ".join(args)


if __name__ == "__main__":
    print(prompt_combo("Where you are from", "New York", "New York City", "NYC"))