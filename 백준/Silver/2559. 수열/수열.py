n, k = map(int, input().split())
temperature = list(map(int, input().split()))

# 누적합
pre = [0]
sum = 0
for i in range(len(temperature)):
    sum += temperature[i]
    pre.append(sum)
max = pre[k]
for i in range(k, len(pre)):
    if max < pre[i]-pre[i-k]:
        max = pre[i]-pre[i-k]
print(max)