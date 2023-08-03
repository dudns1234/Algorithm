import sys
sys.stdin = open('input4.txt')

N, M = map(int,input().split())
matrix = []

for i in range(N):
    numbers = list(map(int,input().split()))
    #print(numbers)
    matrix.append(numbers)
#print(matrix)

# row 기준 반복 (가로우선탐색)
for row in range(len(matrix)):     # for row in range(N)
    #print(matrix[row])
    for col in range(len(matrix[0])):     # for row in range(M)
        print(matrix[row][col])

# col 기준 반복 (세로우선탐색)
for col in range(len(matrix[0])) :
    for row in range(len(matrix)):
        print(matrix[row][col])