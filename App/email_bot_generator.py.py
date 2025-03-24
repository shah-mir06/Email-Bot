
import streamlit as st
from openai import OpenAI
from api import api_for_bot

client = OpenAI(
    api_key= api_for_bot
)

def generate_email(prompt):
    """
    Function to generate a professional email based on user input.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini", 
            messages=[
                {"role": "system", "content": "You are a professional email assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {e}"

st.title("Welcome to Professional Email Generator.")
st.write("Generate professional emails easily!")

user_input = st.text_area("Describe the email you need:")

if st.button("Generate Email"):
    if user_input.strip():
        email_prompt = f"Write a professional email for the following requirement: {user_input}"
        email_text = generate_email(email_prompt)
        
        st.subheader("Here is Your Email:")
        st.write(email_text)
        st.write("Thanks For Using")
        st.write("Stay Happy & Blessed!")
    else:
        st.warning("Please enter a description to generate an email.")
        
st.markdown("Developed By **Shah Mir Usman**")