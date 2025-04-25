import streamlit as st

# Set up the page configuration
st.set_page_config(
    page_title="Multipage App",
    page_icon="🐬"
)

# Define the main page function
def main_page():
    st.title("Home Page")
    st.sidebar.success('Select a page above')
    if "my_input" not in st.session_state:
        st.session_state["my_input"] = ""
    my_input = st.text_input("Input a text here", st.session_state["my_input"])
    submit = st.button("Submit")
    if submit:
        st.session_state["my_input"] = my_input
        st.write("You have entered:", my_input)

# Call the main page function
main_page()