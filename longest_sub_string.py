s = 'ababcdaeafab'
d1 = {}
max_len = 0
left = 0

for right in range(len(s)):
    if s[right] in d1:
        left = max(left, d1[s[right]] + 1)
    d1[s[right]] = right
    max_len = max(max_len, right - left + 1)

print(max_len)