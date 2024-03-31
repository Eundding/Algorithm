import sys
input = sys.stdin.readline

def my_round(a):
    if a - int(a) >= 0.5:
        return int(a) + 1
    return int(a)

n = int(input())
if n:
    l = [int(input()) for _ in range(n)]

    cut = my_round(n * 0.15)
    l.sort()
    if cut > 0:
        new_l = l[cut:-cut]
        print(my_round(sum(l[cut:-cut]) / len(l[cut:-cut])))
    else:
        print(my_round(sum(l) / len(l)))
else:
    print(0)