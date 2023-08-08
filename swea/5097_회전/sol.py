import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

# 내풀이
for tc in range(1, T+1):
    N, M = map(int,input().split())
    temp=list(map(int,input().split()))

    result = []
    for _ in range(M):
        for i in range(len(temp)):
            result.append(temp[i])
    print(f'#{tc} {result[M]}')

    # while len(result) >= M:
        
    #     for i in temp:
    #         print(i)
    #         result.append(i)


# 강사님 풀이 (Queue)   
for tc in range(1, T+1):
    N, M = list(map(int,input().split()))
    numbers=list(map(int,input().split()))

    # 방법1. 직접 M번 반복
    # for _ in range(M):
    #     data = numbers.pop(0)
    #     numbers.append(data)

    # print(numbers[0])
    
    # 방법2.
    remain = M % N
    print(numbers[remain])