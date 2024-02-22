import sys
input = sys.stdin.readline

def tracking(k):
    if k == m:
        for i in range(m):
            print(answer[i], end = ' ')
        print()
        return

    temp = 0
    for i in range(n):
        if checked[i] < m and temp != arr[i]:
            checked[i] += 1
            answer[k] = arr[i]
            temp = arr[i]
            tracking(k+1)
            checked[i] -= 1



n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
answer = [-1]*n
checked = [0]*n
tracking(0)