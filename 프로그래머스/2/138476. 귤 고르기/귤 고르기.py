from collections import defaultdict
def solution(k, tangerine):
    answer = 0
    dict = defaultdict(int)
    for i in range(len(tangerine)):
        dict[tangerine[i]] += 1
    
    dict = sorted(dict.items(), key= lambda x:-x[1]) # idx 1은 value, 0은 key
    cnt = 0
    for i in range(len(dict)):
        cnt += dict[i][1]
        if cnt >= k: 
            answer = i+1
            break
            
    
    return answer