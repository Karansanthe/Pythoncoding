def reverse_words_in_sentence(input_string):
    words = input_string.split()
    return " ".join(words[::-1])

input_string = "I love python programming"
print(reverse_words_in_sentence(input_string))
