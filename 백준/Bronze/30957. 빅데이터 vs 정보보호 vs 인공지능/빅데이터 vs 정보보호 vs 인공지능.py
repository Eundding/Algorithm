n = int(input())
l = list(input())
B, S, A = 0, 0, 0
for i in l:
    if i == "B":
        B += 1
    elif i == "S":
        S += 1
    elif i == "A":
        A += 1

answer = ''
if B == S and S == A:
    answer = 'SCU'
else:
    if B == max(B, S, A):
        answer += 'B'
    if S == max(B, S, A):
        answer += 'S'
    if A == max(B, S, A):
        answer += 'A'
print(answer)
