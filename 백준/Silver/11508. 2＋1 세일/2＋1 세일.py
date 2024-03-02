import sys
input = sys.stdin.readline

n = int(input())
price = [int(input()) for _ in range(n)]
answer = 0
price.sort(reverse=True)

for i in range(n):
    if i % 3 == 0 or i % 3 == 1:
        answer += price[i]
print(answer)