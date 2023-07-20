str1 = 'sony india'
str1 = str1.split()

for i in str1:
    print(i[i.index('n'):], end= ' ')