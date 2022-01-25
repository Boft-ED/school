P = list(range(5, 31))
Q = list(range(14, 24))

results = []

for a1 in range(-100, 100):
    for a2 in range(-100, 100):
        A = list(range(a1, a2))
        count = 0
        for x in range(-100, 100):
            if ((x in P) == (x in Q)) <= (not(x in A)):
                count += 1
        if count >= 200:
            results.append(len(A))

print(max(results))


