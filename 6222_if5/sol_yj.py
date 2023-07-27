import sys
sys.stdin = open('input.txt')

a = input()

if a.isupper():
    code1 = a.lower()
    print(f'{code1}(ASCII:{ord(code1)}) => {a}(ASCII: {ord(a)})')
elif a.islower():
    code2 = a.upper()
    print(f'{a}(ASCII:{ord(a)}) => {code2}(ASCII: {ord(code2)})')
elif a.isalpha() == False:
    print(a)


