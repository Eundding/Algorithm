s = input()
flag = True
check = 'UCPC'

for i in range(4):
    if check[i] in s:
        idx = s.index(check[i])
        s = s[idx+1:]
    else:
        flag = False
        break
if flag:
    print("I love UCPC")
else:
    print("I hate UCPC")