t = int(input())

for i in range(t):
    n = int(input())
    x = list(map(int, input().split()))

    data = [0] * n

    max_value = max(x)
    data[0] = max_value + 1
   
    for i in range(1, n):
        data[i] = x[i-1] + data[i-1]
        
    print(*data)