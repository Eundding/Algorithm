def solution(n):
    answer = 0
    num = []
    for i in range(1, n+1):
        temp = str(i)
        if temp[-1] == '0':
            answer += int(temp)
        elif temp[-1] == '1':
            continue
        elif temp[-1] == '2':
            answer += int(temp)
        elif temp[-1] == '3':
            continue
        elif temp[-1] == '4':
            answer += int(temp)
        elif temp[-1] == '5':
            continue
        elif temp[-1] == '6':
            answer += int(temp)
        elif temp[-1] == '7':
            continue
        elif temp[-1] == '8':
            answer += int(temp)
        elif temp[-1] == '9':
            continue
        
            
    return answer