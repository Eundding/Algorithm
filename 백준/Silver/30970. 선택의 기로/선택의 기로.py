import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr2 = arr[:]

# 첫 번째 방법(품질 내림차순, 가격 오름차순)
arr.sort(key=lambda x: (-x[0], x[1]))
print(arr[0][0], arr[0][1], arr[1][0], arr[1][1])

# 두 번쨰 방법(가격 오름차순, 품질 내림차순)
arr2.sort(key=lambda x: (x[1], -x[0]))
print(arr2[0][0], arr2[0][1], arr2[1][0], arr2[1][1])