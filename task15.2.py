def DEL(n, m):
    if (n and m > 0) and n % m == 0:
        return True
    else:
        return False


results = []

for A in range(0, 10000):
    count = 0
    for x in range(0, 100):
        if (not(DEL(x, A)) and DEL(x, 6)) <= (not(DEL(x, 3))):
            count += 1
    if count >= 100:
        results.append(A)

print(max(results))