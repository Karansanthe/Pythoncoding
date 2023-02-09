input_string = "Hello World"
reversed_string = ""
word_start = 0
for i in range(len(input_string)):
    if input_string[i] == " ":
        reversed_string += input_string[word_start:i][::-1] + " "
        word_start = i + 1
reversed_string += input_string[word_start:][::-1]
print(reversed_string)
