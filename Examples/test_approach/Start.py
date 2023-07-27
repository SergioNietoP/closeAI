import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')


question_1 = "Tell me about a time when you had to work as part of a team. What was your role and how did you contribute to the team's success?"

completion = openai.ChatCompletion.create(
  model = "gpt-3.5-turbo",
  temperature = 0.8,
  max_tokens = 2000,
  messages = [
    {"role": "system", "content": "You are the best personality test evaluator. You are going to receive an answer from a candidate that is applying for a job to this question : '" + question_1 + "'. I need you to give just 2 scores , the creativity score and the average score. Also give me a short explanation of your evaluation with pros and cons. Give you answer in a json format with this fields: score_creativity, average and briefing. " },
    {"role": "user", "content": "I guess I've worked on teams before. I'm usually the one who just goes along with whatever the team decides. I don't like confrontation, so I just do whatever I'm told to do. I don't really remember a specific project or anything."}
  ]
)

print(completion.choices[0].message.content)