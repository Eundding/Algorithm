from collections import defaultdict
def solution(survey, choices):
    answer = ''
    dict = defaultdict(int)
    score = [0, 3, 2, 1, 0, 1, 2, 3]
    for i, type in enumerate(survey):
        if choices[i] <= 3:
            dict[type[0]] += score[choices[i]]   
        elif choices[i] == 4:
            continue
        else: # 5,6,7
            dict[type[1]] += score[choices[i]]   
        
    
    # 비교
    if dict['R'] >= dict['T']:
        answer += 'R'
    else:
        answer += 'T'
    
    if dict['C'] >= dict['F']:
        answer += 'C'
    else:
        answer += 'F'
        
    if dict['J'] >= dict['M']:
        answer += 'J'
    else:
        answer += 'M'
    
    if dict['A'] >= dict['N']:
        answer += 'A'
    else:
        answer += 'N'
    
    
            
            
    return answer