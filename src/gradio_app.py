import gradio as gr
from transcribe import transcribe_audio
from nlp_match import match_question
from tts import text_to_speech

def voice_assistant(audio):
    transcription = transcribe_audio(audio)
    answer = match_question(transcription)
    output_file = "audio_files/output_temp.mp3"
    text_to_speech(answer, output_file)
    return transcription, answer, output_file

interface = gr.Interface(
    fn=voice_assistant,
    inputs=gr.Audio(source="microphone", type="filepath"),
    outputs=["text", "text", "audio"],
    title="Kinyarwanda Voice Assistant"
)
interface.launch()