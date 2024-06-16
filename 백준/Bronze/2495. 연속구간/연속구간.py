def sol(s):
    cnt = 1
    result = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            cnt += 1
        else:
            result = max(cnt, result)
            cnt = 1
    return max(cnt, result)


for _ in range(3):
    s = input()
    print(sol(s))