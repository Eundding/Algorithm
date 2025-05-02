n = input()
answer = 'YES'
for w in 'MOBIS':
    if w not in n:
        answer = 'NO'
        break
print(answer)