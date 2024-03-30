h, m = map(int, input().split())
c = int(input())

all = 60*h + m + c
print((all//60)%24, all%60)