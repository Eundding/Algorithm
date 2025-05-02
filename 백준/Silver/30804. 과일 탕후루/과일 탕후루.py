import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
fruits = list(map(int, input().split()))
start = 0
answer = 0
d = defaultdict(int) # 딕셔너리 생성

for end in range(n):
    d[fruits[end]] += 1

    while len(d) > 2: # 종류가 2개 초과면 => 줄여야함
        d[fruits[start]] -= 1 # start에 있는 과일 줄임
        if d[fruits[start]] == 0: # 줄였는데 0이면 삭제
            del d[fruits[start]]
        start += 1 

    answer = max(answer, end - start + 1)

print(answer)