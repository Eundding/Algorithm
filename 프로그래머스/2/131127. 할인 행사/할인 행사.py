# import copy
from collections import Counter
def solution(want, number, discount):
    answer = 0
    dict1 = {}
    for i in range(len(want)):
        dict1[want[i]] = number[i]
    for i in range(len(discount)):
        if dict1 == Counter(discount[i:i+10]):
            answer += 1

    return answer

#     for i in range(0, len(discount)-sum(number)):
#         dict2 = copy.deepcopy(dict1)
#         cnt = 0
#         for j in range(i, i+sum(number)):
#             if discount[j] not in dict2.keys():
#                 continue
#             elif dict2[discount[j]] <= 0: continue
#             else:
#                 dict2[discount[j]] -= 1  
#                 if dict2[discount[j]] == 0: 
#                     cnt += 1

#             if cnt == len(want):
#                 return i+1
    
#     return 0