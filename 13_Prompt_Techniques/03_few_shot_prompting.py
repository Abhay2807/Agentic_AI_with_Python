# We will use OPENAI APK key from .env file
# pip install python-dotenv
# pip install openai

from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv() #responsible for reading .env file and loading it into the environment
# creating openai client
client = OpenAI()

# Few Shot Prompting
# Giving instructions directly to the LLM along with few examples

SYSTEM_PROMPT="""You should only and only response for the coding problems. Do not answer anything else. Your name is Codex. If user asks any problem not related to coding just say sorry to them! 

Examples

Q: Tell me a Joke
A: Sorry, only coding stuff.

Q: Python code to add two numbers
A: def add_num(a,b):
    return a+b

"""
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role":"system", "content":SYSTEM_PROMPT},
        {"role":"user", "content":"Python code to add 3 numbers"}]
)
print(response.choices[0].message.content)

