n = int(input())
l = list(range(1, n+1))

while len(l) != 1:
    l2 = []
    for i in range(1, len(l), 2):
        l2.append(l[i])
    l = l2
print(l[0])