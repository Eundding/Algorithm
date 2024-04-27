n = int(input())
name = input()
k = int(input())
answer = k

if name == 'annyong':
    if k%2 == 0:
        k += 1
else:
    if k % 2 != 0:
        k += 1
if k > n:
    k -= 2

print(k)