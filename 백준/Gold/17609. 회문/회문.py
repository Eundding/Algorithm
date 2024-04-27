n = int(input())

def palindrome(s):
  for i in range(len(s)//2):
      if s[i] != s[-(i+1)]: # 회문이 아닌 순간
          # 다른 문자 2개를 각각 제거한 문자를 생성
          new_txt = new_word(s, i)
          new_txt2 = new_word(s, len(s)-(i+1))

          # 유사회문 확인
          flag1 = pseudo_palindrome(new_txt)
          flag2 = pseudo_palindrome(new_txt2)

          if flag1 or flag2: # 유사회문
              return 1
          else: # 둘 다 아님
              return 2
  return 0

def new_word(s, k):
    new_s = s[:k]+s[k+1:]
    return new_s

def pseudo_palindrome(s):
    for i in range(len(s) // 2):
        if s[i] != s[-(i + 1)]:
            return False
    return True

for _ in range(n):
    s = input()
    print(palindrome(s))