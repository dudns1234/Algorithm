import sys
sys.stdin = open('input2.txt')

# 1차원 list input 받기

## 방법1
numbers = input().split()
print(numbers)

for num in numbers:
   int_num = int(num)  # 여기서 int로 변환
   if int_num % 2 == 1:
      print(f'{int_num}은 홀수입니다.')

# 방법2
numbers = list(map(int,input().split()))  # map함수 : 여러개 들어가 있는 집합을 하나하나 꺼내서 int로 바꿔주는 함수
print(numbers)

for number in numbers:
   if number % 2 == 1:
      print(f'{number}은 홀수입니다.')




