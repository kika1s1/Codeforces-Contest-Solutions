def answer():
    n, k, passed, pos = map(int, input().split())
    passed -= 1
    pos -= 1
    p = list(map(lambda x: int(x) - 1, input().split()))
    arr = list(map(int, input().split()))

    b, s = [], []
    vb, vs = [False] * n, [False] * n

    while not vb[passed]:
        b.append(arr[passed])
        vb[passed] = True
        passed = p[passed]

    while not vs[pos]:
        s.append(arr[pos])
        vs[pos] = True
        pos = p[pos]

    sb, sc, csb, csc = 0, 0, 0, 0
    for i in range(min(len(b), k)):
        sb = max(sb, csb + b[i] * (k - i))
        csb += b[i]

    for i in range(min(len(s), k)):
        sc = max(sc, csc + s[i] * (k - i))
        csc += s[i]

    print("Draw" if sb == sc else "Bodya" if sb > sc else "Sasha")


test = int(input())
for i in range(test):
    answer()