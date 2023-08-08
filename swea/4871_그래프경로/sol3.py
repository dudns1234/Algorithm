# 인접 리스트 방식으로 그래프로 표현 => 재귀함수를 이용하여 풀아
import sys
from pathlib import Path
from pprint import pprint

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

def dfs(now): # stack을 안쓰고 재귀  if dfs(1) -> df(4), df(3)-> df(4)로 인해 df(6)호출/
    # now 도착하면 방문 체크
    check_list[now] = True

    # 현재 위치를 기준으로 연결된 노드 찾기
    for link in nodes[now]:
        # 방문안한 노드들은 스택에 추가 => 재귀함수 실행
        if not check_list[link]:
            dfs(link)


for tc in range(1, T+1):
    # V : 노드 수(O) / E : 간선 수(/\)

    V, E = list(map(int, input().split()))

    nodes = [ [] for _ in range(V+1) ]  # 2차원배열
    #pprint(nodes)
    #print(V, E)
    # 인접 리스트 방식으로 그래프를 저장
    # 간선의 갯수만큼 반복을 진행
    for line in range(E):
        start, end = list(map(int,input().split()))
        nodes[start].append(end) # node = 배열, start = 1, end = 4, 3 연결
    #print(nodes)


    # S : 출발노드 / G : 도착노드
    S, G = list(map(int,input().split()))

    # 방문 체크용 리스트
    check_list = [False] * (V+1)

    dfs(S)

    if check_list[G]:
        result = 1
    else:
        result = 0

    print(result)
