def intersection(a, b):
    pass


for i in range(174457, 174506):
    for j in range(174457, 174506):
        a = []
        b = []
        for k in range(2, 418):
            if i % k == 0:
                a.append(k)
            if j % k == 0:
                b.append(k)
        if len(a) == len(b) == 2 and intersection(a, b) == []:
            print(a)
            print(b)