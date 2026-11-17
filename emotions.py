from transformers import pipeline

detector = pipeline(
    "text-classification",
    model = "j-hartmann/emotion-english-distilroberta-base",
)

text = "ugh I have three assignments due and I haven't started any of them. I am sweating right now"
result = detector(text)[0]

print(result["label"], round(result["score"], 2))