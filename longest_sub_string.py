str1 = 'ababcdaeafab'
d1 = {}
max_len = 0
left = 0

for right in range(len(str1)):
    if str1[right] in d1:
        left = max(left, d1[str1[right]] + 1)
    d1[str1[right]] = right
    max_len = max(max_len, right - left + 1)

print(max_len)