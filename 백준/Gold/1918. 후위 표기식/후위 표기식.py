import sys
input = sys.stdin.readline

s = list(input().rstrip())
stack = []
answer = ''

for i in range(len(s)):
    if s[i].isalpha(): 
        answer += s[i]
    elif s[i] == '(':
        stack.append(s[i])
    elif s[i] in ['*', '/']:
        while stack and stack[-1] in ['*', '/']:
            answer += stack.pop()
        stack.append(s[i])
    elif s[i] in ['+', '-']:
        while stack and stack[-1] != '(': 
            answer += stack.pop()
        stack.append(s[i])
    else: # )라면
        while stack and stack[-1] != '(':
            answer += stack.pop()
        stack.pop() # 열린 괄호 pop

while stack:
    answer += stack.pop()
print(answer)