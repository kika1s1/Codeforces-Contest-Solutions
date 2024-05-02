from math import gcd
def findMaxim(x):
    maxim = float("-inf")
    ans = -1
    for i in range(1, x):
        if gcd(x, i) + i > maxim:
            maxim = gcd(x, i) + i
            ans = i
    return ans


t = int(input())

for i in range(t):
    x = int(input())
    print(findMaxim(x))
    
    