import sys
sys.stdin = open('input.txt')

a = input()

if a.islower():
    b = a.upper()
else:
    b = a.lower()

print(a,b)
print(ord(a),ord(b)) #아스키코드 확인