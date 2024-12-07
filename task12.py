
cnt = 0

while cnt < 5:
    n = 300000001
    cou = 0
    for i in range(2, int(n ** 0.5 // 1)):
        if n % i == 0:
            cou += 1
            if cou == 5:
                print(n, i)
                cnt +=1
                break
    n += 1
