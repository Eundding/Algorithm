# def solution(numbers):    
#     for i in range(len(numbers)):
#         numbers[i] = str(numbers[i])

#     for i in range(len(numbers)):
#         for j in range(len(numbers)-1, 0, -1):
#             if int(numbers[j-1]+numbers[j]) < int(numbers[j]+numbers[j-1]):
#                 numbers[j], numbers[j-1] = numbers[j-1], numbers[j]
    
#     answer = "".join(numbers)

#     return answer

def solution(numbers):
    for i in range(len(numbers)):
        numbers[i] = str(numbers[i])
    numbers.sort(key = lambda x: x*3, reverse=True)
    
    answer = "".join(numbers)
    if answer[0] == "0":
        return "0"
    return answer