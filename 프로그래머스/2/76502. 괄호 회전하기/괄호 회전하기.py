from collections import deque

def check(q, idx):
    if idx != 0:
        q.rotate(-1)

    stack = [0]
    for i in range(len(q)):
        if q[i] == '[' or q[i] == '(' or q[i] == '{':
            stack.append(q[i])
        # elif (q[i] == ']') and ('[' in stack):
        #     stack.remove('[')
        # elif (q[i] == ')') and ('(' in stack):
        #     stack.remove('(')
        # elif (q[i] == '}') and ('{' in stack):
        #     stack.remove('{')
        elif (q[i] == ']') and (stack[-1] == '['):
            stack.pop()
        elif (q[i] == ')') and (stack[-1] == '('):
            stack.pop()
        elif (q[i] == '}') and (stack[-1] == '{'):
            stack.pop()
        else:
            return False

    if len(stack) == 1:
        return True
    
    return False


def solution(s):
    answer = 0
    queue = deque()
    for i in s:
        queue.append(i)
    for i in range(len(s)):
        if check(queue, i):
            answer += 1
    return answer