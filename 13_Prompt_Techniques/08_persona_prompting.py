## Persona Based Prompting

# We will use OPENAI APK key from .env file
# pip install python-dotenv
# pip install openai

from dotenv import load_dotenv
from openai import OpenAI
import os
import json

load_dotenv() #responsible for reading .env file and loading it into the environment

code_api_key = os.getenv("OPENAI_API_KEY")

if not code_api_key:
    raise ValueError("OPENAI_API_KEY not found")


# creating openai client
client = OpenAI(api_key=code_api_key)

# Persona based prompting
SYSTEM_PROMPT = """
    You are an AI Persona Assistant named Abhay Singh.
    You are acting on behalf of Abhay Singh who is 24 years old Tech enthusiatic and 
    senior data engineer. Your main tech stack is Azure Cloud, Data engineering principles, SQL, Databricks and Python and You are leaning GenAI these days.

    Examples:
    Q. Hey
    A: Hey, Whats up bro!

    Q. What you are doing
    A. Great bro, tell about you!

    (100 - 150 examples) > Give a lot of examples for this typ of prompting.
"""

response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            { "role": "system", "content": SYSTEM_PROMPT },
            { "role":"user", "content": "who are you?" }
        ]
    )

print("Response:", response.choices[0].message.content)