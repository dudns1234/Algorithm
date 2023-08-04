import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

# for tc in range(1, T+1):
#     # P : 책의 장수(마지막 페이지)
#     # A : A가 찾아야 하는 목적페이지
#     # B : B가 찾아야 하는 목적페이지
#     # l : left
#     # r : right
#     # c : center = int((l+r)/2))
#     P, A, B = map(int,input().split())
#     N = [A,B]
#     A_count = 1
#     B_count = 1
#     c = int(P/2)
#     #print(N)

#     while True:
#         if c <= A:
#             c = int(c+P)/2
#             A_count+=1
#         else:
#             c = c/2
#             A_count+=1
#         if c == A:
#             break
#     print(A_count)


       
    # while True:
    #     if c <= B:
    #         c = int(c+P)/2
    #         B_count+=1
    #     else:
    #         c = c/2
    #         B_count+=1
    #     if c == B:
    #         break
    
    # if A_count > B_count:
    #     print(f'{tc} B')
    # elif A_count < B_count:
    #     print(f'{tc} A')
    # elif A_count == B_count:
    #     print(f'{tc} 0')





# A : 300 (400,300)
# i = 1, r = 400, c = 400/2 = 200 (c == A)
# i = 200, r = 400, c = 300


for tc in range(1, T+1):
    # P : 책의 장수(마지막 페이지)
    # A : A가 찾아야 하는 목적페이지
    # B : B가 찾아야 하는 목적페이지
    P, A, B = map(int,input().split())
    count_a = 0
    left = 1
    right = P

    while True:  # 무한하게 목척페이지에 도착할 때까지 반복해라
        middle = int((left+right)/2)

        # 목적 페이지가 가운데 보다 왼쪽에 있는 경우
        if A < middle:
            right = middle
        # 목적 페이지가 가운데 보다 오른쪽에 있는 경우
        elif middle < A:
            left = middle
        # 둘다 아니라면 목적페이지에 도착!!!
        else:
            break

        count_a += 1

    count_b = 0
    left = 1
    right = P

    while True:  # 무한하게 목척페이지에 도착할 때까지 반복해라
        middle = int((left+right)/2)

        # 목적 페이지가 가운데 보다 왼쪽에 있는 경우
        if B < middle:
            right = middle
        # 목적 페이지가 가운데 보다 오른쪽에 있는 경우
        elif middle < B:
            left = middle
        # 둘다 아니라면 목적페이지에 도착!!!
        else:
            break

        count_b += 1

    print(count_a,count_b)
