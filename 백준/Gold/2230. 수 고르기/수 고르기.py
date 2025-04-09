import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()

left, right = 0, 0
result = 2000000000
while right < n:
    diff = arr[right] - arr[left]
    if diff == m:
        result = m
        break
    elif diff < m:
        right += 1
    else:
        left += 1
        result = min(diff, result)

print(result)