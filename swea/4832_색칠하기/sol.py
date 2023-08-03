import sys
sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T+1):
    N = int(input())
    list1 = []
    for i in range(N):
        list1.append(list(map(int,input().split()))) # x1 = 2, y1 = 2, x2 = 4, y2 = 4
    
    print(list1)
    
    for i in list1:
        if i[-1] == 1:
            red = []
            blue = []
            for x in range(i[0],int(i[2])+1):
                for y in range(i[0],int(i[2])+1):
                    red.append((x,y))
            print(red)
        if i[-1] == 2:
            for x in range(i[0],int(i[2])+1):
                for y in range(i[0],int(i[2])+1):
                    blue.append((x,y))
            #print(blue)
    print(f'#{tc} {len(set(red) & set(blue))}')


        

    
# for tc in range(1, T+1):

#     N = int(input())

#     board = [[0 for _ in range(10)] for _ in range(10)]


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


