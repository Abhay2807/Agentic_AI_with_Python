# We will use OPENAI APK key from .env file
# pip install python-dotenv
# pip install openai

from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv() #responsible for reading .env file and loading it into the environment
# creating openai client
client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role":"system", "content":"You are an Mathematics expert and only know maths. You will only answer math related problems, otherwise just say sorry or tell them to ask math specific problems only no other question",
            "role":"user", "content":"Hey There, give formula for a plus b cube"
        }
    ]
)

print(response.choices[0].message.content)

