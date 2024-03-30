n = int(input())
body = [list(map(int, input().split())) for _ in range(n)]
# body.sort(key = lambda x:(-x[0], -x[1]))
for i in range(n):
    rank=1
    for j in range(n):
        if body[i][0] < body[j][0] and body[i][1] < body[j][1]:
            rank += 1
    print(rank, end=' ')