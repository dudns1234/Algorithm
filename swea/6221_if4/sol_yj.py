import sys
sys.stdin = open('input.txt',encoding='UTF8')

a = input()
b = input()

if a == "바위" and b == "가위":
    print("Result : Man1 Win!")
elif a == "바위" and b == "바위":
    print("Result : Draw")