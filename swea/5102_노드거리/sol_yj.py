import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    # V:노드개수
    # E:간선수
    V, E = map(int,input().split())

    nodes = [[] for _ in range(V+1)]
    
    for _ in range(E):
        start, end = list(map(int,input().split()))
        nodes[start].append(end)
        nodes[end].append(start)

    
    S, G = map(int,input().split())

    print(nodes)

    #check_list = [False for _ in range(V+1)]
    check_list = [False] * (V+1)

    queue = []

    queue.append(S)
    check_list[S] = True
    
    count = 0
    while len(queue):

        now = queue.pop(0)
        check_list[now] = True

        for link in nodes[now]:
            if not check_list[link]:
                if link != nodes[G]:
                    count += 1
                else:
                    break
                queue.append(link)

    print(f'#{tc} {count}')




