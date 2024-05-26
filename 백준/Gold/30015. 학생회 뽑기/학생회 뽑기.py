N, K = map(int, input().split())
l = list(map(int, input().split()))

result = 0
for bit in range(31, -1, -1): # 맨 앞 비트부터 확인
    temp_result = result | (1 << bit)

    count = 0
    for i in l: # 임시 결과를 유지할 수 있는 학생 수 세기
        if (i & temp_result) == temp_result:
            count += 1

    if count >= K: # 유지할 수 있는 학생 수 K이상이면
        result = temp_result

print(result)