import openai

# Set the API key
openai.api_key = "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"

# Open the audio file and transcribe it
with open("Examples/answer_2.mp3", "rb") as audio_file:
    transcript = openai.Audio.transcribe(
        file = audio_file,
        model = "whisper-1",
        response_format="text"
    )

# Print the transcript
print(transcript)

question_1 = " Imagine you're leading a team that has a conflict about the direction of a project. How would you resolve this situation?"

completion = openai.ChatCompletion.create(
  model = "gpt-3.5-turbo",
  temperature = 0.8,
  max_tokens = 2000,
  messages = [
    {"role": "system", "content": "You are the best creativity test evaluator. You are going to receive an answer from a candidate that is applying for a job to this question : '" + question_1 + "'. I need you to give scores based on this metrics: Specificity, Relevance, Problem-Solving, Initiative, Outcome, Self-Reflection, Creativity, Communication. Also give me a short explanation of your evaluation with pros and cons. Give an answer in a json format where each field is a metric, and also add average score and the explanation fields." },
    {"role": "user", "content": transcript}
  ]
)

print(completion.choices[0].message.content)