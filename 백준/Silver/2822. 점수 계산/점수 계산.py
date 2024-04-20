import sys
input = sys.stdin.readline

l = [int(input()) for _ in range(8)]
l2 = l[:]
l.sort(reverse=True)
print(sum(l[:5]))

answer = []
for i in range(5):
    for j in range(8):
        if l[i] == l2[j]:
            answer.append(j+1)
            break
answer.sort()
print(*answer)