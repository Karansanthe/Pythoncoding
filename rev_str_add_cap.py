def reverse_sentence_preserve_word_capitalization(input_string):
    words = input_string.split()
    reversed_words = []
    for word in words:
        if word.istitle():
            reversed_words.append(word[::-1].capitalize())
        else:
            reversed_words.append(word[::-1].lower())
    return " ".join(reversed_words[::-1])

input_string = "Hello World"
print(reverse_sentence_preserve_word_capitalization(input_string))
