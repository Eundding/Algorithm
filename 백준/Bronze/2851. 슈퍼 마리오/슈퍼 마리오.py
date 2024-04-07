import sys
input = sys.stdin.readline

arr = []
score = 0
for i in range(10):
    arr.append(int(input()))
    
for j in arr:
    score += j
    if score >= 100:
        if score - 100 > 100 - (score - j):
            score -= j
        break
print(score)