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
        nodes[end][start] = 1

    S, G = list(map(int, input().split()))

    # 방문체크용
    check_list = [False] * (V+1)

    queue = []

    # bfs 시작을 하기위해 시작 노드를 queue에 저장
    now = S
    check_list[now] = True
    queue.append(now)

    # 거리계산을 위한 리스트
    distance = [0] * (V+1)

    while len(queue):

        now = queue.pop()
        check_list[now] = True

        # now와 연결된 다른 노드들 순회
        for link in range(V+1):
            if nodes[now][link] == 1:
                # 아직 방문하지 않은 node가 있다면
                if not check_list[link]:
                    queue.append(link)

                    # 이전 노드의 거리 + 1
                    distance[link] = distance[now] + 1

    print(f'#{tc} {distance[G]}')


# 방문체크와 거리계산 합치기
for tc in range(1, T+1):
    V, E = list(map(int,input().split()))

    nodes = [ [0] * (V+1) for _ in range(V+1)]
    
    for i in range(E):
        start, end = list(map(int,input().split()))
        nodes[start][end] = 1
        nodes[end][start] = 1

    S, G = list(map(int, input().split()))

    # 방문체크용
    #check_list = [False] * (V+1)

    queue = []

    # bfs 시작을 하기위해 시작 노드를 queue에 저장
    now = S
    #check_list[now] = True
    queue.append(now)

    # 거리계산을 위한 리스트
    distance = [0] * (V+1)

    while len(queue):

        now = queue.pop()
        #check_list[now] = True

        # now와 연결된 다른 노드들 순회
        for link in range(V+1):
            if nodes[now][link] == 1:
                # 아직 방문하지 않은 node가 있다면
                if not distance[link]:
                    queue.append(link)

                    # 이전 노드의 거리 + 1
                    distance[link] = distance[now] + 1

                    # 이전 노드의 거리 + 1
    print(f'#{tc} {distance[G]}')