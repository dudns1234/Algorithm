import sys
sys.stdin = open('input3.txt')

# 2차원 list input 받기
N = int(input())
matrix = []

for i in range(N):
   numbers = list(map(int,input().split())) #글자를 숫자로
   print(numbers)  #1차원데이터로 출력
   matrix.append(numbers)
print(matrix) #2차원데이터로 출력

# 이중 for문
for row in matrix:
   #print(row)
   for item in row:
      if item == 5:
         print('5가 있음')
      else:
         print('없음')


