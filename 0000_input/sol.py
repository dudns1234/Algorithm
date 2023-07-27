import sys
sys.stdin = open('input.txt')

# N = int(input())

# if N % 2 == 1:
#     print('홀수')
# else:
#     print('짝수')

# N = int(input())

# if N % 2 == 1:
#     print('홀수')
# else:
#     print('짝수')

#input.txt
# 9 
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 의미 : 맨 첫번째에 있는 9는 testcase(TC) 갯수를 의미함. 그래서 첫번째는 9개의 데이터를 줄거니까 진행하라는 의미

TC = int(input()) #9개라는 testcase를 받고 9개를 진행

for i in range(TC):
    N = int(input())

    if N % 2 == 1:
     print('홀수')
    else:
        print('짝수')

# 1차원 list input 받기

# numbers = input().split()
# #print(numbers)
# for num in numbers:
#    int_num = int(num)
#    if int_num % 2 == 1:
#       print(f'{int_num}은 홀수입니다.')

numbers = list(map(int,input().split()))  # map함수 : 여러개 들어가 있는 집합을 하나하나 꺼내서 int로 바꿔주는 함수
print(numbers)

for number in numbers:
   if number % 2 == 1:
      print(f'{number}은 홀수입니다.')

# 1차원 list input 받기
N = int(input())
matrix = []

for i in range(N):
   numbers = list(map(int,input().split())) #글자를 숫자로
   #print(numbers)  #1차원데이터로 출력
   matrix.append(numbers)
print(matrix) #2차원데이터로 출력


for row in matrix:
   #print(row)
   for item in row:
      if item == 5:
         print('5가 있음')
      else:
         print('없음')


