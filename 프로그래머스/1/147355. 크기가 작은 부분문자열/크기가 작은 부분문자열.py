def solution(t, p):
    answer = 0
    num = []
    for i in range(len(t)-len(p)+1):
        num.append(int(t[i:i+len(p)]))
    p = int(p)
    for i in range(len(num)):
        if p >= num[i]:
            answer += 1
    
        
    return answer