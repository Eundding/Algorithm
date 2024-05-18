n = int(input())
MAX = 1000001
is_prime = [True]*MAX
is_prime[0], is_prime[1] = False, False
answer = -1

# 에라토스테네스의 체
for i in range(2, MAX):
    if is_prime[i]:
        for j in range(i*2, MAX, i):
            is_prime[j] = False

for i in range(n, MAX):
    if is_prime[i] and str(i) == str(i)[::-1]:
        answer = i
        break

if answer == -1:
    print(1003001)
else:
    print(answer)