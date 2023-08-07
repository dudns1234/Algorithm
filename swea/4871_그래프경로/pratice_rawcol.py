import sys
from pathlib import Path
from pprint import pprint

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    V, E = list(map(int,input().split()))

    nodes = [ [0] * (V+1) for _ in range(V+1)]
    
    for i in range(E):
        start, end = list(map(int,input().split()))
        nodes[start][end] = 1

    S, G = list(map(int, input().split()))

    check_list = [False] * (V+1)

    stack = []

    now = S
    check_list[now] = True
    stack.append(now)

    while len(stack):

        now = stack.pop()
        check_list[now] = True

        for link in range(V+1):
            if nodes[now][link] == 1:
                if not check_list[link]:
                    if link == 6:
                        result = 1
                    stack.append(link)
    print(f'#{tc} {result}')

