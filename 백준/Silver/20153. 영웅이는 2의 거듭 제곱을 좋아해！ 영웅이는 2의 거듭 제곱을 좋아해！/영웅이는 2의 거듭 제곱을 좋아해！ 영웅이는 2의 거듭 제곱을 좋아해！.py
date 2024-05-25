# 홀수개 1, 짝수개 0 => XOR
n = int(input())
l = list(map(int, input().split()))
target = 0
for i in range(n):
    target ^= l[i] # 최대 한 개 제거인데 제거를 안하는 경우

answer = target
for i in range(n):
    temp = target ^ l[i] # 숫자 하나씩 제거
    # ex) A ^ B ^ C ^ A = B ^ C
    answer = max(temp, answer)
print(str(answer)+str(answer))