# MiniChatbotStreamlit
Github Link
https://github.com/YinYinPhyo/MiniChatbotStreamlit


Part 1: Preparing the project.
Step 1: Prepare the Python Environment.

At Terminal

python3 -m venv myenv
source myenv/bin/activate

pip install --upgrade pip (Optional but recommended)
pip install openai (Install the openai API package)

Step 2: Create an OpenAI API Key.
First, go to the OpenAI platform. “Create new secret key”

Step 3: Loading OpenAI API Key.
Option 1: Using Environment Variables.

At VSCode Terminal
1. Set an environment variable
export OPENAI_API_KEY="your_openai_api_key_here"
2. Access the environment variable in Python:

import os

openai_api_key = os.getenv('OPENAI_API_KEY')
if not openai_api_key:
    raise ValueError("No API key found in environment variables")


Step 2: Install the necessary packages.

For the project we’ll need:
OpenAI API: openai— the library to use OpenAI models via API calls.

Streamlit: streamlit — to create a User Interface for the chatbot.

Python Dotenv: python-dotenv — to load secret variables from the .env
file.

Tiktoken: tiktoken — for counting tokens.

pip install openai streamlit python-dotenv tiktoken

Part 2: Getting responses from OpenAI API.

Output
<img width="1106" alt="result" src="https://github.com/user-attachments/assets/266a5ae3-127f-4d68-aa53-ed715340c9b8">


### chatbot.py

```python
# This is a Python code snippet
=======

import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()
st.title("My GPT-4o Mini Chatbot 🤖")
# Initialize messages in the session state
if "messages" not in st.session_state:
    st.session_state.messages = []
# Display messages
for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
if user_prompt := st.chat_input("Your Prompt:"):
    st.session_state.messages.append({"role": "user","content": user_prompt})
    with st.chat_message("user"):
        st.markdown(user_prompt)
    with st.chat_message("assistant"):
        chatbot_msg = st.empty()
        full_response = ""
        stream = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": msg["role"],
                "content": msg["content"]}
                for msg in st.session_state["messages"]
            ],
            stream=True,
        )
        for chunk in stream:
            token = chunk.choices[0].delta.content
            if token is not None:
                    full_response = full_response + token
                    chatbot_msg.markdown(full_response)
        chatbot_msg.markdown(full_response)
    st.session_state.messages.append({"role": "assistant","content": full_response})


