n = int(input())
bin_num = bin(n)
bin_num = bin_num[2:]

ans = 0
for i in range(len(bin_num)):
    if bin_num[i] == '1':
        temp = 3**(len(bin_num)-1-i) # 이진수처럼 생각
        ans += temp
print(ans)