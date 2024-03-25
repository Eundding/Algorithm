def solution(n):
    answer = ''
    s1 = '수'
    s2 = '수박'
    if n % 2 == 0:
        answer += s2*(n//2)
    else:
        answer += s2*(n//2)+s1
    return answer