import wave
import io
import numpy as np
import sounddevice as sd
from piper import PiperVoice
import emoji

voice = PiperVoice.load("cs_medium.onnx", "cs_medium.onnx.json")

def ocisti_text(text: str):
    cisty_text = emoji.replace_emoji(text, replace='')
    cisty_text = cisty_text.replace('*', '')
    cisty_text = cisty_text.replace('/a', '')
    cisty_text = cisty_text.replace('(', '')
    cisty_text = cisty_text.replace(')', '')
    return cisty_text

def speak(vstup: str):
    
    text = ocisti_text(vstup)
    
    buffer = io.BytesIO()
    with wave.open(buffer, "wb") as wav_file:
        voice.synthesize_wav(text, wav_file)
    buffer.seek(0)
    with wave.open(buffer, "rb") as wav_file:
        audio = np.frombuffer(wav_file.readframes(wav_file.getnframes()), dtype=np.int16)
    sd.play(audio, samplerate=voice.config.sample_rate)
    sd.wait()