# 흙길 보수하기
# 1) 안겹 2) 일부만 겹 3) 아예 겹
# 덮는 경우 생각 안 함..

import sys
input = sys.stdin.readline
N, L = map(int, input().split())

result = 0
soil = []
for _ in range(N): # 2차원 배열로 만들기
    s, e = map(int, input().split())
    temp = [s, e]
    soil.append(temp)
        
# start 기준으로 정렬하기
soil.sort(key=lambda x:x[0])


ans = 0

ptr = soil[0][0] # 널판지 시작 위치
for start, end in soil:
    if ptr > end:
        continue
    elif ptr < start:
        ptr = start

    dist = end - ptr # 널판지가 필요한 거리
    rest = 1 # 여분
    if dist % L == 0:
        rest = 0
    cnt = dist // L + rest
    ptr += cnt*L
    ans += cnt

print(ans)


