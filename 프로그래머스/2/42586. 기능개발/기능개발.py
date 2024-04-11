def solution(progresses, speeds):
    answer = []
    day, cnt = 0, 0
    
    while len(progresses) > 0:
        if progresses[0] + day*speeds[0] >= 100: # 완료
            cnt += 1
            progresses.pop(0)
            speeds.pop(0)
        else:
            if cnt > 0: # 완료된 기능이 있다면
                answer.append(cnt)
                cnt = 0
            else:
                day += 1
            
            
            
    answer.append(cnt)
    return answer