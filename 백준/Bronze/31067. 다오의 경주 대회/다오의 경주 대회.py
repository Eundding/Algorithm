n, k = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0
cnt = 0

for i in range(1, n):
  if arr[i-1] >= arr[i]:
    arr[i] += k
    cnt += 1
    if arr[i-1] >= arr[i]:
      answer = -1
      break

if answer == -1:
  print(-1)
else:
  print(cnt)