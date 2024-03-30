# import sys
# input = sys.stdin.readline
def check(s):
    for i in range(len(s)//2):
        if s[i] != s[-(i+1)]:
            return False
    return True

while True:
    number = input()
    if number == '0': break
    if check(number):
        print('yes')
    else:
        print('no')