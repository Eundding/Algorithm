def sol(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    s = s.lower()
    flag = True
    miss = ''
    for i in range(len(alphabet)):
        if alphabet[i] not in s:
            flag = False
            miss += alphabet[i]
    if flag:
        return 'pangram'
    else:
        return 'missing '+ miss

T = int(input())
for _ in range(T):
    s = input()
    print(sol(s))