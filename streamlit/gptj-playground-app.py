import streamlit as st
from utils import generate_text

# Page configuration
st.set_page_config(page_title='My GPT-J Playground', layout="centered")

# Page header
st.header("My very own GPT-J Playground")

# Sidebar
st.sidebar.title("GPT-J Parameters")
length_choice = st.sidebar.select_slider("Length", options=['very short', 'short', 'medium', 'long', 'very long'],
                                         value='medium',
                                         help="Length of the model response")
temp = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.5, value=0.6,
                         help="The creativity of the model")
rep_penalty = st.sidebar.slider("Repetition penalty", min_value=0.9, max_value=2.0, value=1.1,
                                help="Penalises the model for repition")

# Prompt text box
prompt = st.text_area("Enter your prompt here:")

if st.button("Run"):
    generated_text = generate_text(prompt)
    st.subheader("Model response:")
    st.write(generated_text)