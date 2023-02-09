input_string = "Hello World"
words = input_string.split()
reversed_words = [word[::-1] for word in words]
reversed_string = " ".join(reversed_words)
print(reversed_string)
