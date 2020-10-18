for i in range(int(input())):
    fl = list(map(int, input().split()))
    it = 0
    tans = 0

    for k in range(fl[1]):
        r = list(map(int, input().split()))
        tans += abs(r[0] - it) + abs(r[1] - r[0])
        it = r[1]

    print(tans)
