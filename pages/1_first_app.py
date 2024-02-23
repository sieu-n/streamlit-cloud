import streamlit as st

st.set_page_config(page_title="First App", page_icon="📈")

# Set the page title
st.title('Welcome to My First App')

# Ask the user for their name
user_name = st.text_input('What is your name?')

# Greet the user
if user_name:
    st.write(f'Hello, {user_name}! Welcome to your first Streamlit app.')
