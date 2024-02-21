import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dogam = [input().strip() for _ in range(n)]
q = [input().strip() for _ in range(m)]
for x in q:
    if x.isdigit():
        print(dogam[int(x)-1])
    else:
        print(dogam.index(x)+1)