import sys
input = sys.stdin.readline

def tracking(k, idx):
    if k == m:
        for i in range(m):
            print(answer[i], end=' ')
        print()
        return

    temp = 0
    for i in range(idx, n):
        if not checked[i] and temp != arr[i]:
            answer[k] = arr[i]
            checked[i] = True
            temp = arr[i]
            idx = i
            tracking(k+1, idx+1)
            checked[i] = False


n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
checked = [False]*n
answer = [-1]*n
tracking(0, 0)