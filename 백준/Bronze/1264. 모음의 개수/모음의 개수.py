while True:
    s = input()
    if s == '#': break
    cnt = 0
    for i in ['a', 'e', 'i', 'o', 'u']:
        cnt += s.count(i.lower()) + s.count(i.upper())
    print(cnt)