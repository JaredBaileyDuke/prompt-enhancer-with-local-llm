###
# Imports
###
import streamlit as st

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
_, row1_col1, _ = st.columns([1,8,1])
_, row2_col1, row2_col2, _ = st.columns([1, column_width, column_width, 1])

with row0_col1:
    ### title
    st.title("Prompt Enhancer with a Local LLM")
    st.write("By Jared Bailey")

    ### initial user prompt
    st.subheader("Enter a Prompt")
    user_prompt = st.text_area("Prompt", "Once upon a time")

    ### user options as checkboxes
    st.subheader("Options")
    option1 = st.checkbox("Option 1")
    option2 = st.checkbox("Option 2")
    option3 = st.checkbox("Option 3")

### generate button
with row1_col1:
    if st.button("Generate"):
        st.write("Generating...")

        with row2_col1:
            # generate output
            output = "This is a generated output from the original prompt."

            # display output
            st.write(output)

        with row2_col2:
            # generate output
            output = "This is a generated output from the enhanced prompt."

            # display output
            st.write(output)