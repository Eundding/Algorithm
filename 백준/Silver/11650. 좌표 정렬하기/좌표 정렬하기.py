T = int(input())
temp = []

for _ in range(T):
    temp.append(list(map(int, input().split())))

temp = sorted(temp, key = lambda x : (x[0], x[1]))

for i in range(len(temp)):
    print(temp[i][0], temp[i][1])