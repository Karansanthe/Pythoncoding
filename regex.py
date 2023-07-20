import re

text = "The quick brown fox jumps over the lazy dog."

pattern = "the"

matches = re.findall(pattern, text)

print(matches)
