N = int(input())
rope = []

for i in range(N):
    r = int(input())
    rope.append(r)

rope.sort()

# print(rope[0] * N) 모든 로프를 써야하는 줄 알았다.

weight = []
for i in range(N):
    w = rope[i] * (N-i)
    weight.append(w)

weight.sort(reverse=True)
print(weight[0])