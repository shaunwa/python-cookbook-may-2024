from openai import OpenAI
import json

client = OpenAI()

text_samples = [
    "McDonalds burgers are not very good",
    "The economy has never been good",
    "The economy has never been so good",
    "I'm sure a new pair of shoes will solve all your problems...",
    "Bitcoin is the cryptocurrency of the year!"
]

analyses = [ ]

for sample in text_samples:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "I'm going to submit a series of text samples, I need you to rate the sentiment of each sample on a scale of -1 to 1, where -1 is very negative, 1 is positive, and 0 is neutral. Please respond to each sample with a JSON object, containing a \"score\" property (-1 to 1) and a \"reason\" property, which is a string explaining your reasoning"},
            {"role": "user", "content": sample }
        ]
    )

    sentiment = { 'text': sample, **json.loads(response.choices[0].message.content) }
    analyses.append(sentiment)

print(analyses)