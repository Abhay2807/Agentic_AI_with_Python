# We will use OPENAI APK key from .env file
# pip install python-dotenv
# pip install openai

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv() #responsible for reading .env file and loading it into the environment
# creating openai client
client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role":"user", "content":"Hey There, I am Abhay"
        }
    ]
)

print(response.choices[0].message.content)

