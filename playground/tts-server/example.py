import time
from TTS.api import TTS

# tts = TTS("tts_models/de/thorsten/tacotron2-DDC")

tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2")
# tts.tts_with_vc_to_file(
#     "Wie sage ich auf Italienisch, dass ich dich liebe?",
#     speaker_wav="target/speaker.wav",
#     file_path="output.wav"
# )

start_time = time.time()

# tts.tts_with_vc_to_file(
#     "Hey my name is Toby, how are you doing today",
#     speaker_wav="toby.wav",
#     file_path="output.wav")

tts.tts_to_file(text="Hey my name is Toby, how are you doing today",
                file_path="out.wav",
                speaker_wav="toby.wav",
                language="en",
                split_sentences=True)

end_time = time.time()

# Calculate elapsed time
elapsed_time = end_time - start_time

print(f"Elapsed time: {elapsed_time} seconds")
