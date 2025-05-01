from fuzzywuzzy import fuzz

qa_pairs = {
    "Mwaramutse ?": "Mwaramutse neza!",  # Hello, what do you speak?
    "Umeze ute?": "Meze neza, murakoze!",                    # How are you?
    "Ijoro ryiza?": "Yego, ryiza cyane!",                 # Is the weather nice?
    " witwa nde?": "nitwa gpt!",    # Can you help me?
    "Amakuru ?": "Amakuru yanjye ni meza!"      # What is your news?
}

def match_question(transcribed_text, threshold=80):
    for question, answer in qa_pairs.items():
        similarity = fuzz.partial_ratio(transcribed_text.lower(), question.lower())
        if similarity > threshold:
            return answer
    return "Sinumva, mwongere musubize."  # I don't understand, please repeat.

if __name__ == "__main__":
    text = "Umeze ute?"
    answer = match_question(text)
    print("Answer:", answer)