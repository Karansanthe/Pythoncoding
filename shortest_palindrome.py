def find(s1):
    for i in range(len(s1)):
        if s1[i:] == s1[i:][::-1]:
            return s1 + s1[:i][::-1]

s1 = 'abc'
print(find(s1))