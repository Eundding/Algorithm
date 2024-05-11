rect = []
for i in range(101):
    temp = ['0']*101
    rect.append(temp)

for i in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(x1+1, x2+1):
        for k in range(y1+1, y2+1):
            rect[j][k] = '1'

cnt = 0
for i in range(101):
    cnt += rect[i].count('1')
print(cnt)