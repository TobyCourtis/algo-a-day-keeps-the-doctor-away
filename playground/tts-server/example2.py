from TTS.api import TTS


# List available 🐸TTS models
print(TTS().list_models())

# Init TTS
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2")


import time
start_time = time.time()
# Run TTS
# ❗ Since this model is multi-lingual voice cloning model, we must set the target speaker_wav and language
# Text to speech list of amplitude values as output
wav = tts.tts(text="Hello world!", speaker_wav="toby.wav", language="en")
# Text to speech to a file
tts.tts_to_file(text="Hello world!", speaker_wav="toby.wav", language="en", file_path="output.wav")


end_time = time.time()

# Calculate elapsed time
elapsed_time = end_time - start_time

print(f"Elapsed time: {elapsed_time} seconds")
