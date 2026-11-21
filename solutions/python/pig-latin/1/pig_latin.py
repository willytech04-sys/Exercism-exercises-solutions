"""Translating text from English to Pig Latin"""


def translate(text):
    """Translate English words into Pig Latin."""

    vowels = "aeiou"
    words = text.split()
    translated_words = []

    for word in words:
        count = 0

        # Rule 1: Words beginning with a vowel, xr, or yt
        if word.startswith(tuple(vowels) + ("xr", "yt")):
            translated_words.append(word + "ay")
            continue

        # Rules 2, 3, and 4
        for letter in word:

            # Handle qu as a consonant cluster
            if word[count:count + 2] == "qu":
                count += 2
                break

            # Stop when a vowel is found
            if letter in vowels:
                break

            # Stop when y follows one or more consonants
            if letter == "y" and count > 0:
                break

            count += 1

        # Move the initial consonant cluster to the end
        new_word = word[count:] + word[:count] + "ay"
        translated_words.append(new_word)

    return " ".join(translated_words)