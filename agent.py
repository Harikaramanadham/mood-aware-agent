import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from transformers import pipeline
from tools import get_schedule, get_deadlines

load_dotenv()

client = genai.Client(api_key=os.getenv("Gemini_API_KEYS"))
detector = pipeline("text-classification", model = "j-hartmann/emotion-english-distilroberta-base")

# two personalities for the brain
CALM = "you are a calm, kind assistant. The user seems stressed. Reply in 3 short lines or less and give only the one next step."
NORMAL = "You are a friendly, helpful assistant for a busy grad student. Be clear and practical."

#feelings that we treat as "Stressed"

STRESS_FEELINGS = ("fear", "sadness", "anger")

def reply_to(message):        #give it a message get back mood and answer
    mood = detector(message)[0]["label"]
    if mood in STRESS_FEELINGS:
        style = CALM
    else:
        style = NORMAL
    response = client.models.generate_content(
        # the brain answer in that style
        model = "gemini-3.5-flash-lite",
        contents = message,
        config= types.GenerateContentConfig(system_instruction=style, 
                                            temperature = 0.3,
                                            tools=[get_schedule, get_deadlines], # the agent's hands
                                            ),
    )
    return mood, response.text


#this part runs on;y when you run this file directly(not when another file imports it)
if __name__ == "__main__":
     while True:
         message = input("YOU:")
         if message.lower() in ("quit", "exit"):
             break
         mood, answer = reply_to(message)
         print(f"[mood:{mood}]")
         print("Agent:", answer)
    