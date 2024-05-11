N, K = map(int, input().split())
arr = list(map(int, input().split()))
time = 0

while True:
    cnt = 0
    flag1, flag2 = False, False
    for i in range(len(arr)):
        if flag1 and flag2: break
        if arr[i] == 0: continue

        if arr[i] == 2 and not flag2:
            flag2 = True
            arr[i] = 0
        elif arr[i] == 1 and not flag1:
            flag1 = True
            arr[i] = 0

        cnt += 1
        if cnt == K: break
    time += 1

    answer = True
    for i in range(len(arr)):
        if arr[i] != 0:
            answer = False
            break

    if answer: break
print(time)