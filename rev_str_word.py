input_string = "Hello, World!"
reversed_string = "".join(reversed(input_string))
print(reversed_string)

"""
# without inbuilt    
def reverse_words_in_sentence(input_string):
    words = input_string.split()
    return " ".join(words[::-1])

input_string = "I love python programming"
print(reverse_words_in_sentence(input_string))
"""