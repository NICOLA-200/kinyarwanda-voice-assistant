import sounddevice as sd
import scipy.io.wavfile as wavfile
import numpy as np

def record_audio(filename, duration=5, sample_rate=16000):
    print("Recording...")
    audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1)
    sd.wait()
    wavfile.write(filename, sample_rate, audio)
    print(f"Saved to {filename}")

if __name__ == "__main__":
    record_audio("audio_files/input1.wav", duration=5)