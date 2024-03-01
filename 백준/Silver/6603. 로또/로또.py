import sys
input = sys.stdin.readline

def back(k, idx):
    if k == 6:
        for i in range(6):
            print(answer[i], end=' ')
        print()
        return

    for i in range(idx, len(arr)):
        if not checked[i]:
            checked[i] = True
            answer[k] = arr[i]
            back(k+1, i+1)
            checked[i] = False


while True:
    l = list(map(int, input().split()))
    if len(l) == 1 and l[0] == 0: break # 0이면 break
    n = l[0]
    arr = l[1:]

    answer = [0]*14
    checked = [False]*n
    back(0, 0)
    print()