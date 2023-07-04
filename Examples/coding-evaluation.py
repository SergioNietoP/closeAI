import openai
import time
import os

openai.api_key = os.getenv('OPENAI_API_KEY')

# Start the timer
start_time = time.time()

question = ""

completion = openai.ChatCompletion.create(
  model = "gpt-3.5-turbo",
  temperature = 0.8,
  max_tokens = 2000,
  messages = [
    {"role": "system", "content": "You are the best coding evaluator, you are an specialist in Python programming. You are going to receive a solution made by a candidate for this question: " + question + ". Give an complex score ( different parameters ) and explanation of your evaluation in a json format." },
    {"role": "user", "content": ""}
  ]
)

print(completion.choices[0].message.content)