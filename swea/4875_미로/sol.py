import sys
from pathlib import Path
from pprint import pprint

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

# for tc in range(1, T+1):
#     N = int(input())
#     miro = []
#     for i in range(N):
#         miro.append(list(input()))
#     #pprint(miro)
    
#     miropan = []
#     for i in range(N):
#         miropan.append([False] * N)
#     #pprint(miropan)

#     path = '0'
#     wall = '1'
#     now = '2'
#     end = '3'

#     stack = []

#     for row in range(len(miro)):
#         for col in range(len(miro[0])): 
#             if miro[row][col] == '2':
#                 stack.append((row,col))

#     #print(stack)
#     result = 0
#     while len(stack):

#         now = stack.pop()
#         row, col = now
#         miropan[row][col] = True

#         for x, y in [(-1,0),(1,0),(0,-1),(0,1)]: # 상 하 좌 우
#             new_row = row+x
#             new_col = col+y
#             if  0 <= new_row < N and 0 <= new_col < N:
#                 if miro[new_row][new_col] == path and not miropan[new_row][new_col]:   
#                     stack.append((new_row,new_col))
    
#                 if miro[new_row][new_col] == end:
#                     result = 1
#                     break

#         if result == 1:
#             break
#     print(result)


# 강사님 풀이
for tc in range(1, T+1):
    N = int(input())

    maze = [list(map(int, input())) for _ in range(N)]

    # 시작점 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start = (i, j)

    
    # dfs를 동작하기 위한 스택
    stack = []
    stack.append(start)

    # 상하좌우 델타값
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    result = 0

    while len(stack):

        now = stack.pop()
        x, y = now[0], now[1]

        maze[x][y] = 1

        # pprint(maze)
        # print()

        # 상하좌우를 바라보는 코드
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로 범위 안에 있다면 진행
            if 0 <= nx < N and 0 <= ny < N:
                # 길이라면
                if maze[nx][ny] == 0:
                    stack.append( (nx, ny) )
                # 도착지점이라면
                elif maze[nx][ny] == 3:
                    result = 1
                    break

    print(f'#{tc} {result}')