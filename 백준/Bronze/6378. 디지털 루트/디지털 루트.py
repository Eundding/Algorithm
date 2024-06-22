while True:
    N = int(input())
    if N == 0: break
    temp = N
    
    while temp >= 10:
        s = str(temp)
        temp = 0
        for i in range(len(s)):
            temp += int(s[i])
    print(temp)