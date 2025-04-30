from transcribe import transcribe_audio
from nlp_match import match_question
from tts import text_to_speech

def voice_assistant(audio_file):
    # Step 1: Transcribe
    transcription = transcribe_audio(audio_file)
    print("Transcription:", transcription)
    
    # Step 2: Match question
    answer = match_question(transcription)
    print("Answer:", answer)
    
    # Step 3: Generate speech
    output_file = audio_file.replace(".wav", "_output.mp3")
    text_to_speech(answer, output_file)
    
    return transcription, answer, output_file

if __name__ == "__main__":
    audio_file = "audio_files/input1.wav"
    transcription, answer, output_file = voice_assistant(audio_file)