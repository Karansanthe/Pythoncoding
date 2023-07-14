text = "Lorem ipsum dolor sit amet consectetur adipiscing elit ipsum ipsum"
words = text.split()
words_count = {}

for word in words:
    words_count[word] = words_count.get(word, 0) + 1
print(words_count)
print(list(words_count.items()))


# Count in array

arr = [1, 3, 4, 5, 3]
count = {}

for i in arr:
    count[i] = count.get(i, 0) + 1
print(count)
