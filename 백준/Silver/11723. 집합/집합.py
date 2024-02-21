import sys
input = sys.stdin.readline

n = int(input())
l = []
for _ in range(n):
    s = input().strip()

    if s == 'all':
        l = [i for i in range(1, 21)]
        continue
    elif s == 'empty':
        l = []
        continue

    else:
        c, i = s.split()
        i = int(i)
        if c == 'add':
            if i not in l:
                l.append(i)

        elif c == 'remove':
            if i in l:
                l.remove(i)

        elif c == 'check':
            if i in l: print(1)
            else: print(0)

        elif c == 'toggle':
            if i in l: l.remove(i)
            else: l.append(i)
