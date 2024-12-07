for n in range(5555, 9999):
    s = [n // 1000 + n // 100 % 10, n // 100 % 10 + n // 10 % 10, n // 10 % 10 + n % 10]
    s.remove(min(s))
    if s[0] > s[1]:
        a = (str(s[1]) + str(s[0]))
    else:
        a = (str(s[0]) + str(s[1]))

    if a == '1418':
        print(n)
        break

# a = 5599