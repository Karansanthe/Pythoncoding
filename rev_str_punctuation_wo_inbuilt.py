def reverse_sentence_with_punctuation(input_string):
    words = input_string.split()
    reversed_words = []
    for word in words:
        if word[-1] in ".!?":
            reversed_word = word[:-1][::-1] + word[-1]
            reversed_words.append(reversed_word)
        else:
            reversed_words.append(word[::-1])
    return " ".join(reversed_words)

input_string = "I love python programming!"
print(reverse_sentence_with_punctuation(input_string))
