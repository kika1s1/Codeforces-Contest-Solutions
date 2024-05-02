def calculate_lcp(s):
    n = len(s)
    lcp = [0] * n
    for i in range(1, n):
        j = lcp[i - 1]
        while j > 0 and s[i] != s[j]:
            j = lcp[j - 1]
        if s[i] == s[j]:
            j += 1
        lcp[i] = j
    return lcp

def find_maximal_lcp(s, l, r):
    n = len(s)
    maximal_lcp = []
    for k in range(l, r + 1):
        max_lcp = 0
        for i in range(n - k + 1):
            substrings = [s[i + j:i + j + k] for j in range(k)]
            lcp = min(len(substrings[j]) for j in range(1, k))
            max_lcp = max(max_lcp, lcp)
        maximal_lcp.append(max_lcp)
    return maximal_lcp

t = int(input())
for _ in range(t):
    n, l, r = map(int, input().split())
    s = input()
    maximal_lcp = find_maximal_lcp(s, l, r)
    print(*maximal_lcp)
