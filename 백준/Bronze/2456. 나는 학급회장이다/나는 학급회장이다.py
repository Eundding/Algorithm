import sys
input = sys.stdin.readline

n = int(input())
num1, num2, num3 = [], [], []
for _ in range(n):
    a, b, c = map(int, input().split())
    num1.append(a)
    num2.append(b)
    num3.append(c)


if sum(num1) > sum(num2) and sum(num1) > sum(num3):
    print(1, sum(num1))
elif sum(num2) > sum(num1) and sum(num2) > sum(num3):
    print(2, sum(num2))
elif sum(num3) > sum(num2) and sum(num3) > sum(num1):
    print(3, sum(num3))
# 3점으로 갈리는 경우
elif num1.count(3) > num2.count(3) and num1.count(3) > num3.count(3):
    print(1, sum(num1))
elif num1.count(3) < num2.count(3) and num2.count(3) > num3.count(3):
    print(2, sum(num2))
elif num3.count(3) > num2.count(3) and num3.count(3) > num1.count(3):
    print(3, sum(num3))
# 모두 같은경우
elif num1.count(3) == num2.count(3) and num1.count(3) == num3.count(3):
    if num1.count(2) == num2.count(2) and num1.count(2) == num3.count(2):
        print(0, sum(num1))

# 2점으로 갈리는 경우
elif num1.count(3) == num2.count(3):
    if num1.count(2) > num2.count(2):
        print(1, sum(num1))
    elif num1.count(2) < num2.count(2):
        print(2, sum(num2))
    else:
        print(0, sum(num1))
elif num1.count(3) == num3.count(3):
    if num1.count(2) > num3.count(2):
        print(1, sum(num1))
    elif num1.count(2) < num3.count(2):
        print(3, sum(num3))
    else:
        print(0, sum(num1))
elif num2.count(3) == num3.count(3):
    if num2.count(2) > num3.count(2):
        print(2, sum(num2))
    elif num2.count(2) < num3.count(2):
        print(3, sum(num3))
    else:
        print(0, sum(num2))

