T = int(input())
def is_prime(a):
    for i in range(2, a):
        if a % i == 0:
            return False
    return True

def is_gold(a):
    for i in range(a//2, a):
        num1, num2 = i, n-i
        if is_prime(num1) and is_prime(num2):
            print(num2, num1)
            return
    return

for _ in range(T):
    n = int(input())
    is_gold(n)