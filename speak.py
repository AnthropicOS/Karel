import wave
import io
import numpy as np
import sounddevice as sd
from piper import PiperVoice

voice = PiperVoice.load("cs_medium.onnx", "cs_medium.onnx.json")

def speak(text: str):
    buffer = io.BytesIO()
    with wave.open(buffer, "wb") as wav_file:
        voice.synthesize_wav(text, wav_file)
    buffer.seek(0)
    with wave.open(buffer, "rb") as wav_file:
        audio = np.frombuffer(wav_file.readframes(wav_file.getnframes()), dtype=np.int16)
    sd.play(audio, samplerate=voice.config.sample_rate)
    sd.wait()