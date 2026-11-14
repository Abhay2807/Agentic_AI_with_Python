# Using google gemini APK key
# pip install -U google-genai


from dotenv import load_dotenv
from google import genai
import os
import time

print("Step 1: Loading environment variables...")
load_dotenv()

print("Step 2: Creating Gemini client...")
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

print("Step 3: Sending request to Gemini...")

start = time.time()

try:
    interaction = client.interactions.create(
        model="gemini-3.8-flash",
        input="Explain how AI works in a few words"
    )

    print("Step 4: Response received!")
    print(interaction.output_text)

except Exception as e:
    print("API Error:", repr(e))

finally:
    print(f"Execution time: {time.time() - start:.2f} seconds")
