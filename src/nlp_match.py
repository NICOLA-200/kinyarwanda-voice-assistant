from fuzzywuzzy import fuzz

qa_pairs = {
    "Mwaramutse, uvuze iki?": "Mwaramutse! Nvuze Kinyarwanda.",  # Hello, what do you speak?
    "Umeze ute?": "Meze neza, murakoze!",                    # How are you?
    "Iri joro ryiza?": "Yego, ryiza cyane!",                 # Is the weather nice?
    "Urashobora kunganira?": "Yego, ndashobora kuganira!",    # Can you help me?
    "Amakuru yawe ni ayahe?": "Amakuru yanjye ni meza!"      # What is your news?
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