###
# Imports
###
import streamlit as st
from source.api_call import llm_message

###
# setup
###

### constants

# page layout as wide
st.set_page_config(layout="wide")

# column width
column_width = 4


###
# Page
###

# page layout
_, row0_col1, _ = st.columns([1,8,1])
_, row1_col1, row1_col2, row1_col3, row1_col4, _ = st.columns([1, 2,2,2,2, 1])
_, row2_col1, row2_col2, row2_col3, _ = st.columns([1, 2,2,4, 1])
_, row3_col1, _ = st.columns([1,8,1])
_, row4_col1, row4_col2, _ = st.columns([1, column_width, column_width, 1])

### prompt and options
with row0_col1:
    ### header
    st.markdown("<h1 style='text-align: center;'>Prompt Enhancement with a Local LLM</h1>", unsafe_allow_html=True)

    ### initial user prompt
    st.subheader("Enter Your Prompt")
    user_prompt = st.text_area(label="Prompt", value="Once upon a time", label_visibility="collapsed")

    ### options
    st.write("")
    st.subheader("Enhancement Options")
    with row1_col1:
        option1 = st.checkbox("Short Response")
    with row1_col2:
        option1 = st.checkbox("Long Response")
    with row1_col3:
        option2 = st.checkbox("Professional Tone")
    with row1_col4:
        option3 = st.checkbox("Forbid Clichés")

    with row2_col1:
        option4 = st.checkbox("Provide Source Citations")
    with row2_col2:
        option5 = st.checkbox("Detailed Response")
    with row2_col3:
        option6 = st.checkbox("Provide Steps Taken to Arrive at Answer")
    # in the style of an email

### generate button
with row3_col1:
    if st.button("Generate"):
        st.write("Generating...")

        with row4_col1:
            # generate output
            output1 = "This is a generated output from the original prompt."

            # display output
            st.write(output1)

        with row4_col2:
            # generate output
            output2 = llm_message(user_message="Write 1 sentence about llamas.").content
            

            # display output
            st.write(output2)