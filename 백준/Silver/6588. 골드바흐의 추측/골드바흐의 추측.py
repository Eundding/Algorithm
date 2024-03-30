import sys
input = sys.stdin.readline

def is_gold(a):
    for i in range(3, a//2+1):
        num1, num2 = i, a-i
        if prime_list[num1] and prime_list[num2]:
            print("%d = %d + %d" %(a, num1, num2))
            return
    print("Goldbach's conjecture is wrong.")
    return

prime_list = [True]*1000000 # 소수로 간주
m = int(1000000**0.5)

for i in range(2, m+1):
    if prime_list[i]:
        for j in range(2*i, len(prime_list), i):
            prime_list[j] = False



while True:
    n = int(input())
    if n == 0: break
    is_gold(n)
