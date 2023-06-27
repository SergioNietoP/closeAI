import openai

# Set the API key
openai.api_key = ""

# Open the audio file and transcribe it
with open("NDkyODU2MDEwNDkyODcy_Hp5xdlTKoq8.mp3", "rb") as audio_file:
    transcript = openai.Audio.transcribe(
        file = audio_file,
        model = "whisper-1",
        response_format="text"
    )

# Print the transcript
print(transcript)
