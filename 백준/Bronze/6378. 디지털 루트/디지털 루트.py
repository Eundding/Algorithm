while True:
    s = input()
    if s == '0': break

    while True:
        result = 0
        if len(s) >= 3 or (len(s) == 2 and int(s[0]) + int(s[1]) >= 10):
            for i in range(len(s)):
                result += int(s[i])
            s = str(result)
        else:
            break

    if len(s) == 1:
        print(s[0])
    else:
        print(int(s[0]) + int(s[1]))