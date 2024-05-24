a, b, c = map(int, input().split())
# b를 c회 반복
# B ^ B = 0
# B ^ B ^ B = B
# ----
# A ^ 0 = A
# A ^ B
if c % 2 == 0: 
    print(a)
else:
    print(a^b)