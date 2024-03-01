import sys
input = sys.stdin.readline

n = int(input())
isUsed1 = [False]*n # 열
isUsed2 = [False]*(n+n-1) # 왼쪽 아래로 대각선
isUsed3 = [False]*(n+n-1) # 오른쪽 아래로 대각선
cnt = 0

def back(cur):
    global cnt
    if cur == n:
        cnt += 1
        return

    for i in range(n):
        if isUsed1[i] or isUsed2[i+cur] or isUsed3[cur - i + n - 1]: continue
        isUsed1[i] = True
        isUsed2[cur+i] = True
        isUsed3[cur-i+n-1] = True
        back(cur+1)
        isUsed1[i] = False
        isUsed2[cur + i] = False
        isUsed3[cur - i + n - 1] = False

back(0)
print(cnt)