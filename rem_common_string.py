def find(s1, s2):
    common = set(s1)
    res = []
    for char in s2:
        if char not in common:
           res.append(char)
    return "".join(res)

s1 = 'apple'
s2 = 'toes'
print(find(s1, s2))