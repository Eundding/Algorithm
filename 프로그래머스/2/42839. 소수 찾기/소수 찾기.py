from itertools import permutations

def check(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    
    l = []
    for i in range(1, len(numbers)+1):
        for comb in permutations(numbers, i):
            temp = ''
            for x in comb:
                temp += x
            if int(temp) not in l:
                l.append(int(temp))
    
    # 소수 판별
    for x in l:
        if  x == 0 or x == 1 : continue
        
        answer += check(x)
    
    return answer