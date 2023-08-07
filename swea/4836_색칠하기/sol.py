import sys
sys.stdin = open('input.txt')

T = int(input())

# 내풀이
for tc in range(1,T+1):
    n = int(input())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().split())))
    #print(matrix)
    red = []
    blue = []

    for i in range(len(matrix)):
        if matrix[i][-1] == 1:
            for x in range(matrix[i][0],matrix[i][2]+1):
                for y in range(matrix[i][1],matrix[i][3]+1):
                    if (x,y) not in red:
                          red.append((x,y))
        if matrix[i][-1] == 2:
            for x in range(matrix[i][0],matrix[i][2]+1):
                for y in range(matrix[i][1],matrix[i][3]+1):
                    if (x,y) not in blue:
                          blue.append((x,y))
    #print(set(red)&set(blue))
    print(f'#{tc} {len(set(red) & set(blue))}')



# 강사님 풀이    
# for tc in range(1, T+1):

#     N = int(input())

#     board = [[0 for _ in range(10)] for _ in range(10)]  10*10 board 만들기


#     for i in range(N):
#         color_data = list(map(int,input().split()))

#         left_top_x = color_data[0]
#         left_top_y = color_data[1]
#         right_bottom_x = color_data[2]
#         right_bottom_y = color_data[3]

#         # 색칠시작

#         for x in range(left_top_x, right_bottom_x+1):
#             for y in range(left_top_y, right_bottom_y+1):
#                 board[x][y] += color_data

#     count = 0

#     for x in range(board) :
#         for y in range(board[0]):
#             if board[x][y] == 3:
#                 count += 1


