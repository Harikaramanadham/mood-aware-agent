import os
from dotenv import load_dotenv
from google import genai
from google .genai import types

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

response = client.models.generate_content(
model = "gemini-3.5-flash",
contents = "I have 3 assignmnets this week and I work on Wednesday and Thursday.Help",
config = types.GenerateContentConfig(
    system_instruction ="deal with student like a kid", temperature = 0.5
    ),
)
print(response.text)

