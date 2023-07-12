str1 = 'Silent'
str2 = 'Listen'

str1 = str1.replace(" ", '').lower()
str2 = str2.replace(" ", '').lower()

char1 = {}
char2 = {}

for char in str1:
    char1[char] = char1.get(char, 0) + 1

for char in str2:
    char2[char] = char2.get(char, 0) + 1

if char1 == char2:
    print("Yes")
else:
    print("No")
