import sys
input = sys.stdin.readline

'''
0 => 10
1 => 1
2 => 2 4 8 6
3 => 3 9 7 1
4 => 4 6
5 => 5
6 => 6
7 => 7 9 3 1
8 => 8 4 2 6
9 => 9 1
'''


def sol(a, b):
    a %= 10

    if a == 0:
        return 10

    elif a in [1, 5, 6]:
        return a

    elif a in [4, 9]:
        if b % 2 == 0:
            return (a**2) % 10
        else:
            return a

    else: # 2, 3, 7, 8
        b %= 4
        if b == 0:
            return (a ** 4) % 10
        else:
            return (a ** b) % 10

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    print(sol(a, b))