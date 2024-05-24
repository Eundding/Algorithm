X = int(input())
bar = 64
current = 0
cnt = 1
while True:
    if bar + current <= X: break
    bar = bar >> 1 # bar //= 2
    if bar + current < X:
        current += bar
        cnt += 1
print(cnt)