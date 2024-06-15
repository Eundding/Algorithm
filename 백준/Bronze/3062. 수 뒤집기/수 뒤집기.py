T = int(input())
for _ in range(T):
    s = input()
    reverse_s = s[::-1]
    result = str(int(s) + int(reverse_s))
    if result == result[::-1]:
        print('YES')
    else:
        print('NO')