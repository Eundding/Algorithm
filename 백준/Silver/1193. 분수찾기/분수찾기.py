n = int(input())
A, B = 0, 0
line = 1

while n > line:
    n -= line
    line += 1

if line % 2 == 0: # 짝수
    A = n
    B = line - n + 1
else: # 홀수
    A = line - n + 1
    B = n

print('%d/%d' %(A, B))
