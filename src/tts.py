from gtts import gTTS
import os

def text_to_speech(text, output_file, lang="sw"):
    tts = gTTS(text=text, lang=lang, slow=False)
    tts.save(output_file)
    os.system(f"mpg123 {output_file}")  # Play audio
    print(f"Saved to {output_file}")

if __name__ == "__main__":
    text_to_speech("Meze neza, murakoze!", "audio_files/output1.mp3")