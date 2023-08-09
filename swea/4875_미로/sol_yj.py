import sys
from pathlib import Path
from pprint import pprint

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    miro = []
    for _ in range(N):
        miro.append(list(map(int,input())))
    #pprint(miro)
    
    miropan = []
    for i in range(N):
        miropan.append([False] * N)
    #pprint(miropan)


    stack = []
    for row in range(len(miro)):
        for col in range(len(miro[0])): 
            if miro[row][col] == 2:
                stack.append((row,col))

    #print(stack)
    result = 0
    while len(stack):
        print(stack)
        now = stack.pop()
        row, col = now
        miropan[row][col] = True

        # miro[row][col] = 1 미로판을 안만들경우

        for x, y in [(-1,0),(1,0),(0,-1),(0,1)]: # 상 하 좌 우
            new_row = row+x
            new_col = col+y
            if  0 <= new_row < N and 0 <= new_col < N:
                if miro[new_row][new_col] == 0 and not miropan[new_row][new_col]:   
                    stack.append((new_row,new_col))
    
                if miro[new_row][new_col] == 3:
                    result = 1
                    break

        if result == 1:
            break
    print(f'#{tc} {result}')


# 미로판을 안만들경우
for tc in range(1, T+1):
    N = int(input())
    miro = []
    for _ in range(N):
        miro.append(list(map(int,input())))
    #pprint(miro)

    stack = []
    for row in range(len(miro)):
        for col in range(len(miro[0])): 
            if miro[row][col] == 2:
                stack.append((row,col))

    #print(stack)
    result = 0
    while len(stack):
        print(stack)
        now = stack.pop()
        row, col = now

        miro[row][col] = 1 

        for x, y in [(-1,0),(1,0),(0,-1),(0,1)]: # 상 하 좌 우
            new_row = row+x
            new_col = col+y
            if  0 <= new_row < N and 0 <= new_col < N:
                if miro[new_row][new_col] == 0:   
                    stack.append((new_row,new_col))

                if miro[new_row][new_col] == 3:
                    result = 1
                    break

        if result == 1:
            break
    print(f'#{tc} {result}')