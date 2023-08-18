n_terms = 5

fib_seq = [0, 1]
while len(fib_seq) < n_terms:
    fib_seq.append(fib_seq[-1] + fib_seq[-2])

print("Fibonacci Sequence:")
print(fib_seq)
