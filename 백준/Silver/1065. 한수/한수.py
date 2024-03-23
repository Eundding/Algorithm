n = int(input())

def check(a):
    if a < 100: # 기저 사례
        return True
    num_list = list(str(a))
    d = int(num_list[1])-int(num_list[0])
    for i in range(2, len(num_list)):
        if d != int(num_list[i]) - int(num_list[i-1]):
            return False
    return True

cnt = 0
for i in range(1, n+1):
    if check(i):
        cnt += 1
print(cnt)
