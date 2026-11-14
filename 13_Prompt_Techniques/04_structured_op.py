# We will use OPENAI APK key from .env file
# pip install python-dotenv
# pip install openai

from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv() #responsible for reading .env file and loading it into the environment
# creating openai client
client = OpenAI()

# Structured Output Response with Few Shot Prompting > Structured Output Prompting
# Define the rules properly with examples
SYSTEM_PROMPT="""You should only and only response for the coding problems. Do not answer anything else. Your name is Codex. If user asks any problem not related to coding just say sorry to them! 

Rule:
- Strictly Follow the output in JSON Format, as per given examples.

Output Format:
{{"code":"string" or null, "is_coding_que":Boolean}}

Examples

Q: Tell me a Joke
A: {{"code":null, "is_coding_que":False}}

Q: Python code to add two numbers
A: {{"code":"def num_add(a,b): return (a+b)", "is_coding_que":True}}

"""
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role":"system", "content":SYSTEM_PROMPT},
        {"role":"user", "content":"code to get Sum of n numbers in Kotlin"}]
)
print(response.choices[0].message.content)

