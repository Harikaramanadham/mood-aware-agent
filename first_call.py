import os
from dotenv import  load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

response = client.models.generate_content(model = "gemini-3.5-flash", contents = "where is the temple of the fifth sage in tears of the kingdom?")

print(response.text)
