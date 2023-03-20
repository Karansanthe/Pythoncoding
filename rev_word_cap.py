# Reverse word with adding cap

def reverse_capital_words(input_string):
    words = input_string.split()
    reversed_words = []
    for word in words:
        if word[0].isupper():
            reversed_words.append(word[::-1])
        else:
            reversed_words.append(word)
    return " ".join(reversed_words)


input_string = "I love Python programming and Java"
print(reverse_capital_words(input_string))
