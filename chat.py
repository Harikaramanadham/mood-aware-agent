import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

chat = client.chats.create(
    model = "gemini-3.5-flash",
    config=types.GenerateContentConfig(
        system_instruction="you are a calm, kind assisstant for a busy grad student. keep answers short."
    ),
)
while True:
    message = input("YOU:")
    if message.lower() in ("quit", "exit"):
        break
    reply = chat.send_message(message)
    print("Agent:", reply.text)