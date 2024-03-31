apartment = []
for i in range(15): # 층
    l = []
    for j in range(1, 15): # 호
        if i == 0:
            l.append(j)
        elif j == 1:
            l.append(1)
        else:
            l.append(apartment[i-1][j-1] + l[j-2])
    apartment.append(l)

T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    print(apartment[k][n-1])


