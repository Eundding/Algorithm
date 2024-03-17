a, b = map(int, input().split())
max_value = max(a, b)
min_value = min(a, b)

if max_value == min_value:
    print(0)
else:
    print(max_value - min_value - 1)
for i in range(min_value+1, max_value):
    print(i, end=' ')