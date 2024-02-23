n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]

def check(r, c): # 기준으로 8X8 체크
    cnt = 0
    for i in range(r, r+8):
        for j in range(c, c+8):
            if (i+j) % 2 == 0 and board[i][j] == 'W':
                continue
            elif (i+j) % 2 != 0 and board[i][j] == 'B':
                continue
            else:
                cnt += 1
    if cnt > 32:
        cnt = 64 - cnt
    return cnt

answer = 1000000000000000
for i in range(n-7):
    for j in range(m-7):
        if answer > check(i, j):
            answer = check(i, j)
print(answer)










