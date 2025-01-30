# Copyright (c) 2025 Louis Jouret
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import streamlit as st
from app.model import load_summarizer

# Initialize session state for text input and output
if 'text_input' not in st.session_state:
    st.session_state.text_input = ""
if 'summary_output' not in st.session_state:
    st.session_state.summary_output = ""

# Load model
summarizer = load_summarizer()

# Streamlit UI
st.title("📝 SummarAIze: AI Text Summarizer")

# Callback function to clear text input and output


def clear_text():
    st.session_state.text_input = ""
    st.session_state.summary_output = ""


# Text input with session state
text = st.text_area("Enter text to summarize:",
                    value=st.session_state.text_input, key="text_input")

# Create two columns for buttons
col1, col2 = st.columns(2)

# Summarize button
if col1.button("Summarize"):
    if text:
        summary = summarizer(text, max_length=150,
                             min_length=50, do_sample=False)
        st.session_state.summary_output = summary[0]["summary_text"]
    else:
        st.error("Please enter text before summarizing.")

# Clear button
col2.button("Clear", on_click=clear_text)

# Display summary output
if st.session_state.summary_output:
    st.subheader("Summary:")
    st.write(st.session_state.summary_output)
