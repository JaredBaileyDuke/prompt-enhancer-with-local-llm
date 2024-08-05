###
# On Click Functions
###

import streamlit as st


def prompt_entered():
    """
    Command to clear prompt screen and move to next page.
    Args:
        None
    Returns:
        None
    """
    st.session_state.prompt_entered = True
    st.session_state.page_tracker += 1


def option_entered():
    """
    Command to move to next enhancement page.
    Args:
        None
    Returns:
        None
    """
    st.session_state.page_tracker += 1


def finish_process():
    """
    Command to skip to the LLM output page.
    Args:
        None
    Returns:
        None
    """
    st.session_state.page_tracker = 8


def restrart():
    """
    Command to restart the process, reseting the variables.
    The on page if statement will reset the page to the prompt page.
    Args:
        None
    Returns:
        None
    """
    st.session_state.prompt_entered = False
    st.session_state.page_tracker = 0
    st.session_state.user_prompt = ""
    st.session_state.option1 = ""
    st.session_state.option2 = ""
    st.session_state.option3 = ""
    st.session_state.option4 = ""
    st.session_state.option5 = ""
    st.session_state.option6 = ""
    st.session_state.option7 = ""
    st.session_state.enhanced_prompt = ""
    st.session_state.llm_output = ""