from flask import Flask, request, jsonify, send_file
from TTS.api import TTS
import os
import uuid

app = Flask(__name__)
audio_storage = {}

# Initialize the TTS model (adjust the model name as necessary)
tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False, gpu=False)


# Endpoint to upload audio file and save it with an ID
@app.route('/upload_audio', methods=['POST'])
def upload_audio():
    if 'audio' not in request.files:
        return jsonify({"error": "No audio file part"}), 400

    file = request.files['audio']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file:
        audio_id = str(uuid.uuid4())
        file_path = os.path.join('audio_files', f'{audio_id}.wav')
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        file.save(file_path)
        audio_storage[audio_id] = file_path
        return jsonify({"audio_id": audio_id}), 200


# Endpoint to generate audio based on ID and text
@app.route('/generate_audio', methods=['POST'])
def generate_audio():
    data = request.json
    audio_id = data.get('audio_id')
    text = data.get('text')

    if not audio_id or not text:
        return jsonify({"error": "Missing audio_id or text"}), 400

    if audio_id not in audio_storage:
        return jsonify({"error": "Invalid audio_id"}), 400

    # Generate audio (TTS)
    output_path = os.path.join('generated_audio', f'{audio_id}.wav')
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    tts.tts_to_file(text=text, file_path=output_path)

    return send_file(output_path, mimetype='audio/wav')


def generate_audio_local(audio_id, text):
    if not audio_id or not text:
        raise ValueError("Missing audio_id or text")

    # Define the output path for the generated audio
    output_path = os.path.join('generated_audio', f'{audio_id}.wav')
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Generate audio using TTS
    tts.tts_to_file(text=text, file_path=output_path)

    print(f"Generated audio saved to: {output_path}")


if __name__ == '__main__':
    # Example input (replace these with actual values)
    example_audio_id = "some-unique-id"
    example_text = "Hello, world!"

    # Generate audio
    generate_audio(example_audio_id, example_text)

if __name__ == '__main__':
    # app.run(debug=True)
    generate_audio_local('fb2a6441-16d1-402a-98b9-776bb79a1972', 'Hello there world how are you doing today. This is a test for Upwork let us see how it goes')
