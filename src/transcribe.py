from transformers import WhisperProcessor, WhisperForConditionalGeneration
import torchaudio

def transcribe_audio(audio_file):
    # Load KinyaWhisper model and processor
    model = WhisperForConditionalGeneration.from_pretrained("benax-rw/KinyaWhisper")
    processor = WhisperProcessor.from_pretrained("benax-rw/KinyaWhisper")
    
    # Load and preprocess audio
    waveform, sample_rate = torchaudio.load(audio_file)
    inputs = processor(waveform.squeeze(), sampling_rate=sample_rate, return_tensors="pt")
    
    # Generate prediction
    predicted_ids = model.generate(inputs["input_features"])
    transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)[0]
    
    # Save transcription
    transcription_file = audio_file.replace(".wav", "_transcription.txt")
    with open(transcription_file, "w", encoding="utf-8") as f:
        f.write(transcription)
    
    return transcription

if __name__ == "__main__":
    text = transcribe_audio("audio_files/input1.wav")
    print("Transcription:", text)