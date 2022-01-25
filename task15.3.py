for a in range(11,100):
    ok = 1
    for x in range(1,100):
        f = (70 % a == 0) and (not(x % 28 == 0) or (x % a == 0) or (x % 21 == 0))
        if f == 0:
            ok = 0
        if ok == 1:
            print(a)
            break