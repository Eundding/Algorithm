def solution(number, limit, power):
    # answer = 0
    # l = []
    # for i in range(1, number+1):
    #     cnt = 0
    #     for j in range(1, i+1):
    #         if i % j == 0:
    #             cnt += 1
    #     l.append(cnt)
    # for i in range(len(l)):
    #     if l[i] <= limit:
    #         answer += l[i]
    #     else:
    #         answer += power

    l = []
    for i in range(1, number+1):
        cnt = 0
        for j in range(1, int(i**0.5)+1): # 1~i의 제곱근
            if i % j == 0:
                cnt += 1
                if j ** 2 != i:
                    cnt += 1
            if cnt > limit:
                cnt = power
                break
        l.append(cnt)
    
            
    return sum(l)