import sys
input = sys.stdin.readline

MAX = 1000000
is_prime = [True]*(MAX*2+1)

is_prime[0] = False
is_prime[1] = False

for i in range(1, MAX+1):
    if is_prime[i]:
        for j in range(i+i, MAX*2+1, i):
            is_prime[j] = False

while True:
    n = int(input())
    if n == 0:
        break
    cnt = 0
    for i in range(n+1, 2*n+1):
        if is_prime[i]:
            cnt += 1
    print(cnt)
