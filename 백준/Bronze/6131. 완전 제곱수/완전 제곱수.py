# 9094번
import sys
input = sys.stdin.readline

n = int(input())
result = 0
for b in range(1, 501):
    for a in range(b+1, 501):
        if a**2 - n == b**2:
            result += 1
print(result)