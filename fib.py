n_terms = 5

fib_seq = [0, 1]
while len(fib_seq) < n_terms:
    fib_seq.append(fib_seq[-1] + fib_seq[-2])

print(fib_seq)

# other method

n = 5
a, b = 0, 1
print(a, end = ' ')

for _ in range(n - 1):
    print(b, end = ' ')
    a, b = b, a+b