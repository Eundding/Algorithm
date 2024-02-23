import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
cnt = 1
target = arr[-1]
arr.pop()

while arr:
    if target < arr[-1]:
        cnt += 1
        target = arr[-1]
    arr.pop()
print(cnt)
