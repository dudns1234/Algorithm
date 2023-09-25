import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    N = map(int,input().split())
    numbers = list(map(int,input().split()))

    heap = [0] * (N+1)
    heap_size = 0

    for i in range(N):
        heap_size += 1
        # 맨 마지막 노드에 삽입하려는 데이터를 할당
        heap[heap_size] = numbers[i]

        chile_idx = heap_size
        parent_idx = chile_idx // 2

        # 힙에 조건에 맞도록 교환 반복
        while parent_idx and heap[parent_idx] > heap[chile_idx] :
            heap[parent_idx], heap[chile_idx] = heap[chile_idx], heap[parent_idx]

            chile_idx = parent_idx
            parent_idx = chile_idx // 2

    node = N // 2
    total = 0

    # 조상에 조상에 조상을 찾다가 루트를 찾을 때까지
    while node:
        total += heap[node]
        node //= 2

    print(total)



    # 파이썬 내장함수로 이진힙 진행하기
    # import heapq
    # heapq.heapify(numbers)
    