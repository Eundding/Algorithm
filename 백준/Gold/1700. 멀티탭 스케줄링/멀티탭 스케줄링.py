import sys
input = sys.stdin.readline
n, k = map(int, input().split()) 
uses = list(map(int, input().split()))
 
elec = []
res = 0 # 갈아낀 횟수
for i in range(k):
    # 이미 있다면
    if uses[i] in elec:
        continue

    # 빈 공간이 있다면
    if len(elec) != n:
        elec.append(uses[i]) 
        continue

    # 가장 멀리 있는 플러그의 인덱스
    far_index = 0
    temp = 0

    # 현재 꽂혀있는 플러그들 확인
    for plug in elec:
        # 앞으로 사용할 플러그에 없으면
        if plug not in uses[i:]:
            temp = plug
            break
        # 현재까지 가장 멀리 있는 플러그보다 멀리 있으면
        elif uses[i:].index(plug) > far_index:
            far_index = uses[i:].index(plug)
            temp= plug
    
    elec[elec.index(temp)] = uses[i]
    res += 1

print(res)