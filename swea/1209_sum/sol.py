import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1,T+1):
    tc = int(input())
    matrix = []

    for _ in range(100):
        row = list(map(int,input().split()))
        matrix.append(row)
    #print(matrix)
    total = 0
    # raw 기준
    for i in range(100):
        temp = 0
        for j in range(100):
           temp += matrix[i][j] # matrix[0][0], [0][1]
    
        if temp > total:
            total = temp

    for i in range(100):
        temp = 0
        for j in range(100):
            temp += matrix[j][i] # matrix[0][0], [1][0]
        
        if temp > total:
            total = temp
    temp = 0
    for i in range(100):
        temp += matrix[i][i]
    
    if temp > total:
        total = temp
    temp = 0
    
    for i in range(100):
        temp += matrix[99-i][i]
    
    if temp > total:
        total = temp

    print(f'#{tc} {total}')


        
        






# # 강사님 풀이
# for tc in range(1, T+1):
#     tc = int(input())

#     matrix = []

#     for _ in range(100):
#         row = list(map(int,input().split()))
#         matrix.append(row)

#     #print(matrix)
#     total = 0

#     # 가로줄
#     for row in range(len(matrix)):  # range(100)
#         temp = 0
#         for col in range(len(matrix[0])):
#             temp += matrix[row][col]
        
#         if total < temp:  # 4835_구간합과 동일
#             total = temp
#     # 세로줄
#     for col in range(100):
#         temp = 0
#         for row in range(100):
#             temp += matrix[row][col]
        
#         if total < temp:
#             total = temp
#     # 대각선 (좌상단 => 우하단 반복)
#     temp = 0
#     for i in range(100):
#        temp += matrix[i][i]

#     if total < temp:
#         total = temp
#     # 대각선 (우상단 => 좌하단 반복)
#     temp = 0 
#     for i in range(100):
#         temp += matrix[i][99-i]
    
#     if total < temp:
#         total = temp
    
# print(f'#{tc} {total}')

