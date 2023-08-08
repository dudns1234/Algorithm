# 인접 행렬 방식으로 그래프로 표현
import sys
from pathlib import Path
from pprint import pprint

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1,T+1):
    V, E = list(map(int,input().split()))

    nodes = [ [] for _ in range(V+1)]

    for _ in range(E):
        start, end = list(map(int,input().split()))
        nodes[start].append(end)

    S, G = list(map(int,input().split()))

    check_list = [False]*(V+1)
    now = S
    check_list[now] = True
    stack = []
    stack.append(now)

    result = 0
    while len(stack):

        now = stack.pop()
        check_list[now] = True

        for line in nodes[now]:
            if not check_list[line]:
                if line == G:
                    result = 1
                stack.append(line)
    
    print(f'{tc} {result}')