import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())


# 강사님 풀이
for tc in range(1, T+1):
    code = input()
    stack = []
    for char in code:
        if char == '(' or char == '{':
            stack.append(char)
        elif len(stack) and char == ')' and stack[-1] == '(':
            stack.pop()
        elif len(stack) and char == '}' and stack[-1] == '{':
            stack.pop()
        elif char == '}' or char == ')':
            stack.append(char)
    
    if len(stack) == 0:
        result = 1
    else:
        result = 0
    
    print(f'#{tc} {result}')


#     for i in a:
#         if i == '(':
#             result.append(i)
#         elif i == ')':
#             result.append(i)
#         elif i == '{':
#             result2.append(i)
#         elif i =='}':
#             result2.append(i)
#         else:
#             pass
# print(result)
# print(result2)

