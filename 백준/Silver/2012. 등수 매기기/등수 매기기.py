import sys
input = sys.stdin.readline

N = int(input())
predict = [int(input()) for _ in range(N)]

predict.sort() # 예상등수 정렬

result = 0
for i in range(1, N+1):
    result += abs(predict[i-1] - i)

print(result)
