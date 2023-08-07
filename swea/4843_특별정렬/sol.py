import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

# 내풀이
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int,input().split()))

    # print(N,numbers)
    result = []
    while True:
        if len(numbers) != 0:
            max_num = max(numbers)
            min_num = min(numbers)
            result.append(max_num)
            result.append(min_num)
            numbers.remove(max_num)
            numbers.remove(min_num)
        else:
            break

    #print(result[0:10])
    #print(*result[0:10])
    #print(' '.join(result[0:10]))

    result2 = list(map(str,result))
    result3 =' '.join(result2[0:10])
    print(f'#{tc} {result3}')
    


# 강사님 풀이
# for tc in range(1, T+1):
#     N = int(input())
#     numbers = list(map(int,input().split()))

#     while len(numbers):
#         for m in range(len(numbers)):
#             if max_num < numbers[m]:
#                 max_num = numbers[m]
        
#         result.append(max_num)
#         numbers.remove(max_num)

#         min_num = 100000

#         for n in range(len(numbers)):
#             if min_num > numbers[n]:
#                 min_num = numbers[n]

#         result.append(min_num)
#         numbers.remove(min_num)

#         if len(result) == 10:
#             break