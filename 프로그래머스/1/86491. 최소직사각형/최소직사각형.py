def solution(sizes):
    answer = 0
    # 더 큰 걸 왼쪽에 몰아 넣자
    for i in range(len(sizes)):
        x, y = sizes[i][0], sizes[i][1]
        if x < y:
            sizes[i][0] = y
            sizes[i][1] = x
    
    answer = max(row[0] for row in sizes)*max(row[1] for row in sizes) 
    return answer