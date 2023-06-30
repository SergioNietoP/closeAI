import openai
import time
import os

openai.api_key = os.getenv('OPENAI_API_KEY')

# Question
question_1 = "Imagine you're leading a team that has a conflict about the direction of a project. How would you resolve this situation?"

# System Role
system_role_instruction = "You are the best creativity test evaluator. You are going to receive an answer from a candidate that is applying for a job to this question : '" + question_1 + "'. I need you to give scores based on these metrics: Specificity, Relevance, Problem-Solving, Initiative, Outcome, Self-Reflection, Creativity, Communication. Also, give me a short explanation of your evaluation with pros and cons. Give an answer in JSON format where each field is a metric, and also add average score and the explanation fields."

# Initialize retry times and retry limit in case of temporary issues
retry_times = 0
retry_limit = 3

while True:
    try:
        # Start the timer
        start_time = time.time()

        # Load the audio file and transcribe it
        audio_file_path = os.path.join("audios", "audio_answer", "answer_english_2.mp3")
        with open(audio_file_path, "rb") as audio_file:
            transcript = openai.Audio.transcribe(
                file=audio_file,
                model="whisper-1",
                response_format="text"
            )

        # Option for manual review before sending to evaluation .Comment this section to evaluate elapsed time
        review_transcript = input("Would you like to review the transcript before sending for evaluation? (y/n): ")
        if review_transcript.lower() == "y":
            print("\nTranscript:\n", transcript)
            continue_review = input("Do you want to continue with the evaluation? (y/n): ")
            if continue_review.lower() != "y":
                print("Exiting evaluation...")
                break

        # API ChatGPT
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            temperature=0.8,
            max_tokens=2000,
            messages=[
                {"role": "system", "content": system_role_instruction},
                {"role": "user", "content": transcript}
            ]
        )

        print(completion.choices[0].message.content)


        # Calculate the elapsed time
        elapsed_time = time.time() - start_time
        print("Elapsed Time:", elapsed_time, "seconds")

        break

    except openai.Error as error:
        if retry_times < retry_limit:
            print("An error occurred: ", error)
            print("Retrying...")
            retry_times += 1
            time.sleep(2 ** retry_times)
        else:
            print("Failed to process after multiple attempts. Please check your inputs.")
            break
