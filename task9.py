def f(a, b):
    if b == 0:
        return 0
    elif a > b:
        return f(a - 1, b) + b
    else:
        return f(a, b - 1) + a

cnt = 0
for a in range(1, 100000):
    for b in range(1, 100000):
        print(f(a, b))
        if f(a, b) == 2097152:
            cnt += 1
            break

