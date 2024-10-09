# Rule-Based Machine Translation (RBMT) - English to Spanish
# A simple dictionary for translation
translation_dict = {
    "hello": "hola",
    "world": "mundo",
    "how": "cómo",
    "are": "estás",
    "you": "tú",
    "good": "bueno",
    "morning": "mañana",
    "afternoon": "tarde",
    "night": "noche"
}

def rule_based_translate(sentence):
    words = sentence.lower().split()  # Convert to lowercase and split sentence into words
    translated_sentence = []
    
    for word in words:
        # Check if the word exists in the dictionary
        if word in translation_dict:
            translated_sentence.append(translation_dict[word])
        else:
            translated_sentence.append(f"[{word}]")  # Keep untranslated words in brackets
    
    return " ".join(translated_sentence)

# Example usage
sentence = "Hello world how are you?"
translated_sentence = rule_based_translate(sentence)
print(f"Original: {sentence}")
print(f"Translated: {translated_sentence}")
