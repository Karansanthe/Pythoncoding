# For even index, if you want for odd (if i % 2 != 0)

input_string = "I love python programming and Java"
words = input_string.split()
reversed_words = []
for i, word in enumerate(words):
    if i % 2 == 0:
        reversed_words.append(word)
    else:
        reversed_words.append(word[::-1])
reversed_string = " ".join(reversed_words)
print(reversed_string)
