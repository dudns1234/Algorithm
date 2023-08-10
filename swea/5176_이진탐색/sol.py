import sys
from pathlib import Path
import statistics as st

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

def inorder(idx):
    global count

    if idx <= N:

        # 왼쪽자식
        inorder(idx*2)

        # 현재노드
        tree[idx] = count
        count += 1   

        # 오른쪽자식
        inorder(idx*2 + 1)


for tc in range(1, T+1):
    N = int(input())

    tree = [0] * (N+1)

    count = 1  # tree에 값을 넣어줄 때 차례로 1 이기 때문에

    inorder(1)   # 1부터 시작하기 때문에

    print(tree)
