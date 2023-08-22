input_sentence = "long lives our elvis"
words = input_sentence.split()
word_counts = {}
anagram_pairs = 0

for word in words:
    sorted_word = ''.join(sorted(word))
    anagram_pairs += word_counts.get(sorted_word, 0)
    word_counts[sorted_word] = word_counts.get(sorted_word, 0) + 1

print(f"{word_counts} anagram pairs.")
