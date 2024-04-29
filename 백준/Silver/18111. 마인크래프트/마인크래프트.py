import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(N)]

min_h = 256 # 높이 최소
max_h = 0 # 높이 최대

# 높이 최소, 최대 구하기
for i in range(N):
    for j in range(M):
        max_h= max(max_h, ground[i][j])
        min_h = min(min_h, ground[i][j])

min_time = 100000000
max_height = 0
temp_B = B
for height in range(0, max_h+1):
    current_time = 0
    temp_B = B
    for i in range(N):
        for j in range(M):
            if height > ground[i][j]: # 블록 쌓아야함 1초
                current_time += height - ground[i][j]
                temp_B -= height - ground[i][j]
            elif height < ground[i][j]: # 블록 버려야함 2초
                current_time += 2*(ground[i][j] - height)
                temp_B += ground[i][j] - height

        if current_time > min_time: break

    if temp_B >= 0 and min_time >= current_time:
        max_height = height
        min_time = current_time

    if temp_B < 0: break # 높이가 n일 때 인벤토리가 음수가 나왔다면, n을 초과하는 높이를 만드려면 전체 필요한 블록 수가 n일 때보다 커야 하므로 

print(min_time, max_height)