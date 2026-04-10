# def solution(people, limit):
#     answer = 0
#     people = sorted(people)
#     visited = [False]*len(people)
#     for i in range(len(people)):
#         if visited[i]:
#             continue
            
#         flag = False
#         visited[i] = True
#         for j in range(len(people)-1, i, -1):
#             if not visited[j] and people[i]+people[j] <= limit:
#                 flag = True # 합쳐졌는지
#                 answer += 1
#                 visited[j] = True
#                 break
#         if not flag:
#             answer += 1
    
#     return answer

# 투포인터
def solution(people, limit):
    answer = 0
    people.sort()
    s, e = 0, len(people)-1 # start,end
    while s <= e:
        if people[s]+people[e] <= limit:
            s += 1
            e -= 1
            answer += 1
            continue
        answer += 1
        e -= 1
            
            
    
    
    return answer