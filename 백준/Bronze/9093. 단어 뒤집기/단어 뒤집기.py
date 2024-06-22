T = int(input())
for _ in range(T):
    l = list(input().split())
    for i in range(len(l)):
        print(l[i][::-1], end=" ")
    print()