import streamlit as st
from utils import generate_text

# Page configuration
st.set_page_config(page_title='My GPT-J Playground', layout="centered")

# Page header
st.header("My very own GPT-J Playground")

# Sidebar title
st.sidebar.title("GPT-J Parameters")

# Length control
length_choice = st.sidebar.select_slider("Length",
                                         options=['very short', 'short', 'medium', 'long', 'very long'],
                                         value='medium',
                                         help="Length of the model response")

# Temperature control
temp = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.5, value=0.6,
                         help="The creativity of the model")

# Repetition penalty control
rep_penalty = st.sidebar.slider("Repetition penalty", min_value=0.9, max_value=2.0, value=1.1,
                                help="Penalises the model for repition")

# Convert length choice to number
length = 30
if length_choice == 'very short':
    length = 5
elif length_choice == 'short':
    length = 15
elif length_choice == 'medium':
    length = 30
elif length_choice == 'long':
    length = 45
elif length_choice == 'very long':
    length = 60

# Prompt text box
prompt = st.text_area("Enter your prompt here:")

# Run button
if st.button("Run"):
    params = {"return_full_text": True,
              "temperature": temp,
              "min_length": len(prompt) // 4 + length - 5,
              "max_length": len(prompt) // 4 + length + 5,
              "do_sample": True,
              "repetition_penalty": rep_penalty,
              "top_k": 20,
              }

    generated_text = generate_text(prompt, params)
    st.subheader("Model response:")
    st.text(generated_text)
