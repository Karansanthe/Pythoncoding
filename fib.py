n_terms = int(input("Enter the number of Fibonacci terms to generate: "))

fib_seq = [0, 1]
while len(fib_seq) < n_terms:
    fib_seq.append(fib_seq[-1] + fib_seq[-2])

print("Fibonacci Sequence:")
print(fib_seq)
