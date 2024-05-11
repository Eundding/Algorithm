# 크림빵
import sys
input = sys.stdin.readline


N, K, P = map(int, input().split()) # 2 3 2 000/111  3개씩 2묶음

cream = list(map(int, input().split()))

ans = 0
num = 0
for i in range(len(cream)):
    if (cream[i] == 0):
        num += 1

    if((i+1) % K == 0):
        if(num < P):
            ans += 1
        num = 0


print(ans)




