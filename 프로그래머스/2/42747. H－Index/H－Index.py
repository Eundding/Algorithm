def solution(citations):
    answer = 0
    citations.sort() # 6 7 8 9
    
    e = citations[-1]
    
    while e:
        cnt = 0
        for i in range(len(citations)):
            if citations[i] >= e:
                cnt += 1
        if cnt >= e:
            return e
        
        e-= 1
    return 0