T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    important  = list(map(int,input().split()))
    index = [i for i in range(N)]
    index[M] = 'target'
    cnt = 0

    while important:
        if important[0] == max(important):
            cnt += 1
            if index[0] == 'target':
                print(cnt)
                break
            important.pop(0)
            index.pop(0)

        else:
            important.append(important.pop(0))
            index.append(index.pop(0))