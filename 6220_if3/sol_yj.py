import sys
sys.stdin = open('input.txt')

a = input()

if a.islower():
    print(f'{a} 는 소문자 입니다.')
else:
    print(f'{a} 는 대문자 입니다.')