arr = [50, 10, 3, 1]
num = 200
notes = []

for i in arr:
    num_notes = num // i
    if num_notes > 0:
        notes.append((i, num_notes))
        num %= i

for i, num_notes in notes:
    print(f"{num_notes} notes of {i}")
