import streamlit as st

# Set the page title
st.title('Welcome to My Streamlit App')

# Ask the user for their name
user_name = st.text_input('What is your name?')

# Greet the user
if user_name:
    st.write(f'Hello, {user_name}! Welcome to your first Streamlit app.')
