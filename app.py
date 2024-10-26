import streamlit as st
import random

# List of supportive responses
responses = [
    "I'm here for you. It’s okay to feel this way.",
    "You are not alone; many people go through this.",
    "Take it one day at a time. You're doing great.",
    "I'm here to listen. Take your time.",
    "Would you like to share more about what's on your mind?",
    "Remember, it's okay to ask for help.",
    "It’s perfectly okay to feel uncertain. Let's work through it together."
]

def get_response(user_input):
    # Basic rule-based response selection
    if "sad" in user_input or "upset" in user_input:
        return "I'm really sorry to hear that you're feeling this way. Let's talk through it."
    elif "anxious" in user_input or "nervous" in user_input:
        return "It's okay to feel anxious. Take a deep breath and let's focus on the present."
    else:
        return random.choice(responses)

# Streamlit setup for chatbot UI
st.title("AI-Powered Mental Health Chatbot")
st.write("I'm here to listen. Type your message below:")

# User input
user_input = st.text_input("You:", "")

# Display response
if user_input:
    response = get_response(user_input.lower())
    st.write("Chatbot:", response)
