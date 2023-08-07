import sys
from pathlib import Path
from pprint import pprint

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    # V : 노드 수 / E : 간선 수 (ex.6 5)
    V, E = list(map(int, input().split()))

    nodes = [[] for i in range(V+1)] 

    # print(nodes)
    for _ in range(E):
        # start : 출발노드 / end : 끝노드 (ex. 1 4 / 1 3 / 2 3 / 2 5 / 4 6)
        start,end = list(map(int, input().split()))
        nodes[start].append(end)
    # print(nodes)

    # S : 시작노드 / G : 도착노드 (ex 1 6) = 1에서 6까지 이동가능한가?
    S, G = list(map(int, input().split()))

    check_list = [False] * (V+1)  # 방문체크용
    stack = []   # 담을곳

    now = S # 시작노드
    check_list[now] = True
    stack.append(now)

    while len(stack):
        # print(stack)
        now = stack.pop()
        check_list[now] = True
        
        for link in nodes[now]: #nodes[3]인 경우 값이 없기때문에 도로 올라감.
            # print(link)
            if not check_list[link]:
                if link == G:
                    result = 1
                stack.append(link)

    print(f'#{tc} {result}')


    