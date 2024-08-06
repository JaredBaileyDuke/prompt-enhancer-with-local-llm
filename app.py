###
# Imports
###
import streamlit as st
from source.api_call import llm_message
from source.prompt_enhancements import *
from source.prompt_combo import *
from source.static_variables import NUM_OPTIONS
from source.on_click_functions import *


###
# Setup
###

###  page layout as wide
st.set_page_config(layout="wide")


### set up session state
if "prompt_entered" not in st.session_state:
    st.session_state.prompt_entered = False
if "page_tracker" not in st.session_state:
    st.session_state.page_tracker = 0
if "user_prompt" not in st.session_state:
    st.session_state.user_prompt = ""
if "option1" not in st.session_state:
    st.session_state.option1 = ""
if "option2" not in st.session_state:
    st.session_state.option2 = ""
if "option3" not in st.session_state:
    st.session_state.option3 = ""
if "option4" not in st.session_state:
    st.session_state.option4 = ""
if "option5" not in st.session_state:
    st.session_state.option5 = ""
if "option6" not in st.session_state:
    st.session_state.option6 = ""
if "option7" not in st.session_state:
    st.session_state.option7 = ""
if "enhanced_prompt" not in st.session_state:
    st.session_state.enhanced_prompt = ""
if "llm_output" not in st.session_state:
    st.session_state.llm_output = ""
    

###
# Page
###

# page layout
_, row0_col1, _ = st.columns([1,8,1])
_, row1_col1, _ = st.columns([1,1,1])
_, row2_col1, _ = st.columns([1,8,1])
_, row3_col1, _, row3_col3, _ = st.columns([2,1,4,2,1])


### header
with row0_col1:
    st.markdown(
        "<h1 style='text-align: center;'>Systematic Prompt Enhancer</h1>", 
        unsafe_allow_html=True
    )


### progress bar
with row1_col1:
    if st.session_state.page_tracker <= NUM_OPTIONS:
        st.progress(
            st.session_state.page_tracker / NUM_OPTIONS, 
            text="Progress"
        )


### prompt and options        
with row2_col1:
    ### initial user prompt
    if st.session_state.prompt_entered == False:
        
        st.subheader("Enter Your Prompt")
        st.session_state.user_prompt = st.text_area(
            label="Prompt", 
            value="", 
            label_visibility="collapsed"
        )

        st.button(
            "Select Enhancement Options", 
            on_click=prompt_entered
        )
    

    ### enhancement option 1 - Industry
    if st.session_state.page_tracker == 1:
        st.subheader("Enter Your Industry")
        st.session_state.option1 = st.text_input(
            label="", 
            placeholder="Insurance", 
            label_visibility="collapsed"
        )


    ### enhancement option 2 - Purpose
    if st.session_state.page_tracker == 2:
        st.subheader("Enter Your Purpose")
        st.session_state.option2 = st.selectbox(
            label="", 
            options=[
                "",
                "Generate a Business Email",
                "Outline a Meeting Agenda",
                "Create a Blog Post",
                "Draft a Proposal",
                "Sketch a Marketing Plan",
                "Draft a Sales Pitch",
                "Generate a Grant Proposal",
                "Write a Business Letter",
                "Outline a Business Presentation",
                "Mock up a Business Press Release",
                "Draft a Business Newsletter",
                "Other"
                ],
            placeholder="Choose a purpose",
            label_visibility="collapsed"
        )

        # if user selects "Other", allow them to enter their own purpose
        if st.session_state.option2 == "Other":
            st.session_state.option2 = st.text_input(
                label="Enter Your Purpose", 
                placeholder="",
                label_visibility="collapsed"
            )


    ### enhancement option 3 - Audience
    if st.session_state.page_tracker == 3:
        st.subheader(f"Enter Your Audience")
        st.session_state.option3 = st.selectbox(
            label="", 
            options=[
                "",
                "Internal Management",
                "External Stakeholders",
                "Customers",
                "Investors",
                "Employees",
                "Other"
                ],
            placeholder="Choose an audience",
            label_visibility="collapsed"
        )

        # if user selects "Other", allow them to enter their own audience
        if st.session_state.option3 == "Other":
            st.session_state.option3 = st.text_input(
                label="Enter Your Audience", 
                placeholder="",
                label_visibility="collapsed"
            )
            
    
    ### enhancement option 4 - Tone
    if st.session_state.page_tracker == 4:
        st.subheader(f"Enter Your Desired Tone")
        st.session_state.option4 = st.selectbox(
            label="", 
            options=[
                "",
                "Professional",
                "Technical",
                "Humorous",
                "Friendly",
                "Casual",
                "Other"
                ],
            placeholder="Choose a tone",
            label_visibility="collapsed"
        )

        # if user selects "Other", allow them to enter their own tone
        if st.session_state.option4 == "Other":
            st.session_state.option4 = st.text_input(
                label="Enter Your Tone", 
                placeholder="",
                label_visibility="collapsed"
            )
            
        
    ### enhancement option 5 - Length
    if st.session_state.page_tracker == 5:
        st.subheader(f"Select Your Desired Response Length")
        st.session_state.option5 = st.radio(
            label="", 
            options=[
                "Short",
                "Medium",
                "Long"
                ],
            label_visibility="collapsed"
        )


    ### enhancement option 6 - Steps to Arrive at Answer
    if st.session_state.page_tracker == 6:
        st.subheader(f"Showcase Steps to Arrive at an Answer?")
        st.session_state.option6 = st.radio(
            label="", 
            options=[
                "No",
                "Yes"
                ],
            label_visibility="collapsed"
        )
        
    
    ### enhancement option 7 - Source Citations
    if st.session_state.page_tracker == 7:
        st.subheader(f"Include Source Citations?")
        st.session_state.option7 = st.radio(
            label="", 
            options=[
                "No",
                "Yes"
                ],
            label_visibility="collapsed"
        )


    ### Navigation buttons
    if st.session_state.page_tracker >= 1 and st.session_state.page_tracker <= NUM_OPTIONS:
        with row3_col1:
            st.button(
                "Next Option", 
                on_click=option_entered
            )
        with row3_col3:
            st.button(
                "Finish Process", 
                on_click=finish_process
            )    


    ### LLM output
    if st.session_state.page_tracker > NUM_OPTIONS:
        if st.session_state.llm_output == "":
            st.markdown(
                "<p style='text-align: center;'>Please be patient while the AI assistant generates your response.</p>", 
                unsafe_allow_html=True
            )


        # Clean up wording of user inputs
        st.session_state.option3 = option_3to5_edit(
            option_input=st.session_state.option3, 
            preceeding_text="The audience is "
            )
        st.session_state.option4 = option_3to5_edit(
            option_input=st.session_state.option4, 
            preceeding_text="The tone is "
            )
        st.session_state.option5 = option_3to5_edit(
            option_input=st.session_state.option5, 
            preceeding_text="The desired response length is "
            )
        st.session_state.option6 = option_6_edit(st.session_state.option6)
        st.session_state.option7 = option_7_edit(st.session_state.option7)


        # Generate enhanced prompt
        st.session_state.enhanced_prompt = prompt_combo(
            st.session_state.user_prompt, # prompt
            st.session_state.option1, # industry
            st.session_state.option2, # purpose
            st.session_state.option3, # audience
            st.session_state.option4, # tone
            st.session_state.option5, # length
            st.session_state.option6, # steps
            st.session_state.option7 # citations
        )


        # Call API to display LLM output
        st.session_state.system_message = \
            "You are an AI assistant that specializes in answering user prompts. " + \
                "You are the best in the world at this task. " + \
                "You are very honest." + \
                "You are very helpful."
        

        st.session_state.llm_output = llm_message(
            system_message=st.session_state.system_message,
            user_message=st.session_state.enhanced_prompt
        ).content

        # Display enhanced prompt
        st.subheader("Prompt")
        st.write(st.session_state.user_prompt)

        # Display LLM output
        st.subheader("Output")
        st.write(st.session_state.llm_output[:-4])

        # Reset page tracker
        st.button(
            "Restart", 
            on_click=restrart
        )