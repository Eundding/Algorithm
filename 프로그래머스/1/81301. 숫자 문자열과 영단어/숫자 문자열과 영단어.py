def solution(s):
    answer = ''

    number = ['zero', 'one', 'two', 'three', 'four', 
              'five', 'six', 'seven', 'eight', 'nine']
    alpha=''
    for i in range(len(s)):
        if s[i].isdigit() :
            answer += s[i]
        else:
            alpha += s[i]
        if alpha in number:
            answer += str(number.index(alpha))
            alpha = ''
    
    return int(answer)