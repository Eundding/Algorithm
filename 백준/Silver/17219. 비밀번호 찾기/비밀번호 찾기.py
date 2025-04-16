import sys
input = sys.stdin.readline
n, m = map(int, input().split())
dict = {}
for i in range(n):
    a, b = input().split()
    dict[a] = b

for j in range(m):
    a = input().rstrip()
    print(dict[a])