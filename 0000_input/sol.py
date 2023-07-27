import sys
sys.stdin = open('input.txt')

TC = int(input()) #9개라는 testcase를 받고 9개를 진행

for i in range(TC):
    N = int(input())

    if N % 2 == 1:
     print('홀수')
    else:
        print('짝수')

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