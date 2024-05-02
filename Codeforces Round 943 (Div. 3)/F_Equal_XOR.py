def is_interesting_subarray(arr, l, r):
    segment_xor = 0
    for i in range(l, r):
        segment_xor ^= arr[i]

    if segment_xor == 0:
        return "YES"

    prefix_xor = 0
    count_prefix = {}
    for i in range(l, r):
        prefix_xor ^= arr[i]
        if prefix_xor == segment_xor:
            if (i + 1) < r and segment_xor in count_prefix:
                return "YES"
            count_prefix[prefix_xor] = 1

    return "NO"


t = int(input())

for _ in range(t):
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))

    for _ in range(q):
        l, r = map(int, input().split())
        print(is_interesting_subarray(arr, l - 1, r))
    print()