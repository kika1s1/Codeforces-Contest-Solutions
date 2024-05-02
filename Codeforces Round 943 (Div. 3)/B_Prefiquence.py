def maxim(t, tc):
    results = []
    
    for _ in range(t):
        n, m, a, b = tc[_]
        
        k = 0
        j = 0
        
        for i in range(n):
            while j < m and b[j] != a[i]:
                j += 1
            if j < m and b[j] == a[i]:
                k += 1
                j += 1
        
        results.append(k)
    
    return results

t = int(input())  
tc = []

for _ in range(t):
    n, m = map(int, input().split())
    a = input()
    b = input()
    tc.append((n, m, a, b))

result = maxim(t, tc)

for res in result:
    print(res)