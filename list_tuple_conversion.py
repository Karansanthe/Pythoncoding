a = [1, 2]
b = [3, 4]
d = [5, 6]
e = ['Hey', 'There']

# Using the extend method
a.extend(b)
print(a)

# Using the + operator
ans = b + d
print(ans)

# To get list as [(3, 4), (5, 6)]
ans = [tuple(b), tuple(d)]
print(ans)

# To get list as (3,4,5,6)
ans = tuple(b + d)
print(ans)

# To get list as [(3, 5), (4, 6)]
ans = list(zip(b, d))
print(ans)

# another method
ans = [(b[i], d[i]) for i in range(len(b))]
print(ans)

# To get list as [(5, 'Hey'), (6, 'There')]
ans = list(zip(d, e))
print(ans)